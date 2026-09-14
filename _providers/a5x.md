---
api_count: 1
apis:
- description: The trading, market data and post-trade interfaces A5X exposes to exchange participants — order entry and drop copy over FIX, a binary market data feed, and post-trade capture, allocation, positioning
  name: A5X Technical Interfaces
  slug: a5x-technical-interfaces
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/a5x-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a5x.com.br/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal-tecnico.a5x.com.br/login
- group: company
  title: ''
  type: Blog
  url: https://a5x.com.br/en/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://a5x.com.br/en/feed/
- group: operate
  title: ''
  type: Support
  url: https://a5x.com.br/en/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://a5x.com.br/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a5x.com.br/en/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/a5x
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/a5x-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/a5x-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/a5x-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/a5x-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/a5x-conformance.yml
coverage:
  checked: '2026-09-05'
  detail: Every A5X technical specification — FIX and binary order entry, market data, drop copy, and the post-trade message catalogs — sits inside the Portal Tecnico wiki at portal-tecnico.a5x.com.br, which returns HTTP 403 to every anonymous request for a document path while the public /docs/ archive on the marketing site holds only three billing pages whose bodies are placeholder text.
  evidence:
  - status: 403
    url: https://portal-tecnico.a5x.com.br/docs
  - status: 403
    url: https://portaldev.a5x.com.br/openapi.json
  - status: 200
    url: https://a5x.com.br/docs/documentacao-sobre-faturamento/
  - status: 404
    url: https://a5x.com.br/.well-known/security.txt
  reason: partner-login
  state: gated
created: '2026-09-05'
description: A5X S.A. is a next-generation derivatives and futures exchange and clearing house being built for the Brazilian market, founded in 2023 in Sao Paulo by former XP executives Carlos Ferreira Filho and Karel Luketic together with Nilson Monteiro (Ideal) and Julian Chediak. It is an asset-light, technology-first venue running on London Stock Exchange Group trading, clearing and market surveillance technology, and it has raised R$385 million (about USD 72.6 million) from investors including IMC Trading, Jump Trading Group, Optiver, XTX Markets and ABN AMRO Clearing. Its listed, financially settled contract set covers stock index futures and options (local and offshore), single stock futures and options, currency futures and options, local interest rate futures and options, and cryptocurrency futures, with European-style options exercised automatically at expiry. For integrators, A5X publishes a technical developer portal covering connectivity (site-to-site VPN, LAN-to-LAN, cross
  connect at Equinix SP3, AWS Direct Connect), order entry, market data, drop copy and post-trade settlement, allocation, positioning and risk interfaces over FIX and binary protocols. The portal requires a login, so those specifications are not publicly readable.
image: https://a5x.com.br/wp-content/uploads/2025/07/A5X-Logo-Vetorizado-Azul-1.png
layout: provider
modified: '2026-09-05'
name: A5X
nav: Providers
network: true
overview: 'A5X publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Capital Markets, Stock Exchange, and Derivatives.


  A5X''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: A5X Plans Pricing
  plan_count: 0
  slug: a5x-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: A5X Rate Limits
  slug: a5x-rate-limits
security:
- kind: domain-security
  name: A5X Domain Security
  slug: a5x-domain-security
  summary_line: TLSv1.3 · DMARC
slug: a5x
tags:
- Company
- Financial Services
- Capital Markets
- Stock Exchange
- Derivatives
- Futures
- Trading
- Market Data
- Clearing
- FIX Protocol
- Brazil
website: https://a5x.com.br/en/
---
