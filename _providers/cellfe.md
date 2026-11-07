---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cellfe/hosts/cellfe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellfe-hosts.yml
- group: other
  href: https://artifacts.apis.io/cellfe/vendors/cellfe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cellfe-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cellfebiotech.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cellfebiotech.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cellfebiotech.com/news/
- group: auth
  href: https://artifacts.apis.io/cellfe/security/cellfe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellfe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cellfebiotech.com/
coverage:
  checked: '2026-10-07'
  detail: CellFE Biotech website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.cellfebiotech.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: CellFE is a biotech company focused on transforming cell therapy manufacturing through microfluidics technology, aiming to make advanced treatments affordable and accessible for patients worldwide. The company provides platforms and services that streamline production, reduce costs, and accelerate the delivery of cell-based medicines.
image: https://www.cellfebiotech.com/wp-content/uploads/2025/01/CellFE-Products1.jpg
layout: provider
modified: '2026-10-07'
name: CellFE
nav: Providers
network: true
overview: CellFE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Cell Therapy, Microfluidics, Healthcare, and Platform.
random_paper: 19
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  previous_composite: 9.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cellfe/cellfe-2026-11-03T123609.png
security:
- kind: domain-security
  name: Cellfe Domain Security
  slug: cellfe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cellfe
tags:
- Biotechnology
- Cell Therapy
- Microfluidics
- Healthcare
- Platform
website: https://www.cellfebiotech.com/
---
