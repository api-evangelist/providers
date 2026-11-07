---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AgentRamp turns your existing API into a hosted MCP server, providing a stable endpoint for AI agents to call your tools.
  name: AgentRamp MCP
  slug: agentramp-mcp
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/agentramp-io/plans/agentramp-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentramp-io-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/agentramp-io/authentication/agentramp-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentramp-io-authentication.yml
- group: agent
  href: https://artifacts.apis.io/agentramp-io/llms/agentramp-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentramp-io-llms.txt
- group: other
  href: https://artifacts.apis.io/agentramp-io/hosts/agentramp-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentramp-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentramp-io/vendors/agentramp-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentramp-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://agentramp.io/login
- group: auth
  href: https://artifacts.apis.io/agentramp-io/security/agentramp-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentramp-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentramp.io/
- group: docs
  title: ''
  type: Documentation
  url: https://agentramp.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://agentramp.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentramp.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentramp.io/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://agentramp.io/docs
coverage:
  checked: '2026-10-30'
  detail: Public documentation exists but no machine-readable OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://agentramp.io/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: AgentRamp provides hosted MCP (Managed Contract Proxy) servers that sit in front of your API documentation, offering a stable, monitored endpoint that agents can call. The service automatically updates as the underlying API specification evolves, ensuring continuity for integrations. It supports various protocols, offers health monitoring, and aims to simplify API versioning and deprecation handling for developers.
image: https://agentramp.io/static/logo-dark.png
layout: provider
modified: '2026-10-30'
name: agentramp-io
nav: Providers
network: true
overview: 'agentramp-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, API Management, Monitoring, and Proxy.


  agentramp-io''s developer surface includes authentication, documentation, pricing, getting-started guide, and 9 more developer resources.'
plans:
- name: Agentramp Io Plans Pricing
  plan_count: 3
  slug: agentramp-io-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Agentramp Io Rate Limits
  slug: agentramp-io-rate-limits
scopes:
- name: Agentramp Io Scopes
  scope_count: 0
  slug: agentramp-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 30.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agentramp-io/agentramp-io-2026-11-03T120405.png
security:
- kind: authentication
  name: Agentramp Io Authentication
  slug: agentramp-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentramp Io Domain Security
  slug: agentramp-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentramp-io
tags:
- Company
- MCP
- API Management
- Monitoring
- Proxy
- Developer Tools
website: https://agentramp.io/
---
