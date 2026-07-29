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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Paylocity Agentic Access
  operation_count: 29
  slug: paylocity-agentic-access
  summary_line: 29 operations · 13 acting
api_count: 11
apis:
- description: REST API for managing employees, demographics, status, pay rates, direct deposit, deductions, earnings, taxes, custom fields, company codes, and onboarding via the Paylocity Integrations platform. Aut
  name: Paylocity Integrations REST API
  slug: rest-api
- description: The Background Check API from Paylocity — 2 operation(s) for background check.
  name: Paylocity Background Check API
  slug: paylocity-background-check-api
- description: The Company API from Paylocity — 2 operation(s) for company.
  name: Paylocity Company API
  slug: paylocity-company-api
- description: The Deductions API from Paylocity — 1 operation(s) for deductions.
  name: Paylocity Deductions API
  slug: paylocity-deductions-api
- description: The Earnings API from Paylocity — 2 operation(s) for earnings.
  name: Paylocity Earnings API
  slug: paylocity-earnings-api
- description: The Employees API from Paylocity — 3 operation(s) for employees.
  name: Paylocity Employees API
  slug: paylocity-employees-api
- description: The LMS API from Paylocity — 1 operation(s) for lms.
  name: Paylocity LMS API
  slug: paylocity-lms-api
- description: The Payroll API from Paylocity — 3 operation(s) for payroll.
  name: Paylocity Payroll API
  slug: paylocity-payroll-api
- description: The Scheduling API from Paylocity — 3 operation(s) for scheduling.
  name: Paylocity Scheduling API
  slug: paylocity-scheduling-api
- description: The Taxes API from Paylocity — 2 operation(s) for taxes.
  name: Paylocity Taxes API
  slug: paylocity-taxes-api
- description: The Time API from Paylocity — 2 operation(s) for time.
  name: Paylocity Time API
  slug: paylocity-time-api
artifact_total: 18
collections:
- collection_type: open
  name: Paylocity Integrations REST API
  slug: open-paylocity
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paylocity-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paylocity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paylocity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paylocity-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paylocity-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Paylocity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paylocity
- group: company
  title: ''
  type: Website
  url: https://www.paylocity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.paylocity.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.paylocity.com/integrations/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.paylocity.com/integrations/reference/api-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paylocity.com/our-products/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.paylocity.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://access.paylocity.com/
- group: operate
  title: ''
  type: Support
  url: https://www.paylocity.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.paylocity.com/resources/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.paylocity.com/llms.txt
created: '2026-05-11'
description: Paylocity is a cloud-based human capital management (HCM) and payroll software provider serving small and mid-sized US employers with payroll, benefits administration, talent management, time and labor tracking, and workforce analytics. The platform powers HR back-office operations along with employee self-service tools. The Paylocity API uses OAuth 2.0 client credentials over api.paylocity.com to expose employee, payroll, deduction, earning, and onboarding data for partner integrations and customer automations.
graphqls:
- description: Paylocity is a cloud HR and payroll platform. The API covers employee records, payroll processing, time and attendance, benefits administration, expense management, performance reviews, and compliance
  name: Paylocity GraphQL API
  slug: paylocity-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paylocity.png
layout: provider
modified: '2026-05-11'
name: Paylocity
nav: Providers
network: true
overview: 'Paylocity publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Background Check API, Company API, Deductions API, and 7 more. Tagged areas include HR, Payroll, HCM, Benefits, and Workforce Management.


  Paylocity''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 10 more developer resources.'
random_paper: 66
scopes:
- name: Paylocity Scopes
  scope_count: 1
  slug: paylocity-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 36.1
  delta: -0.4
  facets:
    commercial_clarity: 23.7
    contract_quality: 59.9
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paylocity/refs/heads/main/screenshots/paylocity-2026-06-20T191505.png
security:
- kind: authentication
  name: Paylocity Authentication
  slug: paylocity-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Paylocity Domain Security
  slug: paylocity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Paylocity Vulnerability Disclosure
  slug: paylocity-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: paylocity
tags:
- HR
- Payroll
- HCM
- Benefits
- Workforce Management
- Time Tracking
website: https://www.paylocity.com
---
