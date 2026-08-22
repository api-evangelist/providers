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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://keyboard.io/
- group: operate
  title: ''
  type: Support
  url: https://shop.keyboard.io/pages/support
- group: company
  title: ''
  type: Blog
  url: https://shop.keyboard.io/blogs/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keyboardio
- group: start
  title: ''
  type: SignUp
  url: https://account.keyboard.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://shop.keyboard.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.keyboard.io/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shop.keyboard.io/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/keyboardio-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/keyboardio-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/keyboardio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/keyboardio-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keyboardio-domain-security.yml
created: '2026-07-17'
description: Keyboardio is a hardware company that designs and sells premium ergonomic mechanical keyboards, including the sculpted hardwood Model 100, the ultra- portable Atreus, and the upcoming Preonic. Its keyboards run fully open-source, reprogrammable firmware (Kaleidoscope) configured through the cross-platform Chrysalis GUI, both developed in the open on GitHub. Keyboardio sells direct through a Shopify storefront at shop.keyboard.io; customer login and account management use Shopify Customer Accounts (OpenID Connect / OAuth 2.0) bound to the keyboard.io domain. Keyboardio has no first-party public HTTP API — this profile captures the real developer, open-source, and identity surfaces the company publishes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keyboardio.png
layout: provider
modified: '2026-07-19'
name: Keyboardio
nav: Providers
network: true
overview: 'Keyboardio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mechanical Keyboards, Hardware, Ergonomics, and Open Source.


  Keyboardio''s developer surface includes support, engineering blog, signup flow, pricing, authentication, and 8 more developer resources.'
random_paper: 15
scopes:
- name: Keyboardio Scopes
  scope_count: 4
  slug: keyboardio-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.1
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keyboardio/refs/heads/main/screenshots/keyboardio-2026-08-07T171131.png
security:
- kind: authentication
  name: Keyboardio Authentication
  slug: keyboardio-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Keyboardio Domain Security
  slug: keyboardio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: keyboardio
tags:
- Company
- Mechanical Keyboards
- Hardware
- Ergonomics
- Open Source
- Firmware
- Keyboards
- E-commerce
website: https://keyboard.io/
---
