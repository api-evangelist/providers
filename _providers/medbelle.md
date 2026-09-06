---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://medbelle.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Medbelle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medbelle/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medbelle-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medbelle-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medbelle-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/medbelle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/medbelle-rate-limits.yml
coverage:
  checked: '2026-08-25'
  detail: Medbelle ceased trading in 2026; medbelle.com now serves a single static farewell page at "/" and a custom 404 for every other path, including the previously indexed /careconnect/ and /about/ pages, and api./docs./developers.medbelle.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://medbelle.com/
  - status: 404
    url: https://medbelle.com/careconnect/
  - status: 404
    url: https://medbelle.com/openapi.json
  - status: 404
    url: https://medbelle.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/Medbelle/repos
  reason: defunct
  state: none
created: '2026-08-25'
description: Medbelle was a London-headquartered digital healthcare company, founded in 2016 by Leander de Laporte and Daniel Kolb, that operated as a "digital hospital" coordinating elective specialist care across the UK. It combined a technology platform (marketed as Medbelle OS, with a CareConnect virtual-first assessment pathway) with human Patient Care Advisers to route patients through consultation, diagnostics, surgery and aftercare, working with clinicians, hospitals, insurers, employers and case managers. Specialties spanned cosmetic, bariatric, orthopaedic and ophthalmic surgery. Medbelle ceased trading in 2026 and its technology platform was transferred elsewhere; medbelle.com now serves a single farewell page and every other path on the domain returns 404. No public developer program, API documentation or machine-readable API contract was ever published, and none survives.
image: https://medbelle.com/assets/medbelle-logo.svg
layout: provider
modified: '2026-08-25'
name: Medbelle
nav: Providers
network: true
overview: Medbelle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Elective Surgery, and Patient Care Coordination.
plans:
- name: Medbelle Plans Pricing
  plan_count: 0
  slug: medbelle-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Medbelle Rate Limits
  slug: medbelle-rate-limits
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 4.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medbelle/refs/heads/main/screenshots/medbelle-2026-09-02T150451.png
security:
- kind: domain-security
  name: Medbelle Domain Security
  slug: medbelle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: medbelle
tags:
- Company
- Healthcare
- Digital Health
- Elective Surgery
- Patient Care Coordination
- United Kingdom
- Defunct
website: https://medbelle.com/
---
