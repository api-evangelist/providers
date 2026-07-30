---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Durable Functions Agentic Access
  operation_count: 14
  slug: durable-functions-agentic-access
  summary_line: 14 operations · 10 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Durable entity management
  name: Azure Durable Functions Entities API
  slug: durable-functions-entities-api
- description: Orchestration instance management
  name: Azure Durable Functions Orchestrations API
  slug: durable-functions-orchestrations-api
artifact_total: 11
collections:
- collection_type: open
  name: Azure Durable Functions HTTP API
  slug: open-durable-functions-http-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/durable-functions-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/durable-functions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/durable-functions-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/durable-functions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-functions/durable/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: other
  title: ''
  type: Repository
  url: https://github.com/Azure/azure-functions-durable-extension
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Azure/azure-functions-mcp-extension
created: '2026-03-27'
description: Azure Durable Functions is a serverless extension for writing stateful workflows and orchestrations in code using Azure Functions. The extension exposes built-in HTTP APIs for managing orchestrations, durable entities, and task hubs.
finops:
- name: Durable Functions Finops
  service_category: API
  slug: durable-functions-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/durable-functions.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Azure Durable Functions
nav: Providers
network: true
overview: 'Azure Durable Functions publishes 2 APIs on the [APIs.io](https://apis.io/) network: Entities API and Orchestrations API. Tagged areas include API Composition, Durable Execution, Serverless Orchestration, and Workflow.


  Azure Durable Functions'' developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Durable Functions Plans Pricing
  plan_count: 3
  slug: durable-functions-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Durable Functions Rate Limits
  slug: durable-functions-rate-limits
score:
  band: thin
  composite: 37.8
  delta: -1.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.2
    developer_ergonomics: 28.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/durable-functions/refs/heads/main/screenshots/durable-functions-2026-06-20T180327.png
security:
- kind: authentication
  name: Durable Functions Authentication
  slug: durable-functions-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Durable Functions Domain Security
  slug: durable-functions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Durable Functions Vulnerability Disclosure
  slug: durable-functions-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: durable-functions
tags:
- API Composition
- Durable Execution
- Serverless Orchestration
- Workflow
website: https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview
---
