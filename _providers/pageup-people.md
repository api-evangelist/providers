---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: REST API suite for the PageUp talent management platform, secured with OAuth 2.0 client-credentials. Covers Core HR, Recruitment, Partner, Performance, and Platform (Exports) endpoint groups. Per-tena
  name: PageUp Talent Management API
  slug: pageup-talent-management-api
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.pageuppeople.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pageuppeople.com/Content/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.pageuppeople.com/Api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.pageuppeople.com/Content/getting-started
- group: company
  title: ''
  type: Blog
  url: https://medium.com/pageup-tech
- group: company
  title: ''
  type: Website
  url: https://www.pageuppeople.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pageuppeople.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.pageuppeople.com/request-a-demo/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pageuppeople.com/request-a-demo/
- group: other
  title: ''
  type: Marketplace
  url: https://www.pageuppeople.com/marketplace/
- group: auth
  title: ''
  type: Authentication
  url: authentication/pageup-people-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pageup-people-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pageup-people-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pageup-people-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pageup-people-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pageuppeople.com/responsible-disclosure/
- group: design
  title: ''
  type: Conformance
  url: conformance/pageup-people-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.pageuppeople.com/how-we-do-it/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/pageup-people-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pageup-people-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pageup-people-llms.txt
created: '2026-07-17'
description: PageUp is an enterprise talent management and talent acquisition software provider headquartered in Melbourne, Australia, serving large organizations across government, healthcare, higher education, retail, and other sectors. The PageUp platform spans recruitment marketing, applicant tracking (ATS), onboarding, performance and development, learning, succession, and workforce analytics. PageUp exposes a REST API suite for clients and integration partners covering Core HR (employees, positions, business units, cost centres, agreements, pay scales, roles, sites, teams), Recruitment (applicants, applications, documents, hire), Partner endpoints (learning activities, SCORM content, assessment, background checking, work compliance), Performance (review reports), and Platform functions (data exports). The API is secured with OAuth 2.0 client-credentials, is documented at developers.pageuppeople.com with a Postman workspace and API release logs, and provisions a UAT sandbox environment;
  per-tenant API domains are provisioned by PageUp for each client.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pageup-people.png
layout: provider
modified: '2026-07-20'
name: PageUp People
nav: Providers
network: true
overview: 'PageUp People publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Talent Management, Talent Acquisition, Human Resources, and Recruiting.


  PageUp People''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, authentication, and 14 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 32.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 32.4
  provenance:
    conformance: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Pageup People Authentication
  slug: pageup-people-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pageup People Domain Security
  slug: pageup-people-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pageup People Vulnerability Disclosure
  slug: pageup-people-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Pageup People Trust Center
  slug: pageup-people-trust-center
  summary_line: ISO/IEC 27001:2022, Texas RAMP
slug: pageup-people
tags:
- Company
- Talent Management
- Talent Acquisition
- Human Resources
- Recruiting
- Applicant Tracking
- Onboarding
- Learning
- HR Technology
- SaaS
website: https://www.pageuppeople.com/
---
