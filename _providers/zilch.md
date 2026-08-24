---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.zilch.com/uk/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.zilch.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.zilch.com/uk/thegreen/
- group: company
  title: ''
  type: News
  url: https://www.zilch.com/corporate/news/
- group: other
  title: ''
  type: Merchants
  url: https://www.zilch.com/uk/retailers/
- group: start
  title: ''
  type: SignUp
  url: https://customers.payzilch.com/apply/
- group: start
  title: ''
  type: Login
  url: https://customers.payzilch.com/login/
- group: auth
  title: ''
  type: Compliance
  url: https://www.zilch.com/uk/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zilch.com/uk/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zilch.com/uk/privacy-notice/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zilch-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zilch-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zilch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zilch.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zilch-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zilch-llms.txt
created: '2026-07-24'
description: 'Zilch is a London-headquartered "buy now, pay later" and ad-subsidised payments network founded in 2018, and one of the United Kingdom''s most prominent BNPL brands. Rather than integrating at each retailer''s checkout, Zilch is deliberately merchant-agnostic: consumers apply in the Zilch mobile app, receive a virtual (and physical) Mastercard, and can Pay-in-3, pay over six weeks, or Pay-now-and-earn-cashback anywhere Mastercard is accepted, online or in-store, through Apple Pay and Google Pay wallets. Because Zilch reaches merchants over the open Mastercard card rails and relies on partners such as Mastercard for card issuing and Checkout.com as its payments processor, it does not operate a public merchant-integration or developer platform the way a PSP or open-banking provider does. As of this review Zilch publishes no developer portal, no API reference, and no downloadable OpenAPI/Swagger specification; its public surface is a consumer marketing site, a help centre, and
  a customer sign-up/login app. This profile therefore records Zilch''s verified public web properties honestly and carries no API entries, because none are publicly documented.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24T18:00:00Z'
name: Zilch
nav: Providers
network: true
overview: 'Zilch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United Kingdom, BNPL, Buy Now Pay Later, and Consumer Credit.


  Zilch''s developer surface includes engineering blog, product news, signup flow, and 13 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 15.0
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Zilch Domain Security
  slug: zilch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zilch Vulnerability Disclosure
  slug: zilch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zilch
tags:
- Payments
- United Kingdom
- BNPL
- Buy Now Pay Later
- Consumer Credit
- Digital Wallet
- Card
- Mastercard
- Fintech
website: https://www.zilch.com/uk/
---
