---
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.adaptx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adaptx.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.adaptx.com/request-info
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MDmetrix
- group: company
  title: ''
  type: Newsroom
  url: https://www.adaptx.com/news
- group: auth
  title: ''
  type: Compliance
  url: conformance/adaptx-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adaptx-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaptx-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptx-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adaptx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adaptx-rate-limits.yml
coverage:
  checked: '2026-09-07'
  detail: AdaptX sells a hosted clinical-analytics application that its own team wires into a health system's EMR under contract — its 74-URL sitemap contains no developer, API, or docs page, /developers /api /docs all 404, and api./app./developer./docs.adaptx.com do not resolve in public DNS at all, so there is no developer program to gate or to read.
  evidence:
  - status: 404
    url: https://www.adaptx.com/developers
  - status: 404
    url: https://www.adaptx.com/docs
  - status: 404
    url: https://www.adaptx.com/openapi.json
  - status: 404
    url: https://www.adaptx.com/.well-known/api-catalog
  - status: 200
    url: https://www.adaptx.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: AdaptX is a Seattle-based clinical performance management company (founded 2016 as MDMetrix, renamed AdaptX in 2021) whose self-serve platform reads a hospital's existing electronic medical record data and turns it into near-real-time analytics that clinical, quality, operational and finance leaders use to measure and reduce clinical variation. Customers include Seattle Children's, Memorial Hermann, Children's Minnesota, USA Health and Kittitas Valley Healthcare, with published case studies covering surgical capacity, emergency department time-to-triage, length of stay, anesthetic greenhouse-gas reduction and health-equity stratification. The product is delivered as a hosted SaaS application on AWS to contracted health systems; as of this profiling pass AdaptX publishes no public developer portal, API reference, or machine-readable API description.
image: https://cdn.prod.website-files.com/60a92df620b4624c09b5ac26/60fdb4f81a5ab2a0549dfbd7_Adaptx_webclip-01.png
layout: provider
modified: '2026-09-07'
name: AdaptX
nav: Providers
network: true
overview: 'AdaptX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Healthcare Analytics, Clinical Data, and Electronic Medical Records.


  AdaptX''s developer surface includes support and 10 more developer resources.'
plans:
- name: Adaptx Plans Pricing
  plan_count: 0
  slug: adaptx-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Adaptx Rate Limits
  slug: adaptx-rate-limits
security:
- kind: domain-security
  name: Adaptx Domain Security
  slug: adaptx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adaptx
tags:
- Company
- Health Care
- Healthcare Analytics
- Clinical Data
- Electronic Medical Records
- Hospital Operations
- Quality Improvement
- Business Intelligence
- SaaS
- Seattle
website: https://www.adaptx.com/
---
