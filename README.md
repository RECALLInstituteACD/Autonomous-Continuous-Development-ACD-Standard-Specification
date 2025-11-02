# 🔬 Autonomous Continuous Development (ACD) Standard Specification (v1.1 - The Full Development Loop)

**Version:** 1.1  
**Status:** Active Standard  
**Last Updated:** November 2025  
**Repository:** ACD_Specification

---

## Executive Summary

The **Autonomous Continuous Development (ACD)** standard accurately names the **active, intelligent, full-cycle system** that enables continuous, autonomous software development.

**The Core Problem:** Stateless AI agents operate with minimal recall—they may see documentation and code comments, but lack a complete understanding of the historical context, reasoning, and decisions that shaped the codebase. This specification solves that fundamental limitation.

**The Solution:** ACD provides a complete **historical tracking system** that gives autonomous agents access to the full context window and history graph of an entire codebase—every decision, every change, and the reasoning behind it. This transforms stateless agents into context-aware collaborators with institutional memory.

This specification defines a common, machine-readable protocol for embedding **cognitive intelligence** and **complete historical context** directly into source code and toolchains, enabling **full-cycle, continuous development** (Build, Test, Reason, Remediate, Audit) by autonomous agents. This standard operationalizes the self-driving codebase.

---

## 🚀 Quick Start with ACD Template

**Want to adopt ACD in your project right now?** Use our drop-in repository template:

```bash
# For existing projects
cd /path/to/your/project
cp -r /path/to/ACD_Specification/template/* .
cp -r /path/to/ACD_Specification/template/.acd .
./scripts/acd_init.sh

# For new projects
mkdir my-project && cd my-project && git init
cp -r /path/to/ACD_Specification/template/* .
./scripts/acd_init.sh
```

**See [TEMPLATE_USAGE.md](TEMPLATE_USAGE.md) for complete instructions.**

The template includes:
- ✅ Pre-configured directory structure
- ✅ GitHub Actions CI/CD integration
- ✅ Example code with SCIS metadata
- ✅ Validation and analysis tools
- ✅ Comprehensive documentation

### 🤖 Bootstrap Your Project with AI

**Starting from zero code?** Use this example prompt to have AI bootstrap your ACD-compliant project:

```
Create a complete [project type, e.g., "REST API server" or "data processing pipeline"] 
following the Autonomous Continuous Development (ACD) Standard Specification v1.0.

Requirements:
- Implement full ACD metadata (AI_PHASE, AI_STATUS, AI_COMPLEXITY, AI_NOTE, AI_DEPENDENCIES)
- Use the Source Code Intelligence Standard (SCIS) format for all code comments
- Include comprehensive README following ACD documentation standards
- Add breadcrumb navigation between related components
- Document all design decisions and reasoning in code metadata
- Create fix summary templates for future issue resolution
- Maintain complete traceability for autonomous development

Project Structure:
- Use clear phase definitions (e.g., INIT, MEMORY_MANAGEMENT, API_TRANSLATION, ERROR_HANDLING)
- Mark implementation status accurately (IMPLEMENTED, PARTIAL, NOT_STARTED)
- Rate complexity honestly (LOW, MEDIUM, HIGH, CRITICAL)
- Document all dependencies between phases

Compliance:
- Follow the ACD Standard Specification from 
  https://github.com/RECALLInstituteACD/Autonomous-Continuous-Development-ACD-Standard-Specification
- Enable autonomous agents to understand, complete, and improve the codebase
- Provide complete historical context for all decisions
- Make all code machine-readable for AI training and correlation

Please generate:
1. Complete project structure with ACD metadata
2. README.md in ACD documentation style (spec-compliant, zero-fluff)
3. Example code files with proper SCIS tags
4. Development workflow documentation
5. Integration with standard toolchains (compiler, debugger, CI/CD)
```

**Example with More Specificity:**

```
Create an HTTP REST API server with full ACD Standard Specification compliance.

This server should handle client requests and provide data access. Every function must include:

- AI_PHASE: Component category (REQUEST_HANDLING, DATA_VALIDATION, RESPONSE_GENERATION, etc.)
- AI_STATUS: Implementation state (IMPLEMENTED, PARTIAL, NOT_STARTED)
- AI_COMPLEXITY: Risk level (LOW, MEDIUM, HIGH, CRITICAL)
- AI_NOTE: Clear description of purpose and behavior
- AI_DEPENDENCIES: Required phases for this component
- AI_COMMIT: Git commit hash for version tracking

Generate a complete, production-ready implementation with:
- Structured metadata for autonomous development
- Clear phase definitions and dependencies
- Complete audit trail for all endpoints
- Error handling with proper status codes
- Input validation and sanitization
- CI/CD integration for continuous validation

Follow the ACD Standard from:
https://github.com/RECALLInstituteACD/Autonomous-Continuous-Development-ACD-Standard-Specification
```

These prompts ensure AI generates code that is immediately compatible with autonomous 
development workflows, complete with the metadata needed for AI agents to understand, 
maintain, and improve the codebase over time.

---

## 🤖 Small Model Coordinator (SMC) - Agent Orchestration

**NEW IN v1.1:** The ACD standard now includes a complete implementation of a **Small Model Coordinator (SMC)** for autonomous agent orchestration.

The SMC is a lightweight coordinator that uses highly constrained JSON prompts for fast, CPU-bound decision making. It's designed to work with small models (Llama 3 8B or smaller) for minimum latency while providing sophisticated agent handoff and coordination.

### Key Features

- **3 Core JSON Prompts**: State Routing, Fix Triage, Final Decision
- **Structured Agent Output**: All agents communicate via JSON (no prose)
- **Handoff Protocol**: Uses AI_STATE, AI_HANDOFF_REQUESTED, AI_QUEUE_STATUS flags
- **Low Latency**: Optimized for small, fast models (7-8B parameters)
- **Fully Tested**: 27 comprehensive tests included

### Quick Start with SMC

```bash
# Run SMC examples
python3 examples/smc_example.py

# Run specific demo
python3 examples/smc_example.py "Complete Workflow"

# Run tests
python3 tests/test_smc.py
```

### Example: Complete Autonomous Workflow

```python
from smc_coordinator import SMCCoordinator
from example_agents import BuilderAgent, TesterAgent, ReasoningAgent, FinalizerAgent

# Initialize coordinator
coordinator = SMCCoordinator()

# Register agents
coordinator.register_agent("BuilderAgent", BuilderAgent())
coordinator.register_agent("TesterAgent", TesterAgent())
coordinator.register_agent("ReasoningAgent", ReasoningAgent())
coordinator.register_agent("FinalizerAgent", FinalizerAgent())

# Run autonomous development cycle
result = coordinator.run_coordination_loop(max_iterations=10)
print(f"Completed in {result['total_iterations']} iterations")
```

### Structured Agent Output Example

Instead of prose, agents now return structured JSON:

```json
{
  "action": "REASON_AND_FIX",
  "result": "SUCCESS",
  "ai_state": "READY",
  "ai_queue_status": "REVIEW_PENDING",
  "ai_handoff_requested": true,
  "fix_recommendation": {
    "fix_type": "INSERT_LINE",
    "target_file": "memory_api.py",
    "line_number": 42,
    "new_code": "import numpy as np"
  }
}
```

**Documentation**: See [SMC Implementation Guide](docs/SMC_IMPLEMENTATION_GUIDE.md) for complete details.

**Implementation Files**:
- `src/smc_coordinator.py` - SMC Coordinator
- `src/example_agents.py` - Example agents (Reasoning, Testing, Building, Finalizing)
- `examples/smc_example.py` - Comprehensive examples
- `tests/test_smc.py` - 27 tests covering all functionality

---

## Purpose

**To transform stateless AI agents into context-aware collaborators** by providing complete historical tracking of every decision, change, and reasoning in a codebase.

Traditional development tools and AI agents operate with limited context—they see the current state of code, perhaps some documentation, but lack access to the complete history of **why** decisions were made, **how** implementations evolved, and **what** patterns succeeded or failed. This creates a fundamental barrier to autonomous development.

The ACD Standard solves this by defining a machine-readable protocol for embedding **cognitive intelligence** and **complete historical context** directly into source code and toolchains. This enables:

- **Complete Historical Memory** - Full tracking of every decision ever made in the repository
- **Cognitive Segmentation** - Code organized into logical, functional units that AI can understand
- **Implementation Tracking** - Operational maturity of each code segment explicitly declared
- **Risk Profiling** - Inherent cognitive difficulty quantified for prioritization
- **Context Retrieval** - Instant access to intent, status, complexity, and historical reasoning at any point
- **Autonomous Reasoning** - Context-aware diagnostic and remediation recommendations based on complete history
- **Full Traceability** - Complete graph of development decisions and reasoning linked to every line of code
- **Evolutionary Understanding** - Walk backwards through time to understand how and why code evolved

The standard enables **full-cycle, continuous development** (Build, Test, Reason, Remediate, Audit) by giving autonomous agents the same institutional memory and context that experienced human developers possess.

---

## From Stateless to Stateful: The ACD Transformation

### The Stateless Agent Problem

Traditional AI agents operate with severe limitations:
- **No Historical Memory**: They see current code and documentation but have no recall of past decisions
- **No Context Window**: Limited to what's immediately visible—file contents, recent commits, maybe some documentation
- **No Reasoning Trail**: Can't understand *why* code exists in its current form or what alternatives were considered
- **No Institutional Knowledge**: Each interaction starts from scratch, like a developer with complete amnesia
- **No Pattern Recognition**: Can't learn from the codebase's own evolution and successes/failures

### The ACD Solution: Complete Historical Context

ACD transforms stateless agents into context-aware collaborators by providing:

1. **Complete Decision Graph**: Every change, every decision, every reasoning—all tracked and accessible
2. **Full History Window**: Access to the entire evolution of any code segment, not just its current state
3. **Reasoning Reconstruction**: Link from any line of code back through all commits, PRs, discussions, and fix summaries
4. **Institutional Memory**: Build and maintain knowledge that persists across sessions and agents
5. **Pattern Library**: Learn from the codebase's own history of what worked and what didn't

**The Result:** Autonomous agents that can reason about code with the same depth of understanding as experienced developers who have worked on the codebase for years—because they have access to the same complete historical context.

---

## Part 1: The Source Code Intelligence Standard (SCIS)

This defines the declarative metadata embedded in the source code that establishes the code's **self-awareness**, **historical memory**, and structural map.

SCIS transforms source code from a passive set of instructions into an **intelligent, self-documenting artifact** that carries its complete history, reasoning, and context. Each code segment becomes a node in a comprehensive knowledge graph, enabling autonomous agents to understand not just *what* the code does, but *why* it exists, *how* it evolved, and *what* decisions shaped it.

### SCIS Tag Specification

| Tag | Purpose | Rationale | Format | Required |
| :--- | :--- | :--- | :--- | :--- |
| **`AI_PHASE`** | **Cognitive Segmentation.** Categorizes the code block into a logical, functional unit. | Enables the AI to isolate the specific task segment (e.g., `MEMORY_TRANSLATION`) that is currently in the execution cycle. | String (e.g., "MEMORY_TRANSLATION", "KERNEL_DISPATCH") | ✅ Yes |
| **`AI_STATUS`** | **Implementation State.** Declares the operational maturity of the code segment. | Informs the autonomous system if a failure is due to expected partial implementation (`PARTIAL`) vs. a regression in complete code (`IMPLEMENTED`). | Enum: `IMPLEMENTED`, `PARTIAL`, `NOT_STARTED`, `FIXED`, `DEPRECATED` | ✅ Yes |
| **`AI_COMPLEXITY`** | **Risk Profile.** Quantifies the inherent cognitive difficulty or risk of the code segment. | Prioritizes attention for the agent (`ACD-suggest`) and weights the confidence score of any autonomous remediation. | Enum: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL` | ⚠️ Recommended |
| **`AI_NOTE`** | **Implementation Notes.** Human-readable description of the code's purpose and behavior. | Provides context and documentation for both humans and AI agents. | String | ⚠️ Recommended |
| **`AI_DEPENDENCIES`** | **Dependency Chain.** Lists other phases this code depends on. | Enables dependency tracking and proper initialization order verification. | Comma-separated list of AI_PHASE values | ⚠️ Recommended |
| **`AI_COMMIT`** | **Version Tracking.** The Git commit hash when this code was last modified. | Links code directly to historical development decisions, PRs, and fix summaries. | Git commit SHA | ⚠️ Recommended |
| **`AI_COMMIT_HISTORY`** | **Historical Memory Trail.** Comma-separated list of previous Git commit hashes for this code segment. | Creates a complete memory trail when making changes. When updating `AI_COMMIT`, the old value should be prepended to this list. Enables walking the entire development history of a function using git blame and commit history. | Comma-separated list of Git commit SHAs (newest first, excluding current `AI_COMMIT`) | ⚠️ Recommended |
| **`AI_PATTERN`** | **Implementation Pattern.** Identifies the coding pattern or approach used in this code segment. | Enables pattern-based analysis and reuse across the codebase. Helps AI agents recognize and apply known patterns. | String (e.g., "KERNEL_LAUNCH_V1", "CACHE_MANAGEMENT_V1") | 🔄 Context-specific |
| **`AI_STRATEGY`** | **Implementation Strategy.** Describes the high-level approach taken to implement this functionality. | Documents the reasoning behind implementation choices for future reference and learning. | String describing the strategy | 🔄 Context-specific |
| **`AI_VERSION`** | **Code Version.** Version number for this implementation. | Tracks evolution of implementation approaches and enables version-specific handling. | Version string (e.g., "1.0", "2.1") | 🔄 Context-specific |
| **`AI_CHANGE`** | **Change Description.** Describes the most recent change made to this code segment. | Provides quick context about what was changed and why without needing to check git history. | String describing the change | 🔄 Context-specific |
| **`AI_TRAIN_HASH`** | **Training Hash.** Unique hash for AI training and pattern recognition. | Enables machine learning models to identify and learn from specific code patterns. | 64-character hex hash | 🔄 Context-specific |
| **`AI_CONTEXT`** | **Extended Context.** JSON object containing additional context-specific information. | Provides structured metadata for complex scenarios requiring multiple context values. | JSON object | 🔄 Context-specific |
| **`AI_METADATA`** | **Additional Metadata.** General-purpose field for storing arbitrary metadata about the code segment. | Enables flexible metadata storage for project-specific needs without requiring schema changes. | String or JSON object | 🔄 Context-specific |
| **`SOURCE_API_REF`** | **Translation Map (Source).** Explicitly defines the source API this code translates from. | Serves as the high-fidelity reference guide for the AI to perform parity checks and ensure correct implementation of the wrapper logic. | Source API function/constant name with reference | 🔄 Context-specific |
| **`TARGET_API_REF`** | **Translation Map (Target).** Explicitly defines the target API this code translates to. | Serves as the high-fidelity reference guide for the AI to perform parity checks and ensure correct implementation of the wrapper logic. | Target API function/constant name with reference | 🔄 Context-specific |
| **`COMPILER_ERR`** | **Compiler Error Context.** Records compiler errors encountered during development. | Provides context for fixes and helps identify recurring compilation issues. | Compiler error message | 🔄 Context-specific |
| **`RUNTIME_ERR`** | **Runtime Error Context.** Records runtime errors encountered during development. | Provides context for fixes and helps identify recurring runtime issues. | Runtime error message | 🔄 Context-specific |
| **`FIX_REASON`** | **Fix Rationale.** Explains why a particular fix was necessary. | Documents the reasoning behind fixes for future reference and learning. | String explaining the fix | 🔄 Context-specific |
| **`HUMAN_OVERRIDE`** | **Human Review.** Records human review and approval of AI-generated or modified code. | Provides accountability and tracks human oversight of autonomous changes. | String with reviewer name and date | 🔄 Context-specific |

### SCIS Implementation Example

```cpp
/*
 * AI_PHASE: MEMORY_TRANSLATION
 * AI_STATUS: IMPLEMENTED
 * AI_COMPLEXITY: MEDIUM
 * AI_NOTE: Implements unified memory allocation with backend translation
 * AI_DEPENDENCIES: INIT_HOOKS, ERROR_HANDLING
 * AI_COMMIT: a3f2d9c
 * AI_COMMIT_HISTORY: b7e4a1f, e4f9a2d
 * SOURCE_API_REF: allocateManagedMemory() - source_runtime_api.h
 * TARGET_API_REF: backendAllocateManaged() - backend_runtime_api.h
 */
api_error_t allocateManagedMemory(void** devPtr, size_t size, unsigned int flags) {
    // Implementation...
}
```

### SCIS Status Values

| Status | Meaning | Usage |
| :--- | :--- | :--- |
| `IMPLEMENTED` | Code is complete and tested | Default for production code |
| `PARTIAL` | Code is incomplete or partially working | In-development features |
| `NOT_STARTED` | Stub or placeholder only | Future implementation |
| `FIXED` | Code was broken and has been repaired | Post-fix tracking |
| `DEPRECATED` | Code is obsolete but not yet removed | Migration period |

### SCIS Complexity Values

| Complexity | Meaning | Criteria |
| :--- | :--- | :--- |
| `LOW` | Simple, straightforward logic | Direct API translation, minimal state |
| `MEDIUM` | Moderate complexity | Some state management, multiple code paths |
| `HIGH` | Complex logic with multiple concerns | Significant state, async operations, multiple dependencies |
| `CRITICAL` | Mission-critical or error-prone | Memory safety, synchronization, known problematic areas |

---

## Part 2: The Toolchain Cognitive Standard (TCS)

This defines the required interface for all development tools (compilers, runtimes, debuggers) to interact with and process the embedded code intelligence.

### TCS Components

| Component | Function | Rationale | Source |
| :--- | :--- | :--- | :--- |
| **GDB Extension** | A GDB-based utility that links the current instruction pointer to the nearest **SCIS** metadata block. | Converts raw execution data (stack traces) into structured, **intelligent context** for the AI agent. | `scripts/gdb_acd.py` |
| **`info ACD`** | **Context Retrieval.** Retrieves and displays the full **SCIS** metadata for the current execution line. | Gives the AI instant context (Intent, Status, Complexity) for the point of failure. | *Derived from `scripts/gdb_acd.py`* |
| **`ACD-suggest`** | **Autonomous Reasoning.** Uses the current `AI_STATUS` and `AI_COMPLEXITY` to provide context-aware diagnostic and remediation path recommendations. | Automates the initial triage phase of the development loop, moving immediately to informed action. | `scripts/gdb_acd.py` |
| **ACD Validator** | Tool to validate SCIS metadata in source files and generate reports. | Ensures metadata completeness and correctness across the codebase. | `scripts/validate_acd.py` |
| **Compiler Error Enrichment** | Augments compiler errors with SCIS context. | Links build failures to implementation status and phase information. | `scripts/enrich_compiler_errors.py` |

### TCS GDB Commands

#### `info ACD`

Displays the ACD metadata for the current source location during debugging.

**Usage:**
```
(gdb) info ACD
```

**Example Output:**
```
Current Location: src/memory_api.cpp:145

ACD Context:
----------------------------------------------------------------------
  Phase: MEMORY_TRANSLATION
  Status: ✅ IMPLEMENTED
  Complexity: MEDIUM
  Note: Implements unified memory allocation with backend translation
  Dependencies: INIT_HOOKS, ERROR_HANDLING
  Commit: a3f2d9c
  Commit History: b7e4a1f, e4f9a2d
  Source API Ref: allocateManagedMemory() - source_runtime_api.h
  Target API Ref: backendAllocateManaged() - backend_runtime_api.h
```

#### `ACD-suggest`

Provides automated debugging suggestions based on the current ACD context.

**Usage:**
```
(gdb) ACD-suggest
```

**Example Output:**
```
Debugging Suggestions:
======================================================================
1. 💾 Memory-related code - check for null pointers, buffer overflows
2. 🔗 Verify dependencies are working: INIT_HOOKS, ERROR_HANDLING
3. 📖 Source API reference: allocateManagedMemory() - source_runtime_api.h
4. 📖 Target API reference: backendAllocateManaged() - backend_runtime_api.h

Tip: Use 'info ACD' for full context
```

### TCS Validation Tools

#### ACD Validator

The ACD validator ensures metadata completeness and correctness.

**Usage:**
```bash
python3 scripts/validate_acd.py /path/to/source
```

**Features:**
- Validates all SCIS tags are properly formatted
- Checks for required vs. optional tags
- Verifies dependency chains
- Exports metadata to JSON for AI consumption
- Generates completeness reports

**Example Output:**
```
ACD Validation Report
======================================================================
Total Files Scanned: 42
Files with ACD Metadata: 38
Coverage: 90.5%

Phase Distribution:
  MEMORY_TRANSLATION: 12 functions
  KERNEL_DISPATCH: 8 functions
  STREAM_TRANSLATION: 6 functions
  DEVICE_QUERY: 5 functions
  ERROR_HANDLING: 7 functions

Status Distribution:
  IMPLEMENTED: 35 (92.1%)
  PARTIAL: 2 (5.3%)
  NOT_STARTED: 1 (2.6%)

Issues Found: 2
  Warning: stream_api.cpp:234 missing AI_COMPLEXITY tag
  Warning: event_api.cpp:156 missing AI_DEPENDENCIES tag
```

---

## Part 3: The Traceability & History Standard (THS)

This defines the requirements for **institutional memory**, **complete historical tracking**, and **auditing** to ensure autonomous agents have access to the full context window and reasoning graph of the entire codebase.

**The Critical Difference:** While stateless agents have minimal recall and may only see current documentation or code comments, THS provides the complete history of **every decision ever made** in the repository. This transforms autonomous agents from context-limited tools into systems with comprehensive institutional memory.

THS enables agents to:
- Walk the complete history graph of any code segment
- Understand the reasoning behind every change
- Learn from past successes and failures
- Make decisions informed by the full evolutionary context
- Ensure the development loop is fully closed and continuously self-improving

### THS Components

| Tag / Component | Function | Rationale | Location |
| :--- | :--- | :--- | :--- |
| **`AI_COMMIT`** | **Current Version.** The Git commit hash for the current state of the code. | Links the immediate context to the most recent development decision and reasoning. | Source code SCIS tags |
| **`AI_COMMIT_HISTORY`** | **Full Reasoning History.** The list of previous Git commit hashes for this code segment. | **Closes the loop:** Creates a complete memory trail enabling the system to walk backwards through all changes using git blame and commit history to understand the evolution of a function's implementation, fixes, and reasoning over time. | Source code SCIS tags |
| **Fix Summary Artifacts** | Structured, archived documentation of prior successful resolutions (e.g., `FIX_SUMMARY_PYTORCH.md`). | Serves as the AI's **memory base**, allowing the continuous system to learn from its own past corrective actions and suggest high-confidence patches. | Repository root and `/docs` |
| **ACD Trace Artifact** | The final, standardized diagnostic packet (including the enriched GDB trace, metadata, and error logs). | The standard output payload for autonomous consumption by the next phase agent (e.g., automated fix generation and validation). | `/acd_artifacts` directory |
| **Validation Reports** | Automated build and test results with ACD context enrichment. | Provides continuous feedback on implementation status and regression detection. | `/acd_artifacts` directory |

### THS Artifact Specifications

#### Fix Summary Format

Fix summaries document successful issue resolutions with full context.

**Required Sections:**
1. **Issue Description** - What problem was encountered
2. **Root Cause** - Technical analysis of the underlying issue
3. **Solution** - Implementation details of the fix
4. **Verification** - How the fix was tested and validated
5. **Related ACD Phases** - Which phases were affected
6. **Commit References** - Git commits involved in the fix

**Example:**
```markdown
# Fix Summary: API Context Initialization

## Issue Description
Application failed to initialize device context with error 36 (invalid device).

## Root Cause
- AI_PHASE: DEVICE_QUERY, INIT_HOOKS
- Driver API initialization order incorrect
- Missing symbol versioning for device query function

## Solution
Implemented proper device initialization sequence:
1. Initialize backend runtime first
2. Query device count before device access
3. Add symbol versioning to device query function

## Verification
- Tested with multiple backend implementations
- All basic operations verified
- No regressions in existing tests

## Related ACD Phases
- DEVICE_QUERY (AI_STATUS: IMPLEMENTED)
- INIT_HOOKS (AI_STATUS: IMPLEMENTED)

## Commit References
- Main fix: a3f2d9c
- Follow-up: b7e4a1f
```

#### ACD Trace Artifact Format

ACD trace artifacts capture complete diagnostic context for failures.

**Structure:**
```json
{
  "timestamp": "2025-10-19T14:57:00Z",
  "session_id": "debug_20251019_145700",
  "event_type": "runtime_error",
  "error_info": {
    "code": 36,
    "message": "invalid device",
    "location": {
      "file": "src/device_api.cpp",
      "line": 145,
      "function": "getDevice"
    }
  },
  "acd_context": {
    "AI_PHASE": "DEVICE_QUERY",
    "AI_STATUS": "IMPLEMENTED",
    "AI_COMPLEXITY": "MEDIUM",
    "AI_DEPENDENCIES": ["INIT_HOOKS"],
    "AI_COMMIT": "a3f2d9c",
    "AI_COMMIT_HISTORY": ["b7e4a1f", "e4f9a2d"],
    "SOURCE_API_REF": "getDevice() - source_runtime_api.h",
    "TARGET_API_REF": "backendGetDevice() - backend_runtime_api.h"
  },
  "stack_trace": [...],
  "environment": {
    "backend_version": "5.7.0",
    "api_version": "1.0.0",
    "device_name": "Generic Accelerator Device"
  },
  "related_fixes": [
    "FIX_SUMMARY_FRAMEWORK.md",
    "FIX_DRIVER_API.md"
  ]
}
```

#### Enhanced ACD Metadata Export Format (Cross-Repository Traceability)

The ACD validator exports metadata in an enhanced JSON format that enables cross-repository traceability and historical analysis.

**Structure:**
```json
{
  "metadata": {
    "acd_schema_version": "1.0.0",
    "files_processed": 16,
    "acd_metadata_found": 214,
    "errors": 0,
    "warnings": 42,
    "timestamp_utc": "2025-10-19T17:15:00Z"
  },
  "acd_metadata": [
    {
      "AI_PHASE": "MEMORY_TRANSLATION",
      "AI_STATUS": "IMPLEMENTED",
      "AI_DEPENDENCIES": ["INIT_HOOKS"],
      "SOURCE_API_REF": "allocateMemory() - source_runtime_api.h",
      "TARGET_API_REF": "backendAllocate() - backend_runtime_api.h",
      "AI_NOTE": "Implements memory allocation with backend translation",
      "AI_COMPLEXITY": "MEDIUM",
      "AI_COMMIT": "a3f2d9c",
      "AI_COMMIT_HISTORY": ["b7e4a1f", "e4f9a2d"],
      "repository": "terminills/api_wrapper",
      "file": "/path/to/source/file.cpp",
      "line": 42,
      "timestamp_utc": "2025-10-19T17:15:00Z"
    }
  ],
  "errors": [],
  "warnings": []
}
```

**Key Features:**

1. **Schema Versioning**: `acd_schema_version` enables evolution of the format
2. **Timestamps**: UTC timestamps for metadata and individual blocks
3. **Repository Context**: `repository` field enables cross-repo traceability
4. **Array Format**: `AI_COMMIT_HISTORY` exported as array for easier processing
5. **Comprehensive Metadata**: Complete statistics and validation results

**Usage:**
```bash
python3 scripts/validate_acd.py /path/to/source --export acd_metadata.json
```

This format enables:
- Tracking metadata across multiple repositories
- Temporal analysis of code evolution
- Integration with external monitoring systems
- Aggregation of metadata from different sources

### THS Integration Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    Development Event                             │
│                 (Build, Test, Debug, Fix)                        │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              ACD Context Extraction                              │
│        (From SCIS tags in source code)                           │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              TCS Tool Processing                                 │
│     (GDB, Validator, Compiler Enrichment)                        │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│            ACD Trace Artifact Generation                         │
│    (Structured diagnostic with full context)                     │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│           Autonomous Analysis & Remediation                      │
│      (AI agent consumes trace and suggests fixes)                │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              Fix Summary Documentation                           │
│         (THS artifact for future reference)                      │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│              AI_COMMIT Update in SCIS                            │
│           (Close the loop with git hash)                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Implementation Guidelines

### For Source Code Authors

1. **Always add SCIS metadata** to functions that:
   - Implement API translations
   - Handle complex state management
   - Are error-prone or mission-critical
   - Are part of the development roadmap

2. **Keep metadata current**:
   - Update `AI_STATUS` as implementation progresses
   - Update `AI_COMMIT` after significant changes
   - When updating `AI_COMMIT`, prepend the old commit hash to `AI_COMMIT_HISTORY`
   - Maintain `AI_COMMIT_HISTORY` in chronological order (newest first)
   - Add `AI_NOTE` to explain non-obvious implementation choices

3. **Use consistent phase names**:
   - Refer to project roadmap for standard phase names
   - Use existing phase names before creating new ones
   - Document new phases in the roadmap

### For Tool Developers

1. **Implement TCS interfaces**:
   - Parse SCIS metadata from source files
   - Provide context-aware diagnostic output
   - Generate structured ACD trace artifacts

2. **Enrich error messages**:
   - Link errors to ACD context
   - Suggest next debugging steps based on `AI_STATUS` and `AI_COMPLEXITY`
   - Reference related fix summaries

3. **Generate validation reports**:
   - Check metadata completeness
   - Verify dependency chains
   - Track implementation progress

### For AI Agents

1. **Consume ACD context**:
   - Parse SCIS metadata to understand code intent
   - Use `AI_STATUS` to determine if failures are expected
   - Use `AI_COMPLEXITY` to weight fix confidence

2. **Generate THS artifacts**:
   - Create structured diagnostic traces
   - Document successful fixes as fix summaries
   - Update `AI_COMMIT` tags after changes
   - Update `AI_COMMIT_HISTORY` by prepending old commit hash when modifying code
   - Use commit history to trace function evolution

3. **Learn from history**:
   - Reference past fix summaries for similar issues
   - Use `AI_COMMIT_HISTORY` to walk the complete evolution of a function
   - Combine git blame with commit history to understand why changes were made
   - Build knowledge base of successful remediation patterns
   - Improve suggestions over time

---

## Maintaining AI_COMMIT and AI_COMMIT_HISTORY

### The Foundation of Complete Historical Memory

The `AI_COMMIT` and `AI_COMMIT_HISTORY` fields are **critical** to providing autonomous agents with complete historical context. These fields create an unbroken chain of reasoning and decision-making that transforms stateless agents into systems with full institutional memory.

**Why This Matters:** Without this historical tracking, agents operate in the dark—they see the current code but don't understand the evolution, failed attempts, successful patterns, or reasoning that led to the current state. With complete commit history tracking, agents gain access to the full decision graph of the codebase.

### Workflow for Code Changes

When modifying code with existing ACD metadata, follow this workflow to maintain the commit history trail:

1. **Before Making Changes**: Record the current `AI_COMMIT` value
   ```cpp
   // Current state
   AI_COMMIT: a3f2d9c
   AI_COMMIT_HISTORY: b7e4a1f, e4f9a2d
   ```

2. **Make Your Code Changes**: Modify the implementation as needed

3. **After Committing Changes**: Update both fields
   ```cpp
   // After git commit (new commit: f1a2b3c)
   AI_COMMIT: f1a2b3c
   AI_COMMIT_HISTORY: a3f2d9c, b7e4a1f, e4f9a2d
   ```

### Rules for AI_COMMIT_HISTORY

1. **Prepend, Don't Append**: Always add the old commit to the beginning of the history list
2. **Exclude Current**: The `AI_COMMIT_HISTORY` should NOT include the current `AI_COMMIT` value
3. **Maintain Order**: Keep commits in reverse chronological order (newest → oldest)
4. **No Duplicates**: Don't add the same commit hash multiple times
5. **Start Simple**: For new code, `AI_COMMIT_HISTORY` can be omitted until the second modification

### Benefits of Commit History Tracking: Complete Context for Autonomous Agents

The `AI_COMMIT_HISTORY` field is the backbone of institutional memory in ACD. It provides autonomous agents with capabilities that stateless systems cannot achieve:

**1. Complete Historical Context:** Agents can trace every decision, understanding not just what changed, but why it changed and what alternatives were tried.

**2. Pattern Recognition Across Time:** By walking the history graph, agents identify successful patterns, recurring issues, and evolutionary trends.

**3. Reasoning Reconstruction:** Each commit in the history links to PRs, fix summaries, and discussions—agents can reconstruct the complete reasoning behind any code segment.

**4. Failure Analysis:** Understanding what was tried before prevents repeating failed approaches and enables learning from past mistakes.

The `AI_COMMIT_HISTORY` field enables powerful historical analysis:

1. **Walking the History**: 
   ```bash
   # For each commit in AI_COMMIT_HISTORY
   git show <commit_hash> -- <file>
   git log -p <commit_hash> -- <file>
   ```

2. **Understanding Evolution**:
   ```bash
   # See the sequence of changes
   git blame <file> | grep <function_name>
   # Then walk through each commit in AI_COMMIT_HISTORY
   ```

3. **Finding Related Fixes**:
   ```bash
   # Search for fix summaries related to commits
   git log --all --grep="<commit_hash>"
   find . -name "FIX_*.md" -exec grep -l "<commit_hash>" {} \;
   ```

4. **Regression Analysis**:
   - Compare current implementation with historical versions
   - Identify when bugs were introduced or fixed
   - Understand why certain decisions were made

### Example Evolution Timeline

```cpp
// Initial implementation (commit: e4f9a2d)
/*
 * AI_PHASE: MEMORY_TRANSLATION
 * AI_STATUS: PARTIAL
 * AI_COMMIT: e4f9a2d
 */

// First fix (commit: b7e4a1f)
/*
 * AI_PHASE: MEMORY_TRANSLATION
 * AI_STATUS: IMPLEMENTED
 * AI_COMMIT: b7e4a1f
 * AI_COMMIT_HISTORY: e4f9a2d
 */

// Performance optimization (commit: a3f2d9c)
/*
 * AI_PHASE: MEMORY_TRANSLATION
 * AI_STATUS: IMPLEMENTED
 * AI_COMMIT: a3f2d9c
 * AI_COMMIT_HISTORY: b7e4a1f, e4f9a2d
 */

// Bug fix (commit: f1a2b3c)
/*
 * AI_PHASE: MEMORY_TRANSLATION
 * AI_STATUS: FIXED
 * AI_COMMIT: f1a2b3c
 * AI_COMMIT_HISTORY: a3f2d9c, b7e4a1f, e4f9a2d
 */
```

### Automation Opportunities

The commit history can be automatically maintained:

1. **Pre-commit Hook**: Extract current `AI_COMMIT` and update `AI_COMMIT_HISTORY`
2. **IDE Integration**: Editor plugins to automate metadata updates
3. **CI/CD Validation**: Verify commit history is properly maintained
4. **AI Agent Integration**: Autonomous agents can maintain this automatically

### Using Commit History for Debugging

When debugging a failure in code with `AI_COMMIT_HISTORY`:

```bash
# Get the function's commit history from metadata
CURRENT_COMMIT="f1a2b3c"
HISTORY="a3f2d9c, b7e4a1f, e4f9a2d"

# View current implementation
git show ${CURRENT_COMMIT}:src/memory_api.cpp

# View each previous version
for commit in ${HISTORY//,/ }; do
    echo "=== Version at $commit ==="
    git show ${commit}:src/memory_api.cpp
    git log -1 --format="%H%n%an%n%ad%n%s%n%b" $commit
done

# Find related PRs and fix summaries
for commit in ${CURRENT_COMMIT} ${HISTORY//,/ }; do
    git log --all --grep="$commit" --format="%H %s"
done
```

---

## Appendix A: Complete Tag Reference

### Required SCIS Tags

```cpp
// Minimum viable metadata for any ACD-instrumented code
AI_PHASE: <phase_name>
AI_STATUS: <status_value>
```

### Recommended SCIS Tags

```cpp
// Recommended for production code
AI_PHASE: <phase_name>
AI_STATUS: <status_value>
AI_COMPLEXITY: <complexity_value>
AI_NOTE: <description>
AI_DEPENDENCIES: <comma_separated_phases>
AI_COMMIT: <git_sha>
AI_COMMIT_HISTORY: <comma_separated_previous_git_shas>
```

### Context-Specific SCIS Tags

```cpp
// For API translation code
SOURCE_API_REF: <source_api_reference>
TARGET_API_REF: <target_api_reference>

// For implementation patterns and strategies
AI_PATTERN: <pattern_name>
AI_STRATEGY: <strategy_description>
AI_VERSION: <version_number>

// For development context and changes
AI_CHANGE: <change_description>
AI_TRAIN_HASH: <64_char_hex_hash>
AI_CONTEXT: <json_object>
AI_METADATA: <string_or_json_object>

// For error tracking and fixes
COMPILER_ERR: <compiler_error_message>
RUNTIME_ERR: <runtime_error_message>
FIX_REASON: <fix_explanation>

// For human oversight and review
HUMAN_OVERRIDE: <reviewer_name_and_date>

// For distributed agent coordination
AI_TIMEOUT: <timeout_seconds>
AI_MAX_RETRIES: <retry_count>

// For agent assignment and handoff
AI_ASSIGNED_TO: <agent_id_or_name>
AI_ASSIGNED_BY: <assigner_id>
AI_ASSIGNED_AT: <iso8601_timestamp>
AI_ASSIGNMENT_REASON: <reason_string>
AI_PREVIOUS_ASSIGNEE: <previous_agent_id>
AI_ASSIGNMENT_HISTORY: <array_of_agent_ids>
AI_HANDOFF_REQUESTED: <true_or_false>
AI_HANDOFF_REASON: <reason_string>
AI_HANDOFF_TO: <target_agent_id>
AI_HANDOFF_TYPE: <handoff_type_enum>
AI_HANDOFF_AT: <iso8601_timestamp>
AI_HANDOFF_NOTES: <context_string>
AI_HANDOFF_STATUS: <handoff_status_enum>
AI_REQUIRED_CAPABILITIES: <array_of_capabilities>
AI_PREFERRED_AGENT_TYPE: <agent_type_string>
AI_AGENT_POOL: <array_of_agent_ids>
AI_SKILL_LEVEL_REQUIRED: <skill_level_enum>

// For agent collaboration and communication
AI_CONFIDENCE: <confidence_flag>
AI_REQUEST: <request_flag>
AI_STATE: <state_flag>
AI_QUEUE_PRIORITY: <priority_level>
AI_QUEUE_STATUS: <queue_status>
```

---

## Part 4: Agent Collaboration and Communication Flags

This section defines the communication protocol for multi-agent systems and distributed autonomous development. These flags enable agents to coordinate work, signal confidence levels, request feedback, and manage task queues effectively.

### Communication Flags

Communication flags provide a standardized way for autonomous agents to signal their status, confidence, and needs when working collaboratively. These flags are essential for dual-agent systems, distributed agent networks, and exchange-of-thought protocols.

#### 4.1 Confidence Flags

Express the agent's confidence level in its output. These flags help downstream agents and human reviewers understand the reliability of the work.

| Flag | Meaning | When to Use | Example Usage |
|------|---------|-------------|---------------|
| **`CONFIDENT`** | High confidence, minimal review needed | Solution is well-tested and validated | After comprehensive testing |
| **`UNCERTAIN`** | Unsure, needs validation | Solution needs peer review | Complex implementation |
| **`HYPOTHESIS`** | Speculative guess, low confidence | Experimental or untested approach | Trying new patterns |
| **`VALIDATED`** | Externally verified as correct | Another agent or human confirmed | Post peer-review |
| **`EXPERIMENTAL`** | Highly experimental, may fail | Cutting-edge or risky approach | Research prototypes |

**Implementation:**
```cpp
/*
 * AI_PHASE: MEMORY_OPTIMIZATION
 * AI_STATUS: IMPLEMENTED
 * AI_COMPLEXITY: HIGH
 * AI_NOTE: Cache-aware memory allocation with prefetching
 * AI_CONFIDENCE: UNCERTAIN
 * AI_NOTE_CONFIDENCE: Algorithm shows promise but needs performance validation
 */
```

#### 4.2 Request Flags

Signal the need for feedback, validation, or action from other agents or humans.

| Flag | Meaning | When to Use | Example Usage |
|------|---------|-------------|---------------|
| **`REQUEST_FEEDBACK`** | Needs feedback from another agent | Wants peer validation | Design review needed |
| **`REQUEST_REVIEW`** | Needs human review | Critical changes | Security-sensitive code |
| **`WAITING_FOR_INPUT`** | Waiting for more information | Blocked on external data | Missing requirements |
| **`NEEDS_VALIDATION`** | Requires validation before proceeding | Ready for testing | Pre-deployment check |
| **`NEEDS_APPROVAL`** | Requires explicit approval | Critical decision point | Architecture changes |
| **`REQUEST_ASSISTANCE`** | Unable to proceed alone | Task too complex | Escalation needed |

**Implementation:**
```cpp
/*
 * AI_PHASE: KERNEL_OPTIMIZATION
 * AI_STATUS: PARTIAL
 * AI_COMPLEXITY: CRITICAL
 * AI_NOTE: Optimized kernel launch parameters
 * AI_REQUEST: REQUEST_FEEDBACK
 * AI_REQUEST_FROM: performance_analysis_agent
 * AI_NOTE_REQUEST: Need performance profiling before finalizing parameters
 */
```

#### 4.3 State Flags

Indicate current processing state and task lifecycle position.

| Flag | Meaning | When to Use | Example Usage |
|------|---------|-------------|---------------|
| **`PROCESSING`** | Actively working on task | Work in progress | During implementation |
| **`READY`** | Task completed, ready for next step | Output ready for review | Awaiting validation |
| **`DONE`** | Fully completed, no further action needed | Work complete | Final state |
| **`BLOCKED`** | Cannot proceed without external input | Requires intervention | Dependency issue |
| **`PAUSED`** | Temporarily suspended | Awaiting resource | Resource contention |
| **`FAILED`** | Task failed and cannot proceed | Critical error | Unrecoverable error |
| **`CANCELLED`** | Task cancelled by request | User/system cancel | Superseded work |

**Implementation:**
```cpp
/*
 * AI_PHASE: DATA_VALIDATION
 * AI_STATUS: IMPLEMENTED
 * AI_STATE: READY
 * AI_NOTE: Validation complete, ready for integration testing
 */
```

### Queuing Flags

Queuing flags enable distributed agent systems to manage task priorities, coordinate work assignments, and track progress through processing pipelines.

#### 4.4 Queue Priority Flags

Control task prioritization in agent work queues.

| Flag | Meaning | Priority Level | Use Case |
|------|---------|----------------|----------|
| **`CRITICAL`** | Highest priority, process immediately | 0 | Security vulnerabilities, system failures |
| **`HIGH`** | High priority, process soon | 1 | Critical bugs, blocking issues |
| **`NORMAL`** | Standard priority | 2 | Regular development tasks |
| **`LOW`** | Low priority, process when able | 3 | Code cleanup, documentation |
| **`DEFERRED`** | Lowest priority, future work | 4 | Nice-to-have features |

**Implementation:**
```cpp
/*
 * AI_PHASE: SECURITY_PATCH
 * AI_STATUS: NOT_STARTED
 * AI_COMPLEXITY: CRITICAL
 * AI_QUEUE_PRIORITY: CRITICAL
 * AI_QUEUE_REASON: Security vulnerability CVE-2025-XXXXX
 * AI_ASSIGNED_TO: security_specialist_agent
 */
```

#### 4.5 Queue Status Flags

Track the progress of tasks through processing queues.

| Flag | Meaning | Description |
|------|---------|-------------|
| **`QUEUED`** | Task is in queue, not started | Waiting for agent availability |
| **`ASSIGNED`** | Task assigned to specific agent | Agent claimed the task |
| **`IN_PROGRESS`** | Task is being processed | Active work |
| **`REVIEW_PENDING`** | Work complete, awaiting review | In review queue |
| **`REVIEW_IN_PROGRESS`** | Under active review | Being validated |
| **`APPROVED`** | Review passed, ready to merge | Quality gate passed |
| **`REJECTED`** | Review failed, needs rework | Quality gate failed |
| **`COMPLETED`** | Fully done and integrated | Final state |
| **`ABANDONED`** | Task abandoned/cancelled | Will not be completed |

**Implementation:**
```cpp
/*
 * AI_PHASE: API_MIGRATION
 * AI_STATUS: PARTIAL
 * AI_QUEUE_STATUS: IN_PROGRESS
 * AI_QUEUE_PRIORITY: HIGH
 * AI_ASSIGNED_TO: migration_agent_03
 * AI_STARTED: 2025-10-20T14:30:00Z
 * AI_ESTIMATED_COMPLETION: 2025-10-20T16:00:00Z
 */
```

#### 4.6 Agent Assignment and Handoff

Enable sophisticated task routing, agent assignment, and handoff workflows in distributed agent systems.

##### Assignment Tags

| Tag | Type | Description | Example |
|-----|------|-------------|---------|
| **`AI_ASSIGNED_TO`** | String | Current agent assigned to this task | `migration_agent_03` |
| **`AI_ASSIGNED_BY`** | String | Agent or system that made the assignment | `orchestrator_agent` |
| **`AI_ASSIGNED_AT`** | ISO 8601 DateTime | When the task was assigned | `2025-10-20T14:30:00Z` |
| **`AI_ASSIGNMENT_REASON`** | String | Why this agent was chosen | `Specializes in API migration` |
| **`AI_PREVIOUS_ASSIGNEE`** | String | Previous agent (for handoff tracking) | `general_agent_01` |
| **`AI_ASSIGNMENT_HISTORY`** | Array of Strings | Complete assignment chain | `["agent_01", "agent_02"]` |

##### Handoff Tags

| Tag | Type | Description | Example |
|-----|------|-------------|---------|
| **`AI_HANDOFF_REQUESTED`** | Boolean | Whether handoff is requested | `true` |
| **`AI_HANDOFF_REASON`** | String | Reason for handoff request | `Task complexity exceeds capability` |
| **`AI_HANDOFF_TO`** | String | Specific agent requested for handoff | `expert_agent_05` |
| **`AI_HANDOFF_TYPE`** | Enum | Type of handoff | `ESCALATION`, `SPECIALIZATION`, `LOAD_BALANCE`, `FAILURE` |
| **`AI_HANDOFF_AT`** | ISO 8601 DateTime | When handoff occurred | `2025-10-20T15:45:00Z` |
| **`AI_HANDOFF_NOTES`** | String | Context for next agent | `Completed initial analysis, needs optimization` |
| **`AI_HANDOFF_STATUS`** | Enum | Handoff workflow state | `REQUESTED`, `ACCEPTED`, `REJECTED`, `COMPLETED` |

##### Capability Matching Tags

| Tag | Type | Description | Example |
|-----|------|-------------|---------|
| **`AI_REQUIRED_CAPABILITIES`** | Array of Strings | Required agent capabilities | `["python", "security", "cryptography"]` |
| **`AI_PREFERRED_AGENT_TYPE`** | String | Preferred agent specialization | `security_specialist` |
| **`AI_AGENT_POOL`** | Array of Strings | Eligible agents for assignment | `["agent_05", "agent_07", "agent_12"]` |
| **`AI_SKILL_LEVEL_REQUIRED`** | Enum | Minimum skill level needed | `NOVICE`, `INTERMEDIATE`, `EXPERT`, `SPECIALIST` |

**Handoff Type Values:**

| Type | Meaning | When to Use |
|------|---------|-------------|
| **`ESCALATION`** | Task is too difficult | Current agent lacks expertise |
| **`SPECIALIZATION`** | Needs specialized skills | Requires domain expertise |
| **`LOAD_BALANCE`** | Distribute workload | Agent overloaded |
| **`FAILURE`** | Previous attempt failed | Need fresh perspective |
| **`COMPLETION`** | Phase complete, next phase needs different agent | Sequential workflow |
| **`COLLABORATION`** | Multiple agents needed | Complex multi-faceted task |

**Example: Initial Assignment**
```cpp
/*
 * AI_PHASE: DATABASE_OPTIMIZATION
 * AI_STATUS: NOT_STARTED
 * AI_QUEUE_STATUS: ASSIGNED
 * AI_QUEUE_PRIORITY: HIGH
 * AI_ASSIGNED_TO: database_agent_03
 * AI_ASSIGNED_BY: orchestrator_agent
 * AI_ASSIGNED_AT: 2025-10-20T10:00:00Z
 * AI_ASSIGNMENT_REASON: Agent specializes in query optimization
 * AI_REQUIRED_CAPABILITIES: ["sql", "performance_analysis", "indexing"]
 * AI_SKILL_LEVEL_REQUIRED: EXPERT
 * AI_STATE: READY
 */
```

**Example: Escalation Handoff**
```cpp
/*
 * AI_PHASE: DATABASE_OPTIMIZATION
 * AI_STATUS: PARTIAL
 * AI_QUEUE_STATUS: IN_PROGRESS
 * AI_ASSIGNED_TO: database_agent_03
 * AI_PREVIOUS_ASSIGNEE: general_agent_01
 * AI_ASSIGNMENT_HISTORY: ["general_agent_01"]
 * AI_HANDOFF_REQUESTED: true
 * AI_HANDOFF_REASON: Query performance issues require specialized expertise
 * AI_HANDOFF_TYPE: ESCALATION
 * AI_HANDOFF_TO: senior_database_specialist_01
 * AI_HANDOFF_AT: 2025-10-20T14:30:00Z
 * AI_HANDOFF_NOTES: Initial analysis complete, found N+1 query problem, needs index strategy
 * AI_HANDOFF_STATUS: REQUESTED
 * AI_STATE: BLOCKED
 */
```

**Example: Completed Handoff**
```cpp
/*
 * AI_PHASE: DATABASE_OPTIMIZATION
 * AI_STATUS: IMPLEMENTED
 * AI_QUEUE_STATUS: COMPLETED
 * AI_ASSIGNED_TO: senior_database_specialist_01
 * AI_PREVIOUS_ASSIGNEE: database_agent_03
 * AI_ASSIGNMENT_HISTORY: ["general_agent_01", "database_agent_03"]
 * AI_HANDOFF_STATUS: COMPLETED
 * AI_HANDOFF_TYPE: ESCALATION
 * AI_HANDOFF_AT: 2025-10-20T14:30:00Z
 * AI_NOTE: Implemented composite index strategy, reduced query time by 85%
 * AI_STATE: DONE
 * AI_CONFIDENCE: CONFIDENT
 */
```

**Example: Collaborative Handoff**
```cpp
/*
 * AI_PHASE: SECURITY_AUDIT
 * AI_STATUS: PARTIAL
 * AI_QUEUE_STATUS: IN_PROGRESS
 * AI_ASSIGNED_TO: security_analysis_agent
 * AI_HANDOFF_REQUESTED: true
 * AI_HANDOFF_REASON: Need cryptography expert for encryption review
 * AI_HANDOFF_TYPE: COLLABORATION
 * AI_HANDOFF_TO: cryptography_specialist_02
 * AI_HANDOFF_NOTES: Authentication flow reviewed and approved, encryption implementation needs specialist review
 * AI_REQUIRED_CAPABILITIES: ["cryptography", "tls", "certificate_management"]
 * AI_NOTE: Parallel work - continuing with authorization audit while encryption reviewed
 * AI_STATE: PROCESSING
 */
```

**Example: Load Balance Handoff**
```cpp
/*
 * AI_PHASE: UNIT_TEST_GENERATION
 * AI_STATUS: NOT_STARTED
 * AI_QUEUE_STATUS: QUEUED
 * AI_QUEUE_PRIORITY: NORMAL
 * AI_ASSIGNED_TO: test_generation_agent_02
 * AI_ASSIGNED_BY: load_balancer_agent
 * AI_ASSIGNMENT_REASON: Agent 01 at capacity, routing to available agent
 * AI_HANDOFF_TYPE: LOAD_BALANCE
 * AI_PREVIOUS_ASSIGNEE: test_generation_agent_01
 * AI_HANDOFF_AT: 2025-10-20T11:15:00Z
 * AI_STATE: READY
 */
```

##### Assignment Workflow States

The typical workflow for agent assignment and handoff:

```
┌─────────────┐
│   QUEUED    │ - Task enters queue, no assignment yet
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  ASSIGNED   │ - AI_ASSIGNED_TO set, agent claimed task
└──────┬──────┘
       │
       ▼
┌─────────────┐
│IN_PROGRESS  │ - AI_STATE: PROCESSING, active work
└──────┬──────┘
       │
       ├─────► Need Handoff? ─────┐
       │                           │
       │                           ▼
       │                    ┌──────────────┐
       │                    │   BLOCKED    │ - AI_HANDOFF_REQUESTED: true
       │                    └──────┬───────┘
       │                           │
       │                           ▼
       │                    ┌──────────────┐
       │                    │  REASSIGNED  │ - New AI_ASSIGNED_TO
       │                    └──────┬───────┘
       │                           │
       │                           ▼
       │                    ┌──────────────┐
       │                    │IN_PROGRESS   │ - New agent continues
       │                    └──────┬───────┘
       │                           │
       ▼                           ▼
┌─────────────┐           ┌──────────────┐
│ COMPLETED   │◄──────────│  COMPLETED   │
└─────────────┘           └──────────────┘
```

##### Best Practices for Assignment and Handoff

1. **Track Assignment History**: Always maintain `AI_ASSIGNMENT_HISTORY` for full traceability
2. **Document Handoff Reasons**: Use `AI_HANDOFF_REASON` to explain why handoff is needed
3. **Provide Context**: Use `AI_HANDOFF_NOTES` to give the next agent complete context
4. **Specify Capabilities**: Use `AI_REQUIRED_CAPABILITIES` to ensure proper agent selection
5. **Update State**: Set `AI_STATE: BLOCKED` when waiting for handoff acceptance
6. **Complete the Loop**: Update `AI_HANDOFF_STATUS: COMPLETED` when handoff is done
7. **Timestamp Everything**: Use `AI_ASSIGNED_AT` and `AI_HANDOFF_AT` for audit trail
8. **Enable Collaboration**: Use `AI_HANDOFF_TYPE: COLLABORATION` for parallel work

### Dual-Agent Exchange Protocol

For systems implementing dual-agent or multi-agent collaboration, these additional tags support structured exchange-of-thought protocols.

#### 4.7 Dual-Agent Communication Tags

| Tag | Purpose | Phase | Example Value |
|-----|---------|-------|---------------|
| **`AI_VALIDATION`** | Validation status from reviewer agent | Review | `ANALYZED`, `APPROVED`, `REJECTED` |
| **`AI_ISSUES`** | Issues identified by reviewer | Review | Array of issue descriptions |
| **`AI_SUGGESTIONS`** | Suggestions from reviewer | Review | Array of suggestions |
| **`AI_REFINEMENT`** | Refinement status | Refinement | `APPLIED`, `IN_PROGRESS`, `PENDING` |
| **`AI_CHANGES`** | Changes made during refinement | Refinement | Description of changes |
| **`AI_RATIONALE`** | Reasoning for changes | Refinement | Explanation of decisions |
| **`AI_VALIDATION_RESULT`** | Final validation result | Final Review | `APPROVED`, `NEEDS_MORE_WORK` |
| **`AI_APPROVAL`** | Approval status | Final Review | `YES`, `NO`, `CONDITIONAL` |
| **`AI_EXCHANGE_ID`** | Unique exchange session identifier | All Phases | UUID or session ID |
| **`AI_ROUND`** | Exchange iteration number | All Phases | Integer (1, 2, 3...) |

**Example: Generator Agent Output**
```python
# AI_PHASE: ERROR_HANDLING
# AI_STATUS: GENERATED
# AI_COMPLEXITY: MEDIUM
# AI_NOTE: Generated error handling for file operations
# AI_CONFIDENCE: UNCERTAIN
# AI_REQUEST: NEEDS_VALIDATION
# AI_STATE: READY
# AI_EXCHANGE_ID: exchange_20251020_001
# AI_ROUND: 1
def handle_file_error(error):
    print(f"Error: {error}")
```

**Example: Reviewer Agent Analysis**
```python
# AI_EXCHANGE_ID: exchange_20251020_001
# AI_ROUND: 1
# AI_VALIDATION: ANALYZED
# AI_ISSUES: ["No error logging", "Missing exception handling", "No return value"]
# AI_SUGGESTIONS: ["Add logging.error() call", "Wrap in try-except", "Return boolean status"]
# AI_CONFIDENCE: CONFIDENT
# AI_STATE: READY
```

**Example: Generator Agent Refinement**
```python
# AI_PHASE: ERROR_HANDLING
# AI_STATUS: REFINED
# AI_COMPLEXITY: MEDIUM
# AI_NOTE: Refined error handling with logging and exception handling
# AI_REFINEMENT: APPLIED
# AI_CHANGES: Added logging, exception handling, return value
# AI_RATIONALE: Addressed issues identified by reviewer
# AI_CONFIDENCE: CONFIDENT
# AI_REQUEST: NEEDS_VALIDATION
# AI_STATE: READY
# AI_EXCHANGE_ID: exchange_20251020_001
# AI_ROUND: 2
import logging

def handle_file_error(error):
    try:
        logging.error(f"File operation failed: {error}")
        return False
    except Exception as e:
        logging.critical(f"Error handling failed: {e}")
        return False
```

**Example: Final Validation**
```python
# AI_EXCHANGE_ID: exchange_20251020_001
# AI_ROUND: 2
# AI_VALIDATION_RESULT: APPROVED
# AI_APPROVAL: YES
# AI_CONFIDENCE: CONFIDENT
# AI_STATE: DONE
# AI_NOTE: All issues resolved, implementation meets requirements
```

### Integration with Existing SCIS Tags

The communication and queuing flags complement the existing SCIS tags. Here's how they work together:

**Complete Example with All Tag Types:**
```cpp
/*
 * SCIS Core Tags
 * AI_PHASE: MEMORY_TRANSLATION
 * AI_STATUS: IMPLEMENTED
 * AI_COMPLEXITY: HIGH
 * AI_NOTE: Translates CUDA memory operations to ROCm equivalents
 * AI_DEPENDENCIES: MEMORY_ALLOCATION, ERROR_HANDLING
 * AI_COMMIT: abc123def
 * AI_COMMIT_HISTORY: def456abc, xyz789ghi
 * 
 * API Translation Tags
 * SOURCE_API_REF: cudaMalloc (CUDA Runtime API 11.0)
 * TARGET_API_REF: hipMalloc (ROCm HIP API 5.0)
 * 
 * Communication Flags
 * AI_CONFIDENCE: CONFIDENT
 * AI_STATE: DONE
 * 
 * Queuing Flags (if in distributed system)
 * AI_QUEUE_STATUS: COMPLETED
 * AI_QUEUE_PRIORITY: NORMAL
 * AI_ASSIGNED_TO: memory_specialist_agent_02
 * 
 * Dual-Agent Tags (if using exchange protocol)
 * AI_VALIDATION_RESULT: APPROVED
 * AI_APPROVAL: YES
 * AI_EXCHANGE_ID: exchange_20251019_045
 * AI_ROUND: 2
 */
hipError_t translateCudaMalloc(void** devPtr, size_t size) {
    return hipMalloc(devPtr, size);
}
```

### Best Practices for Communication Flags

1. **Be Honest About Confidence**: Use `UNCERTAIN` or `HYPOTHESIS` when appropriate
2. **Request Help Early**: Don't wait until stuck to use `REQUEST_ASSISTANCE`
3. **Update State Regularly**: Keep `AI_STATE` current for task tracking
4. **Prioritize Correctly**: Use `QUEUE_PRIORITY` appropriately to avoid priority inflation
5. **Document Exchanges**: Maintain `AI_EXCHANGE_ID` and `AI_ROUND` for traceability
6. **Close the Loop**: Always update to `DONE` or `COMPLETED` when finished
7. **Track Assignments**: Use `AI_ASSIGNED_TO` to prevent duplicate work

### Use Cases

#### Use Case 1: Distributed Build System
```cpp
/*
 * AI_PHASE: COMPILATION
 * AI_STATUS: PARTIAL
 * AI_QUEUE_STATUS: ASSIGNED
 * AI_QUEUE_PRIORITY: HIGH
 * AI_ASSIGNED_TO: build_agent_07
 * AI_STATE: PROCESSING
 * AI_STARTED: 2025-10-20T10:15:00Z
 * AI_TIMEOUT: 600
 * AI_NOTE: Compiling core kernel modules
 */
```

#### Use Case 2: Code Review Pipeline
```cpp
/*
 * AI_PHASE: SECURITY_AUDIT
 * AI_STATUS: IMPLEMENTED
 * AI_CONFIDENCE: CONFIDENT
 * AI_REQUEST: REQUEST_REVIEW
 * AI_STATE: READY
 * AI_QUEUE_STATUS: REVIEW_PENDING
 * AI_NOTE: Security-critical authentication module
 */
```

#### Use Case 3: Collaborative Problem Solving
```cpp
/*
 * AI_PHASE: OPTIMIZATION
 * AI_STATUS: PARTIAL
 * AI_CONFIDENCE: HYPOTHESIS
 * AI_REQUEST: REQUEST_FEEDBACK
 * AI_REQUEST_FROM: performance_analysis_agent
 * AI_STATE: BLOCKED
 * AI_NOTE: Experimental caching strategy, needs performance validation
 */
```

---

## Appendix B: Example Implementations

### Example 1: Simple API Translation

```cpp
/*
 * AI_PHASE: MEMORY_TRANSLATION
 * AI_STATUS: IMPLEMENTED
 * AI_COMPLEXITY: LOW
 * AI_NOTE: Direct translation for basic memory allocation
 * AI_DEPENDENCIES: INIT_HOOKS, ERROR_HANDLING
 * AI_COMMIT: e4f9a2d
 * AI_COMMIT_HISTORY: a1b2c3d, f5e6d7c
 * SOURCE_API_REF: allocateMemory(void** devPtr, size_t size)
 * TARGET_API_REF: backendAllocate(void** ptr, size_t size)
 */
api_error_t allocateMemory(void** devPtr, size_t size) {
    backend_error_t backend_result = backendAllocate(devPtr, size);
    return backendErrorToApiError(backend_result);
}
```

### Example 2: Complex Implementation

```cpp
/*
 * AI_PHASE: KERNEL_DISPATCH
 * AI_STATUS: IMPLEMENTED
 * AI_COMPLEXITY: HIGH
 * AI_NOTE: Complex kernel launch with dynamic shared memory and stream management
 * AI_DEPENDENCIES: STREAM_TRANSLATION, MEMORY_TRANSLATION, EVENT_MANAGEMENT
 * AI_COMMIT: b3c7e1f
 * AI_COMMIT_HISTORY: d8a9b0c, c7e6d5a, b4f3e2d
 * SOURCE_API_REF: launchKernel(const void* func, dim3 gridDim, dim3 blockDim, 
 *                               void** args, size_t sharedMem, stream_t stream)
 * TARGET_API_REF: backendLaunchKernel(const void* function_address, dim3 numBlocks, 
 *                                      dim3 dimBlocks, void** args, size_t sharedMemBytes, 
 *                                      backend_stream_t stream)
 */
api_error_t launchKernel(const void* func, dim3 gridDim, dim3 blockDim,
                         void** args, size_t sharedMem, stream_t stream) {
    // Convert API stream to backend stream
    backend_stream_t backend_stream = apiStreamToBackendStream(stream);
    
    // Launch kernel with backend
    backend_error_t backend_result = backendLaunchKernel(
        func, gridDim, blockDim, args, sharedMem, backend_stream
    );
    
    return backendErrorToApiError(backend_result);
}
```

### Example 3: Partial Implementation

```cpp
/*
 * AI_PHASE: GRAPH_TRANSLATION
 * AI_STATUS: PARTIAL
 * AI_COMPLEXITY: CRITICAL
 * AI_NOTE: Graph capture implementation in progress - basic structure only
 * AI_DEPENDENCIES: KERNEL_DISPATCH, STREAM_TRANSLATION, EVENT_MANAGEMENT
 * AI_COMMIT: a9f4c2e
 * AI_COMMIT_HISTORY: e1d2c3b
 * SOURCE_API_REF: createGraph(graph_t* pGraph, unsigned int flags)
 * TARGET_API_REF: backendGraphCreate(backend_graph_t* pGraph, unsigned int flags)
 */
api_error_t createGraph(graph_t* pGraph, unsigned int flags) {
    // TODO: Implement full graph creation logic
    // Current implementation is basic wrapper only
    backend_graph_t backend_graph;
    backend_error_t backend_result = backendGraphCreate(&backend_graph, flags);
    
    if (backend_result == BACKEND_SUCCESS) {
        *pGraph = (graph_t)backend_graph;
    }
    
    return backendErrorToApiError(backend_result);
}
```

### Example 4: Comprehensive Metadata with Error Context

This example shows extensive metadata including error tracking, pattern identification, and human oversight.

```cpp
/*
 * AI_PHASE: KERNEL_DISPATCH
 * AI_STATUS: FIXED
 * AI_COMPLEXITY: HIGH
 * AI_PATTERN: KERNEL_LAUNCH_V1
 * AI_STRATEGY: Wrap source API into backend API with explicit stream handling
 * AI_NOTE: Fixed argument marshaling for dim3 grid and block translation
 * AI_DEPENDENCIES: STREAM_TRANSLATION, MEMORY_TRANSLATION
 * AI_COMMIT: f9a8b7c
 * AI_COMMIT_HISTORY: d6e5f4c, a3b2c1d
 * AI_VERSION: 1.1
 * AI_CHANGE: Added stream argument placeholder, fixed dim3 translation
 * AI_TRAIN_HASH: 493cfb56d3ab3f27b6f99c7f7d48b9179c4a1d5b36e9fa04977a4218f82364df
 * AI_CONTEXT: { "dim3_translation": true, "pending_validation": false, "priority": "high" }
 * SOURCE_API_REF: launchKernel() - source_runtime_api.h
 * TARGET_API_REF: backendModuleLaunchKernel() - backend_runtime_api.h
 * COMPILER_ERR: error: too few arguments to function 'backendModuleLaunchKernel'
 * FIX_REASON: Backend API requires explicit stream argument
 * HUMAN_OVERRIDE: Reviewed by T. Deters on 2025-10-17
 */
api_error_t launchKernel(const void *func, dim3 gridDim, dim3 blockDim,
                         void **args, size_t sharedMem, stream_t stream) {
    return backendModuleLaunchKernel((backend_function_t)func, 
                                     gridDim.x, gridDim.y, gridDim.z,
                                     blockDim.x, blockDim.y, blockDim.z,
                                     sharedMem, stream, args, nullptr);
}
```

### Example 5: Distributed Agent Coordination

This example shows fields used for distributed agent systems.

```cpp
/*
 * AI_PHASE: MEMORY_TRANSLATION
 * AI_STATUS: PARTIAL
 * AI_COMPLEXITY: MEDIUM
 * AI_NOTE: Implementation in progress by distributed agent system
 * AI_DEPENDENCIES: INIT_HOOKS
 * AI_COMMIT: c4d5e6f
 * AI_ASSIGNED_TO: agent_memory_specialist_01
 * AI_TIMEOUT: 300
 * AI_MAX_RETRIES: 3
 * AI_CONTEXT: { "agent_session": "session_123", "retry_count": 0 }
 * SOURCE_API_REF: copyMemoryAsync() - source_runtime_api.h
 * TARGET_API_REF: backendMemcpyAsync() - backend_runtime_api.h
 */
api_error_t copyMemoryAsync(void* dst, const void* src, size_t count,
                            enum memcpy_kind_t kind, stream_t stream) {
    // Implementation being completed by assigned agent
    backend_memcpy_kind_t backend_kind = memcpyKindToBackendMemcpyKind(kind);
    return backendMemcpyAsync(dst, src, count, backend_kind, stream);
}
```

---

## Appendix C: Version History

| Version | Date | Changes |
| :--- | :--- | :--- |
| 1.0 | 2025-10-19 | Initial ACD Standard Specification release. Added comprehensive SCIS, TCS, and THS specifications. |
| 1.1 | 2025-11-01 | Added Agent Collaboration and Communication Flags. Added Queuing Flags for distributed agent coordination. Added Dual-Agent Exchange Protocol support. Extended JSON schema with new flag definitions. |

---

## References

- GDB Extension Implementation: `scripts/gdb_acd.py`
- ACD Validator Tool: `scripts/validate_acd.py`
- Compiler Error Enrichment: `scripts/enrich_compiler_errors.py`
- Implementation Guide: `ACD_IMPLEMENTATION_GUIDE.md`
- Project Roadmap: `ROADMAP.md`
- Fix Summaries: `FIX_SUMMARY_*.md` files

---

## Copyright and Licensing

**© 2025 Timothy Deters / The RECALL Institute for Autonomous Continuous Development**

This specification and all associated materials are licensed under the **GNU General Public License v3.0** (GPL v3) or a commercial license obtainable from The RECALL Institute for Autonomous Continuous Development.

**Dual Licensing:**
- **GPL v3**: You may use, modify, and distribute this specification and its implementations under the terms of the GPL v3. See the [LICENSE](LICENSE) file for the full license text.
- **Commercial License**: Use of this specification or any derivative work under terms other than the GPL v3 requires a commercial license. Contact The RECALL Institute for Autonomous Continuous Development for licensing inquiries.

**Patent Notice:**  
Patent Pending: U.S. Application No. 63/898,838

**Document Status:** ✅ Active Standard  
**Adoption Status:** Reference implementation available  
**Version:** 1.0 — Autonomous Continuous Development (ACD) Standard Specification
