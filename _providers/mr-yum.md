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
  href: https://artifacts.apis.io/mr-yum/hosts/mr-yum-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mr-yum-hosts.yml
- group: other
  href: https://artifacts.apis.io/mr-yum/vendors/mr-yum-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mr-yum-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mr-yum/security/mr-yum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mr-yum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.meandu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.meandu.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.meandu.com/
- group: company
  title: ''
  type: Blog
  url: https://www.meandu.com/blog
- group: commercial
  title: ''
  type: Legal
  url: https://www.meandu.com/legal-stuff
coverage:
  checked: '2026-10-27'
  detail: The developer portal at https://www.meandu.com/ serves only JavaScript‑rendered pages and provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.meandu.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Mr Yum, now operating under the brand Me&U, provides a cloud‑based platform that enables restaurants and hospitality venues to personalize guest experiences, streamline ordering, payments, loyalty programs, and staff management. The solution supports multi‑vendor ordering, CRM integration, and reservation handling, aiming to boost operational efficiency and customer satisfaction across the hospitality industry.
image: https://cdn.prod.website-files.com/68cb96140013fa535857f2bf/692d1368cfee03cc357a9a46_homeOG.jpg
layout: provider
modified: '2026-10-27'
name: Mr Yum
nav: Providers
network: true
overview: 'Mr Yum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, RestaurantTech, Software-as-a-Service, Ordering, and Loyalty.


  Mr Yum''s developer surface includes documentation, engineering blog, legal docs, and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mr-yum/mr-yum-2026-11-03T135900.png
security:
- kind: domain-security
  name: Mr Yum Domain Security
  slug: mr-yum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mr-yum
tags:
- Hospitality
- RestaurantTech
- Software-as-a-Service
- Ordering
- Loyalty
website: https://www.meandu.com/
---
