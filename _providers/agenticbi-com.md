---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for AgenticBI analytics and reporting.
  name: AgenticBI REST API
  slug: agenticbi-rest-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/agenticbi-com/authentication/agenticbi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenticbi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/agenticbi-com/errors/agenticbi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agenticbi-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/agenticbi-com/llms/agenticbi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenticbi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agenticbi-com/well-known/agenticbi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenticbi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenticbi-com/hosts/agenticbi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticbi-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agenticbi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agenticbi.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://app.agenticbi.com/plans
- group: docs
  title: ''
  type: Documentation
  url: https://app.agenticbi.com/docs/getting-started.html
- group: start
  title: ''
  type: GettingStarted
  url: https://app.agenticbi.com/docs/docs/getting-started.html
- group: auth
  href: https://artifacts.apis.io/agenticbi-com/security/agenticbi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticbi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agenticbi.com/
coverage:
  checked: '2026-11-01'
  detail: The public documentation pages describe the REST API but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other spec is published.
  evidence:
  - status: 200
    url: https://app.agenticbi.com/docs/rest-api.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agentic BI lets users ask a single natural‑language prompt and receive full analytics results, including charts, Slack alerts, and scheduled reports, without their data ever reaching OpenAI or Google. The platform runs on private AI models or lets users choose third‑party models, connects to any data source—SQL, NoSQL, REST APIs—without custom pipelines, and delivers answers in Slack, Teams, email, or via Claude, ChatGPT, Cursor, and other MCP clients. It offers a free trial and emphasizes data privacy and flexibility for businesses.
image: https://framerusercontent.com/assets/NQhYnzhZSWNyAe0N0Gd6Q1z048.png
layout: provider
modified: '2026-11-01'
name: Agentic BI
nav: Providers
network: true
overview: 'Agentic BI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Business Intelligence, Automation, and Software-as-a-Service.


  Agentic BI''s developer surface includes authentication, pricing, documentation, getting-started guide, and 8 more developer resources.'
plans:
- name: Agenticbi Com Plans Pricing
  plan_count: 0
  slug: agenticbi-com-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 19.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenticbi Com Authentication
  slug: agenticbi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agenticbi Com Domain Security
  slug: agenticbi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agenticbi-com
tags:
- Artificial Intelligence
- Analytics
- Business Intelligence
- Automation
- Software-as-a-Service
website: https://www.agenticbi.com/
---
