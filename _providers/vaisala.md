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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Blog
  url: https://www.vaisala.com/en/blog/2026-10/people-vaisala-meet-karla-tapia-senior-marketing-manager
- group: auth
  title: ''
  type: Security
  url: https://www.vaisala.com/en/vaisala-policies#security-policy
- group: auth
  href: https://artifacts.apis.io/vaisala/well-known/vaisala-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vaisala-security.txt
- group: agent
  href: https://artifacts.apis.io/vaisala/well-known/vaisala-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vaisala-well-known.yml
- group: other
  href: https://artifacts.apis.io/vaisala/hosts/vaisala-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vaisala-hosts.yml
- group: other
  href: https://artifacts.apis.io/vaisala/vendors/vaisala-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vaisala-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vaisala.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.vaisala.com/news-and-media/news
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vaisala.com/
- group: auth
  href: https://artifacts.apis.io/vaisala/security/vaisala-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vaisala-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vaisala/security/vaisala-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vaisala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vaisala.com
- group: operate
  title: ''
  type: Support
  url: https://www.vaisala.com/en/support-portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vaisala.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vaisala.com/en/vaisala-privacy-policy
coverage:
  checked: '2026-10-15'
  detail: Documentation site serves only a JavaScript shell with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.vaisala.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Vaisala is a global leader in measurement instruments and intelligence, providing weather, climate and industrial solutions. With over 1 million sensors manufactured annually and a presence in 150+ countries, Vaisala delivers reliable data for climate action, aviation, energy and many other sectors, supporting customers worldwide with innovative technologies and services.
layout: provider
modified: '2026-10-14'
name: Vaisala
nav: Providers
network: true
overview: 'Vaisala is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Climate, Sensors, and Industrial.


  Vaisala''s developer surface includes engineering blog, documentation, support, and 12 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 45.5
    operational_transparency: 13.2
  previous_composite: 17.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vaisala/vaisala-2026-11-03T145605.png
security:
- kind: domain-security
  name: Vaisala Domain Security
  slug: vaisala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vaisala Vulnerability Disclosure
  slug: vaisala-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vaisala
tags:
- Company
- Weather
- Climate
- Sensors
- Industrial
website: https://www.vaisala.com
---
