---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Server-to-server REST API for managing businesses, channels, videos, livestreams, playlists, products, business stores, and insights, plus HMAC-signed webhooks. Secured with OAuth 2.0 (client credenti
  name: Firework Public API
  slug: firework-public-api
artifact_total: 9
asyncapis:
- description: ''
  name: Firework Webhooks
  slug: firework-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/firework/plans/firework-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/firework-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://firework.com/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://www.firework.com/
- group: auth
  href: https://artifacts.apis.io/firework/security/firework-domain-security.yml
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
  href: https://artifacts.apis.io/firework/authentication/firework-authentication.yml
  title: ''
  type: Authentication
  url: authentication/firework-authentication.yml
- group: auth
  href: https://artifacts.apis.io/firework/scopes/firework-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/firework-scopes.yml
- group: agent
  href: https://artifacts.apis.io/firework/well-known/firework-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/firework-well-known.yml
- group: build
  href: https://artifacts.apis.io/firework/packages/firework-packages.yml
  title: ''
  type: Packages
  url: packages/firework-packages.yml
- group: build
  href: https://artifacts.apis.io/firework/packages/firework-packages.yml
  title: ''
  type: SDKs
  url: packages/firework-packages.yml
- group: design
  href: https://artifacts.apis.io/firework/components/firework-components.yml
  title: ''
  type: Components
  url: components/firework-components.yml
- group: design
  href: https://artifacts.apis.io/firework/asyncapi/firework-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/firework-webhooks.yml
- group: design
  href: https://artifacts.apis.io/firework/conventions/firework-conventions.yml
  title: ''
  type: Conventions
  url: conventions/firework-conventions.yml
- group: design
  href: https://artifacts.apis.io/firework/conformance/firework-conformance.yml
  title: ''
  type: Conformance
  url: conformance/firework-conformance.yml
- group: operate
  href: https://artifacts.apis.io/firework/changelog/firework-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/firework-changelog.yml
- group: design
  href: https://artifacts.apis.io/firework/lifecycle/firework-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/firework-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/firework/data-model/firework-data-model.yml
  title: ''
  type: DataModel
  url: data-model/firework-data-model.yml
- group: agent
  href: https://artifacts.apis.io/firework/llms/firework-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/firework-llms.txt
created: '2026-07-17'
description: Firework is a video commerce platform that helps brands and retailers bring the in-store experience and human connection online through shoppable short-form video, livestream shopping, 1:1 video chat, digital showrooms, and an AI shopping agent. Operated by Loop Now Technologies and backed by SoftBank (a $150M Series C led SoftBank's investment), Firework powers 1,500+ global brands and has driven $300M+ in GMV across 2+ trillion video views. For developers it offers a Web SDK, native Android/iOS SDKs, React Native and Flutter plugins, embeddable web components (Hero Unit, Carousel, Player Deck, Storyblock, Floating Player), a server-side REST Public API (https://api.firework.com/api/v1) secured with OAuth 2.0 (client credentials and authorization-code + PKCE with dynamic client registration), HMAC-signed webhooks, and turnkey commerce-platform integrations for Shopify, Magento, WooCommerce, Salesforce Commerce Cloud, and BigCommerce.
finops:
- has_sources: true
  method: derived
  name: Firework Finops
  primary_unit: 1k additional video views
  service_category: ''
  slug: firework-finops
  template: false
image: https://firework.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at api.firework.com over HTTP.
  name: Firework MCP Server
  slug: firework
modified: '2026-10-06'
name: Firework
nav: Providers
network: true
overview: 'Firework is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Video Commerce, Shoppable Video, and Livestream Shopping.


  The Firework catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Firework''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
plans:
- name: Firework Plans Pricing
  plan_count: 9
  slug: firework-plans-pricing
- name: Firework Price Estimates
  plan_count: 0
  slug: firework-price-estimates
random_paper: 9
scopes:
- name: Firework Scopes
  scope_count: 12
  slug: firework-scopes
  summary_line: 12 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 64.3
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 57.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/firework/firework-2026-07-25T214557.png
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
website: https://www.firework.com/
---
