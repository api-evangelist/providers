---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.valerahealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.valerahealth.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.valerahealth.com/help-center/
- group: operate
  title: ''
  type: Support
  url: https://www.valerahealth.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.valerahealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.valerahealth.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valerahealth
- group: design
  title: ''
  type: Conformance
  url: conformance/valera-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/valera-health-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valera-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valera-health-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Valera Health is a virtual behavioral-health care provider, not a software vendor — it runs on NextGen Healthcare for its clinical record and patient portal, publishes no developer portal, docs subdomain or reference of any kind, and its only externally addressable API host, api.valerahealth.com, is the private Node/Express backend for its own patient app, which answered 404 for every discovery path probed.
  evidence:
  - status: 404
    url: https://api.valerahealth.com/openapi.json
  - status: 404
    url: https://api.valerahealth.com/graphql
  - status: 404
    url: https://www.valerahealth.com/llms.txt
  - status: 404
    url: https://www.valerahealth.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'Valera Health is a Brooklyn, New York based virtual behavioral health provider delivering therapy, psychiatry, group therapy, comprehensive Dialectical Behavior Therapy (DBT), suicide care and youth support programs to adults and children through an in-house clinical team, a care-coordinator model and a patient mobile app. It is a care-delivery organization rather than a software vendor: revenue comes from commercial insurance, Medicaid and Medicare reimbursement, and the clinical record and patient portal run on third-party health IT (the patient portal is operated by NextGen Healthcare at pxpportal.nextgen.com). As of this profile Valera Health publishes no developer program, no public API reference, and no machine-readable contract of any kind; its only externally addressable API host, api.valerahealth.com, is the private backend for its own patient application.'
image: https://www.valerahealth.com/wp-content/uploads/2025/01/valera-home-main-1024x966.jpg
layout: provider
modified: '2026-09-02'
name: Valera Health
nav: Providers
network: true
overview: 'Valera Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Behavioral Health, and Mental Health.


  Valera Health''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 8
security:
- kind: domain-security
  name: Valera Health Domain Security
  slug: valera-health-domain-security
  summary_line: TLSv1.3
slug: valera-health
tags:
- Company
- Health
- Healthcare
- Behavioral Health
- Mental Health
- Telehealth
- Telemedicine
- Psychiatry
- Digital Health
website: https://www.valerahealth.com/
---
