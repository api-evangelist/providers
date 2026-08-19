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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Oximy Agentic Access
  operation_count: 4
  slug: oximy-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: Project bootstrap — settings and policy configuration.
  name: Oximy Init API
  slug: oximy-init-api
- description: Policy configuration and server-side rule evaluation.
  name: Oximy Policy API
  slug: oximy-policy-api
- description: LLM request/response event ingestion.
  name: Oximy Telemetry API
  slug: oximy-telemetry-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oximy Public Init API
  slug: open-oximy-init-api
- collection_type: open
  name: Oximy Public Init Policy API
  slug: open-oximy-policy-api
- collection_type: open
  name: Oximy Public Init Telemetry API
  slug: open-oximy-telemetry-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/oximy-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://oximy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oximy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oximy.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oximy.com/docs/developer/public-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oximy.com/docs/developer/public-api
- group: company
  title: ''
  type: Blog
  url: https://oximy.com/blog
- group: operate
  title: ''
  type: Support
  url: https://oximy.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oximy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oximy.com/privacy
- group: build
  title: ''
  type: Packages
  url: packages/oximy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/oximy-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oximy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oximy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oximy-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oximy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oximy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oximy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oximy-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oximy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oximy-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oximy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oximy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oximy-authentication.yml
created: '2026-07-17'
description: Oximy is an AI adoption and governance platform — "the AI adoption engine for every company." It gives organizations visibility into how their people and applications use AI tools across the enterprise (tracking thousands of AI tools across categories), surfaces risks and recommendations, and lets teams ask natural-language questions about their AI usage. For developers, Oximy ships a Public API (https://api.oximy.com) and an official TypeScript SDK that wrap any OpenAI-compatible client to capture zero-overhead LLM telemetry and enforce usage policy inline — PII detection and redaction, prompt-injection detection, deny/allow lists, and token/cost/rate limits. Backed by Y Combinator (W26) and Blume Ventures; founded by Naman Ambavi.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oximy.png
layout: provider
mcp_servers:
- description: ''
  name: oximy-mcp.yml
  slug: oximy-mcpyml
modified: '2026-07-20'
name: Oximy
nav: Providers
network: true
overview: 'Oximy publishes 3 APIs on the [APIs.io](https://apis.io/) network: Init API, Policy API, and Telemetry API. Tagged areas include Company, AI Governance, LLM Observability, AI Adoption, and Telemetry.


  Oximy''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 18 more developer resources.'
random_paper: 119
score:
  band: developing
  composite: 46.3
  delta: 3.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 60.1
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oximy/refs/heads/main/screenshots/oximy-2026-08-07T191209.png
security:
- kind: authentication
  name: Oximy Authentication
  slug: oximy-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Oximy Domain Security
  slug: oximy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: oximy
tags:
- Company
- AI Governance
- LLM Observability
- AI Adoption
- Telemetry
- Policy Enforcement
- Artificial Intelligence
- Developer Tools
website: https://oximy.com
---
