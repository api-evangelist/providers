---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/lavante-com/hosts/lavante-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lavante-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lavante-com/vendors/lavante-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lavante-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/lavante-com/security/lavante-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lavante-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.lavante.com/
coverage:
  checked: '2026-10-29'
  detail: Lavante’s website redirects to PRGX and provides no public API documentation or machine‑readable specification.
  evidence:
  - status: 302
    url: https://www.lavante.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'Lavante is a venture‑backed technology company identified in the API Evangelist harvest backlog (source: vc‑portfolio; backed by sapphire‑ventures). Its public web presence redirects from www.lavante.com to the PRGX Global website, indicating it operates as a product or subsidiary within PRGX’s portfolio of tech‑enabled procurement and spend‑analytics solutions. Lavante’s positioning focuses on helping enterprises recover lost profit and optimize source‑to‑pay (S2P) data through analytics, audit services, and automation tools, aligning with PRGX’s broader mission to unlock savings and improve business health for large organizations.'
image: https://www.prgx.com/wp-content/uploads/2025/07/BHP-small.png
layout: provider
modified: '2026-10-28'
name: Lavante
nav: Providers
network: true
overview: Lavante is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Analytics, Procurement, and Software-as-a-Service.
plans:
- name: Lavante Com Plans Pricing
  plan_count: 0
  slug: lavante-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Lavante Com Rate Limits
  slug: lavante-com-rate-limits
scopes:
- name: Lavante Com Scopes
  scope_count: 0
  slug: lavante-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lavante-com/lavante-com-2026-11-03T134719.png
security:
- kind: authentication
  name: Lavante Com Authentication
  slug: lavante-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lavante Com Domain Security
  slug: lavante-com-domain-security
  summary_line: DNSSEC
slug: lavante-com
tags:
- Company
- Finance
- Analytics
- Procurement
- Software-as-a-Service
website: http://www.lavante.com/
---
