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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.fleetsharp.com/security-policy
- group: other
  href: https://artifacts.apis.io/fleetsharp/vendors/fleetsharp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fleetsharp-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.fleetsharp.com/?rb.routing.mode=proxy&rb.routing.signature=236106
- group: auth
  href: https://artifacts.apis.io/fleetsharp/well-known/fleetsharp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fleetsharp-security.txt
- group: auth
  href: https://artifacts.apis.io/fleetsharp/well-known/fleetsharp-fleetsharp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fleetsharp-fleetsharp-security.txt
- group: agent
  href: https://artifacts.apis.io/fleetsharp/well-known/fleetsharp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fleetsharp-well-known.yml
- group: other
  href: https://artifacts.apis.io/fleetsharp/hosts/fleetsharp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fleetsharp-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.fleetsharp.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://help.fleetsharp.com/
- group: auth
  href: https://artifacts.apis.io/fleetsharp/security/fleetsharp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fleetsharp-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fleetsharp/security/fleetsharp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fleetsharp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fleetsharp.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fleetsharp.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fleetsharp.com/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://activate.fleetsharp.com/getstarted/
coverage:
  checked: '2026-10-28'
  detail: The site provides no developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://www.fleetsharp.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: FleetSharp provides GPS-based fleet tracking solutions, offering real-time vehicle location, driver behavior monitoring, equipment tracking, dash camera integration, and fuel cost reduction tools. Their platform enables businesses to improve safety, efficiency, and asset utilization through powerful mapping, alerts, and analytics.
image: https://www.fleetsharp.com/assets/images/heroimages/tool-tracker.jpg
layout: provider
modified: '2026-10-28'
name: FleetSharp
nav: Providers
network: true
overview: 'FleetSharp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include GPS, Fleet Tracking, Asset Management, Dash Cameras, and Software.


  FleetSharp''s developer surface includes support, documentation, getting-started guide, and 12 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 18.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fleetsharp/fleetsharp-2026-11-03T132130.png
security:
- kind: domain-security
  name: Fleetsharp Domain Security
  slug: fleetsharp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fleetsharp Vulnerability Disclosure
  slug: fleetsharp-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fleetsharp
tags:
- GPS
- Fleet Tracking
- Asset Management
- Dash Cameras
- Software
website: https://fleetsharp.com/
---
