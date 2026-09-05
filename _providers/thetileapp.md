---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://thetileapp.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.life360.com/ — a different registrable domain (thetileapp.com -> life360.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/life360/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thetileapp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/life360
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/thetileapp-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thetileapp-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thetileapp-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thetileapp-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://support.thetileapp.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thetileapp.com/en-us/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thetileapp.com/en-us/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://thetileapp.com
created: '2026-07-17'
description: Tile is a consumer Bluetooth-tracker company whose Tile Mate, Pro, Slim, and Sticker devices help people find everyday items such as keys, wallets, bags, and phones, backed by the crowd-sourced Tile "Find" network that anonymously relays location when another Tile user passes a lost item. Founded in 2012, Tile was acquired by Life360 in 2021 and now operates as part of the Life360 family-safety platform. Tile publishes consumer apps for iOS and Android and a support and legal surface, but does not offer an official public developer API, developer portal, or SDK; only third-party community libraries wrap its private app API. This API Evangelist profile captures the company's public web and security-program surface. Surfaced as a portfolio company of Slow Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thetileapp.png
layout: provider
modified: '2026-07-21'
name: Tile (thetileapp)
nav: Providers
network: true
overview: 'Tile (thetileapp) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bluetooth, Location, Tracking, and Consumer Electronics.


  Tile (thetileapp)''s developer surface includes support and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thetileapp/refs/heads/main/screenshots/thetileapp-2026-09-02T163524.png
security:
- kind: domain-security
  name: Thetileapp Domain Security
  slug: thetileapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thetileapp Vulnerability Disclosure
  slug: thetileapp-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: thetileapp
tags:
- Company
- Bluetooth
- Location
- Tracking
- Consumer Electronics
- IoT
- Find My
- Life360
website: https://thetileapp.com
---
