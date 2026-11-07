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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://demo.wallosapp.com
  baseurl_source: spec
  description: API documentation for Wallos
  name: Wallos API
  slug: wallos-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/wallos/conformance/wallos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wallos-conformance.yml
- group: other
  href: https://artifacts.apis.io/wallos/hosts/wallos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wallos-hosts.yml
- group: other
  href: https://artifacts.apis.io/wallos/vendors/wallos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wallos-vendors.yml
- group: auth
  href: https://artifacts.apis.io/wallos/security/wallos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wallos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wallosapp.com/
created: '2026-10-28'
description: Wallos is an open-source personal subscription tracker that helps users manage and monitor their recurring expenses across various services. It provides a web interface to add, edit, and view subscription details, set reminders, and generate reports, empowering individuals to gain control over their finances and avoid unwanted charges.
image: https://wallosapp.com/images/logo/wallos.png
layout: provider
modified: '2026-10-28'
name: Wallos
nav: Providers
network: true
overview: Wallos is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Subscription, Finance, Open Source, and Tracker.
random_paper: 10
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 32.9
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/wallos/wallos-2026-11-03T145955.png
security:
- kind: domain-security
  name: Wallos Domain Security
  slug: wallos-domain-security
  summary_line: TLSv1.3
slug: wallos
tags:
- Company
- Subscription
- Finance
- Open Source
- Tracker
- Personal
website: https://wallosapp.com/
---
