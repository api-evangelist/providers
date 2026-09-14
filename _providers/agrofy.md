---
api_count: 1
apis:
- description: 'Agrofy Developers is the company''s marketed partner-integration program for marketplace sellers — listing management, lead management and catalog synchronisation. Agrofy publishes no machine-readable '
  name: Agrofy Marketplace API
  slug: agrofy-marketplace-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agrofy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agrofy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.agrofy.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://contenido.agrofy.com.ar/es/
- group: operate
  title: ''
  type: Support
  url: https://www.agrofy.com.ar/contacts
- group: company
  title: ''
  type: Blog
  url: https://news.agrofy.com.ar/
- group: start
  title: ''
  type: Login
  url: https://www.agrofy.com.ar/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agrofy.com.ar/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agrofy.com.ar/politicas-de-privacidad
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agrofy-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/agrofy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agrofy-rate-limits.yml
coverage:
  checked: '2026-09-13'
  detail: Agrofy markets an integration program at developers.agrofy.com whose own four-step onboarding is a contact form an advisor answers before any reference guide is shared, and all eight of that portal's per-country "API docs" links fail before HTTP — developers.agrofy.com.ar, .com.br and .com.bo are CNAMEs pointing at NXDOMAIN targets under route53.prod-us-1.eks.agrofy.com, and developers.agrofy.cl, .com.co, .com.pe, .com.py and .com.uy have no DNS record at all.
  evidence:
  - status: 200
    url: https://developers.agrofy.com/
  - status: 0
    url: https://developers.agrofy.com.ar/docs
  - status: 403
    url: https://apigateway-argentina.agrofy.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-09-13'
description: Agrofy is a Latin American agribusiness technology company founded in 2015 in Rosario, Argentina, operating the region's largest online marketplace for agricultural inputs, machinery, farmland, vehicles and services. The company runs three business units — Agrofy Market (the marketplace, live in Argentina and Brazil with country storefronts across Bolivia, Chile, Colombia, Paraguay, Peru and Uruguay), Agrofy News (an agricultural news publication) and Agrofy Pay (payments, credit and financing for agribusiness transactions). Agrofy markets a partner integration program, Agrofy Developers, for sellers who want to automate listings and lead management inside the marketplace.
image: https://www.agrofy.com/imagenes/logo-agrofy-sin-tag.png
layout: provider
modified: '2026-09-13'
name: Agrofy
nav: Providers
network: true
overview: 'Agrofy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Agribusiness, Agtech, and Marketplace.


  Agrofy''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Agrofy Plans Pricing
  plan_count: 0
  slug: agrofy-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Agrofy Rate Limits
  slug: agrofy-rate-limits
security:
- kind: domain-security
  name: Agrofy Domain Security
  slug: agrofy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agrofy
tags:
- Company
- Agriculture
- Agribusiness
- Agtech
- Marketplace
- E-Commerce
- Payments
- Latin America
- Argentina
- Brazil
website: https://www.agrofy.com/
---
