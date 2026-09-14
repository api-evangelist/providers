---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeremc36d-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aerem.co/
- group: company
  title: ''
  type: Blog
  url: https://www.aerem.co/blog
- group: operate
  title: ''
  type: Support
  url: https://www.aerem.co/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aerem.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerem.co/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeremc36d-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/aeremc36d-packages.yml
coverage:
  checked: '2026-09-10'
  detail: 'Aerem ships real software — a Webflow marketing site, Next.js installer and monitoring portals, a B2B marketplace and two mobile apps — but exposes none of it to third parties: there is no developer portal (https://www.aerem.co/developers returns 404), the provider''s own llms.txt indexes every public page and lists no API or developer section, /.well-known/ is a blanket nginx 403 on all six application hosts, and the only backend that answers anonymously, auth.aerem.co, returns the plain string "Server is up and running" with no discovery document.'
  evidence:
  - status: 404
    url: https://www.aerem.co/developers
  - status: 200
    url: https://www.aerem.co/llms.txt
  - status: 404
    url: https://partner.aerem.co/openapi.json
  - status: 403
    url: https://auth.aerem.co/.well-known/openid-configuration
  - status: 404
    url: https://api.github.com/orgs/aerem
  reason: no-developer-program
  state: none
created: '2026-09-10'
description: Aerem is a Mumbai-based "FinTech for CleanTech" group that finances, supplies and monitors rooftop solar in India. The group comprises Aerem Solutions Private Limited, NetZero Finance Private Limited — an RBI-licensed, solar-focused NBFC — and Sunstore Solar Private Limited. Aerem underwrites collateral-free rooftop solar loans for MSMEs and homeowners, provides supply chain finance to solar EPC installers, runs the SunStore B2B solar equipment marketplace, and operates AeROC, an inverter-agnostic remote monitoring portal for installed plants. It also ships two mobile products — the Aerem App for borrowers and the Aerem Partner App for installers — and an AAA (Aerem Asset Assurance) quality-certification programme for EPCs. Aerem publishes a machine-readable llms.txt and five first-party npm packages, but no public API, developer portal or machine-readable API contract of any kind.
image: https://cdn.prod.website-files.com/659794dc6660d7bd9a22884d/69fc574bc9b0245e966fc0ed_754ed9b4063855dc515626105e5540d4_logo-new.svg
layout: provider
modified: '2026-09-10'
name: Aerem
nav: Providers
network: true
overview: 'Aerem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Lending, Energy, and Solar.


  Aerem''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Aeremc36D Plans Pricing
  plan_count: 0
  slug: aeremc36d-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Aeremc36D Rate Limits
  slug: aeremc36d-rate-limits
security:
- kind: domain-security
  name: Aeremc36D Domain Security
  slug: aeremc36d-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aeremc36d
tags:
- Company
- Financial Services
- Lending
- Energy
- Solar
- Clean Energy
- Fintech
- Marketplace
- India
- Non-Banking Financial Company
website: https://www.aerem.co/
---
