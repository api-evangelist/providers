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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-01'
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
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TrueAccord Recover Customers API
  slug: open-trueaccord-customers-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/trueaccord-capability-edges.yml
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
  name: TrueAccord MCP Server
  slug: trueaccord-mcp-server
modified: '2026-07-21'
name: TrueAccord
nav: Providers
network: true
overview: 'TrueAccord publishes 1 API on the [APIs.io](https://apis.io/) network: Customers API. Tagged areas include Company, Debt Collection, Financial-Services, Fintech, and Machine-Learning.


  TrueAccord''s developer surface includes documentation, API reference, engineering blog, authentication, and 17 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 57.8
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 35.3
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Financial-Services
- Fintech
- Machine-Learning
- Collection
- Consumer Finance
website: https://www.trueaccord.com
---
