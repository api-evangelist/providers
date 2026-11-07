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
  href: https://artifacts.apis.io/wixsite-com/hosts/wixsite-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wixsite-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/wixsite-com/vendors/wixsite-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wixsite-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/wixsite-com/security/wixsite-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wixsite-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://percolata.wixsite.com/percolata
- group: docs
  title: ''
  type: Documentation
  url: https://percolata.wixsite.com/percolata
- group: operate
  title: ''
  type: ContactForm
  url: https://percolata.wixsite.com/percolata/contact-form
- group: commercial
  title: ''
  type: TermsOfService
  url: https://percolata.wixsite.com/percolata/terms-of-policy
- group: build
  title: ''
  type: Integration
  url: https://percolata.wixsite.com/percolata/een-integration
coverage:
  checked: '2026-10-24'
  detail: The provider's documentation site is a Wix-generated page rendered via JavaScript, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://percolata.wixsite.com/percolata
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Percolata offers AI-based people counting technology for global businesses to comply with COVID-19 occupancy limit laws. It provides predictive analytics to forecast sales and foot traffic, helping organizations optimize staffing and delivery levels. The company leverages machine learning to improve marketing and operations decisions, aiming to increase revenue during the pandemic and beyond.
layout: provider
modified: '2026-10-24'
name: Percolata
nav: Providers
network: true
overview: 'Percolata is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Analytics, Retail, and Staffing.


  Percolata''s developer surface includes documentation and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wixsite-com/wixsite-com-2026-11-03T150220.png
security:
- kind: domain-security
  name: Wixsite Com Domain Security
  slug: wixsite-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wixsite-com
tags:
- Company
- Artificial Intelligence
- Analytics
- Retail
- Staffing
website: https://percolata.wixsite.com/percolata
---
