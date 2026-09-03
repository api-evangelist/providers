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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: OAuth 2.0 / OpenID Connect customer-account surface exposed on the soundboks.com store domain by the Shopify Customer Accounts platform. Discovered via the standard /.well-known/openid-configuration a
  name: Soundboks Customer Account API (Shopify)
  slug: soundboks-customer-account-api-shopify
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://soundboks.com
- group: operate
  title: ''
  type: Support
  url: https://soundboks.com/pages/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soundboks.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soundboks.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/soundboks-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soundboks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/soundboks-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundboks-domain-security.yml
created: '2026-07-17'
description: Soundboks is a Danish consumer-electronics company that designs and manufactures loud, durable, battery-powered Bluetooth party speakers (Soundboks 4, Soundboks Mix) plus companion products such as Lightboks party lights. Products are sold direct-to-consumer through a Shopify-powered storefront and controlled with a companion iOS/Android app that supports wireless playback and multi-speaker pairing (TeamUp). Soundboks does not publish a first-party developer API or SDK; its only programmatic surface is the Shopify Customer Account API (OAuth 2.0 / OpenID Connect) exposed on its own store domain via the standard Shopify discovery documents, which is what this enrichment pass captured.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soundboks.png
layout: provider
modified: '2026-07-21'
name: Soundboks
nav: Providers
network: true
overview: 'Soundboks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Electronics, Audio, Bluetooth Speakers, and Hardware.


  Soundboks'' developer surface includes support, authentication, and 6 more developer resources.'
random_paper: 18
scopes:
- name: Soundboks Scopes
  scope_count: 4
  slug: soundboks-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soundboks/refs/heads/main/screenshots/soundboks-2026-09-02T160248.png
security:
- kind: authentication
  name: Soundboks Authentication
  slug: soundboks-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Soundboks Domain Security
  slug: soundboks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soundboks
tags:
- Company
- Consumer Electronics
- Audio
- Bluetooth Speakers
- Hardware
- E-Commerce
- Shopify
- Direct to Consumer
website: https://soundboks.com
---
