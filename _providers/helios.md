---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.helios.do/
- group: company
  title: ''
  type: Blog
  url: https://blog.helios.do/
- group: operate
  title: ''
  type: HelpCenter
  url: https://intercom.help/heliosdo/fr/
- group: operate
  title: ''
  type: Support
  url: https://www.helios.do/contact/
- group: start
  title: ''
  type: SignUp
  url: https://www.helios.do/inscription/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.helios.do/documents/conditions_tarifaires.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.helios.do/documents/Conditions_Generales_Helios.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.helios.do/documents/Politique_De_Confidentialite.pdf
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/helios-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/helios-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/helios-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/helios-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helios-domain-security.yml
coverage:
  checked: '2026-08-17'
  detail: helios is a consumer neobank that ships only an end-user mobile and web banking app — it publishes no developer portal, API reference, SDK or webhook surface, and as a payment services agent of OKALI (REGAFI 731225) it exposes no PSD2 dedicated interface of its own; /openapi.json, /graphql, /mcp, /api and every /.well-known/ path return a real 404 on www.helios.do (a nonsense control path also 404s, so these are not soft-404s), and certificate-transparency enumeration of *.helios.do lists app, backoffice, blog, email, go, help and meta but no api.* host of any kind.
  evidence:
  - status: 404
    url: https://www.helios.do/openapi.json
  - status: 404
    url: https://www.helios.do/.well-known/agent-card.json
  - status: 404
    url: https://www.helios.do/api
  - status: 200
    url: https://www.helios.do/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: helios is a French sustainable-banking company (HELIOS SAS, Paris) offering current, Premium, joint, youth, Liberté and independent/professional accounts, a green savings passbook, sustainable life insurance and wooden or recycled-plastic Visa cards through iOS, Android and web. It is a société à mission and a certified B Corp whose promise is that no customer euro finances fossil fuels or polluting industry, and it publishes the list of transition projects it funds. helios is registered in REGAFI under 731225 as a payment services agent of OKALI, the ACPR-approved electronic money institution that services the accounts. It publishes no public API, SDK, webhook or developer portal; the one machine-readable document it serves is an llms.txt AI-usage policy.
image: https://a.storyblok.com/f/279083/1200x630/38722f8a58/meta-image.png
layout: provider
modified: '2026-08-17'
name: helios
nav: Providers
network: true
overview: 'helios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Fintech, Neobank, and Sustainable Finance.


  helios'' developer surface includes engineering blog, support, signup flow, pricing, and 9 more developer resources.'
plans:
- name: Helios Plans Pricing
  plan_count: 0
  slug: helios-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Helios Rate Limits
  slug: helios-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/helios/refs/heads/main/screenshots/helios-2026-09-02T145716.png
security:
- kind: domain-security
  name: Helios Domain Security
  slug: helios-domain-security
  summary_line: TLSv1.3 · DMARC
slug: helios
tags:
- Company
- Banking
- Fintech
- Neobank
- Sustainable Finance
- Payments
- Climate Tech
- France
website: https://www.helios.do/
---
