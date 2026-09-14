---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.fluor.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fluor
- group: company
  title: ''
  type: Blog
  url: https://newsroom.fluor.com/rss/pressrelease.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.fluor.com/contact-us/general
- group: start
  title: ''
  type: Login
  url: https://www.fluor.com/client-login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fluor.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fluor.com/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fluor-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fluor-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fluor-llms.txt
coverage:
  checked: '2026-09-10'
  detail: Fluor sells engineering, procurement and construction services, not software — the fluor.com sitemap's 1,201 URLs contain no developer, API or documentation page, api/developer/developers/docs/apis.fluor.com all resolve NXDOMAIN, and the only machine-readable document served anywhere on the estate is an RFC 8414 OAuth metadata file belonging to the Eightfold recruiting platform running under careers.fluor.com.
  evidence:
  - status: 200
    url: https://www.fluor.com/sitemap.xml
  - status: 404
    url: https://www.fluor.com/llms.txt
  - status: 404
    url: https://www.fluor.com/openapi.json
  - status: 404
    url: https://www.fluor.com/.well-known/api-catalog
  - status: 200
    url: https://careers.fluor.com/.well-known/oauth-authorization-server
  reason: not-a-software-company
  state: none
created: '2026-03-21'
description: 'Fluor Corporation (NYSE: FLR) is a Fortune 500 engineering, procurement, construction and maintenance company headquartered in Irving, Texas. Fluor designs and builds capital projects and provides project-management services for energy, chemicals, life sciences, mining and metals, advanced technologies, infrastructure and government clients worldwide, and licenses its own process technologies such as Econamine FG Plus and Fluor Solvent. Fluor sells engineering and construction services rather than software: it operates no developer program, publishes no API reference, and serves no machine-readable API contract. Its business-to-business integration with suppliers runs inside SAP Ariba and Workday, whose contracts belong to those vendors. This is an independent API Evangelist profile of Fluor''s public surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fluor.png
layout: provider
modified: '2026-09-10'
name: Fluor
nav: Providers
network: true
overview: 'Fluor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Engineering, Construction, Procurement, and Project Management.


  Fluor''s developer surface includes engineering blog, support, and 8 more developer resources.'
press:
- date: '2026-05-25'
  title: Business Incubation – Accelerating Emerging Technologies
  url: https://www.fluor.com/services-and-expertise/innovation-and-expertise/business-incubation/
- date: '2026-05-25'
  title: Fluor Uses IBM Watson to Deliver Predictive Analytics ...
  url: https://www.prnewswire.com/news-releases/fluor-uses-ibm-watson-to-deliver-predictive-analytics-capability-for-megaprojects-300711688.html
- date: '2026-05-25'
  title: 'Fluor Corporation (FLR): This Industrial Stock Is Already ...'
  url: https://finance.yahoo.com/news/fluor-corporation-flr-industrial-stock-114846750.html
- date: '2026-05-25'
  title: Quarterly Results - Fluor Corporation - Financials
  url: https://fluorenterprisesinc2023rbcr.q4web.com/financials/quarterly-results/default.aspx
- date: '2026-05-25'
  title: Fluor Selected for Expansion of Large-Scale Biologics ...
  url: https://www.sttinfo.fi/tiedote/69952904/fluor-selected-for-expansion-of-large-scale-biologics-manufacturing-facility-in-scandinavia?publisherId=58763726
random_paper: 6
screenshot: https://raw.githubusercontent.com/api-evangelist/fluor/refs/heads/main/screenshots/fluor-2026-06-20T181338.png
security:
- kind: domain-security
  name: Fluor Domain Security
  slug: fluor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fluor Vulnerability Disclosure
  slug: fluor-vulnerability-disclosure
  summary_line: Hackerone
slug: fluor
tags:
- Fortune 500
- Engineering
- Construction
- Procurement
- Project Management
- Energy
- Infrastructure
- Mining
website: https://www.fluor.com
---
