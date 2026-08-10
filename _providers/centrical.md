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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centrical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centrical.com/
- group: operate
  title: ''
  type: Support
  url: https://support.centrical.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://centrical.com/resources/?_cat=blog
- group: commercial
  title: ''
  type: Pricing
  url: https://centrical.com/get-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://centrical.com/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centrical.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centrical.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gameffective
- group: design
  title: ''
  type: Conformance
  url: conformance/centrical-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/centrical-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/centrical-llms.txt
coverage:
  checked: '2026-08-09'
  detail: Centrical's integration/API reference lives only inside its Zendesk help center — the anonymous Help Center API returns 401 "Couldn't authenticate you", so the articles require an active customer sign-in, and centrical.com's 197-page sitemap contains no developer, API or docs page at all.
  evidence:
  - status: 401
    url: https://support.centrical.com/api/v2/help_center/en-us/articles.json
  - status: 404
    url: https://centrical.com/openapi.json
  - status: 404
    url: https://centrical.com/.well-known/agent-card.json
  - status: 200
    url: https://centrical.com/customer-resources/
  reason: customer-only-docs
  state: gated
created: '2026-08-09'
description: 'Centrical (legally Biz-Effective Ltd., founded in Israel in 2013 and known as GamEffective until its 2019 rebrand) sells a performance-experience platform for frontline and contact-center employees. The product combines advanced gamification, personalized microlearning, real-time performance management, AI-assisted coaching, quality management and voice-of-the-employee surveys into a single agent-facing experience, and is used by Microsoft, Verizon Cellular Sales, Teleperformance, Hilton and Synchrony among others. Centrical is integration-heavy rather than developer-facing: it ingests KPI and activity data from CRM, POS, telephony, WFM, VoC and contact-center systems (including a packaged Amazon Connect / Contact Lens integration, a Salesforce AppExchange listing and a Microsoft Teams app) over API, SFTP and email. That data and integration API is documented for contracted customers only — Centrical publishes no public developer portal, API reference, or machine-readable contract.'
image: https://centrical.com/wp-content/themes/centrical-master/assets/img/favicon/apple-touch-icon.png
layout: provider
modified: '2026-08-09'
name: Centrical
nav: Providers
network: true
overview: 'Centrical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Engagement, Performance Management, Gamification, and Microlearning.


  Centrical''s developer surface includes support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 20.9
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 5.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: domain-security
  name: Centrical Domain Security
  slug: centrical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: centrical
tags:
- Company
- Employee Engagement
- Performance Management
- Gamification
- Microlearning
- Contact Center
- Workforce Engagement Management
- Coaching
- Quality Management
- Human Resources
- SaaS
website: https://centrical.com/
---
