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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.changetip.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/changecoin
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/changetip/refs/heads/main/packages/changetip-packages.yml
  title: ''
  type: Packages
  url: packages/changetip-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/changetip/refs/heads/main/packages/changetip-packages.yml
  title: ''
  type: SDKs
  url: packages/changetip-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/changetip/refs/heads/main/security/changetip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/changetip-domain-security.yml
created: '2026-07-17'
description: ChangeTip was a Bitcoin micropayments and social-tipping service built by ChangeCoin, Inc. (San Francisco), founded in 2013. It let people send small bitcoin tips across Twitter, Reddit, YouTube, Twitch, Facebook, Slack, email, and text by replying with an amount, settling the micropayment behind the scenes to a hosted wallet. ChangeTip published an open API and first-party client libraries (Python and JavaScript) so the community could build tipping integrations and pair external wallets. The company raised roughly $3.5M and was backed by 500 Startups, Pantera Capital, and Gil Penchina. ChangeCoin was acquired by Airbnb in 2016 and the tipping service was discontinued in November 2016; the site now serves only a shutdown notice with balance withdrawal. This profile is retained as a historical/defunct provider record in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/changetip.png
layout: provider
modified: '2026-07-18'
name: ChangeTip
nav: Providers
network: true
overview: ChangeTip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bitcoin, Cryptocurrency, Micropayments, and Payments.
random_paper: 1
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/changetip/refs/heads/main/screenshots/changetip-2026-07-25T205037.png
security:
- kind: domain-security
  name: Changetip Domain Security
  slug: changetip-domain-security
  summary_line: no transport/DNS hardening detected
slug: changetip
tags:
- Company
- Bitcoin
- Cryptocurrency
- Micropayments
- Payments
- Tipping
- Social Media
- Wallets
- Defunct
website: https://www.changetip.com
---
