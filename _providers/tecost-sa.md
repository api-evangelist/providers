---
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.tecost.ch/
- group: company
  title: ''
  type: Blog
  url: https://www.tecost.ch/fr/actualites
- group: operate
  title: ''
  type: Support
  url: https://www.tecost.ch/fr/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tecost.ch/fr/protection-des-donnees
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tecost-sa
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tecost-sa-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tecost-sa-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tecost-sa-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/tecost-sa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tecost-sa-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: Tecost markets an openEHR-based Data Integration Hub plus HL7 and SOAP integration for the Carefolio suite, but every Carefolio host is customer-only — www.carefolio.ch answers nginx 403 to anonymous requests and tenant hosts such as daler.carefolio.ch redirect to a Microsoft Entra ID SAML sign-in — so no reference, WSDL or openEHR artifact is reachable without an active institutional tenant.
  evidence:
  - status: 403
    url: https://www.carefolio.ch/
  - status: 200
    url: https://daler.carefolio.ch/
  - status: 403
    url: https://www.tecost.ch/.well-known/security.txt
  - status: 404
    url: https://www.tecost.ch/openapi.json
  - status: 404
    url: https://www.carefolio.ch/rest/openehr/v1/definition/template/adl1.4
  reason: customer-only-docs
  state: gated
created: '2026-09-02'
description: Tecost SA is a Swiss health-information-technology company, founded in 1997 and based in Fribourg, that designs, develops, implements, hosts and operates clinical information systems for hospitals, clinics, psychiatric and rehabilitation institutions, long-term care facilities and home-care organizations across French- and German-speaking Switzerland. Its product line is the Carefolio suite — Acute, Rehabilitation, Psy, LongTerm, AtHome, Critical Care 3C, Network, Portal, Workshop, AI and the openEHR-based Carefolio DIH Data Integration Hub — alongside consulting, change management, custom development, 24/7 maintenance and SaaS operations. Tecost is a named industry partner of the openEHR Foundation and states that it is making openEHR the cornerstone of its clinical-data interoperability. It publishes no public developer portal, API reference or machine-readable contract; Carefolio is delivered as per-customer tenants behind Microsoft Entra ID single sign-on, so any integration
  contract reaches integrators under a commercial agreement rather than through a public surface.
image: https://www.tecost.ch/images/logo-tecost.svg
layout: provider
modified: '2026-09-02'
name: Tecost SA
nav: Providers
network: true
overview: 'Tecost SA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Electronic Health Records, and Clinical Information Systems.


  Tecost SA''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Tecost Sa Plans Pricing
  plan_count: 0
  slug: tecost-sa-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Tecost Sa Rate Limits
  slug: tecost-sa-rate-limits
security:
- kind: domain-security
  name: Tecost Sa Domain Security
  slug: tecost-sa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tecost-sa
tags:
- Company
- Health
- Healthcare
- Electronic Health Records
- Clinical Information Systems
- openEHR
- Interoperability
- Hospital Software
- Long-Term Care
- Home Care
- Switzerland
website: https://www.tecost.ch/
---
