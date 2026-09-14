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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/profility-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://profility.com/
- group: company
  title: ''
  type: About
  url: https://profility.com/about/
- group: other
  title: ''
  type: Products
  url: https://profility.com/products/
- group: company
  title: ''
  type: Blog
  url: https://profility.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://profility.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://profility.com/profility-privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://dashboard.profility.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/profility-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/profility-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/profility-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Profility ships its post-acute care platform only as two ASP.NET customer login applications (dashboard.profility.com, ranking.profility.com) which return clean 404s on every OpenAPI, GraphQL, MCP and agent-card path, and the company publishes no developer portal, API reference, SDK or pricing page anywhere on profility.com.
  evidence:
  - status: 404
    url: https://dashboard.profility.com/openapi.json
  - status: 404
    url: https://dashboard.profility.com/swagger/v1/swagger.json
  - status: 404
    url: https://dashboard.profility.com/.well-known/agent-card.json
  - status: 404
    url: https://ranking.profility.com/openapi.json
  - status: 404
    url: https://ranking.profility.com/graphql
  - status: 202
    url: https://profility.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Profility, Inc. is a Boston-based healthcare technology company whose AI-powered platform supports collaboration and decision-making across the post-acute care continuum. Its cloud platform combines large historical patient datasets with predictive analytics to build personalized care-planning profiles, predict rehabilitation success and readmission risk across post-acute settings, and guide placement and referral decisions between hospitals, skilled nursing facilities, home health, behavioral health and dialysis providers. Its PReP Authorize product automates prior authorization and concurrent review for managed-care patients, covering managed-care contract intelligence, denial reduction and audit preparedness. Profility markets analytical reporting that scores post-acute providers and maps local market position for referral-pattern optimization. The company reports deployment across 500+ facilities. Profility ships its platform as an end-user web application; it publishes
  no public developer program, API reference or machine-readable specification.
layout: provider
modified: '2026-08-26'
name: Profility
nav: Providers
network: true
overview: 'Profility is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Health IT, Post-Acute Care, Artificial Intelligence, and Predictive Analytics.


  Profility''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Profility Plans Pricing
  plan_count: 0
  slug: profility-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Profility Rate Limits
  slug: profility-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/profility/refs/heads/main/screenshots/profility-2026-09-02T152123.png
security:
- kind: domain-security
  name: Profility Domain Security
  slug: profility-domain-security
  summary_line: TLSv1.3 · DMARC
slug: profility
tags:
- Healthcare
- Health IT
- Post-Acute Care
- Artificial Intelligence
- Predictive Analytics
- Care Coordination
- Prior Authorization
- Revenue Cycle Management
website: https://profility.com/
---
