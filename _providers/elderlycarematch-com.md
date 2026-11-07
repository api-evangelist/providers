---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 9.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Agent2Agent (A2A 1.0) surface: an agent card at https://www.elderlycarematch.com/.well-known/agent-card.json (version 1.5.3, one JSONRPC interface, also mirrored at the legacy /.well-known/agent.json)'
  name: Elderly Care Match A2A Agent
  slug: elderly-care-match-a2a-agent
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.elderlycarematch.com/
- group: company
  title: ''
  type: Blog
  url: https://www.elderlycarematch.com/learning-center
- group: operate
  title: ''
  type: Support
  url: https://www.elderlycarematch.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elderlycarematch.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elderlycarematch.com/privacy-policy
- group: other
  href: https://artifacts.apis.io/elderlycarematch-com/a2a/elderlycarematch-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/elderlycarematch-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/elderlycarematch-com/llms/elderlycarematch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elderlycarematch-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.elderlycarematch.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/elderlycarematch-com/well-known/elderlycarematch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elderlycarematch-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/elderlycarematch-com/authentication/elderlycarematch-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elderlycarematch-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/elderlycarematch-com/conventions/elderlycarematch-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elderlycarematch-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/elderlycarematch-com/errors/elderlycarematch-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elderlycarematch-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/elderlycarematch-com/conformance/elderlycarematch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elderlycarematch-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/elderlycarematch-com/lifecycle/elderlycarematch-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elderlycarematch-com-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/elderlycarematch-com/plans/elderlycarematch-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elderlycarematch-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/elderlycarematch-com/rate-limits/elderlycarematch-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elderlycarematch-com-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/elderlycarematch-com/packages/elderlycarematch-com-packages.yml
  title: ''
  type: Packages
  url: packages/elderlycarematch-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/elderlycarematch-com/security/elderlycarematch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elderlycarematch-com-domain-security.yml
- group: other
  href: https://artifacts.apis.io/elderlycarematch-com/regulatory/elderlycarematch-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/elderlycarematch-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.elderlycarematch.com/privacy-policy
- group: operate
  title: ''
  type: IncidentNotification
  url: https://www.elderlycarematch.com/privacy-policy
- group: other
  title: ''
  type: DataResidency
  url: https://www.elderlycarematch.com/privacy-policy
- group: other
  title: ''
  type: Subprocessors
  url: https://www.elderlycarematch.com/privacy-policy
created: '2026-09-19'
description: 'Elderly Care Match is a Washington State senior-care directory and placement service that helps families find and compare licensed adult family homes (AFH), assisted living, memory care, nursing homes / skilled nursing and independent living, with listings that are free to browse, many cross-checked against the WA DSHS/ALTSA licence registry, and coverage strongest across the Seattle-Tacoma-Bellevue / Puget Sound metro. Its only machine interface is an Agent2Agent (A2A 1.0) agent: a card served at /.well-known/agent-card.json and a JSON-RPC 2.0 endpoint at https://www.elderlycarematch.com/a2a/v1 that answers anonymously with four read-only skills — search facilities by location, care type, Medicaid acceptance, vacancy and price; fetch a facility''s public profile; search the Learning Center guides; and hand a family off to a care advisor by returning a public form URL. It publishes no OpenAPI, SDK or MCP server; llms.txt is the documentation and robots.txt explicitly welcomes
  AI crawlers on /.well-known/ and /a2a/.'
image: https://www.elderlycarematch.com/images/brand/icon-512.png
layout: provider
modified: '2026-09-19'
name: Elderly Care Match
nav: Providers
network: true
overview: 'Elderly Care Match is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Senior Care, Elder Care, Assisted Living, Memory Care, and Adult Family Homes.


  Elderly Care Match''s developer surface includes engineering blog, support, authentication, and 20 more developer resources.'
plans:
- name: Elderlycarematch Com Plans Pricing
  plan_count: 0
  slug: elderlycarematch-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Elderlycarematch Com Rate Limits
  slug: elderlycarematch-com-rate-limits
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 22.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/elderlycarematch-com/elderlycarematch-com-2026-10-11T104101.png
security:
- kind: authentication
  name: Elderlycarematch Com Authentication
  slug: elderlycarematch-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Elderlycarematch Com Domain Security
  slug: elderlycarematch-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elderlycarematch-com
tags:
- Senior Care
- Elder Care
- Assisted Living
- Memory Care
- Adult Family Homes
- Nursing Homes
- Care Directory
- Healthcare
- Agents
- A2A
- Agent-Native
- Washington State
- United States
website: https://www.elderlycarematch.com/
---
