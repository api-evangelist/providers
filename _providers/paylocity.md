---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Paylocity Agentic Access
  operation_count: 29
  slug: paylocity-agentic-access
  summary_line: 29 operations · 13 acting
api_count: 1
apis:
- description: REST API for managing employees, demographics, status, pay rates, direct deposit, deductions, earnings, taxes, custom fields, company codes, and onboarding via the Paylocity Integrations platform. Aut
  name: Paylocity Integrations REST API
  slug: rest-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The Background Check API from Paylocity — 2 operation(s) for background check.
  name: Paylocity Background Check API
  slug: paylocity-background-check-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The Company API from Paylocity — 2 operation(s) for company.
  name: Paylocity Company API
  slug: paylocity-company-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The Deductions API from Paylocity — 1 operation(s) for deductions.
  name: Paylocity Deductions API
  slug: paylocity-deductions-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The Earnings API from Paylocity — 2 operation(s) for earnings.
  name: Paylocity Earnings API
  slug: paylocity-earnings-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The Employees API from Paylocity — 3 operation(s) for employees.
  name: Paylocity Employees API
  slug: paylocity-employees-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The LMS API from Paylocity — 1 operation(s) for lms.
  name: Paylocity LMS API
  slug: paylocity-lms-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The Payroll API from Paylocity — 3 operation(s) for payroll.
  name: Paylocity Payroll API
  slug: paylocity-payroll-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The Scheduling API from Paylocity — 3 operation(s) for scheduling.
  name: Paylocity Scheduling API
  slug: paylocity-scheduling-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The Taxes API from Paylocity — 2 operation(s) for taxes.
  name: Paylocity Taxes API
  slug: paylocity-taxes-api
- baseURL: https://api.paylocity.com/api
  baseurl_source: declared
  description: The Time API from Paylocity — 2 operation(s) for time.
  name: Paylocity Time API
  slug: paylocity-time-api
artifact_total: 29
collections:
- collection_type: open
  name: Paylocity Integrations REST Background Check API
  slug: open-paylocity-background-check-api
- collection_type: open
  name: Paylocity Integrations REST Background Check Company API
  slug: open-paylocity-company-api
- collection_type: open
  name: Paylocity Integrations REST Background Check Deductions API
  slug: open-paylocity-deductions-api
- collection_type: open
  name: Paylocity Integrations REST Background Check Earnings API
  slug: open-paylocity-earnings-api
- collection_type: open
  name: Paylocity Integrations REST Background Check Employees API
  slug: open-paylocity-employees-api
- collection_type: open
  name: Paylocity Integrations REST Background Check LMS API
  slug: open-paylocity-lms-api
- collection_type: open
  name: Paylocity Integrations REST Background Check Payroll API
  slug: open-paylocity-payroll-api
- collection_type: open
  name: Paylocity Integrations REST Background Check Scheduling API
  slug: open-paylocity-scheduling-api
- collection_type: open
  name: Paylocity Integrations REST Background Check Taxes API
  slug: open-paylocity-taxes-api
- collection_type: open
  name: Paylocity Integrations REST Background Check Time API
  slug: open-paylocity-time-api
- collection_type: open
  name: Paylocity Integrations REST API
  slug: open-paylocity
common:
- group: other
  href: https://artifacts.apis.io/paylocity/capabilities/paylocity-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/paylocity-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/paylocity/agentic-access/paylocity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paylocity-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/paylocity/security/paylocity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/paylocity-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/paylocity/security/paylocity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paylocity-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/paylocity/authentication/paylocity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paylocity-authentication.yml
- group: auth
  href: https://artifacts.apis.io/paylocity/scopes/paylocity-scopes.yml
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paylocity.png
layout: provider
mcp_servers:
- description: Remote MCP server at developer.paylocity.com over HTTP; 5 tools listed.
  name: Paylocity MCP Server
  slug: paylocity
modified: '2026-05-11'
name: Paylocity
nav: Providers
network: true
overview: 'Paylocity publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Background Check API, Company API, Deductions API, and 8 more. Tagged areas include Human Resources, Payroll, HCM, Benefits, and Workforce Management.


  The Paylocity catalog on APIs.io includes 1 Spectral governance ruleset.


  Paylocity''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 11 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Paylocity API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: paylocity-rules
scopes:
- name: Paylocity Scopes
  scope_count: 1
  slug: paylocity-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 6.6
    contract_governance: 13.6
    contract_quality: 42.9
    developer_ergonomics: 28.6
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/paylocity/paylocity-2026-06-20T191505.png
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
- Human Resources
- Payroll
- HCM
- Benefits
- Workforce Management
- Time Tracking
- Employee Benefits
website: https://www.paylocity.com
---
