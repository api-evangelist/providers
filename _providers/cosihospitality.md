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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cosihospitality/refs/heads/main/hosts/cosihospitality-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cosihospitality-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cosihospitality/refs/heads/main/vendors/cosihospitality-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cosihospitality-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cosihospitality/refs/heads/main/security/cosihospitality-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cosihospitality-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getcosi.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.getcosi.com
  - status: 403
    url: https://equityzen.com/company/cosihospitality
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Cosihospitality operates under the Così brand, providing catering services and fresh food ordering through its website getcosi.com. The company offers a range of menu options, location-based catering, and an online ordering platform for events and corporate clients. It serves multiple US cities, supports online quotes, loyalty programs, and integrates with third‑party delivery services. The platform includes detailed FAQs, a story about the brand, and contact options for catering inquiries.
image: https://images.getbento.com/accounts/2b3fa09317b4f49d36c34188bda32d3f/media/images/71967logo.png?w=1200&fit=fill&auto=compress,format&cs=origin&h=600&bg=fff&pad=100
layout: provider
modified: '2026-10-11'
name: Cosihospitality
nav: Providers
network: true
overview: Cosihospitality is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Catering, Food Tech, OnlineOrdering, and Hospitality.
random_paper: 12
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cosihospitality Domain Security
  slug: cosihospitality-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cosihospitality
tags:
- Company
- Catering
- Food Tech
- OnlineOrdering
- Hospitality
website: https://www.getcosi.com
---
