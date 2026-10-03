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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aspirefoodgroup/refs/heads/main/hosts/aspirefoodgroup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aspirefoodgroup-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aspirefoodgroup/refs/heads/main/vendors/aspirefoodgroup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aspirefoodgroup-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://aspirefg.com/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aspirefoodgroup/refs/heads/main/security/aspirefoodgroup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aspirefoodgroup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aspirefg.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/aspirefoodgroup
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Aspire Food Group pioneers sustainable insect agriculture, producing protein from crickets at scale. Leveraging robotics, automation, and advanced technologies, they aim to meet growing global food demand with environmentally responsible solutions. Their vision is a world transformed by insect technology, delivering healthy, scalable protein while reducing environmental impact.
layout: provider
modified: '2026-09-26'
name: Aspirefoodgroup
nav: Providers
network: true
overview: Aspirefoodgroup is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Food, Agriculture, Insect Protein, Sustainability, and Technology.
random_paper: 19
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aspirefoodgroup Domain Security
  slug: aspirefoodgroup-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aspirefoodgroup
tags:
- Food
- Agriculture
- Insect Protein
- Sustainability
- Technology
website: https://aspirefg.com
---
