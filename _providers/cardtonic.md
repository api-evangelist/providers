---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: The Cardtonic Gift Card Developer API enables merchants and platforms to integrate gift card services into their websites, mobile apps, and point-of-sale systems. The API exposes a catalog of more tha
  name: Cardtonic Gift Card Developer API
  slug: gift-card-developer-api
- description: Cardtonic Virtual Dollar Cards are user-facing USD-denominated cards that let African customers pay merchants that accept Visa/Mastercard globally. The product is currently consumed through the Cardto
  name: Cardtonic Virtual Dollar Card
  slug: virtual-dollar-card
- description: Cardtonic Bill Payments cover airtime top-ups, mobile data, electricity, TV subscriptions, and betting wallets across more than 100 countries, consumed through the Cardtonic app and dashboard. Partner
  name: Cardtonic Bill Payments
  slug: bill-payments
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-cardtonic
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardtonic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardtonic.com/
- group: other
  title: ''
  type: Developer
  url: https://cardtonic.com/developer
- group: other
  title: ''
  type: Dashboard
  url: https://dashboard.cardtonic.com/
- group: start
  title: ''
  type: Login
  url: https://cardtonic.com/login
- group: start
  title: ''
  type: Signup
  url: https://cardtonic.com/register
- group: company
  title: ''
  type: About
  url: https://cardtonic.com/about
- group: company
  title: ''
  type: Blog
  url: https://cardtonic.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://cardtonic.com/faq
- group: operate
  title: ''
  type: Contact
  url: https://cardtonic.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cardtonic.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardtonic.com/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/cardtonic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cardtonic
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/cardtonic/
- group: agent
  title: ''
  type: LlmsText
  url: https://cardtonic.com/llms.txt
created: '2025-02-08'
description: Cardtonic is an Africa-focused fintech platform that lets users trade gift cards (sell unused cards for cash and buy over 14,000 local and international gift cards), issue virtual dollar cards, pay bills (airtime, data, electricity, TV, betting), purchase eSIMs in 140+ countries, and shop for gadgets through its Just Gadgets storefront. Cardtonic supports Naira and Cedi settlement for users in Nigeria and Ghana, holds PCI DSS certification, and operates under Nigeria Data Protection Commission (NDPC) oversight. For businesses, Cardtonic offers a Gift Card Developer API (currently waitlist-only) that lets merchants embed gift card purchasing, sales, bulk ordering, inventory, and redemption into websites, mobile apps, and point-of-sale systems.
finops:
- name: Cardtonic Finops
  service_category: Fintech / Gift Cards
  slug: cardtonic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cardtonic.png
layout: provider
modified: '2026-04-23'
name: Cardtonic
nav: Providers
network: true
overview: 'Cardtonic publishes 1 API on the [APIs.io](https://apis.io/) network: Gift Card Developer API. Tagged areas include Africa, Bill Payments, eSIM, Finance, and Fintech.


  Cardtonic''s developer surface includes signup flow, engineering blog, FAQ, and 13 more developer resources.'
plans:
- name: Cardtonic Plans Pricing
  plan_count: 1
  slug: cardtonic-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: Cardtonic Rate Limits
  slug: cardtonic-rate-limits
score:
  band: thin
  composite: 29.1
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 32.3
    developer_ergonomics: 2.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cardtonic/refs/heads/main/screenshots/cardtonic-2026-06-20T173956.png
security:
- kind: domain-security
  name: Cardtonic Domain Security
  slug: cardtonic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cardtonic
tags:
- Africa
- Bill Payments
- eSIM
- Finance
- Fintech
- Gift Cards
- Ghana
- Nigeria
- Payments
- Virtual Dollar Cards
website: https://cardtonic.com/
---
