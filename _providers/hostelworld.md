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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/hostelworld/llms/hostelworld-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hostelworld-llms.txt
- group: agent
  href: https://artifacts.apis.io/hostelworld/well-known/hostelworld-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hostelworld-well-known.yml
- group: other
  href: https://artifacts.apis.io/hostelworld/hosts/hostelworld-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hostelworld-hosts.yml
- group: other
  href: https://artifacts.apis.io/hostelworld/vendors/hostelworld-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hostelworld-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://signup.hostelworld.com/en/property/intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hostelworld
- group: auth
  href: https://artifacts.apis.io/hostelworld/security/hostelworld-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hostelworld-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hostelworld.com/
- group: operate
  title: ''
  type: Support
  url: https://hwhelp.hostelworldgroup.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.hostelworld.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hostelworld.com/legal/hostel-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hostelworld.com/legal/security-privacy/
coverage:
  checked: 2026-09-23
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts found after probing known API hosts.
  evidence:
  - status: 404
    url: https://api.hostelworld.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: Online confirmed bookings for backpacker hostels around the world. City guides, sightseeing, entertainment and backpacking information for hostels and backpacker tours around the world.
image: https://a.hwstatic.com/image/upload/f_auto,q_auto,h_600/v1647449187/pwa/hostelworld.png
layout: provider
modified: '2026-09-23'
name: Hostelworld
nav: Providers
network: true
overview: 'Hostelworld is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Accommodation, Booking, and Hospitality.


  Hostelworld''s developer surface includes signup flow, support, engineering blog, and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 46.4
    operational_transparency: 2.6
  previous_composite: 13.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hostelworld/hostelworld-2026-10-11T105428.png
security:
- kind: domain-security
  name: Hostelworld Domain Security
  slug: hostelworld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hostelworld
tags:
- Company
- Travel
- Accommodation
- Booking
- Hospitality
website: https://hostelworld.com/
---
