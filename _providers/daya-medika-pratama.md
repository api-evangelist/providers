---
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://dayamedikapratama.com/
- group: company
  title: ''
  type: About
  url: https://dayamedikapratama.com/about-us/
- group: other
  title: ''
  type: ProductPage
  url: https://afyabetter.com/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://afyabetter.com/documentation/
- group: company
  title: ''
  type: Careers
  url: https://dayamedikapratama.com/careers/
- group: operate
  title: ''
  type: ContactForm
  url: https://dayamedikapratama.com/contact-us/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/daya-medika-pratama-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/daya-medika-pratama-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/daya-medika-pratama-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daya-medika-pratama-domain-security.yml
coverage:
  checked: '2026-09-02'
  detail: Daya Medika Pratama ships AFYA Better HIS and AFYA Insurance as installed end-user hospital software sold through a "Talk To Us" form, and the only documentation it publishes is an Indonesian end-user knowledge base at afyabetter.com/documentation/ whose one substantive article is an Excel-template data import walkthrough — no developer portal, no API reference, no api./developer./docs. subdomain in DNS, and /openapi.json, /graphql, /apis.json and every /.well-known/ path 404 on both the corporate and product hosts.
  evidence:
  - status: 200
    url: https://afyabetter.com/documentation/
  - status: 200
    url: https://afyabetter.com/docs/afya-office/import-data/
  - status: 404
    url: https://dayamedikapratama.com/openapi.json
  - status: 404
    url: https://dayamedikapratama.com/.well-known/api-catalog
  - status: 200
    url: https://dayamedikapratama.com/wp-sitemap-posts-page-1.xml
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: PT Daya Medika Pratama (DMP) is an Indonesian healthcare IT company in Central Jakarta that builds and implements hospital information systems and insurance core systems. It has worked in IT since 2007 — first as a systems integrator building data-acquisition systems for textile production machinery, later as a Microsoft Business Solution Partner in healthcare and education — and today sells AFYA Better HIS (a hospital information system with an openEHR-based clinical data repository, stated as connected to BPJS Kesehatan, Kemenkes/SATUSEHAT, FHIR and Better, and in use at more than 40 Indonesian hospitals), AFYA Insurance (policy and claims management), implementation of the Better digital health platform, and Microsoft Dynamics 365 as hospital back office. It is an openEHR industry partner and a Better (better.care) partner for the Indonesian market, and runs AFYA Better Academy, an openEHR and FHIR training programme for hospital IT staff. Its positioning line is "One Patient
  One Record for Better Health". DMP publishes no public API, developer portal, SDK or machine-readable contract; the standards it names are national platforms its products consume on a hospital's behalf, not APIs it ships.
image: https://dayamedikapratama.com/wp-content/uploads/2024/10/cropped-Colored.png
layout: provider
modified: '2026-09-02'
name: Daya Medika Pratama
nav: Providers
network: true
overview: Daya Medika Pratama is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Information System, Electronic Health Records, and openEHR.
plans:
- name: Daya Medika Pratama Plans Pricing
  plan_count: 0
  slug: daya-medika-pratama-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Daya Medika Pratama Rate Limits
  slug: daya-medika-pratama-rate-limits
security:
- kind: domain-security
  name: Daya Medika Pratama Domain Security
  slug: daya-medika-pratama-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: daya-medika-pratama
tags:
- Company
- Healthcare
- Health Information System
- Electronic Health Records
- openEHR
- FHIR
- Hospital
- Insurance
- Systems Integrator
- Microsoft Dynamics 365
- Indonesia
website: https://dayamedikapratama.com/
---
