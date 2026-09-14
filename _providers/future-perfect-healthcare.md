---
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.healthcare.future-perfect.co/
- group: company
  title: ''
  type: Blog
  url: https://www.healthcare.future-perfect.co/index.php/latest-news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.healthcare.future-perfect.co/index.php/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/future-perfect-healthcare/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/FPerfect_health
- group: auth
  title: ''
  type: DomainSecurity
  url: security/future-perfect-healthcare-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/future-perfect-healthcare-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/future-perfect-healthcare-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/future-perfect-healthcare-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/future-perfect-healthcare-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/future-perfect-healthcare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/future-perfect-healthcare-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/future-perfect-healthcare-llms.txt
coverage:
  checked: '2026-09-02'
  detail: 'Future Perfect''s own G-Cloud 14 PANACEA entry answers "API: Yes", "API documentation: Yes" and "API documentation formats: Open API (also known as Swagger)", but that OpenAPI is supplied only to contracted customers — the company runs no developer portal at all, and every discovery path on its Joomla marketing site (/openapi.json, /swagger.json, /api-docs, /docs, /developers, /llms.txt and all seven /.well-known/ paths) returns the same 404 error page, with no api./docs./developer. subdomain resolving in DNS.'
  evidence:
  - status: 200
    url: https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/557090777176539
  - status: 404
    url: https://www.healthcare.future-perfect.co/openapi.json
  - status: 404
    url: https://www.healthcare.future-perfect.co/.well-known/api-catalog
  - status: 200
    url: https://www.healthcare.future-perfect.co/index.php/component/sppagebuilder/?view=page&id=531
  reason: customer-only-docs
  state: gated
created: '2026-09-02'
description: Future Perfect (Healthcare) Limited is a UK health-informatics company that builds PANACEA, an integrated care-pathway electronic record platform built on an openEHR clinical repository. PANACEA connects existing provider systems as nodes through single sign-on so that shared care records, Cancer Alliances, pathology networks and genomics registries can work from one real-time, vendor-neutral record rather than from siloed exports. Around it the company sells openEHR integration and development, clinical safety assurance to NHS DCB0129/DCB0160, hosting and co-development of AI clinical decision support, and UK resale of openEHR e-learning. It is a listed openEHR International industry partner (Bronze, renewed February 2026) and sells to the NHS through the UK G-Cloud 14 framework. The company declares that PANACEA exposes APIs for openEHR, HL7 v2 and FHIR data exchange, documented in OpenAPI, but publishes no developer portal, base URL or contract publicly.
image: https://www.healthcare.future-perfect.co/images/fav-fp300x.png
layout: provider
modified: '2026-09-02'
name: Future Perfect (Healthcare)
nav: Providers
network: true
overview: 'Future Perfect (Healthcare) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Electronic Health Records, and openEHR.


  Future Perfect (Healthcare)''s developer surface includes engineering blog, authentication, and 11 more developer resources.'
plans:
- name: Future Perfect Healthcare Plans Pricing
  plan_count: 3
  slug: future-perfect-healthcare-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Future Perfect Healthcare Rate Limits
  slug: future-perfect-healthcare-rate-limits
security:
- kind: authentication
  name: Future Perfect Healthcare Authentication
  slug: future-perfect-healthcare-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Future Perfect Healthcare Domain Security
  slug: future-perfect-healthcare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: future-perfect-healthcare
tags:
- Company
- Healthcare
- Health IT
- Electronic Health Records
- openEHR
- Interoperability
- Clinical Decision Support
- Genomics
- Artificial Intelligence
- NHS
- United Kingdom
website: https://www.healthcare.future-perfect.co/
---
