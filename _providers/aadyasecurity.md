---
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.judysecurity.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.judysecurity.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.judysecurity.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.judysecurity.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.judysecurity.ai/guides/judy-security-standard-terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://portal.judysecurity.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.judysecurity.ai/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aadyasecurity-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aadyasecurity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aadyasecurity-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aadyasecurity-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aadyasecurity-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: AaDya Security ships as Judy Security and runs a customer portal, a Kiflo partner portal and an Atlassian Statuspage, but no developer program of any kind - www.judysecurity.ai/openapi.json, /swagger.json, /api-docs, /docs and /llms.txt all 404 against the Webflow site, the same paths on portal.judysecurity.ai and dns.judysecurity.ai return only SPA shells, the two "API integration" guides it publishes document ConnectWise's and Autotask's APIs rather than its own, and there is no GitHub organization under any aadya/judy spelling.
  evidence:
  - status: 404
    url: https://www.judysecurity.ai/openapi.json
  - status: 404
    url: https://www.judysecurity.ai/api-docs
  - status: 404
    url: https://www.judysecurity.ai/llms.txt
  - status: 404
    url: https://portal.judysecurity.ai/openapi.json
  - status: 404
    url: https://api.github.com/orgs/judysecurity
  - status: 200
    url: https://www.judysecurity.ai/guides
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: AaDya Security, founded in 2019 by Raffaele Mautone and rebranded in 2023 around its product as Judy Security, sells an all-in-one AI-driven cybersecurity platform to small and midsize businesses, schools, non-profits and public-sector buyers, almost entirely through MSP and MSSP partners. The Judy platform bundles endpoint detection and response, DNS filtering, a password manager, a cloud SIEM and XDR ("Blue Team"), automated compliance management and reporting, secure and passwordless authentication, and security awareness training behind a single Control Center. The company publishes no developer program, no public API reference and no machine-readable API contract; its documented API surface is outbound only - configuration guides for pushing Judy Portal tickets into ConnectWise PSA and Datto Autotask using those vendors' APIs. It does operate a public Atlassian Statuspage for the platform.
image: https://cdn.prod.website-files.com/65f9c8c42e34897f931cc72d/66c78770b6ff7f165eb5ef33_Favicon.png
layout: provider
modified: '2026-09-05'
name: AaDya Security (Judy Security)
nav: Providers
network: true
overview: 'AaDya Security (Judy Security) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Endpoint Detection and Response, and SIEM.


  AaDya Security (Judy Security)''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Aadyasecurity Plans Pricing
  plan_count: 0
  slug: aadyasecurity-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Aadyasecurity Rate Limits
  slug: aadyasecurity-rate-limits
security:
- kind: domain-security
  name: Aadyasecurity Domain Security
  slug: aadyasecurity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aadyasecurity
tags:
- Company
- Security
- Cybersecurity
- Endpoint Detection and Response
- SIEM
- DNS Filtering
- Password Management
- Compliance
- Security Awareness Training
- Managed Service Providers
- Small Business
website: https://www.judysecurity.ai/
---
