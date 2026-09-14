---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abmrespiratorycare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abmrc.com/
- group: company
  title: ''
  type: Blog
  url: https://abmrc.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://abmrc.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://abmrc.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abmrc.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abmrc.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abmrc/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abmrespiratorycare-llms.txt
coverage:
  checked: '2026-09-06'
  detail: ABM Respiratory Care builds BiWaze airway-clearance and cough-assist hardware sold through demo requests and reimbursement channels, and its whole public presence is a WordPress marketing site at abmrc.com plus a WordPress eIFU manuals portal at eifu.abmrc.com — no api/developer/docs/ status subdomain resolves, and the only machine-readable endpoint on either host is the default WordPress core REST API at /wp-json/, which is CMS scaffolding rather than a product API.
  evidence:
  - status: 404
    url: https://abmrc.com/openapi.json
  - status: 404
    url: https://abmrc.com/llms.txt
  - status: 404
    url: https://abmrc.com/.well-known/agent-card.json
  - status: 404
    url: https://eifu.abmrc.com/openapi.json
  - status: 200
    url: https://abmrc.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'ABM Respiratory Care (ABMRC, LLC — operating with Advanced Biomechanics Private Limited in Bangalore, India and Advanced Bio Machines PTE LTD in Singapore, with US headquarters in Eagan, Minnesota) is a privately held respiratory medical device manufacturer founded by CTO Vinay Joshi and led by CEO Greg Miller. It designs, manufactures and sells airway clearance and lung ventilation hardware under the BiWaze brand — BiWaze Clear (oscillation and lung expansion therapy) and BiWaze Cough (mechanical insufflation-exsufflation) — in both hospital and home-care configurations, sold through direct sales, demo requests and reimbursement channels rather than self-service signup. ABM Respiratory Care is a physical device company: it publishes no developer portal, no public API, no SDK and no machine-readable specification, and its entire public web surface is a WordPress marketing site at abmrc.com plus a separate WordPress electronic instructions-for-use portal at eifu.abmrc.com.'
image: https://abmrc.com/wp-content/uploads/2025/11/product-001.webp
layout: provider
modified: '2026-09-06'
name: ABM Respiratory Care
nav: Providers
network: true
overview: 'ABM Respiratory Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, MedTech, and Respiratory Care.


  ABM Respiratory Care''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 3
security:
- kind: domain-security
  name: Abmrespiratorycare Domain Security
  slug: abmrespiratorycare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: abmrespiratorycare
tags:
- Company
- Medical Devices
- Healthcare
- MedTech
- Respiratory Care
- Airway Clearance
- Mechanical Ventilation
- Pulmonology
- Home Health
- Hospital Equipment
website: https://abmrc.com/
---
