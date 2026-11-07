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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/agentorist-com/hosts/agentorist-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentorist-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentorist-com/vendors/agentorist-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentorist-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentorist-com/security/agentorist-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentorist-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentorist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentorist.com/docs
- group: auth
  title: ''
  type: Security
  url: https://agentorist.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentorist.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentorist.com/terms
coverage:
  checked: '2026-11-01'
  detail: No public API documentation or machine-readable contract was found on the provider's site.
  evidence:
  - status: 200
    url: https://agentorist.com/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Agentorist is a trusted booking intermediary for the Agentic economy, enabling discovery, routing, and booking of experiences, events, hotels, packages, cars, restaurants, and any bookable service through AI agents. Built on the Model Context Protocol, it integrates with Claude, ChatGPT, Grok, and Gemini, offering developers a platform to connect AI with real-world bookings.
layout: provider
modified: '2026-11-01'
name: Agentorist
nav: Providers
network: true
overview: 'Agentorist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Booking, Artificial Intelligence, Intermediary, Travel, and Platform.


  Agentorist''s developer surface includes documentation and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 5.3
  previous_composite: 11.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentorist Com Domain Security
  slug: agentorist-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentorist-com
tags:
- Booking
- Artificial Intelligence
- Intermediary
- Travel
- Platform
- Agentorist
website: https://agentorist.com/
---
