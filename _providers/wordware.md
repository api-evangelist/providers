---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Run deployed WordApps programmatically. Each published WordApp exposes a run endpoint (POST /api/released-app/{app_id}/run) that accepts a JSON body of named inputs (text, image, audio) plus a semanti
  name: Wordware WordApps API
  slug: wordware-wordapps-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wordware-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/wordware-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wordware-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wordware-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/wordware-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wordware-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wordware-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wordware-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://wordware.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wordware.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wordware.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wordware.ai/tour
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/6Zm5FGC2kR
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wordware-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wordware.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wordware.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://app.wordware.ai
created: '2026-07-17'
description: Wordware is a San Francisco AI company (YC S23, backed by Felicis and Spark Capital) that built a web-hosted IDE for building AI agents and LLM applications with natural language "flows". Every flow can be deployed as a standalone WordApp that is simultaneously a web app and a streaming REST API, authenticated with bearer API keys and versioned with a simplified major.minor scheme. In 2026 the company pivoted its flagship product to Sauna, a proactive AI assistant, while the Wordware V1 platform and its WordApps API remain available at app.wordware.ai.
image: https://github.com/wordware-ai.png
layout: provider
mcp_servers:
- description: ''
  name: wordware-mcp.yml
  slug: wordware-mcpyml
modified: '2026-07-21'
name: Wordware
nav: Providers
network: true
overview: 'Wordware publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, AI Agents, LLM, Prompt Engineering, and Workflow Automation.


  Wordware''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 12 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 26.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 26.6
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Wordware Authentication
  slug: wordware-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wordware Domain Security
  slug: wordware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wordware
tags:
- Artificial Intelligence
- AI Agents
- LLM
- Prompt Engineering
- Workflow Automation
- No Code
- Company
website: https://wordware.ai
---
