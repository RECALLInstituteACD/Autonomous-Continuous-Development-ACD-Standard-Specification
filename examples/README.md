# ACD Examples

This directory contains example implementations demonstrating the Autonomous Continuous Development (ACD) Standard Specification.

## Examples

### 1. example_with_acd.py

Basic Python example demonstrating how to add SCIS metadata to Python code using comments.

**AI_PHASE:** EXAMPLE_IMPLEMENTATION  
**AI_STATUS:** IMPLEMENTED  
**AI_COMPLEXITY:** LOW  
**AI_NOTE:** Basic example of SCIS metadata in Python

**Usage:**
```bash
python3 examples/example_with_acd.py
```

**Features:**
- SCIS metadata in Python comments
- Example phases (INIT, ERROR_HANDLING, VALIDATION, CORE_LOGIC, LOGGING)
- Demonstrates AI_STATUS, AI_COMPLEXITY, AI_DEPENDENCIES tags

### 2. smc_example.py

Comprehensive demonstration of the Small Model Coordinator (SMC) system for autonomous agent orchestration.

**AI_PHASE:** EXAMPLE_IMPLEMENTATION  
**AI_STATUS:** IMPLEMENTED  
**AI_COMPLEXITY:** MEDIUM  
**AI_NOTE:** Complete demonstration of SMC coordinator with agent handoff

**Usage:**
```bash
# Run all demos
python3 examples/smc_example.py

# Run specific demo
python3 examples/smc_example.py "Basic Coordination"
python3 examples/smc_example.py "State Routing Prompt"
python3 examples/smc_example.py "Fix Triage Prompt"
python3 examples/smc_example.py "Final Decision Prompt"
python3 examples/smc_example.py "Agent Structured Output"
python3 examples/smc_example.py "Complete Workflow"
```

**Available Demos:**

#### Basic Coordination
Demonstrates the complete coordination loop with multiple agents, showing how the coordinator manages agent handoff using AI_STATE, AI_HANDOFF_REQUESTED, and AI_QUEUE_STATUS flags.

Example output:
```
Total Iterations: 3
Final State: DONE
```

#### State Routing Prompt
Shows how the coordinator generates constrained JSON prompts for agent selection based on global system state.

Example prompt:
```json
{
  "task": "state_routing",
  "instruction": "Determine the next agent to execute...",
  "input": {
    "last_action": "BUILD",
    "ai_state": "READY",
    "available_agents": ["ReasoningAgent", "TesterAgent"]
  },
  "output_format": {
    "next_agent": "string",
    "rationale": "string"
  }
}
```

#### Fix Triage Prompt
Demonstrates error analysis and routing decisions for remediation.

Example prompt:
```json
{
  "task": "fix_triage",
  "input": {
    "errors": ["ImportError: No module named 'numpy'"],
    "error_count": 1
  },
  "output_format": {
    "action": "ROUTE_REASONER|ROUTE_TESTER|...",
    "context_focus": "string"
  }
}
```

#### Final Decision Prompt
Shows commit/finalize decision logic based on build and test success rates.

Example prompt:
```json
{
  "task": "final_decision",
  "input": {
    "build_success_rate": 0.98,
    "test_success_rate": 0.95,
    "threshold_build": 0.95,
    "threshold_test": 0.90
  },
  "output_format": {
    "commit_required": "boolean",
    "next_agent": "string"
  }
}
```

#### Agent Structured Output
Demonstrates the structured JSON output protocol used by all agents.

Example outputs from different agents:
- **ReasoningAgent**: Returns structured fix recommendations
- **TesterAgent**: Returns test results with success rates
- **BuilderAgent**: Returns build status and errors
- **FinalizerAgent**: Returns commit readiness status

#### Complete Workflow
Shows a full autonomous development workflow from build to finalization:

1. **Build Phase**: BuilderAgent compiles code
2. **Test Phase**: TesterAgent runs tests
3. **Analysis Phase**: ReasoningAgent analyzes errors (if any)
4. **Finalization Phase**: FinalizerAgent prepares commit

Example workflow:
```
Stage 1: Initial Build → SUCCESS (build_success_rate: 1.0)
Stage 2: Testing → PARTIAL (test_success_rate: 0.9, 1 failure)
Stage 3: Error Analysis → Fix recommended
Stage 4: Finalization → READY TO COMMIT
```

## Agent Communication Protocol

All agents in the SMC system communicate via structured JSON output:

```json
{
  "action": "ACTION_NAME",
  "result": "SUCCESS|FAILURE|PARTIAL",
  "ai_state": "PROCESSING|READY|DONE|BLOCKED|...",
  "ai_queue_status": "QUEUED|IN_PROGRESS|COMPLETED|...",
  "ai_handoff_requested": true|false,
  "context_specific_data": {}
}
```

### Required Output Fields

- **action**: The action performed by the agent
- **result**: Result status (SUCCESS, FAILURE, PARTIAL)
- **ai_state**: Updated AI_STATE value from ACD standard
- **ai_queue_status**: Updated AI_QUEUE_STATUS value
- **ai_handoff_requested**: Whether handoff to another agent is needed

### Optional Output Fields

Agents can include additional context-specific fields:
- **fix_recommendation**: Structured fix details (ReasoningAgent)
- **test_results**: Test execution results (TesterAgent)
- **build_results**: Build output (BuilderAgent)
- **commit_ready**: Finalization status (FinalizerAgent)
- **errors**: Error list for next agent

## SMC Coordinator Features

### 1. State Routing
Uses global system state to determine the next agent to execute.

**Inputs:**
- Last action and agent
- Current AI_STATE
- Current AI_QUEUE_STATUS
- AI_HANDOFF_REQUESTED flag

**Output:**
- Next agent to execute
- Rationale for selection

### 2. Fix Triage
Analyzes top errors and determines remediation strategy.

**Inputs:**
- Top 5 error messages
- Total error count

**Output:**
- Action to take (ROUTE_REASONER, ROUTE_TESTER, etc.)
- Context focus area

### 3. Final Decision
Determines if work is ready to commit based on metrics.

**Inputs:**
- Build success rate
- Test success rate
- Defined thresholds

**Output:**
- Whether commit is required
- Next agent for commit or remediation

## Integration with ACD Standard

The SMC implementation fully integrates with ACD Standard Specification v1.1:

- **SCIS Tags**: All code includes proper AI_PHASE, AI_STATUS, AI_COMPLEXITY metadata
- **Communication Flags**: Uses AI_STATE, AI_CONFIDENCE, AI_REQUEST from Part 4
- **Queuing Flags**: Implements AI_QUEUE_STATUS, AI_QUEUE_PRIORITY
- **Handoff Protocol**: Uses AI_HANDOFF_REQUESTED, AI_HANDOFF_TYPE

## Testing

All examples include comprehensive tests in `/tests/test_smc.py`:

```bash
# Run SMC tests
python3 tests/test_smc.py

# Run with verbose output
python3 tests/test_smc.py -v
```

**Test Coverage:**
- 27 tests covering all coordinator and agent functionality
- GlobalStatus data structure tests
- Prompt generation tests
- Agent execution tests
- Structured output validation tests
- Coordination loop tests

## Documentation

Detailed documentation available in:
- `/docs/SMC_IMPLEMENTATION_GUIDE.md`: Complete implementation guide
- `/README.md`: ACD Standard Specification v1.1
- `/spec/ACD_SCHEMA_v1.1.json`: JSON schema with SMC fields

## Implementation Files

Source files for SMC system:
- `/src/smc_coordinator.py`: SMC Coordinator implementation
- `/src/example_agents.py`: Example agent implementations
- `/tests/test_smc.py`: Comprehensive test suite

## Best Practices

1. **Always Return Structured JSON**: Agents must return valid JSON with required fields
2. **Update Global Status**: Use ai_state, ai_queue_status, ai_handoff_requested to control flow
3. **Keep Prompts Constrained**: Limit rationales to 200 characters for fast inference
4. **Test Thoroughly**: Write tests for each agent and coordinator function
5. **Use ACD Metadata**: Include proper SCIS tags in all code
6. **Log Execution**: Maintain detailed logs for debugging

## Advanced Usage

### Custom Agent Implementation

Create custom agents by inheriting from BaseAgent:

```python
from example_agents import BaseAgent

class MyCustomAgent(BaseAgent):
    def execute(self, global_status):
        # Your logic here
        return {
            "action": "MY_ACTION",
            "result": "SUCCESS",
            "ai_state": "READY",
            "ai_queue_status": "COMPLETED",
            "ai_handoff_requested": False
        }
```

### Backend Integration

Integrate with actual AI models:

```python
class ModelBackend:
    def generate(self, prompt):
        # Call your model API
        response = self.model.generate(prompt)
        return response

coordinator = SMCCoordinator(model_backend=ModelBackend())
```

### Multi-Agent Workflows

Chain multiple agents for complex workflows:

```python
coordinator.register_agent("Analyzer", AnalyzerAgent())
coordinator.register_agent("Implementer", ImplementerAgent())
coordinator.register_agent("Tester", TesterAgent())
coordinator.register_agent("Reviewer", ReviewerAgent())
coordinator.register_agent("Finalizer", FinalizerAgent())

result = coordinator.run_coordination_loop(max_iterations=20)
```

## References

- ACD Standard: `/README.md`
- SMC Guide: `/docs/SMC_IMPLEMENTATION_GUIDE.md`
- Implementation: `/src/smc_coordinator.py`
- Tests: `/tests/test_smc.py`

---

**Copyright (C) 2025 Timothy Deters / R.E.C.A.L.L. Foundation**

Licensed under GPL v3. For commercial licensing inquiries, contact the R.E.C.A.L.L. Foundation.

Patent Pending: U.S. Application No. 63/898,838
