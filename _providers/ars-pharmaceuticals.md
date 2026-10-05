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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ars-pharmaceuticals/refs/heads/main/hosts/ars-pharmaceuticals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ars-pharmaceuticals-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ars-pharmaceuticals/refs/heads/main/vendors/ars-pharmaceuticals-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ars-pharmaceuticals-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ars-pharmaceuticals/refs/heads/main/security/ars-pharmaceuticals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ars-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ir.ars-pharma.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI or other machine-readable contract discovered at api.ars-pharma.com endpoints.
  evidence:
  - status: 0
    url: https://api.ars-pharma.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: ARS Pharmaceuticals is a biopharmaceutical company focused on developing innovative therapies for rare diseases. The company operates globally with a strong pipeline of products and a commitment to patient care, research, and collaboration with healthcare partners. It maintains an investor relations site and corporate information portal, providing detailed product, pipeline, and regulatory information.
layout: provider
modified: '2026-09-26'
name: ARS Pharmaceuticals
nav: Providers
network: true
overview: ARS Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Healthcare, Pharmaceuticals, and Rare Disease.
random_paper: 3
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 4
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
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ars Pharmaceuticals Domain Security
  slug: ars-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ars-pharmaceuticals
tags:
- Company
- Biopharma
- Healthcare
- Pharmaceuticals
- Rare Disease
website: https://ir.ars-pharma.com
---
