---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apnimed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apnimed.com/
- group: company
  title: ''
  type: About
  url: https://apnimed.com/about/
- group: company
  title: ''
  type: Blog
  url: https://apnimed.com/news/
- group: operate
  title: ''
  type: Support
  url: https://apnimed.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apnimed.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apnimed.com/privacy-policy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.apnimed.com/
- group: company
  title: ''
  type: Careers
  url: https://apnimed.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apnimed
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/apnimed_stock/
- group: company
  title: ''
  type: BlogFeeds
  url: https://apnimed.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://apnimed.com/news/
- group: other
  title: ''
  type: Research
  url: https://apnimed.com/publications/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apnimed-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Apnimed is a clinical-stage drug developer whose product is an oral pill (AD109) for obstructive sleep apnea, so there is no software surface to expose; apnimed.com is a WordPress marketing site whose full Yoast sitemap lists 24 pages and not one developer, API, or documentation page, and api./docs./developer.apnimed.com do not resolve in DNS.
  evidence:
  - status: 404
    url: https://apnimed.com/openapi.json
  - status: 404
    url: https://apnimed.com/llms.txt
  - status: 404
    url: https://apnimed.com/.well-known/agent-card.json
  - status: 404
    url: https://apnimed.com/.well-known/security.txt
  - status: 0
    url: https://api.apnimed.com/openapi.json
  - status: 404
    url: https://ir.apnimed.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Apnimed is a late-stage clinical-stage pharmaceutical company headquartered in Cambridge, Massachusetts, developing novel oral drug therapies for sleep-related breathing disorders. Its lead candidate AD109 (Oxnimbi) is a fixed-dose combination of an anti-muscarinic and a selective norepinephrine reuptake inhibitor, designed to improve upper-airway muscle activity and treat an underlying neuromuscular cause of obstructive sleep apnea (OSA) rather than manage it mechanically. The company was founded in 2017, partners with Shionogi through the Shionogi-Apnimed Sleep Science (SASS) joint venture, and had a New Drug Application for AD109 accepted by the FDA in 2026. Apnimed is a drug developer, not a software vendor: it publishes no developer portal, API documentation, or machine-readable API artifacts.'
image: https://apnimed.com/wp-content/themes/apnimed/favicon/android-icon-192x192.png
layout: provider
modified: '2026-08-06'
name: Apnimed
nav: Providers
network: true
overview: 'Apnimed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Healthcare, and Life Sciences.


  Apnimed''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/apnimed/refs/heads/main/screenshots/apnimed-2026-08-07T161455.png
security:
- kind: domain-security
  name: Apnimed Domain Security
  slug: apnimed-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apnimed
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Healthcare
- Life Sciences
- Sleep Medicine
- Clinical Trials
website: https://apnimed.com/
---
