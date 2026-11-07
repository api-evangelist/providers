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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Secondfactor Webhooks
  slug: secondfactor-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.secondfactor.ai/
- group: design
  href: https://artifacts.apis.io/secondfactor/asyncapi/secondfactor-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/secondfactor-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/secondfactor/authentication/secondfactor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/secondfactor-authentication.yml
- group: design
  href: https://artifacts.apis.io/secondfactor/errors/secondfactor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/secondfactor-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/secondfactor/llms/secondfactor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/secondfactor-llms.txt
- group: other
  href: https://artifacts.apis.io/secondfactor/hosts/secondfactor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/secondfactor-hosts.yml
- group: other
  href: https://artifacts.apis.io/secondfactor/vendors/secondfactor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/secondfactor-vendors.yml
- group: build
  href: https://artifacts.apis.io/secondfactor/packages/secondfactor-packages.yml
  title: ''
  type: SDKs
  url: packages/secondfactor-packages.yml
- group: build
  href: https://artifacts.apis.io/secondfactor/packages/secondfactor-packages.yml
  title: ''
  type: Packages
  url: packages/secondfactor-packages.yml
- group: auth
  href: https://artifacts.apis.io/secondfactor/security/secondfactor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/secondfactor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://secondfactor.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.secondfactor.ai
- group: operate
  title: ''
  type: Support
  url: https://secondfactor.ai/support
- group: company
  title: ''
  type: Blog
  url: https://secondfactor.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://secondfactor.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.secondfactor.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://secondfactor.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://secondfactor.ai/privacy
created: '2026-10-27'
description: SecondFactor provides an OTP Delivery & Verification API that enables developers to send one‑time passwords via SMS, WhatsApp, Viber, and RCS. The platform intelligently routes messages to the lowest‑cost channel, offers automatic fallback, delivery logs, template management, and a pricing calculator. It aims to reduce authentication costs and improve user experience with a single, multi‑channel API. Documentation, pricing, and support are available online, and the service is trusted by global companies for secure, fast, and affordable OTP delivery.
image: https://secondfactor.ai/assets/og-default.png
layout: provider
modified: '2026-10-27'
name: SecondFactor
nav: Providers
network: true
overview: 'SecondFactor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OTP, Authentication, Multi-Channel, and Messaging.


  The SecondFactor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SecondFactor''s developer surface includes getting-started guide, authentication, documentation, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 33.3
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.5
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
screenshot: https://apis.io/screenshots/secondfactor/secondfactor-2026-11-03T142933.png
security:
- kind: authentication
  name: Secondfactor Authentication
  slug: secondfactor-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Secondfactor Domain Security
  slug: secondfactor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: secondfactor
tags:
- Company
- OTP
- Authentication
- Multi-Channel
- Messaging
website: https://secondfactor.ai
---
