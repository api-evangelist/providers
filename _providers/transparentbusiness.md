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
  url: security/transparentbusiness-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transparentbusiness-llms.txt
- group: company
  title: ''
  type: Website
  url: https://transparentbusiness.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://transparentbusiness.com/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://transparentbusiness.com/blog.html
- group: start
  title: ''
  type: SignUp
  url: https://transparentbusiness.com/signup
- group: start
  title: ''
  type: Login
  url: https://transparentbusiness.com/signin
- group: operate
  title: ''
  type: HelpCenter
  url: https://transparentbussiness.zendesk.com/hc/en-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transparentbusiness.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transparentbusiness.com/privacy.html
- group: operate
  title: ''
  type: ContactUs
  url: https://transparentbusiness.com/contact.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transparentbusiness
coverage:
  checked: '2026-08-05'
  detail: 'TransparentBusiness ships a hosted timer/timesheet product and nothing else: its own 54-article Zendesk knowledge base returns zero hits for "API", "webhook" and "SDK" against a working control (33 hits for "time"), its site navigation carries no developer or integrations link, and every archived /api* URL was captured as a 404.'
  evidence:
  - status: 200
    url: https://transparentbussiness.zendesk.com/api/v2/help_center/articles/search.json?query=API
  - status: 200
    url: https://transparentbussiness.zendesk.com/api/v2/help_center/en-us/articles.json
  - status: 403
    url: https://www.transparentbusiness.com/llms.txt
  - status: 403
    url: https://www.transparentbusiness.com/openapi.json
  - status: 404
    url: https://transparentbusiness.com/api/
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'TransparentBusiness is a New York based SaaS company, founded in 2012 by Alex Konanykhin and Silvina Moschini, that sells a cloud platform for managing and monitoring remote workforces: a desktop timer, screenshot-based activity verification, timesheets, task assignment, and real-time project cost and progress reporting for distributed teams and contractors. The company also operates the SheWorks! and Yandiki talent marketplaces and the CloudWorking Academy training platform, and was later renamed Unicoin, Inc. The product is delivered as a hosted web application plus downloadable desktop timer clients; the company publishes no public developer program, API reference, SDK, or machine-readable specification.'
image: https://transparentbusiness.com/img/index-slide-bg-1.jpg
layout: provider
modified: '2026-08-05'
name: TransparentBusiness
nav: Providers
network: true
overview: 'TransparentBusiness is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Remote Work, Workforce Management, Time Tracking, and Productivity.


  TransparentBusiness'' developer surface includes pricing, engineering blog, signup flow, and 9 more developer resources.'
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/transparentbusiness/refs/heads/main/screenshots/transparentbusiness-2026-09-02T164133.png
security:
- kind: domain-security
  name: Transparentbusiness Domain Security
  slug: transparentbusiness-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: transparentbusiness
tags:
- Company
- Remote Work
- Workforce Management
- Time Tracking
- Productivity
- Project Management
- Human Resources
- Software-as-a-Service
website: https://transparentbusiness.com/
---
