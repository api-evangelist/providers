---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The IYK API provides primitives for building digi-physical experiences. Core endpoints manage chips (NFC tags such as NTAG 424, KONG, and ARX HaLo), chip groups, items, taps/refs (validated physical i
  name: IYK API
  slug: iyk-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iyk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iyk.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iyk.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.iyk.app
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iyk.app/api-quickstart
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/ezppV2nj7w
- group: start
  title: ''
  type: SignUp
  url: https://studio.iyk.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assets.iyk.app/iyk-terms-of-service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assets.iyk.app/iyk-privacy-policy.pdf
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iyk-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/iyk-authentication.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/iyk-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iyk-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/iyk-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/iyk-well-known.yml
created: '2026-07-17'
description: IYK provides useful primitives and apps for building digi-physical (phygital) experiences, connecting physical products and merchandise to blockchain tokens, POAPs, and digital content through NFC chips. The IYK API exposes three categories of endpoints - Core (chips, chip groups, items, taps/refs, OTP codes, and phygitals), Modules (POAP Events and Guestbook Events), and Self-Service POAP Devices - letting brands and artists chip physical items, verify authentic taps, gate content and rewards, mint or transfer linked NFTs, and recognize fans who show up. IYK Music applies the same primitives to fan engagement, turning chipped merch and show check-ins into a living fan identity. IYK is backed by a16z.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iyk.png
layout: provider
modified: '2026-07-19'
name: IYK
nav: Providers
network: true
overview: 'IYK publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, NFC, Phygital, Blockchain, and NFT.


  IYK''s developer surface includes documentation, getting-started guide, support, signup flow, authentication, and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 25.4
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iyk/refs/heads/main/screenshots/iyk-2026-07-25T223022.png
security:
- kind: authentication
  name: Iyk Authentication
  slug: iyk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Iyk Domain Security
  slug: iyk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iyk
tags:
- Company
- NFC
- Phygital
- Blockchain
- NFT
- POAP
- Chips
- Authentication
- Fan Engagement
- Web3
website: https://iyk.app
---
