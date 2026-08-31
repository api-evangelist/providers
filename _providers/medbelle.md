---
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
  scored_at: '2026-08-30'
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
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 4.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
