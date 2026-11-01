---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/royal-caribbean/hosts/royal-caribbean-hosts.yml
  title: ''
  type: Hosts
  url: hosts/royal-caribbean-hosts.yml
- group: other
  href: https://artifacts.apis.io/royal-caribbean/vendors/royal-caribbean-vendors.yml
  title: ''
  type: Vendors
  url: vendors/royal-caribbean-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://royalcaribbeangroup.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://dev.royalcaribbeangroup.com/
- group: company
  title: ''
  type: Blog
  url: https://www.royalcaribbeangroup.com/news/
- group: auth
  href: https://artifacts.apis.io/royal-caribbean/security/royal-caribbean-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/royal-caribbean-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RCCL
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/royal-caribbean-group
- group: company
  title: ''
  type: Website
  url: https://www.royalcaribbeangroup.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.royalcaribbeangroup.com/royal-caribbeans-privacy-notice/
- group: other
  title: ''
  type: ConsumerSite
  url: https://www.royalcaribbean.com/
- group: start
  title: ''
  type: TravelPartnerPortal
  url: https://www.cruisingpower.com/
- group: design
  href: https://artifacts.apis.io/royal-caribbean/vocabulary/royal-caribbean-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/royal-caribbean-vocabulary.yml
coverage:
  checked: '2026-10-20'
  detail: Royal Caribbean Group publishes no public API or contract; api.* hosts serve no OpenAPI/GraphQL/MCP, dev.royalcaribbeangroup.com is a mirror of the corporate site rather than a developer portal, and travel-partner integration sits behind the authenticated CruisingPower agent portal.
  evidence:
  - status: 200
    url: https://dev.royalcaribbeangroup.com/
  - status: 403
    url: https://www.royalcaribbean.com/mcp/v1
  - status: 404
    url: https://www.royalcaribbean.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-05-05'
description: Royal Caribbean Group is a global cruise vacation company operating Royal Caribbean International, Celebrity Cruises, and Silversea Cruises. Royal Caribbean does not publish a public developer API. Travel partner and agent integration is operated through the CruisingPower B2B portal (cruisingpower.com), which requires authenticated agent access. The company also operates loyalty (Crown & Anchor Society) and consumer booking platforms with no public API surface.
features:
- description: Consumer-facing platform for searching and booking cruise itineraries
  name: Cruise Booking Platform
- description: Authenticated travel agent portal for booking, commissions, and group management
  name: CruisingPower B2B Portal
- description: Loyalty program tracking tier benefits across Royal Caribbean cruises
  name: Crown & Anchor Society
- description: Royal Caribbean International, Celebrity Cruises, and Silversea Cruises
  name: Brand Portfolio
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/royal-caribbean.png
layout: provider
modified: '2026-10-06'
name: Royal Caribbean Group
nav: Providers
network: true
overview: 'Royal Caribbean Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cruise Lines, Travel, Hospitality, Cruises, and Leisure.


  Royal Caribbean Group''s developer surface includes documentation, engineering blog, and 11 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 28.3
    catalog_earned_first_party: 0.0
    catalog_gap: 86.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 3.8
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 5.3
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/royal-caribbean/royal-caribbean-2026-06-20T193231.png
security:
- kind: domain-security
  name: Royal Caribbean Domain Security
  slug: royal-caribbean-domain-security
  summary_line: TLSv1.3 · HSTS
slug: royal-caribbean
tags:
- Cruise Lines
- Travel
- Hospitality
- Cruises
- Leisure
use_cases:
- description: Travel agents book cruises and manage groups via CruisingPower
  name: Travel Agent Booking
- description: Travelers search itineraries, ships, and onboard experiences
  name: Consumer Cruise Search
- description: Crown & Anchor members accrue points and unlock cruise perks
  name: Loyalty Tier Management
website: https://www.royalcaribbeangroup.com/
---
