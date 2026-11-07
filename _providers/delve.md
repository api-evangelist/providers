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
  href: https://artifacts.apis.io/delve/hosts/delve-hosts.yml
  title: ''
  type: Hosts
  url: hosts/delve-hosts.yml
- group: other
  href: https://artifacts.apis.io/delve/vendors/delve-vendors.yml
  title: ''
  type: Vendors
  url: vendors/delve-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.delve.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.delve.com/news
- group: auth
  href: https://artifacts.apis.io/delve/security/delve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delve-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.delve.com
coverage:
  checked: '2026-10-23'
  detail: Docs require login and render via JavaScript, preventing machine-readable spec retrieval.
  evidence:
  - status: 200
    url: https://www.delve.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Delve is a technology company focused on providing advanced data analytics and integration solutions for enterprises. The company offers APIs that enable customers to ingest, process, and visualize large datasets, facilitating better decision-making and operational efficiency. Delve’s platform emphasizes security, scalability, and ease of integration across various industry sectors.
image: https://cms.delve.com/assets/images/_1200x630_crop_center-center_82_none/Delve_titlecard.png?mtime=1654035558
layout: provider
modified: '2026-10-22'
name: Delve
nav: Providers
network: true
overview: Delve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, Integration, Enterprise, and API Platform.
random_paper: 0
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  previous_composite: 6.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/delve/delve-2026-11-03T130518.png
security:
- kind: domain-security
  name: Delve Domain Security
  slug: delve-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: delve
tags:
- Company
- Data Analytics
- Integration
- Enterprise
- API Platform
website: https://www.delve.com
---
