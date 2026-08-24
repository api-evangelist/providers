---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
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
score:
  band: emerging
  composite: 16.1
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
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
