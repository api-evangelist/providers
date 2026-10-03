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
  href: https://raw.githubusercontent.com/api-evangelist/better-meat/refs/heads/main/hosts/better-meat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/better-meat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-meat/refs/heads/main/vendors/better-meat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/better-meat-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bmcingredients.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.bmcingredients.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/better-meat/refs/heads/main/security/better-meat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/better-meat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bmcingredients.com
coverage:
  checked: '2026-09-28'
  detail: OpenAPI spec endpoints (e.g., https://api.bmcingredients.com/openapi.json) returned no content.
  evidence:
  - status: 0
    url: https://api.bmcingredients.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Better Meat, operating under the brand BMC Ingredients, develops high‑protein mycelium‑based ingredients to create sustainable, animal‑free food products. The company focuses on biotechnology and food‑tech innovations that reduce environmental impact while delivering nutritious alternatives to traditional meat.
image: http://static1.squarespace.com/static/6883c85106f2737232592a9d/t/6a458a0a02b4a53962d93976/1782942218222/bmc_ingredients_logo_blue_orange.png?format=1500w
layout: provider
modified: '2026-09-28'
name: Better Meat
nav: Providers
network: true
overview: Better Meat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Tech, Biotechnology, Sustainable Food, and Mycelium.
random_paper: 14
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Better Meat Domain Security
  slug: better-meat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: better-meat
tags:
- Company
- Food Tech
- Biotechnology
- Sustainable Food
- Mycelium
- Alternative Protein
website: https://www.bmcingredients.com
---
