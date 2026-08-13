---
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: Connect point-of-sale software directly to Zeller Terminal hardware to initiate and manage in-person card payments. Delivered through the Zeller Payments SDK (React, React Native, Windows .NET, Androi
  name: Zeller Terminal API
  slug: zeller-terminal-api
- description: Accept payments inside web and mobile apps via Zeller's Online integration. Part of the Zeller Developer Suite; access to full API documentation is by request behind a free developer account.
  name: Zeller Online Payments API
  slug: zeller-online-api
- description: Accept contactless card and mobile-wallet payments on a phone with no separate terminal, integrated through the Zeller Payments SDK. Documentation is gated behind a free Zeller Developer account.
  name: Zeller Tap to Pay API
  slug: zeller-tap-to-pay-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeller-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeller-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zeller-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zeller-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/zeller-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zeller-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zeller-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.myzeller.com/au/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zeller-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.myzeller.com/au
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.myzeller.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.myzeller.com/au/developer-suite
- group: start
  title: ''
  type: SignUp
  url: https://developer.myzeller.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.myzeller.com/au/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.myzeller.com/au/blog
- group: operate
  title: ''
  type: Support
  url: https://www.myzeller.com/au/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.myzeller.com/au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.myzeller.com/au/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myzeller
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/zeller
created: '2026-07-24'
description: 'Zeller is a Melbourne-founded Australian payments and business banking company (founded 2020 by former Square Australia executives Ben Pfisterer and Dominic Yap) that gives SMEs an integrated stack of card payment acceptance, a transaction account, a Mastercard debit card, and financial management tools in one place. As a merchant acquirer it processes in-person and online card payments (Visa, Mastercard, eftpos, American Express, JCB, Apple Pay, Google Wallet) across its Zeller Terminal hardware, Tap to Pay on mobile, and online checkout, positioning itself against Square and fellow ASX-adjacent acquirer Tyro. Zeller reached unicorn status on a 2022 Series B. Its API posture is developer-account-gated: the Zeller Developer Suite ships Payments SDKs (React, React Native, Windows .NET, Android, iOS) plus Terminal, Online, and Tap to Pay integration APIs, with reference documentation unlocked only after creating a free developer account. The developer portal authenticates through
  an Auth0 (OAuth2 / OpenID Connect) tenant; no OpenAPI specification is published for anonymous download.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: zeller-mcp.yml
  slug: zeller-mcpyml
modified: '2026-07-24'
name: Zeller
nav: Providers
network: true
overview: 'Zeller publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, Payment Gateway, Payment Processing, and Acquiring.


  Zeller''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, support, and 14 more developer resources.'
random_paper: 54
score:
  band: thin
  composite: 33.4
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 33.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Zeller Authentication
  slug: zeller-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Zeller Domain Security
  slug: zeller-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zeller
tags:
- Payments
- Australia
- Payment Gateway
- Payment Processing
- Acquiring
- Merchant Services
- Point of Sale
- In-Person Payments
- Tap to Pay
- SME
website: https://www.myzeller.com/au
---
