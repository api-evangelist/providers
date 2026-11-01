---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'REST API for the Acquire (formerly Tagove) customer support platform: conversations/cases, messages, notes, contacts, companies, phone, chatbots, cards, analytics, knowledge base, and account settings'
  name: Acquire Support & Conversations API
  slug: tagove-acquire-support-api
artifact_total: 4
asyncapis:
- description: ''
  name: Tagove Webhooks
  slug: tagove-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://acquire.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.acquire.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.acquire.io
- group: docs
  title: ''
  type: APIReference
  url: https://developer.acquire.io/rest-apis/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.acquire.io/master.md
- group: operate
  title: ''
  type: Support
  url: https://help.acquire.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acquireio
- group: commercial
  title: ''
  type: Pricing
  url: https://acquire.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.acquire.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acquire.io/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://acquire.io/blog
- group: agent
  href: https://artifacts.apis.io/tagove/llms/tagove-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tagove-llms.txt
- group: auth
  href: https://artifacts.apis.io/tagove/authentication/tagove-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tagove-authentication.yml
- group: design
  href: https://artifacts.apis.io/tagove/conventions/tagove-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tagove-conventions.yml
- group: design
  href: https://artifacts.apis.io/tagove/errors/tagove-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/tagove-error-codes.yml
- group: design
  href: https://artifacts.apis.io/tagove/asyncapi/tagove-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tagove-webhooks.yml
- group: build
  href: https://artifacts.apis.io/tagove/packages/tagove-packages.yml
  title: ''
  type: Packages
  url: packages/tagove-packages.yml
- group: build
  href: https://artifacts.apis.io/tagove/packages/tagove-packages.yml
  title: ''
  type: SDKs
  url: packages/tagove-packages.yml
- group: design
  href: https://artifacts.apis.io/tagove/components/tagove-components.yml
  title: ''
  type: Components
  url: components/tagove-components.yml
- group: design
  href: https://artifacts.apis.io/tagove/lifecycle/tagove-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tagove-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tagove/conformance/tagove-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tagove-conformance.yml
- group: design
  href: https://artifacts.apis.io/tagove/data-model/tagove-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tagove-data-model.yml
- group: auth
  href: https://artifacts.apis.io/tagove/security/tagove-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tagove-domain-security.yml
created: '2026-07-17'
description: Tagove was a live chat, video chat, and co-browsing customer support platform (a 500 Global portfolio company) that now operates as Acquire.io. Acquire is an omnichannel customer support and conversational engagement platform whose developer platform (developer.acquire.io) exposes a REST API for conversations/cases, messages, contacts, companies, chatbots, knowledge base, analytics, and account settings, plus outbound HMAC-SHA256-signed webhooks, iOS/Android/JS SDKs, and an embeddable live-chat and co-browse widget. This profile was enriched from the Acquire developer documentation; no machine-readable OpenAPI is published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tagove.png
layout: provider
modified: '2026-07-21'
name: Tagove
nav: Providers
network: true
overview: 'Tagove is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Service, Live Chat, Conversational AI, and Co-Browsing.


  The Tagove catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tagove''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 16 more developer resources.'
random_paper: 22
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 64.3
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 38.7
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tagove/tagove-2026-10-11T130607.png
security:
- kind: authentication
  name: Tagove Authentication
  slug: tagove-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Tagove Domain Security
  slug: tagove-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tagove
tags:
- Company
- Customer Service
- Live Chat
- Conversational AI
- Co-Browsing
- Chatbots
- Webhook
- Customer Communication
- Help Desk
website: https://acquire.io
---
