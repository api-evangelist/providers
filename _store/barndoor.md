---
aid: barndoor
name: Barndoor
description: Barndoor AI is the control plane for agentic AI, providing secure access and governance for AI agents and Model Context Protocol (MCP) servers. Founded in 2024 by Oren Michels (founder of Mashery), Barndoor enables enterprise teams to orchestrate AI agent workflows, govern MCP server access, and maintain security and accountability across distributed AI systems. The Barndoor SDK enables developers to connect to governed MCP servers for platforms like Salesforce, Notion, and GitHub.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - AI Governance
  - Agentic AI
  - MCP
  - Model Context Protocol
  - Security
url: https://raw.githubusercontent.com/api-evangelist/barndoor/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-21'
specificationVersion: '0.19'
apis: []
common:
  - type: Website
    url: https://barndoor.ai/
    name: Barndoor AI
  - type: Documentation
    url: https://docs.barndoor.ai/
    name: Barndoor Developer Documentation
  - type: Documentation
    url: https://docs.barndoor.ai/sdks/introduction
    name: Barndoor SDKs
  - type: GitHub
    url: https://github.com/barndoor-ai
    name: Barndoor AI GitHub
  - type: About
    url: https://barndoor.ai/about-us/
    name: About Barndoor AI
  - type: Security
    url: https://barndoor.ai/security/
    name: Security
  - type: SpectralRules
    url: rules/barndoor-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/barndoor-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ai-governance.yaml
  - type: JSON-LD
    url: json-ld/barndoor-context.jsonld
  - name: Features
    type: Features
    data:
      - name: MCP Governance
        description: Secure access control and governance for Model Context Protocol servers.
      - name: AI Agent Orchestration
        description: Control plane for managing and coordinating AI agent workflows.
      - name: SDK Integration
        description: SDKs for connecting to governed MCP servers across platforms.
      - name: Enterprise Security
        description: Data governance, access policies, and accountability for AI deployments.
      - name: Platform Connectors
        description: Pre-built connections to Salesforce, Notion, GitHub, and other platforms.
      - name: Audit and Compliance
        description: Oversight and audit trails for AI agent actions and outputs.
  - name: Use Cases
    type: UseCases
    data:
      - name: Enterprise AI Governance
        description: Apply access policies and governance to AI agents across the organization.
      - name: MCP Server Management
        description: Centrally manage and secure MCP server deployments for AI agents.
      - name: Agentic Workflow Orchestration
        description: Coordinate multi-agent workflows with security and accountability controls.
      - name: AI Security
        description: Prevent unauthorized AI agent actions and data exfiltration.
      - name: Developer Tooling
        description: SDK and API tools for building governed AI agent integrations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
