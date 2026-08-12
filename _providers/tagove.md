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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-11'
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
  title: ''
  type: LLMsTxt
  url: llms/tagove-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tagove-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tagove-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tagove-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tagove-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/tagove-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tagove-packages.yml
- group: design
  title: ''
  type: Components
  url: components/tagove-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tagove-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tagove-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tagove-data-model.yml
- group: auth
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
overview: 'Tagove publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Support, Live Chat, Conversational, and Co-browsing.


  The Tagove catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tagove''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 16 more developer resources.'
random_paper: 66
score:
  band: thin
  composite: 41.2
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 58.7
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 13.2
  previous_composite: 42.3
  provenance:
    conformance: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
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
- Customer Support
- Live Chat
- Conversational
- Co-browsing
- Chatbots
- Webhooks
- Customer Communication
- Help Desk
website: https://acquire.io
---
