---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/techstyle-fashion-group-domain-security.yml
coverage:
  checked: '2026-08-29'
  detail: 'TechStyle Fashion Group has no corporate web presence left to profile: techstyle.com 301s to www.techstylefashiongroup.com, which refuses TLS on port 443 entirely and answers plain HTTP with a Gandi domain-parking page for every path — including /openapi.json, /llms.txt and every /.well-known/* probe — while techstyleos.com, the TechStyle OS platform domain, is parked the same way; api.techstyle.com, developer.techstyle.com, docs.techstyle.com and developer.techstylefashiongroup.com do not resolve at all, there is no GitHub organization, and the only first-party API hosts that exist belong to the operating brands (gateway.fabletics.com, gateway.savagex.com), which answer 403 to everything and are profiled as separate providers. The existing Website pointer to a Hiive secondary-market listing was removed — a trading-venue page is not the company''s own web presence.'
  evidence:
  - status: 301
    url: https://techstyle.com/
  - status: 200
    url: http://www.techstylefashiongroup.com/
  - status: 200
    url: http://www.techstylefashiongroup.com/openapi.json
  - status: 200
    url: http://www.techstylefashiongroup.com/llms.txt
  - status: 200
    url: http://www.techstylefashiongroup.com/.well-known/agent-card.json
  - status: 200
    url: http://www.techstylefashiongroup.com/.well-known/security.txt
  - status: 200
    url: http://www.techstyleos.com/
  - status: 403
    url: https://gateway.fabletics.com/openapi.json
  - status: 403
    url: https://gateway.savagex.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/techstyle
  - status: 404
    url: https://api.github.com/orgs/techstyleos
  - status: 404
    url: https://www.fabletics.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: 'TechStyle Fashion Group is the El Segundo, California holding company founded in March 2010 by Don Ressler and Adam Goldenberg as JustFab Inc. and renamed TechStyle Fashion Group in August 2016. It builds and operates direct-to-consumer membership fashion brands on a shared, proprietary commerce and personalization platform once marketed as TechStyle OS — Fabletics (with the Yitty shapewear line), Savage X Fenty, JustFab, ShoeDazzle and FabKids — selling apparel, footwear, activewear, intimates and accessories through a VIP membership subscription that gives members monthly credits, member pricing and a monthly skip window. The group reported more than five million paying VIP members and roughly $800 million in revenue as of 2019, and has since reorganized so that Fabletics, Savage X Fenty and the Global Fashion Brands unit (JustFab, ShoeDazzle, FabKids) run as standalone operating companies on the shared supply chain, fulfillment and technology stack. The TechStyle corporate
  identity itself has been retired: both techstyle.com and techstyleos.com now redirect to a Gandi domain-parking page at techstylefashiongroup.com that answers on plain HTTP only, so the group publishes no corporate site, no developer program, no API reference and no machine-readable contract of its own. The live API surface belongs to the operating brands, which are profiled separately in this network.'
layout: provider
modified: '2026-08-29'
name: Techstyle Fashion Group
nav: Providers
network: true
overview: Techstyle Fashion Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Apparel, Retail, and E-Commerce.
random_paper: 20
security:
- kind: domain-security
  name: Techstyle Fashion Group Domain Security
  slug: techstyle-fashion-group-domain-security
  summary_line: DMARC
slug: techstyle-fashion-group
tags:
- Company
- Fashion
- Apparel
- Retail
- E-Commerce
- Direct to Consumer
- Subscription
- Holding Company
---
