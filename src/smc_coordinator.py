#!/usr/bin/env python3
"""
Small Model Coordinator (SMC) Implementation

This module implements a lightweight coordinator model for autonomous agent orchestration
using highly constrained JSON prompts for fast, CPU-bound decision making.

AI_PHASE: AGENT_COORDINATION
AI_STATUS: IMPLEMENTED
AI_COMPLEXITY: HIGH
AI_NOTE: Core coordinator for autonomous agent handoff and orchestration
AI_DEPENDENCIES: 
AI_COMMIT: initial

Copyright (C) 2025 Timothy Deters / R.E.C.A.L.L. Foundation

This file is part of the ACD Specification.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""

import json
from typing import Dict, Any, List, Optional
from enum import Enum
from dataclasses import dataclass, asdict


class AgentState(Enum):
    """Agent state enumeration matching ACD standard"""
    PROCESSING = "PROCESSING"
    READY = "READY"
    DONE = "DONE"
    BLOCKED = "BLOCKED"
    PAUSED = "PAUSED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class QueueStatus(Enum):
    """Queue status enumeration matching ACD standard"""
    QUEUED = "QUEUED"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    REVIEW_PENDING = "REVIEW_PENDING"
    REVIEW_IN_PROGRESS = "REVIEW_IN_PROGRESS"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    COMPLETED = "COMPLETED"
    ABANDONED = "ABANDONED"


@dataclass
class GlobalStatus:
    """
    AI_PHASE: AGENT_COORDINATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: MEDIUM
    AI_NOTE: Represents the global state of the development system
    """
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
    
    def __post_init__(self):
        if self.top_errors is None:
            self.top_errors = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        result = asdict(self)
        result['ai_state'] = self.ai_state.value
        result['ai_queue_status'] = self.ai_queue_status.value
        return result


@dataclass
class RoutingDecision:
    """
    AI_PHASE: AGENT_COORDINATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: LOW
    AI_NOTE: Output from state routing prompt
    """
    next_agent: str
    rationale: str


@dataclass
class TriageDecision:
    """
    AI_PHASE: AGENT_COORDINATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: LOW
    AI_NOTE: Output from fix triage prompt
    """
    action: str
    context_focus: str


@dataclass
class FinalDecision:
    """
    AI_PHASE: AGENT_COORDINATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: LOW
    AI_NOTE: Output from final decision prompt
    """
    commit_required: bool
    next_agent: str
    rationale: str


class SMCCoordinator:
    """
    Small Model Coordinator for autonomous agent orchestration.
    
    AI_PHASE: AGENT_COORDINATION
    AI_STATUS: IMPLEMENTED
    AI_COMPLEXITY: HIGH
    AI_NOTE: Lightweight coordinator using constrained JSON prompts for fast decisions
    AI_DEPENDENCIES: 
    
    This coordinator uses highly constrained JSON prompts designed for small,
    fast, CPU-bound models (e.g., Llama 3 8B or smaller specialized agents).
    """
    
    def __init__(self, model_backend: Optional[Any] = None):
        """
        Initialize the SMC Coordinator.
        
        Args:
            model_backend: Optional backend for AI model inference. If None,
                          uses simulated responses for testing/demo.
        """
        self.model_backend = model_backend
        self.global_status = GlobalStatus(
            last_action="INIT",
            last_agent="SYSTEM",
            last_result="SUCCESS",
            ai_state=AgentState.READY,
            ai_queue_status=QueueStatus.QUEUED,
            ai_handoff_requested=False
        )
        self.agents_registry = {}
    
    def register_agent(self, agent_name: str, agent_instance: Any) -> None:
        """
        Register an agent with the coordinator.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: LOW
        AI_NOTE: Maintains registry of available agents
        
        Args:
            agent_name: Unique identifier for the agent
            agent_instance: Agent object implementing execute() method
        """
        self.agents_registry[agent_name] = agent_instance
    
    def state_routing_prompt(self, global_status: GlobalStatus) -> str:
        """
        Generate State Routing prompt for coordinator model.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: MEDIUM
        AI_NOTE: Constrained JSON prompt for next agent selection
        
        Input: Global Status & Last Action
        Output: {"next_agent": "...", "rationale": "..."}
        
        Args:
            global_status: Current system state
            
        Returns:
            JSON prompt string
        """
        prompt = {
            "task": "state_routing",
            "instruction": "Determine the next agent to execute based on current state. Respond ONLY with valid JSON.",
            "input": {
                "last_action": global_status.last_action,
                "last_agent": global_status.last_agent,
                "last_result": global_status.last_result,
                "ai_state": global_status.ai_state.value,
                "ai_queue_status": global_status.ai_queue_status.value,
                "ai_handoff_requested": global_status.ai_handoff_requested,
                "available_agents": list(self.agents_registry.keys())
            },
            "output_format": {
                "next_agent": "string (one of available_agents or 'NONE')",
                "rationale": "string (brief explanation)"
            },
            "constraints": [
                "Response must be valid JSON",
                "next_agent must be from available_agents or 'NONE'",
                "rationale must be under 200 characters"
            ]
        }
        return json.dumps(prompt, indent=2)
    
    def fix_triage_prompt(self, errors: List[str]) -> str:
        """
        Generate Fix Triage prompt for coordinator model.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: MEDIUM
        AI_NOTE: Constrained JSON prompt for error triage
        
        Input: Top 5 Errors/Crash Info
        Output: {"action": "ROUTE_REASONER", "context_focus": "..."}
        
        Args:
            errors: List of error messages (top 5)
            
        Returns:
            JSON prompt string
        """
        prompt = {
            "task": "fix_triage",
            "instruction": "Analyze errors and determine routing action. Respond ONLY with valid JSON.",
            "input": {
                "errors": errors[:5],  # Top 5 errors only
                "error_count": len(errors)
            },
            "output_format": {
                "action": "string (ROUTE_REASONER, ROUTE_TESTER, ROUTE_FINALIZER, or MANUAL_REVIEW)",
                "context_focus": "string (area needing attention)"
            },
            "constraints": [
                "Response must be valid JSON",
                "action must be one of: ROUTE_REASONER, ROUTE_TESTER, ROUTE_FINALIZER, MANUAL_REVIEW",
                "context_focus must identify specific code area or phase"
            ]
        }
        return json.dumps(prompt, indent=2)
    
    def final_decision_prompt(self, build_success: float, test_success: float) -> str:
        """
        Generate Final Decision prompt for coordinator model.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: MEDIUM
        AI_NOTE: Constrained JSON prompt for commit/finalize decision
        
        Input: Build/Test Success Rate
        Output: {"commit_required": "...", "next_agent": "Finalizer"}
        
        Args:
            build_success: Build success rate (0.0 to 1.0)
            test_success: Test success rate (0.0 to 1.0)
            
        Returns:
            JSON prompt string
        """
        prompt = {
            "task": "final_decision",
            "instruction": "Determine if work is ready to commit. Respond ONLY with valid JSON.",
            "input": {
                "build_success_rate": build_success,
                "test_success_rate": test_success,
                "threshold_build": 0.95,
                "threshold_test": 0.90
            },
            "output_format": {
                "commit_required": "boolean",
                "next_agent": "string (agent to handle next step)",
                "rationale": "string (brief explanation)"
            },
            "constraints": [
                "Response must be valid JSON",
                "commit_required based on thresholds",
                "If commit_required is true, next_agent should be 'Finalizer'",
                "If commit_required is false, next_agent should suggest remediation"
            ]
        }
        return json.dumps(prompt, indent=2)
    
    def parse_routing_decision(self, response: str) -> RoutingDecision:
        """
        Parse coordinator response into RoutingDecision.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: LOW
        AI_NOTE: Parses JSON response from state routing
        """
        data = json.loads(response)
        return RoutingDecision(
            next_agent=data["next_agent"],
            rationale=data["rationale"]
        )
    
    def parse_triage_decision(self, response: str) -> TriageDecision:
        """
        Parse coordinator response into TriageDecision.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: LOW
        AI_NOTE: Parses JSON response from fix triage
        """
        data = json.loads(response)
        return TriageDecision(
            action=data["action"],
            context_focus=data["context_focus"]
        )
    
    def parse_final_decision(self, response: str) -> FinalDecision:
        """
        Parse coordinator response into FinalDecision.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: LOW
        AI_NOTE: Parses JSON response from final decision
        """
        data = json.loads(response)
        return FinalDecision(
            commit_required=data["commit_required"],
            next_agent=data["next_agent"],
            rationale=data["rationale"]
        )
    
    def execute_routing(self) -> RoutingDecision:
        """
        Execute state routing logic.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: MEDIUM
        AI_NOTE: Main routing logic using AI_STATE and AI_HANDOFF_REQUESTED
        
        Returns:
            RoutingDecision with next agent and rationale
        """
        prompt = self.state_routing_prompt(self.global_status)
        
        if self.model_backend:
            response = self.model_backend.generate(prompt)
        else:
            # Simulated response for testing
            response = self._simulate_routing_response()
        
        return self.parse_routing_decision(response)
    
    def execute_triage(self, errors: List[str]) -> TriageDecision:
        """
        Execute fix triage logic.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: MEDIUM
        AI_NOTE: Triage errors and determine next action
        
        Args:
            errors: List of error messages
            
        Returns:
            TriageDecision with action and context focus
        """
        prompt = self.fix_triage_prompt(errors)
        
        if self.model_backend:
            response = self.model_backend.generate(prompt)
        else:
            # Simulated response for testing
            response = self._simulate_triage_response(errors)
        
        return self.parse_triage_decision(response)
    
    def execute_final_decision(self) -> FinalDecision:
        """
        Execute final decision logic.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: MEDIUM
        AI_NOTE: Determine if work is ready to commit
        
        Returns:
            FinalDecision with commit requirement and next agent
        """
        prompt = self.final_decision_prompt(
            self.global_status.build_success_rate,
            self.global_status.test_success_rate
        )
        
        if self.model_backend:
            response = self.model_backend.generate(prompt)
        else:
            # Simulated response for testing
            response = self._simulate_final_decision_response()
        
        return self.parse_final_decision(response)
    
    def run_coordination_loop(self, max_iterations: int = 10) -> Dict[str, Any]:
        """
        Main coordination loop for agent handoff protocol.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: HIGH
        AI_NOTE: Implements handoff logic reading AI_STATE, AI_HANDOFF_REQUESTED, AI_QUEUE_STATUS
        
        Args:
            max_iterations: Maximum number of coordination cycles
            
        Returns:
            Dictionary with execution summary
        """
        iteration = 0
        execution_log = []
        
        while iteration < max_iterations:
            iteration += 1
            
            # Check termination conditions
            if self.global_status.ai_state == AgentState.DONE:
                execution_log.append({
                    "iteration": iteration,
                    "action": "TERMINATE",
                    "reason": "AI_STATE is DONE"
                })
                break
            
            if self.global_status.ai_state == AgentState.FAILED:
                execution_log.append({
                    "iteration": iteration,
                    "action": "TERMINATE",
                    "reason": "AI_STATE is FAILED"
                })
                break
            
            # Execute routing decision
            routing = self.execute_routing()
            
            execution_log.append({
                "iteration": iteration,
                "routing_decision": {
                    "next_agent": routing.next_agent,
                    "rationale": routing.rationale
                },
                "global_status": self.global_status.to_dict()
            })
            
            # Handle routing decision
            if routing.next_agent == "NONE" or routing.next_agent not in self.agents_registry:
                execution_log.append({
                    "iteration": iteration,
                    "action": "TERMINATE",
                    "reason": f"No valid next agent: {routing.next_agent}"
                })
                break
            
            # Execute agent
            agent = self.agents_registry[routing.next_agent]
            agent_result = agent.execute(self.global_status)
            
            # Update global status based on agent result
            self._update_status_from_result(agent_result, routing.next_agent)
            
            execution_log.append({
                "iteration": iteration,
                "agent_executed": routing.next_agent,
                "agent_result": agent_result
            })
        
        return {
            "total_iterations": iteration,
            "final_state": self.global_status.to_dict(),
            "execution_log": execution_log
        }
    
    def _update_status_from_result(self, result: Dict[str, Any], agent_name: str) -> None:
        """
        Update global status based on agent execution result.
        
        AI_PHASE: AGENT_COORDINATION
        AI_STATUS: IMPLEMENTED
        AI_COMPLEXITY: MEDIUM
        AI_NOTE: Updates global state from structured agent output
        """
        self.global_status.last_action = result.get("action", "UNKNOWN")
        self.global_status.last_agent = agent_name
        self.global_status.last_result = result.get("result", "UNKNOWN")
        
        # Update AI_STATE if provided
        if "ai_state" in result:
            self.global_status.ai_state = AgentState(result["ai_state"])
        
        # Update AI_QUEUE_STATUS if provided
        if "ai_queue_status" in result:
            self.global_status.ai_queue_status = QueueStatus(result["ai_queue_status"])
        
        # Update AI_HANDOFF_REQUESTED if provided
        if "ai_handoff_requested" in result:
            self.global_status.ai_handoff_requested = result["ai_handoff_requested"]
        
        # Update metrics if provided
        if "build_success_rate" in result:
            self.global_status.build_success_rate = result["build_success_rate"]
        
        if "test_success_rate" in result:
            self.global_status.test_success_rate = result["test_success_rate"]
        
        if "errors" in result:
            self.global_status.top_errors = result["errors"][:5]
            self.global_status.error_count = len(result["errors"])
    
    # Simulation methods for testing without actual AI backend
    
    def _simulate_routing_response(self) -> str:
        """Simulate routing response for testing"""
        if self.global_status.ai_handoff_requested:
            next_agent = "ReasoningAgent"
        elif self.global_status.ai_state == AgentState.READY:
            next_agent = "ReasoningAgent"
        elif self.global_status.error_count > 0:
            next_agent = "ReasoningAgent"
        else:
            next_agent = "FinalizerAgent"
        
        return json.dumps({
            "next_agent": next_agent,
            "rationale": f"Selected {next_agent} based on current state"
        })
    
    def _simulate_triage_response(self, errors: List[str]) -> str:
        """Simulate triage response for testing"""
        if len(errors) > 3:
            action = "ROUTE_REASONER"
            context = "Multiple errors detected"
        elif len(errors) > 0:
            action = "ROUTE_REASONER"
            context = "Single error needs fixing"
        else:
            action = "ROUTE_TESTER"
            context = "No errors, proceed to testing"
        
        return json.dumps({
            "action": action,
            "context_focus": context
        })
    
    def _simulate_final_decision_response(self) -> str:
        """Simulate final decision response for testing"""
        commit = (
            self.global_status.build_success_rate >= 0.95 and
            self.global_status.test_success_rate >= 0.90
        )
        
        if commit:
            next_agent = "FinalizerAgent"
            rationale = "Build and test success rates meet thresholds"
        else:
            next_agent = "ReasoningAgent"
            rationale = "Success rates below threshold, need fixes"
        
        return json.dumps({
            "commit_required": commit,
            "next_agent": next_agent,
            "rationale": rationale
        })
