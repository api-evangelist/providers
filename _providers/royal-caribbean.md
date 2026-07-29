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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 8
common:
- group: auth
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
- group: other
  title: ''
  type: ConsumerSite
  url: https://www.royalcaribbean.com/
- group: start
  title: ''
  type: TravelPartnerPortal
  url: https://www.cruisingpower.com/
- group: other
  title: ''
  type: LoyaltyProgram
  url: https://www.royalcaribbean.com/loyalty/crown-and-anchor
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/royal-caribbean-vocabulary.yml
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
modified: '2026-05-16'
name: Royal Caribbean Group
nav: Providers
network: true
overview: Royal Caribbean Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cruise Lines, Travel, and Hospitality.
random_paper: 75
score:
  band: minimal
  composite: 6.0
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 10.4
    operational_transparency: 5.3
  previous_composite: 7.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/royal-caribbean/refs/heads/main/screenshots/royal-caribbean-2026-06-20T193231.png
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
use_cases:
- description: Travel agents book cruises and manage groups via CruisingPower
  name: Travel Agent Booking
- description: Travelers search itineraries, ships, and onboard experiences
  name: Consumer Cruise Search
- description: Crown & Anchor members accrue points and unlock cruise perks
  name: Loyalty Tier Management
website: https://www.royalcaribbeangroup.com/
---
