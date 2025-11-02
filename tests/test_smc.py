#!/usr/bin/env python3
"""
Test suite for SMC Coordinator and Example Agents

AI_PHASE: TEST_IMPLEMENTATION
AI_STATUS: IMPLEMENTED
AI_COMPLEXITY: MEDIUM
AI_NOTE: Comprehensive tests for SMC coordinator functionality
AI_DEPENDENCIES: AGENT_COORDINATION, AGENT_IMPLEMENTATION

Copyright (C) 2025 Timothy Deters / R.E.C.A.L.L. Foundation

This file is part of the ACD Specification.
"""

import unittest
import json
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from smc_coordinator import (
    SMCCoordinator, GlobalStatus, AgentState, QueueStatus,
    RoutingDecision, TriageDecision, FinalDecision
)
from example_agents import ReasoningAgent, TesterAgent, FinalizerAgent, BuilderAgent


class TestGlobalStatus(unittest.TestCase):
    """
    Test GlobalStatus data structure.
    
    AI_PHASE: TEST_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: LOW
    AI_NOTE: Tests for GlobalStatus dataclass
    """
    
    def test_global_status_creation(self):
        """Test creating GlobalStatus instance"""
        status = GlobalStatus(
            last_action="BUILD",
            last_agent="BuilderAgent",
            last_result="SUCCESS",
            ai_state=AgentState.READY,
            ai_queue_status=QueueStatus.COMPLETED,
            ai_handoff_requested=False
        )
        
        self.assertEqual(status.last_action, "BUILD")
        self.assertEqual(status.last_agent, "BuilderAgent")
        self.assertEqual(status.ai_state, AgentState.READY)
        self.assertEqual(status.ai_handoff_requested, False)
    
    def test_global_status_to_dict(self):
        """Test converting GlobalStatus to dictionary"""
        status = GlobalStatus(
            last_action="TEST",
            last_agent="TesterAgent",
            last_result="FAILURE",
            ai_state=AgentState.BLOCKED,
            ai_queue_status=QueueStatus.REJECTED,
            ai_handoff_requested=True
        )
        
        status_dict = status.to_dict()
        
        self.assertIsInstance(status_dict, dict)
        self.assertEqual(status_dict["last_action"], "TEST")
        self.assertEqual(status_dict["ai_state"], "BLOCKED")
        self.assertEqual(status_dict["ai_queue_status"], "REJECTED")
        self.assertTrue(status_dict["ai_handoff_requested"])


class TestSMCCoordinator(unittest.TestCase):
    """
    Test SMC Coordinator functionality.
    
    AI_PHASE: TEST_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: MEDIUM
    AI_NOTE: Tests for SMCCoordinator class
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.coordinator = SMCCoordinator()
    
    def test_coordinator_initialization(self):
        """Test coordinator initializes correctly"""
        self.assertIsNotNone(self.coordinator.global_status)
        self.assertEqual(self.coordinator.global_status.ai_state, AgentState.READY)
        self.assertEqual(len(self.coordinator.agents_registry), 0)
    
    def test_register_agent(self):
        """Test registering agents"""
        agent = ReasoningAgent()
        self.coordinator.register_agent("ReasoningAgent", agent)
        
        self.assertIn("ReasoningAgent", self.coordinator.agents_registry)
        self.assertEqual(self.coordinator.agents_registry["ReasoningAgent"], agent)
    
    def test_state_routing_prompt(self):
        """Test state routing prompt generation"""
        self.coordinator.register_agent("ReasoningAgent", ReasoningAgent())
        
        prompt = self.coordinator.state_routing_prompt(self.coordinator.global_status)
        
        self.assertIsInstance(prompt, str)
        prompt_data = json.loads(prompt)
        
        self.assertEqual(prompt_data["task"], "state_routing")
        self.assertIn("input", prompt_data)
        self.assertIn("output_format", prompt_data)
        self.assertIn("available_agents", prompt_data["input"])
    
    def test_fix_triage_prompt(self):
        """Test fix triage prompt generation"""
        errors = ["Error 1", "Error 2", "Error 3"]
        prompt = self.coordinator.fix_triage_prompt(errors)
        
        self.assertIsInstance(prompt, str)
        prompt_data = json.loads(prompt)
        
        self.assertEqual(prompt_data["task"], "fix_triage")
        self.assertIn("errors", prompt_data["input"])
        self.assertEqual(len(prompt_data["input"]["errors"]), 3)
    
    def test_final_decision_prompt(self):
        """Test final decision prompt generation"""
        prompt = self.coordinator.final_decision_prompt(0.95, 0.90)
        
        self.assertIsInstance(prompt, str)
        prompt_data = json.loads(prompt)
        
        self.assertEqual(prompt_data["task"], "final_decision")
        self.assertIn("build_success_rate", prompt_data["input"])
        self.assertIn("test_success_rate", prompt_data["input"])
        self.assertEqual(prompt_data["input"]["build_success_rate"], 0.95)
        self.assertEqual(prompt_data["input"]["test_success_rate"], 0.90)
    
    def test_parse_routing_decision(self):
        """Test parsing routing decision from JSON"""
        response = json.dumps({
            "next_agent": "ReasoningAgent",
            "rationale": "Need to analyze errors"
        })
        
        decision = self.coordinator.parse_routing_decision(response)
        
        self.assertIsInstance(decision, RoutingDecision)
        self.assertEqual(decision.next_agent, "ReasoningAgent")
        self.assertEqual(decision.rationale, "Need to analyze errors")
    
    def test_parse_triage_decision(self):
        """Test parsing triage decision from JSON"""
        response = json.dumps({
            "action": "ROUTE_REASONER",
            "context_focus": "MEMORY_TRANSLATION"
        })
        
        decision = self.coordinator.parse_triage_decision(response)
        
        self.assertIsInstance(decision, TriageDecision)
        self.assertEqual(decision.action, "ROUTE_REASONER")
        self.assertEqual(decision.context_focus, "MEMORY_TRANSLATION")
    
    def test_parse_final_decision(self):
        """Test parsing final decision from JSON"""
        response = json.dumps({
            "commit_required": True,
            "next_agent": "FinalizerAgent",
            "rationale": "All tests passing"
        })
        
        decision = self.coordinator.parse_final_decision(response)
        
        self.assertIsInstance(decision, FinalDecision)
        self.assertTrue(decision.commit_required)
        self.assertEqual(decision.next_agent, "FinalizerAgent")
    
    def test_execute_routing(self):
        """Test executing routing decision"""
        self.coordinator.register_agent("ReasoningAgent", ReasoningAgent())
        
        decision = self.coordinator.execute_routing()
        
        self.assertIsInstance(decision, RoutingDecision)
        self.assertIsInstance(decision.next_agent, str)
        self.assertIsInstance(decision.rationale, str)
    
    def test_execute_triage(self):
        """Test executing triage decision"""
        errors = ["ImportError: No module named 'test'"]
        
        decision = self.coordinator.execute_triage(errors)
        
        self.assertIsInstance(decision, TriageDecision)
        self.assertIn(decision.action, ["ROUTE_REASONER", "ROUTE_TESTER", "ROUTE_FINALIZER", "MANUAL_REVIEW"])
    
    def test_execute_final_decision(self):
        """Test executing final decision"""
        self.coordinator.global_status.build_success_rate = 0.98
        self.coordinator.global_status.test_success_rate = 0.95
        
        decision = self.coordinator.execute_final_decision()
        
        self.assertIsInstance(decision, FinalDecision)
        self.assertIsInstance(decision.commit_required, bool)
    
    def test_update_status_from_result(self):
        """Test updating global status from agent result"""
        result = {
            "action": "BUILD",
            "result": "SUCCESS",
            "ai_state": "READY",
            "ai_queue_status": "COMPLETED",
            "ai_handoff_requested": False,
            "build_success_rate": 1.0
        }
        
        self.coordinator._update_status_from_result(result, "BuilderAgent")
        
        self.assertEqual(self.coordinator.global_status.last_action, "BUILD")
        self.assertEqual(self.coordinator.global_status.last_agent, "BuilderAgent")
        self.assertEqual(self.coordinator.global_status.ai_state, AgentState.READY)
        self.assertEqual(self.coordinator.global_status.build_success_rate, 1.0)
    
    def test_coordination_loop_basic(self):
        """Test basic coordination loop"""
        # Register agents
        self.coordinator.register_agent("ReasoningAgent", ReasoningAgent())
        self.coordinator.register_agent("FinalizerAgent", FinalizerAgent())
        
        # Set up state that will complete quickly
        self.coordinator.global_status.build_success_rate = 0.98
        self.coordinator.global_status.test_success_rate = 0.95
        
        # Run loop
        result = self.coordinator.run_coordination_loop(max_iterations=3)
        
        self.assertIn("total_iterations", result)
        self.assertIn("final_state", result)
        self.assertIn("execution_log", result)
        self.assertLessEqual(result["total_iterations"], 3)


class TestReasoningAgent(unittest.TestCase):
    """
    Test ReasoningAgent functionality.
    
    AI_PHASE: TEST_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: MEDIUM
    AI_NOTE: Tests for ReasoningAgent class
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = ReasoningAgent()
        self.global_status = GlobalStatus(
            last_action="BUILD",
            last_agent="BuilderAgent",
            last_result="FAILURE",
            ai_state=AgentState.BLOCKED,
            ai_queue_status=QueueStatus.REJECTED,
            ai_handoff_requested=True
        )
    
    def test_agent_initialization(self):
        """Test agent initializes correctly"""
        self.assertEqual(self.agent.name, "ReasoningAgent")
    
    def test_execute_with_errors(self):
        """Test agent execution with errors"""
        self.global_status.top_errors = ["ImportError: No module named 'test'"]
        
        result = self.agent.execute(self.global_status)
        
        self.assertIsInstance(result, dict)
        self.assertIn("action", result)
        self.assertIn("result", result)
        self.assertIn("ai_state", result)
        self.assertIn("ai_queue_status", result)
        self.assertIn("fix_recommendation", result)
    
    def test_execute_no_errors(self):
        """Test agent execution without errors"""
        self.global_status.top_errors = []
        
        result = self.agent.execute(self.global_status)
        
        self.assertEqual(result["action"], "ANALYZE")
        self.assertEqual(result["result"], "SUCCESS")
        self.assertEqual(result["ai_state"], "DONE")
    
    def test_structured_output_format(self):
        """Test that output is properly structured JSON"""
        self.global_status.top_errors = ["SyntaxError: invalid syntax"]
        
        result = self.agent.execute(self.global_status)
        
        # Verify can be serialized to JSON
        json_str = json.dumps(result)
        self.assertIsInstance(json_str, str)
        
        # Verify has required fields
        self.assertIn("action", result)
        self.assertIn("result", result)
        self.assertIn("ai_state", result)
        self.assertIn("ai_handoff_requested", result)


class TestTesterAgent(unittest.TestCase):
    """
    Test TesterAgent functionality.
    
    AI_PHASE: TEST_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: MEDIUM
    AI_NOTE: Tests for TesterAgent class
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = TesterAgent()
        self.global_status = GlobalStatus(
            last_action="BUILD",
            last_agent="BuilderAgent",
            last_result="SUCCESS",
            ai_state=AgentState.READY,
            ai_queue_status=QueueStatus.COMPLETED,
            ai_handoff_requested=True
        )
    
    def test_agent_initialization(self):
        """Test agent initializes correctly"""
        self.assertEqual(self.agent.name, "TesterAgent")
    
    def test_execute_tests(self):
        """Test agent execution"""
        result = self.agent.execute(self.global_status)
        
        self.assertIsInstance(result, dict)
        self.assertIn("action", result)
        self.assertIn("result", result)
        self.assertIn("test_results", result)
        self.assertIn("test_success_rate", result)
    
    def test_structured_output_format(self):
        """Test that output is properly structured JSON"""
        result = self.agent.execute(self.global_status)
        
        # Verify can be serialized to JSON
        json_str = json.dumps(result)
        self.assertIsInstance(json_str, str)
        
        # Verify test results structure
        self.assertIn("test_results", result)
        test_results = result["test_results"]
        self.assertIn("total", test_results)
        self.assertIn("passed", test_results)
        self.assertIn("failed", test_results)


class TestFinalizerAgent(unittest.TestCase):
    """
    Test FinalizerAgent functionality.
    
    AI_PHASE: TEST_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: MEDIUM
    AI_NOTE: Tests for FinalizerAgent class
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = FinalizerAgent()
        self.global_status = GlobalStatus(
            last_action="TEST",
            last_agent="TesterAgent",
            last_result="SUCCESS",
            ai_state=AgentState.READY,
            ai_queue_status=QueueStatus.APPROVED,
            ai_handoff_requested=True
        )
    
    def test_agent_initialization(self):
        """Test agent initializes correctly"""
        self.assertEqual(self.agent.name, "FinalizerAgent")
    
    def test_execute_success(self):
        """Test agent execution with high success rates"""
        self.global_status.build_success_rate = 0.98
        self.global_status.test_success_rate = 0.95
        
        result = self.agent.execute(self.global_status)
        
        self.assertEqual(result["action"], "FINALIZE")
        self.assertEqual(result["result"], "SUCCESS")
        self.assertTrue(result["commit_ready"])
        self.assertEqual(result["ai_state"], "DONE")
    
    def test_execute_failure(self):
        """Test agent execution with low success rates"""
        self.global_status.build_success_rate = 0.75
        self.global_status.test_success_rate = 0.80
        
        result = self.agent.execute(self.global_status)
        
        self.assertEqual(result["action"], "FINALIZE")
        self.assertEqual(result["result"], "FAILURE")
        self.assertFalse(result["commit_ready"])
        self.assertTrue(result["ai_handoff_requested"])


class TestBuilderAgent(unittest.TestCase):
    """
    Test BuilderAgent functionality.
    
    AI_PHASE: TEST_IMPLEMENTATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: MEDIUM
    AI_NOTE: Tests for BuilderAgent class
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = BuilderAgent()
        self.global_status = GlobalStatus(
            last_action="INIT",
            last_agent="SYSTEM",
            last_result="SUCCESS",
            ai_state=AgentState.READY,
            ai_queue_status=QueueStatus.QUEUED,
            ai_handoff_requested=False
        )
    
    def test_agent_initialization(self):
        """Test agent initializes correctly"""
        self.assertEqual(self.agent.name, "BuilderAgent")
    
    def test_execute_build(self):
        """Test agent execution"""
        result = self.agent.execute(self.global_status)
        
        self.assertIsInstance(result, dict)
        self.assertIn("action", result)
        self.assertIn("result", result)
        self.assertIn("build_results", result)
        self.assertIn("build_success_rate", result)


def run_tests():
    """Run all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestGlobalStatus))
    suite.addTests(loader.loadTestsFromTestCase(TestSMCCoordinator))
    suite.addTests(loader.loadTestsFromTestCase(TestReasoningAgent))
    suite.addTests(loader.loadTestsFromTestCase(TestTesterAgent))
    suite.addTests(loader.loadTestsFromTestCase(TestFinalizerAgent))
    suite.addTests(loader.loadTestsFromTestCase(TestBuilderAgent))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
