# Small Model Coordinator (SMC) Implementation Guide

## Overview

The Small Model Coordinator (SMC) is a lightweight orchestration system for autonomous agent coordination. It implements a highly constrained JSON prompt protocol designed for small, fast, CPU-bound models (e.g., Llama 3 8B or smaller specialized agents).

**AI_PHASE:** AGENT_COORDINATION  
**AI_STATUS:** IMPLEMENTED  
**AI_COMPLEXITY:** HIGH  
**AI_NOTE:** Complete SMC implementation with agent handoff protocol

## Core Concepts

### 1. Small Model Coordinator (SMC_Coordinator)

The coordinator manages agent lifecycle and orchestration using three core decision prompts:

- **State Routing**: Determines which agent to execute next
- **Fix Triage**: Analyzes errors and determines remediation strategy
- **Final Decision**: Decides whether work is ready to commit

### 2. Structured Agent Output

All agents communicate via structured JSON output containing:

```json
{
  "action": "ACTION_NAME",
  "result": "SUCCESS|FAILURE|PARTIAL",
  "ai_state": "PROCESSING|READY|DONE|BLOCKED|PAUSED|FAILED|CANCELLED",
  "ai_queue_status": "QUEUED|ASSIGNED|IN_PROGRESS|...",
  "ai_handoff_requested": true|false,
  "additional_context": "..."
}
```

### 3. Handoff Protocol

The coordinator reads three key flags to determine agent handoff:

- **AI_STATE**: Current processing state
- **AI_HANDOFF_REQUESTED**: Whether handoff is needed
- **AI_QUEUE_STATUS**: Progress through processing queue

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   SMC Coordinator                            │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │    State     │  │     Fix      │  │    Final     │     │
│  │   Routing    │  │   Triage     │  │  Decision    │     │
│  │    Prompt    │  │    Prompt    │  │   Prompt     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────────────────────────────────────────┐      │
│  │          Agent Registry                           │      │
│  │  • BuilderAgent    • ReasoningAgent              │      │
│  │  • TesterAgent     • FinalizerAgent              │      │
│  └──────────────────────────────────────────────────┘      │
│                                                              │
│  ┌──────────────────────────────────────────────────┐      │
│  │          Global Status                            │      │
│  │  • AI_STATE         • AI_QUEUE_STATUS            │      │
│  │  • AI_HANDOFF_REQUESTED                          │      │
│  │  • Build/Test Metrics • Error List               │      │
│  └──────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
              ┌──────────────────────────┐
              │  Coordination Loop       │
              │  1. Check AI_STATE       │
              │  2. Execute Routing      │
              │  3. Run Selected Agent   │
              │  4. Update Global Status │
              │  5. Repeat until DONE    │
              └──────────────────────────┘
```

## Core Prompts

### 1. State Routing Prompt

**Purpose**: Determine the next agent to execute based on current system state.

**Input**:
```json
{
  "last_action": "string",
  "last_agent": "string",
  "last_result": "string",
  "ai_state": "string",
  "ai_queue_status": "string",
  "ai_handoff_requested": boolean,
  "available_agents": ["agent1", "agent2", ...]
}
```

**Output**:
```json
{
  "next_agent": "agent_name or NONE",
  "rationale": "brief explanation (< 200 chars)"
}
```

**Constraints**:
- Response must be valid JSON
- `next_agent` must be from `available_agents` or "NONE"
- `rationale` must be under 200 characters

### 2. Fix Triage Prompt

**Purpose**: Analyze errors and determine routing action for remediation.

**Input**:
```json
{
  "errors": ["error1", "error2", ...],  // Top 5 errors
  "error_count": number
}
```

**Output**:
```json
{
  "action": "ROUTE_REASONER|ROUTE_TESTER|ROUTE_FINALIZER|MANUAL_REVIEW",
  "context_focus": "area needing attention"
}
```

**Constraints**:
- Response must be valid JSON
- `action` must be one of the four specified values
- `context_focus` must identify specific code area or phase

### 3. Final Decision Prompt

**Purpose**: Determine if work is ready to commit based on success metrics.

**Input**:
```json
{
  "build_success_rate": number,  // 0.0 to 1.0
  "test_success_rate": number,   // 0.0 to 1.0
  "threshold_build": 0.95,
  "threshold_test": 0.90
}
```

**Output**:
```json
{
  "commit_required": boolean,
  "next_agent": "agent_name",
  "rationale": "brief explanation"
}
```

**Constraints**:
- Response must be valid JSON
- `commit_required` based on thresholds
- If `commit_required` is true, `next_agent` should be "Finalizer"
- If `commit_required` is false, `next_agent` should suggest remediation

## Agent Implementation

### Base Agent Interface

All agents must inherit from `BaseAgent` and implement the `execute()` method:

```python
class BaseAgent(ABC):
    @abstractmethod
    def execute(self, global_status: GlobalStatus) -> Dict[str, Any]:
        """
        Execute agent logic and return structured output.
        
        Returns:
            Dict with structured output including:
            - action: Action performed
            - result: Result status (SUCCESS, FAILURE, PARTIAL)
            - ai_state: Updated AI_STATE value
            - ai_queue_status: Updated AI_QUEUE_STATUS value
            - ai_handoff_requested: Whether handoff is needed
            - Additional context-specific fields
        """
        pass
```

### Example Agent Implementations

#### ReasoningAgent

Analyzes errors and generates structured fix recommendations.

**Structured Output Example**:
```json
{
  "action": "REASON_AND_FIX",
  "result": "SUCCESS",
  "ai_state": "PROCESSING",
  "ai_queue_status": "IN_PROGRESS",
  "ai_handoff_requested": false,
  "fix_recommendation": {
    "fix_type": "INSERT_LINE",
    "target_file": "memory_api.py",
    "line_number": 42,
    "error_type": "IMPORT",
    "new_code": "import numpy as np",
    "confidence": 0.8
  },
  "errors_remaining": 1
}
```

#### TesterAgent

Executes tests and reports structured results.

**Structured Output Example**:
```json
{
  "action": "RUN_TESTS",
  "result": "SUCCESS",
  "ai_state": "READY",
  "ai_queue_status": "APPROVED",
  "ai_handoff_requested": true,
  "test_results": {
    "total": 10,
    "passed": 9,
    "failed": 1,
    "skipped": 0,
    "failures": ["test_memory: AssertionError at line 45"]
  },
  "test_success_rate": 0.9,
  "errors": ["test_memory: AssertionError at line 45"]
}
```

#### BuilderAgent

Executes build and reports structured results.

**Structured Output Example**:
```json
{
  "action": "BUILD",
  "result": "SUCCESS",
  "ai_state": "READY",
  "ai_queue_status": "COMPLETED",
  "ai_handoff_requested": true,
  "build_results": {
    "status": "SUCCESS",
    "duration": 45.2,
    "warnings": 2,
    "errors": []
  },
  "build_success_rate": 1.0,
  "errors": []
}
```

#### FinalizerAgent

Prepares work for commit and finalization.

**Structured Output Example**:
```json
{
  "action": "FINALIZE",
  "result": "SUCCESS",
  "ai_state": "DONE",
  "ai_queue_status": "COMPLETED",
  "ai_handoff_requested": false,
  "commit_ready": true,
  "commit_message": "Autonomous development cycle completed successfully",
  "build_success_rate": 0.98,
  "test_success_rate": 0.95
}
```

## Usage Example

### Basic Coordination Setup

```python
from smc_coordinator import SMCCoordinator
from example_agents import ReasoningAgent, TesterAgent, FinalizerAgent, BuilderAgent

# Initialize coordinator
coordinator = SMCCoordinator()

# Register agents
coordinator.register_agent("BuilderAgent", BuilderAgent())
coordinator.register_agent("ReasoningAgent", ReasoningAgent())
coordinator.register_agent("TesterAgent", TesterAgent())
coordinator.register_agent("FinalizerAgent", FinalizerAgent())

# Set initial state
coordinator.global_status.top_errors = [
    "ImportError: No module named 'numpy'"
]
coordinator.global_status.ai_state = AgentState.READY
coordinator.global_status.ai_handoff_requested = True

# Run coordination loop
result = coordinator.run_coordination_loop(max_iterations=10)

# Print results
print(f"Completed in {result['total_iterations']} iterations")
print(f"Final state: {result['final_state']['ai_state']}")
```

### Custom Agent Implementation

```python
from example_agents import BaseAgent

class CustomAgent(BaseAgent):
    def execute(self, global_status):
        # Your custom logic here
        
        # Return structured output
        return {
            "action": "CUSTOM_ACTION",
            "result": "SUCCESS",
            "ai_state": "READY",
            "ai_queue_status": "COMPLETED",
            "ai_handoff_requested": False,
            "custom_data": {
                "key": "value"
            }
        }

# Register with coordinator
coordinator.register_agent("CustomAgent", CustomAgent())
```

## Handoff Protocol Details

### State Transitions

```
READY → PROCESSING → READY → DONE
   ↓         ↓          ↓
BLOCKED   BLOCKED   BLOCKED
   ↓         ↓          ↓
FAILED    FAILED    FAILED
```

### Handoff Decision Logic

The coordinator uses the following logic to determine handoffs:

1. **Check AI_STATE**:
   - If `DONE`: Terminate coordination
   - If `FAILED`: Terminate coordination with error
   - If `BLOCKED`: Route to ReasoningAgent
   - If `READY`: Execute routing decision

2. **Check AI_HANDOFF_REQUESTED**:
   - If `true`: Execute state routing to find next agent
   - If `false`: Continue with current agent

3. **Check AI_QUEUE_STATUS**:
   - `QUEUED`: Assign to appropriate agent
   - `IN_PROGRESS`: Continue with current agent
   - `REVIEW_PENDING`: Route to review agent
   - `APPROVED`: Route to next pipeline stage
   - `REJECTED`: Route to ReasoningAgent for fixes
   - `COMPLETED`: Check for next work or finalize

### Global Status Management

The coordinator maintains global status that is passed to all agents:

```python
@dataclass
class GlobalStatus:
    last_action: str
    last_agent: str
    last_result: str
    ai_state: AgentState
    ai_queue_status: QueueStatus
    ai_handoff_requested: bool
    build_success_rate: float = 0.0
    test_success_rate: float = 0.0
    error_count: int = 0
    top_errors: List[str] = None
```

## Integration with ACD Standard

The SMC implementation fully integrates with the ACD Standard Specification v1.1:

### SCIS Tags in Code

All coordinator and agent code includes proper ACD metadata:

```python
"""
AI_PHASE: AGENT_COORDINATION
AI_STATUS: IMPLEMENTED
AI_COMPLEXITY: HIGH
AI_NOTE: Core coordinator for autonomous agent handoff
AI_DEPENDENCIES: 
AI_COMMIT: initial
"""
```

### Communication Flags

The implementation uses ACD communication flags:

- **AI_STATE**: Current processing state (from Part 4 of ACD spec)
- **AI_QUEUE_STATUS**: Queue progress tracking
- **AI_HANDOFF_REQUESTED**: Handoff request flag
- **AI_CONFIDENCE**: Agent confidence in output (optional)

### Queuing Flags

The implementation supports ACD queuing flags:

- **AI_QUEUE_PRIORITY**: Task priority (CRITICAL, HIGH, NORMAL, LOW, DEFERRED)
- **AI_QUEUE_STATUS**: Queue state tracking
- **AI_ASSIGNED_TO**: Current agent assignment

## Low-Latency Backend

The SMC is designed to work with small, fast models:

### Recommended Models

1. **Llama 3 8B**: Balanced performance and speed
2. **Phi-3 Mini**: Extremely fast inference
3. **Mistral 7B**: Good reasoning with low latency
4. **Specialized SMC Models**: Custom-trained small models for coordination tasks

### Backend Integration

```python
# Example backend integration
class FastModelBackend:
    def __init__(self, model_path):
        self.model = load_model(model_path)
    
    def generate(self, prompt: str) -> str:
        # Fast inference optimized for JSON output
        response = self.model.generate(
            prompt,
            max_tokens=200,  # Constrained output
            temperature=0.1,  # Low temperature for consistency
            format="json"  # Force JSON output
        )
        return response

# Use with coordinator
backend = FastModelBackend("llama-3-8b-instruct")
coordinator = SMCCoordinator(model_backend=backend)
```

## Testing

Comprehensive tests are provided in `tests/test_smc.py`:

```bash
# Run all SMC tests
python3 tests/test_smc.py

# Run specific test class
python3 -m unittest tests.test_smc.TestSMCCoordinator

# Run with verbose output
python3 tests/test_smc.py -v
```

## Examples

Complete examples are provided in `examples/smc_example.py`:

```bash
# Run all demos
python3 examples/smc_example.py

# Run specific demo
python3 examples/smc_example.py "Basic Coordination"
python3 examples/smc_example.py "State Routing"
python3 examples/smc_example.py "Complete Workflow"
```

## Best Practices

1. **Keep Prompts Constrained**: Limit output to 200 characters for rationales
2. **Use Structured Output**: Always return valid JSON from agents
3. **Set Clear Thresholds**: Define success rate thresholds explicitly
4. **Handle Errors Gracefully**: Always include error context in output
5. **Log Everything**: Maintain detailed execution logs for debugging
6. **Test Extensively**: Write tests for each agent and coordinator function
7. **Monitor Performance**: Track coordination loop iterations and timing

## Performance Considerations

- **Prompt Size**: Keep prompts under 2KB for fast inference
- **Model Size**: Use 7-8B parameter models for best speed/quality balance
- **Output Tokens**: Limit to 200 tokens maximum per coordination decision
- **Caching**: Cache model responses for repeated states
- **Batching**: Process multiple coordination decisions in parallel when possible

## Future Enhancements

- **Multi-Agent Collaboration**: Support for parallel agent execution
- **Learning from History**: Train coordinator on successful patterns
- **Adaptive Thresholds**: Dynamically adjust success rate thresholds
- **Distributed Coordination**: Scale to multiple coordinator instances
- **Model Distillation**: Create even smaller specialized models

## References

- ACD Standard Specification v1.1: `/README.md`
- JSON Schema: `/spec/ACD_SCHEMA_v1.1.json`
- Example Agents: `/src/example_agents.py`
- SMC Coordinator: `/src/smc_coordinator.py`
- Tests: `/tests/test_smc.py`
- Examples: `/examples/smc_example.py`

---

**Copyright (C) 2025 Timothy Deters / R.E.C.A.L.L. Foundation**

This implementation is part of the ACD Specification and is licensed under GPL v3.
For commercial licensing inquiries, contact the R.E.C.A.L.L. Foundation.

Patent Pending: U.S. Application No. 63/898,838
