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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://zeroclick.ai
- group: docs
  title: ''
  type: Documentation
  url: https://zeroclick.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://zeroclick.ai/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zeroclick.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zeroclick.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/piedotorg
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/piedotorg/zeroclick
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/packages/zeroclick-packages.yml
  title: ''
  type: Packages
  url: packages/zeroclick-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/packages/zeroclick-packages.yml
  title: ''
  type: SDKs
  url: packages/zeroclick-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/authentication/zeroclick-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zeroclick-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/conventions/zeroclick-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zeroclick-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/conventions/zeroclick-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/zeroclick-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/errors/zeroclick-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zeroclick-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/conformance/zeroclick-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zeroclick-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/data-model/zeroclick-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zeroclick-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/lifecycle/zeroclick-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zeroclick-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/security/zeroclick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zeroclick-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/well-known/zeroclick-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zeroclick-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/llms/zeroclick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zeroclick-llms.txt
created: '2026-07-17'
description: ZeroClick is the agent-first storefront and transaction layer that lets businesses sell directly to AI agents. It turns any existing API or offering into an agent-purchasable service, publishing a machine-readable storefront so agents can discover it and adding agent identity, agent-native payment rails (x402 and MPP, the Machine Payments Protocol), signed proxying, and per-transaction analytics in front of the seller's unchanged upstream API. Sellers keep their product, pricing, and customer experience, add a small guard to billed endpoints via the @zeroclickai/sellers SDK, and settle revenue to their own connected Stripe account. ZeroClick launched in July 2026, raised $55M, is backed by Forerunner Ventures, and is a product of the People's Internet Experiment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeroclick.png
layout: provider
modified: '2026-07-21'
name: Zeroclick
nav: Providers
network: true
overview: 'Zeroclick is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agentic Commerce, Agentic Payments, and API Monetization.


  Zeroclick''s developer surface includes documentation, API reference, authentication, and 16 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.4
    operational_transparency: 2.6
  previous_composite: 20.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/zeroclick/refs/heads/main/screenshots/zeroclick-2026-09-02T171707.png
security:
- kind: authentication
  name: Zeroclick Authentication
  slug: zeroclick-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zeroclick Domain Security
  slug: zeroclick-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zeroclick
tags:
- Company
- Artificial Intelligence
- Agentic Commerce
- Agentic Payments
- API Monetization
- x402
- Machine Payments Protocol
- Agent Identity
- Stripe
website: https://zeroclick.ai
---
