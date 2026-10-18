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
  href: https://raw.githubusercontent.com/api-evangelist/carbocode/refs/heads/main/hosts/carbocode-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbocode-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbocode/refs/heads/main/vendors/carbocode-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbocode-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbocode/refs/heads/main/security/carbocode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbocode-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbocode.com
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at the API host.
  evidence:
  - status: 0
    url: https://api.carbocode.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Carbocode is a glycosphingolipid company focused on developing and commercializing carbohydrate-based therapeutics. The firm specializes in research and production of complex glycosphingolipids for use in medical and scientific applications, offering expertise in lipid synthesis, analysis, and supply chain management. While primarily a biotech entity, Carbocode maintains a corporate website providing company information, product overviews, and contact details.
image: https://storage.googleapis.com/wzsitethumbnails/site-42356272/800x500.jpg
layout: provider
modified: '2026-10-06'
name: Carbocode
nav: Providers
network: true
overview: Carbocode is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Glycosphingolipids, Therapeutics, and Research.
random_paper: 6
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
    mcp: derived
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
  name: Carbocode Domain Security
  slug: carbocode-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: carbocode
tags:
- Company
- Biotechnology
- Glycosphingolipids
- Therapeutics
- Research
website: https://carbocode.com
---
