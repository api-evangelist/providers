---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dedalus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dedalus.com/global/en/
- group: company
  title: ''
  type: Blog
  url: https://www.dedalus.com/global/en/perspectives/
- group: company
  title: ''
  type: News
  url: https://www.dedalus.com/global/en/media/news/
- group: operate
  title: ''
  type: Support
  url: https://www.dedalus.com/global/en/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dedalus.com/global/en/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dedalus.com/global/en/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.dedalus.com/global/en/about-us/regulatory-compliance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Dedalus-healthcare-ohc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dedalus-group/
- group: company
  title: ''
  type: Jobs
  url: https://www.dedalus.com/global/en/working-at-dedalus/
- group: design
  title: ''
  type: Conformance
  url: conformance/dedalus-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dedalus-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Dedalus markets an "API economy" and an HL7 FHIR API management component inside DC4H, but every product page ends at a "request a demo" contact form instead of a reference — there is no developer host at all (developer/developers/api/docs.dedalus.com are NXDOMAIN) and every /.well-known/, /llms.txt and /openapi.json path on www.dedalus.com 301s to the corporate homepage.
  evidence:
  - status: 200
    url: https://www.dedalus.com/global/en/our-offer/products/dc4h/
  - status: 301
    url: https://www.dedalus.com/openapi.json
  - status: 301
    url: https://www.dedalus.com/.well-known/agent-card.json
  - status: 0
    url: https://developer.dedalus.com/
  reason: sales-gate
  state: gated
created: '2026-09-02'
description: Dedalus Group is a European healthcare and diagnostics software provider headquartered in Florence, Italy, supplying clinical information systems, electronic patient records, laboratory and diagnostic imaging software to hospitals, laboratories and care networks across roughly 40 countries. Its product estate includes the ORBIS and ORBIS U electronic patient record suites, the Lorenzo EPR in the UK, X1.V1 in Italy, and DC4H (Digital Connect 4 Health) / Open Health Connect, an HL7 FHIR-based interoperability and longitudinal-patient-record platform the company markets under an "API economy" model. Dedalus states that DC4H exposes an FHIR API management component that third-party developers can build against, and the company participates in the openEHR community, but as of this profiling pass it publishes no public developer portal, no API reference, no OpenAPI or FHIR CapabilityStatement, and no sandbox on any dedalus.com host — integration access runs through a sales and customer-support
  motion rather than a self-serve developer surface.
image: https://www.dedalus.com/global/wp-content/uploads/sites/9/2023/12/logo_Site-Image.jpg
layout: provider
modified: '2026-09-02'
name: Dedalus
nav: Providers
network: true
overview: 'Dedalus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Electronic Health Records, and Interoperability.


  Dedalus'' developer surface includes engineering blog, product news, support, and 10 more developer resources.'
plans:
- name: Dedalus Plans Pricing
  plan_count: 0
  slug: dedalus-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Dedalus Rate Limits
  slug: dedalus-rate-limits
security:
- kind: domain-security
  name: Dedalus Domain Security
  slug: dedalus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dedalus
tags:
- Company
- Healthcare
- Health IT
- Electronic Health Records
- Interoperability
- FHIR
- HL7
- openEHR
- Clinical Software
- Laboratory Information Systems
- Medical Imaging
- Europe
website: https://www.dedalus.com/global/en/
---
