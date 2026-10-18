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
  href: https://raw.githubusercontent.com/api-evangelist/circtec/refs/heads/main/hosts/circtec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circtec-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/circtec/refs/heads/main/vendors/circtec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/circtec-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/circtec/refs/heads/main/security/circtec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circtec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-10-08'
  detail: Circtec provides sustainability products and has no developer portal or API documentation.
  evidence:
  - status: 200
    url: https://www.circtec.com
  reason: not-a-software-company
  state: none
created: '2026-10-08'
description: Circtec is a UK‑based innovator and operator of pyrolysis technology that recycles end‑of‑life tyres into renewable drop‑in fuels and circular chemicals. Since 2009 the company has developed cutting‑edge processes to extract carbon black and other valuable compounds, delivering sustainable fuels and liquid chemicals for the petrochemical and oil sectors. Circtec focuses on scaling sustainability through smart chemistry and advanced engineering, positioning itself as a leader in the circular economy and renewable energy markets.
image: https://www.circtec.com/wp-content/uploads/2021/05/infographic_24_05_21B-scaled.jpg
layout: provider
modified: '2026-10-08'
name: Circtec
nav: Providers
network: true
overview: Circtec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sustainability, Pyrolysis, RenewableEnergy, and Circular Economy.
random_paper: 7
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
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
  name: Circtec Domain Security
  slug: circtec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: circtec
tags:
- Company
- Sustainability
- Pyrolysis
- RenewableEnergy
- Circular Economy
website: https://www.nasdaqprivatemarket.com/
---
