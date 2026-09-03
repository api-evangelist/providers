---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'Versioned REST API for MSME credit assessment and decisioning. Submits applications for real-time scoring and returns a decision, risk flags, and pricing (e.g. POST /v1/assessments). Supports webhook '
  name: Abwab.ai Credit Intelligence API
  slug: abwabai-credit-intelligence-api
artifact_total: 3
asyncapis:
- description: ''
  name: Abwab Ai Webhooks
  slug: abwab-ai-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abwab-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abwab.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://abwab.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://abwab.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://abwab.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://abwab.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://abwab.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abwab.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abwab.ai/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://abwab.ai/platform/compliance
- group: design
  title: ''
  type: Conformance
  url: conformance/abwab-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abwab-ai-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abwab-ai-llms.txt
created: '2026-07-17'
description: Abwab.ai is an AI-powered credit intelligence platform for MSME (micro, small, and medium enterprise) lending, used by banks, NBFIs, fintechs, funds, and digital platforms to originate loans, assess credit risk, price, and monitor MSME loan portfolios across the full lending lifecycle. The platform combines rules and AI models for real-time credit decisioning, agentic credit intelligence that surfaces leads and flags portfolio risk, and embedded financing for existing SME platforms. It is API-first, plugging into existing loan-origination and core-banking systems without core replacement, with a versioned REST API (api.abwab.ai), webhook notifications, and Python/Node.js SDKs in development. Abwab is focused on the Saudi Arabian market with in-Kingdom data residency and alignment to the SAMA Cybersecurity Framework, PDPL, and Sharia-compliant lending (used by Kafalah). Backed by Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abwab-ai.png
layout: provider
modified: '2026-07-17'
name: Abwab Ai
nav: Providers
network: true
overview: 'Abwab Ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MSME Lending, Credit Intelligence, Credit Decisioning, and Credit Scoring.


  The Abwab Ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Abwab Ai''s developer surface includes documentation, API reference, engineering blog, support, and 9 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 33.6
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abwab-ai/refs/heads/main/screenshots/abwab-ai-2026-07-25T181413.png
security:
- kind: domain-security
  name: Abwab Ai Domain Security
  slug: abwab-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abwab-ai
tags:
- Company
- MSME Lending
- Credit Intelligence
- Credit Decisioning
- Credit Scoring
- Fintech
- Embedded Finance
- Lending
- Saudi Arabia
- Artificial Intelligence
website: https://abwab.ai
---
