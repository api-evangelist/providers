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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Trueaccord Agentic Access
  operation_count: 6
  slug: trueaccord-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Create, retrieve, and manage customers (consumers) and their debts.
  name: TrueAccord Customers API
  slug: trueaccord-customers-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.trueaccord.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.trueaccord.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trueaccord.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trueaccord.com/recover/recover-api-reference
- group: company
  title: ''
  type: Blog
  url: https://blog.trueaccord.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trueaccord.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trueaccord.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.trueaccord.com/it-security
- group: auth
  title: ''
  type: Authentication
  url: authentication/trueaccord-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trueaccord-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/trueaccord-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trueaccord-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trueaccord-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trueaccord-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trueaccord-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trueaccord-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trueaccord-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/trueaccord-recover-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trueaccord-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: TrueAccord is a digital-first, omnichannel debt collection agency that uses data science and machine learning to recover consumer debt with a consumer-friendly, self-service experience. Through its Recover API, creditors and debt buyers place consumers and their debts for collection and manage customer records — customers, their contact information (addresses, phones, emails), and the debts placed against them — over a simple HTTPS interface secured with HTTP Basic authentication (API key as username) plus an X-TA-CREDITOR header for multi-creditor accounts. TrueAccord also operates first-party collections through its Sentry Credit subsidiary and its HeartBeat and HumAIn platforms, and is ISO 27001 certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trueaccord.png
layout: provider
mcp_servers:
- description: ''
  name: trueaccord-mcp.yml
  slug: trueaccord-mcpyml
modified: '2026-07-21'
name: TrueAccord
nav: Providers
network: true
overview: 'TrueAccord publishes 1 API on the [APIs.io](https://apis.io/) network: Customers API. Tagged areas include Company, Debt Collection, Financial Services, Fintech, and Machine Learning.


  TrueAccord''s developer surface includes documentation, API reference, engineering blog, authentication, and 16 more developer resources.'
random_paper: 24
score:
  band: thin
  composite: 38.2
  delta: -0.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.2
    developer_ergonomics: 40.8
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Trueaccord Authentication
  slug: trueaccord-authentication
  summary_line: http · 1 scheme
slug: trueaccord
tags:
- Company
- Debt Collection
- Financial Services
- Fintech
- Machine Learning
- Collections
- Consumer Finance
website: https://www.trueaccord.com
---
