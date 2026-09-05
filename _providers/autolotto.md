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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autolotto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lottery.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lottery.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lottery.com/privacy
created: '2026-07-17'
description: AutoLotto, Inc. operates Lottery.com, a mobile platform that lets users in participating US states play official draw lottery games such as Powerball and Mega Millions from their phones, track tickets, view winning numbers, jackpot sizes and draw times, and collect winnings to a linked bank account. Beyond the consumer app, AutoLotto runs a business data-licensing offering that syndicates results and draw data for hundreds of lottery games worldwide to partner digital properties. AutoLotto is venture-backed (500 Global, Pantera Capital) and its parent trades publicly. As of this enrichment pass Lottery.com exposes no public developer API, OpenAPI specification, SDKs, or self-service developer portal; data access is arranged through a manual "license our data" inquiry form rather than a programmatic surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autolotto.png
layout: provider
modified: '2026-07-18'
name: AutoLotto
nav: Providers
network: true
overview: AutoLotto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lottery, Gaming, Consumer, and Mobile.
random_paper: 16
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autolotto/refs/heads/main/screenshots/autolotto-2026-07-25T201825.png
security:
- kind: domain-security
  name: Autolotto Domain Security
  slug: autolotto-domain-security
  summary_line: TLSv1.3 · DMARC
slug: autolotto
tags:
- Company
- Lottery
- Gaming
- Consumer
- Mobile
- Data Licensing
- Entertainment
website: https://lottery.com
---
