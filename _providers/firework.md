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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Server-to-server REST API for managing businesses, channels, videos, livestreams, playlists, products, business stores, and insights, plus HMAC-signed webhooks. Secured with OAuth 2.0 (client credenti
  name: Firework Public API
  slug: firework-public-api
artifact_total: 5
asyncapis:
- description: ''
  name: Firework Webhooks
  slug: firework-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firework-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.firework.com/firework-for-developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firework.com/firework-for-developers
- group: docs
  title: ''
  type: APIReference
  url: https://docs.firework.com/firework-for-developers/api/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.firework.com/firework-for-developers/readme
- group: company
  title: ''
  type: Blog
  url: https://firework.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://firework.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://api.firework.com/auth/business_auth/callback
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firework.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firework.com/legal/privacypolicy
- group: operate
  title: ''
  type: Support
  url: https://firework.com/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loopsocial
- group: operate
  title: ''
  type: StatusPage
  url: https://firework.statuspage.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/firework-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/firework-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/firework-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/firework-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/firework-packages.yml
- group: design
  title: ''
  type: Components
  url: components/firework-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/firework-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/firework-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/firework-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/firework-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/firework-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/firework-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/firework-llms.txt
created: '2026-07-17'
description: Firework is a video commerce platform that helps brands and retailers bring the in-store experience and human connection online through shoppable short-form video, livestream shopping, 1:1 video chat, digital showrooms, and an AI shopping agent. Operated by Loop Now Technologies and backed by SoftBank (a $150M Series C led SoftBank's investment), Firework powers 1,500+ global brands and has driven $300M+ in GMV across 2+ trillion video views. For developers it offers a Web SDK, native Android/iOS SDKs, React Native and Flutter plugins, embeddable web components (Hero Unit, Carousel, Player Deck, Storyblock, Floating Player), a server-side REST Public API (https://api.firework.com/api/v1) secured with OAuth 2.0 (client credentials and authorization-code + PKCE with dynamic client registration), HMAC-signed webhooks, and turnkey commerce-platform integrations for Shopify, Magento, WooCommerce, Salesforce Commerce Cloud, and BigCommerce.
image: https://firework.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Firework
nav: Providers
network: true
overview: 'Firework publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Video Commerce, Shoppable Video, and Livestream Shopping.


  The Firework catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Firework''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 19 more developer resources.'
random_paper: 12
scopes:
- name: Firework Scopes
  scope_count: 12
  slug: firework-scopes
  summary_line: 12 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 47.7
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firework/refs/heads/main/screenshots/firework-2026-07-25T214557.png
security:
- kind: authentication
  name: Firework Authentication
  slug: firework-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Firework Domain Security
  slug: firework-domain-security
  summary_line: TLSv1.3 · HSTS
slug: firework
tags:
- Company
- Consumer
- Video Commerce
- Shoppable Video
- Livestream Shopping
- E-Commerce
- Retail
- Video
- SDK
- Webhook
website: https://docs.firework.com/firework-for-developers
---
