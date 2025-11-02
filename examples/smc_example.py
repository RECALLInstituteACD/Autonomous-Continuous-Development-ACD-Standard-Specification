#!/usr/bin/env python3
"""
Example SMC Coordinator Usage

This script demonstrates the Small Model Coordinator (SMC) system in action,
showing how agents communicate via structured JSON output and how the coordinator
manages agent handoff using AI_STATE, AI_HANDOFF_REQUESTED, and AI_QUEUE_STATUS flags.

AI_PHASE: EXAMPLE_IMPLEMENTATION
AI_STATUS: IMPLEMENTED
AI_COMPLEXITY: MEDIUM
AI_NOTE: Complete demonstration of SMC coordinator with agent handoff
AI_DEPENDENCIES: AGENT_COORDINATION, AGENT_IMPLEMENTATION

Copyright (C) 2025 Timothy Deters / R.E.C.A.L.L. Foundation

This file is part of the ACD Specification.
"""

import sys
import json
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from smc_coordinator import SMCCoordinator, GlobalStatus, AgentState, QueueStatus
from example_agents import ReasoningAgent, TesterAgent, FinalizerAgent, BuilderAgent


def demo_basic_coordination():
    """
    Demonstrate basic SMC coordination with agent handoff.
    
    AI_PHASE: EXAMPLE_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: MEDIUM
    AI_NOTE: Shows simple coordination loop
    """
    print("=" * 80)
    print("SMC Coordinator - Basic Coordination Demo")
    print("=" * 80)
    print()
    
    # Initialize coordinator
    coordinator = SMCCoordinator()
    
    # Register agents
    coordinator.register_agent("ReasoningAgent", ReasoningAgent())
    coordinator.register_agent("TesterAgent", TesterAgent())
    coordinator.register_agent("FinalizerAgent", FinalizerAgent())
    coordinator.register_agent("BuilderAgent", BuilderAgent())
    
    # Set up initial state with some errors
    coordinator.global_status.top_errors = [
        "ImportError: No module named 'numpy'",
        "SyntaxError: unexpected EOF while parsing"
    ]
    coordinator.global_status.error_count = 2
    coordinator.global_status.ai_state = AgentState.READY
    coordinator.global_status.ai_handoff_requested = True
    
    print("Initial Global Status:")
    print(json.dumps(coordinator.global_status.to_dict(), indent=2))
    print()
    
    # Run coordination loop
    print("Running coordination loop...")
    print()
    result = coordinator.run_coordination_loop(max_iterations=5)
    
    # Print results
    print("=" * 80)
    print("Coordination Results")
    print("=" * 80)
    print()
    print(f"Total Iterations: {result['total_iterations']}")
    print()
    print("Final State:")
    print(json.dumps(result['final_state'], indent=2))
    print()
    print("Execution Log:")
    for entry in result['execution_log']:
        print("-" * 80)
        print(json.dumps(entry, indent=2))
    print()


def demo_routing_prompt():
    """
    Demonstrate State Routing prompt generation.
    
    AI_PHASE: EXAMPLE_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: LOW
    AI_NOTE: Shows routing prompt structure
    """
    print("=" * 80)
    print("SMC Coordinator - State Routing Prompt Demo")
    print("=" * 80)
    print()
    
    coordinator = SMCCoordinator()
    coordinator.register_agent("ReasoningAgent", ReasoningAgent())
    coordinator.register_agent("TesterAgent", TesterAgent())
    coordinator.register_agent("FinalizerAgent", FinalizerAgent())
    
    # Generate routing prompt
    prompt = coordinator.state_routing_prompt(coordinator.global_status)
    
    print("State Routing Prompt:")
    print(prompt)
    print()
    
    # Execute routing
    decision = coordinator.execute_routing()
    print("Routing Decision:")
    print(f"  Next Agent: {decision.next_agent}")
    print(f"  Rationale: {decision.rationale}")
    print()


def demo_triage_prompt():
    """
    Demonstrate Fix Triage prompt generation.
    
    AI_PHASE: EXAMPLE_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: LOW
    AI_NOTE: Shows triage prompt structure
    """
    print("=" * 80)
    print("SMC Coordinator - Fix Triage Prompt Demo")
    print("=" * 80)
    print()
    
    coordinator = SMCCoordinator()
    
    # Sample errors
    errors = [
        "ImportError: No module named 'numpy'",
        "SyntaxError: unexpected EOF while parsing",
        "TypeError: unsupported operand type(s) for +: 'int' and 'str'",
        "NameError: name 'variable_x' is not defined",
        "AttributeError: 'NoneType' object has no attribute 'value'"
    ]
    
    # Generate triage prompt
    prompt = coordinator.fix_triage_prompt(errors)
    
    print("Fix Triage Prompt:")
    print(prompt)
    print()
    
    # Execute triage
    decision = coordinator.execute_triage(errors)
    print("Triage Decision:")
    print(f"  Action: {decision.action}")
    print(f"  Context Focus: {decision.context_focus}")
    print()


def demo_final_decision_prompt():
    """
    Demonstrate Final Decision prompt generation.
    
    AI_PHASE: EXAMPLE_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: LOW
    AI_NOTE: Shows final decision prompt structure
    """
    print("=" * 80)
    print("SMC Coordinator - Final Decision Prompt Demo")
    print("=" * 80)
    print()
    
    coordinator = SMCCoordinator()
    
    # Scenario 1: High success rates
    print("Scenario 1: High Success Rates")
    coordinator.global_status.build_success_rate = 0.98
    coordinator.global_status.test_success_rate = 0.95
    
    prompt = coordinator.final_decision_prompt(0.98, 0.95)
    print("Final Decision Prompt:")
    print(prompt)
    print()
    
    decision = coordinator.execute_final_decision()
    print("Final Decision:")
    print(f"  Commit Required: {decision.commit_required}")
    print(f"  Next Agent: {decision.next_agent}")
    print(f"  Rationale: {decision.rationale}")
    print()
    
    # Scenario 2: Low success rates
    print("Scenario 2: Low Success Rates")
    coordinator.global_status.build_success_rate = 0.75
    coordinator.global_status.test_success_rate = 0.80
    
    decision = coordinator.execute_final_decision()
    print("Final Decision:")
    print(f"  Commit Required: {decision.commit_required}")
    print(f"  Next Agent: {decision.next_agent}")
    print(f"  Rationale: {decision.rationale}")
    print()


def demo_agent_structured_output():
    """
    Demonstrate structured output from agents.
    
    AI_PHASE: EXAMPLE_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: LOW
    AI_NOTE: Shows structured JSON output from agents
    """
    print("=" * 80)
    print("Agent Structured Output Demo")
    print("=" * 80)
    print()
    
    # Create global status with errors
    global_status = GlobalStatus(
        last_action="BUILD",
        last_agent="BuilderAgent",
        last_result="FAILURE",
        ai_state=AgentState.BLOCKED,
        ai_queue_status=QueueStatus.REJECTED,
        ai_handoff_requested=True,
        top_errors=[
            "ImportError: No module named 'numpy'",
            "SyntaxError: unexpected EOF while parsing"
        ]
    )
    
    # Test ReasoningAgent
    print("ReasoningAgent Structured Output:")
    print("-" * 80)
    reasoning_agent = ReasoningAgent()
    result = reasoning_agent.execute(global_status)
    print(json.dumps(result, indent=2))
    print()
    
    # Test TesterAgent
    print("TesterAgent Structured Output:")
    print("-" * 80)
    tester_agent = TesterAgent()
    result = tester_agent.execute(global_status)
    print(json.dumps(result, indent=2))
    print()
    
    # Test BuilderAgent
    print("BuilderAgent Structured Output:")
    print("-" * 80)
    builder_agent = BuilderAgent()
    result = builder_agent.execute(global_status)
    print(json.dumps(result, indent=2))
    print()
    
    # Test FinalizerAgent with good metrics
    print("FinalizerAgent Structured Output (Success Case):")
    print("-" * 80)
    global_status.build_success_rate = 0.98
    global_status.test_success_rate = 0.95
    finalizer_agent = FinalizerAgent()
    result = finalizer_agent.execute(global_status)
    print(json.dumps(result, indent=2))
    print()


def demo_complete_workflow():
    """
    Demonstrate complete autonomous development workflow.
    
    AI_PHASE: EXAMPLE_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: HIGH
    AI_NOTE: Shows complete workflow from error to finalization
    """
    print("=" * 80)
    print("Complete Autonomous Development Workflow")
    print("=" * 80)
    print()
    
    # Initialize coordinator
    coordinator = SMCCoordinator()
    
    # Register agents
    coordinator.register_agent("BuilderAgent", BuilderAgent())
    coordinator.register_agent("ReasoningAgent", ReasoningAgent())
    coordinator.register_agent("TesterAgent", TesterAgent())
    coordinator.register_agent("FinalizerAgent", FinalizerAgent())
    
    # Simulate workflow stages
    print("Stage 1: Initial Build")
    print("-" * 80)
    coordinator.global_status.ai_state = AgentState.READY
    coordinator.global_status.ai_queue_status = QueueStatus.QUEUED
    coordinator.global_status.last_action = "INIT"
    
    # Build phase (simulated success)
    builder_agent = BuilderAgent()
    build_result = builder_agent.execute(coordinator.global_status)
    print("Build Result:")
    print(json.dumps(build_result, indent=2))
    coordinator._update_status_from_result(build_result, "BuilderAgent")
    print()
    
    print("Stage 2: Testing")
    print("-" * 80)
    tester_agent = TesterAgent()
    test_result = tester_agent.execute(coordinator.global_status)
    print("Test Result:")
    print(json.dumps(test_result, indent=2))
    coordinator._update_status_from_result(test_result, "TesterAgent")
    print()
    
    print("Stage 3: Error Analysis (if needed)")
    print("-" * 80)
    if coordinator.global_status.test_success_rate < 1.0:
        reasoning_agent = ReasoningAgent()
        reason_result = reasoning_agent.execute(coordinator.global_status)
        print("Reasoning Result:")
        print(json.dumps(reason_result, indent=2))
        coordinator._update_status_from_result(reason_result, "ReasoningAgent")
    else:
        print("No errors detected, skipping reasoning phase")
    print()
    
    print("Stage 4: Finalization")
    print("-" * 80)
    # Set success rates for finalization
    coordinator.global_status.build_success_rate = 0.98
    coordinator.global_status.test_success_rate = 0.95
    
    finalizer_agent = FinalizerAgent()
    final_result = finalizer_agent.execute(coordinator.global_status)
    print("Finalization Result:")
    print(json.dumps(final_result, indent=2))
    print()
    
    print("Final Global Status:")
    print(json.dumps(coordinator.global_status.to_dict(), indent=2))
    print()


def main():
    """Main entry point for demos"""
    demos = [
        ("Basic Coordination", demo_basic_coordination),
        ("State Routing Prompt", demo_routing_prompt),
        ("Fix Triage Prompt", demo_triage_prompt),
        ("Final Decision Prompt", demo_final_decision_prompt),
        ("Agent Structured Output", demo_agent_structured_output),
        ("Complete Workflow", demo_complete_workflow),
    ]
    
    if len(sys.argv) > 1:
        # Run specific demo
        demo_name = sys.argv[1]
        for name, func in demos:
            if demo_name.lower() in name.lower():
                func()
                return
        print(f"Demo '{demo_name}' not found")
        print("Available demos:")
        for name, _ in demos:
            print(f"  - {name}")
    else:
        # Run all demos
        for i, (name, func) in enumerate(demos):
            if i > 0:
                print("\n" * 3)
            func()


if __name__ == "__main__":
    main()
