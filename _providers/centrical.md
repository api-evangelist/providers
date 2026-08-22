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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 5
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
- group: auth
  title: ''
  type: TrustCenter
  url: security/centrical-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://centrical.statuspage.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/centrical-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/centrical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/centrical-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/centrical-llms.txt
coverage:
  checked: '2026-08-10'
  detail: 'Centrical runs a real production API — api.centrical.me is a live AWS API Gateway custom domain that rejects every anonymous request with its own ForbiddenException, and Centrical''s status page lists a "Core Api" component in all three regions plus a "Management API" — but not one byte of it is documented publicly: the integration reference sits inside the Zendesk help center, whose anonymous Help Center API returns 401 and whose web UI returns 403, and centrical.com''s 197-page sitemap contains no developer, API or docs page at all.'
  evidence:
  - status: 403
    url: https://api.centrical.me/openapi.json
  - status: 401
    url: https://support.centrical.com/api/v2/help_center/en-us/articles.json
  - status: 403
    url: https://support.centrical.com/hc/en-us
  - status: 404
    url: https://centrical.com/openapi.json
  - status: 200
    url: https://centrical.statuspage.io/api/v2/summary.json
  reason: customer-only-docs
  state: gated
created: '2026-08-09'
description: 'Centrical (legally Biz-Effective Ltd., founded in Israel in 2013 and known as GamEffective until its 2019 rebrand) sells a performance-experience platform for frontline and contact-center employees. The product combines advanced gamification, personalized microlearning, real-time performance management, AI-assisted coaching, quality management and voice-of-the-employee surveys into a single agent-facing experience, and is used by Microsoft, Verizon Cellular Sales, Teleperformance, Hilton and Synchrony among others. Centrical is integration-heavy rather than developer-facing: it ingests KPI and activity data from CRM, POS, telephony, WFM, VoC and contact-center systems (including a packaged Amazon Connect / Contact Lens integration, a Salesforce AppExchange listing and a Microsoft Teams app) over API, SFTP and email. That data and integration API is documented for contracted customers only — Centrical publishes no public developer portal, API reference, or machine-readable contract.
  The API itself is demonstrably real and entirely gated: api.centrical.me is a live AWS API Gateway host that rejects anonymous callers, and Centrical''s public status page lists a "Core Api" component in its North America, Europe and APAC regions alongside a "Management API".'
image: https://centrical.com/wp-content/themes/centrical-master/assets/img/favicon/apple-touch-icon.png
layout: provider
modified: '2026-08-10'
name: Centrical
nav: Providers
network: true
overview: 'Centrical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Engagement, Performance Management, Gamification, and Microlearning.


  Centrical''s developer surface includes support, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Centrical Plans Pricing
  plan_count: 1
  slug: centrical-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Centrical Rate Limits
  slug: centrical-rate-limits
score:
  band: thin
  composite: 27.1
  delta: -0.5
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 27.6
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Centrical Authentication
  slug: centrical-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Centrical Domain Security
  slug: centrical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Centrical Trust Center
  slug: centrical-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701, SOC 2 Type II, Cloud Security Alliance STAR Registry, EU General Data Protection Regulation, California Consumer Privacy Act
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
