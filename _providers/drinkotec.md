---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://drinkotec.ch/drinkotec-api/
  - plans/drinkotec-plans-pricing.yml
  trial: false
  try_now: false
api_count: 1
apis:
- description: The DRINKOTEC API is the integration surface for DRINKOTEC's connected beverage dispensing systems and its LOOP360 beverage productivity platform, used to expand DRINKOTEC functionality with third-par
  name: DRINKOTEC API
  slug: drinkotec
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drinkotec-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/drinkotec-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://info.drinkotec.ch/en/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://info.drinkotec.ch/en/blog/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drinkotec
coverage:
  checked: '2026-09-06'
  detail: DRINKOTEC's own API page states that "a complete reference documentation is available and includes every endpoint, attribute and supported method", but publishes no link to it and no base URL — the page's only call to action is a "MEET OUR SOFTWARE ENGINEERS" button pointing at a form to book a visit or callback at the Nyon office, so the contract sits behind a sales conversation rather than a URL.
  evidence:
  - status: 503
    url: https://drinkotec.ch/drinkotec-api/
  - status: 200
    url: http://web.archive.org/web/20260419112516id_/https://drinkotec.ch/drinkotec-api/
  - status: 404
    url: https://api.drinkotec.ch/openapi.json
  - status: 404
    url: https://api.drinkotec.ch/.well-known/agent-card.json
  - status: 200
    url: https://info.drinkotec.ch/en/blog
  reason: sales-gate
  state: gated
created: '2025-03-01'
description: DRINKOTEC is a Swiss beverage technology company headquartered in Nyon, Vaud, that designs, builds and services connected beverage dispensing systems and the software that runs them. Its hardware line covers all-in-one and modern postmix dispensers (NEO, VISION PX), compact premix dispensing (DRAFTER), cocktails and blends (MANHATTAN), self-service walls, contactless payment (BEVPAY), beer and wine counting and control (LEVELUP, BEERMAX), automatic keg switching, cellar cooling monitoring and water fountains. LOOP360, its cloud beverage productivity and analytics platform, connects dispensed beverages to a central system and is marketed as integrating with ERP and CRM platforms. DRINKOTEC sells into breweries, bars, pubs, nightclubs, restaurants, hotels, festivals, sports arenas, cruise ships, offices, schools and healthcare, and markets a RESTful DRINKOTEC API for third-party integration whose reference documentation is not published publicly.
finops:
- name: Drinkotec Finops
  service_category: API
  slug: drinkotec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drinkotec.png
layout: provider
modified: '2026-09-06'
name: DRINKOTEC
nav: Providers
network: true
overview: 'DRINKOTEC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Beverages, Beverage Dispensing, Hospitality, Point of Sale, and IoT.


  DRINKOTEC''s developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Drinkotec Plans Pricing
  plan_count: 0
  slug: drinkotec-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Drinkotec Rate Limits
  slug: drinkotec-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/drinkotec/refs/heads/main/screenshots/drinkotec-2026-06-20T180234.png
security:
- kind: authentication
  name: Drinkotec Authentication
  slug: drinkotec-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Drinkotec Domain Security
  slug: drinkotec-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: drinkotec
tags:
- Beverages
- Beverage Dispensing
- Hospitality
- Point of Sale
- IoT
- Analytics
- Payments
---
