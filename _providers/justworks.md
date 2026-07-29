---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Justworks Agentic Access
  operation_count: 27
  slug: justworks-agentic-access
  summary_line: 27 operations · 9 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: Read employee, contractor, and member information from the Justworks Partner API. Provides access to member profiles, employment history, pay history, custom-field values, and U.S. tax identifiers (SS
  name: Justworks Members API
  slug: justworks-members-api
- description: Read company-level data from the Justworks Partner API including company identity, departments, offices, bank account on file (masked), verified business information, custom-field definitions, and the
  name: Justworks Company API
  slug: justworks-company-api
- description: Manage employee deductions — list deduction types, create one-time and recurring deductions, update existing deductions, and cancel deductions in bulk. The primary write surface of the Justworks Partn
  name: Justworks Deductions API
  slug: justworks-deductions-api
- description: 'Manage Justworks Partner API webhooks. Justworks signs every request, delivers events at-least-once with automatic retries, and closes a webhook on sustained failures (resumable via API). Event types '
  name: Justworks Webhooks API
  slug: justworks-webhooks-api
- description: OAuth 2.0 token endpoints for the Justworks Partner API. Authorization code is the only supported grant for initial token acquisition; refresh token grant is supported for renewal. Access tokens are v
  name: Justworks OAuth API
  slug: justworks-oauth-api
- description: Read access to Justworks deduction type catalog
  name: Justworks Deduction Types API
  slug: justworks-deduction-types-api
- description: Read access to payroll runs and per-payroll fees
  name: Justworks Payrolls API
  slug: justworks-payrolls-api
- description: Read access to per-member paystubs
  name: Justworks Paystubs API
  slug: justworks-paystubs-api
- description: Asynchronous balance reports for time-off policies
  name: Justworks Time Off Balances API
  slug: justworks-time-off-balances-api
- description: Read access to time-off policy catalog
  name: Justworks Time Off Policies API
  slug: justworks-time-off-policies-api
- description: Read access to time-off requests submitted by members
  name: Justworks Time Off Requests API
  slug: justworks-time-off-requests-api
artifact_total: 52
collections:
- collection_type: open
  name: Justworks Company API
  slug: open-justworks-company-api
- collection_type: open
  name: Justworks Deductions API
  slug: open-justworks-deductions-api
- collection_type: open
  name: Justworks Members API
  slug: open-justworks-members-api
- collection_type: open
  name: Justworks OAuth API
  slug: open-justworks-oauth-api
- collection_type: open
  name: Justworks Payroll API
  slug: open-justworks-payroll-api
- collection_type: open
  name: Justworks Time Off API
  slug: open-justworks-time-off-api
- collection_type: open
  name: Justworks Webhooks API
  slug: open-justworks-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/justworks-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/justworks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/justworks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/justworks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/justworks-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.justworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://public-api.justworks.com/v1/docs
- group: start
  title: ''
  type: Portal
  url: https://www.justworks.com/partners
- group: start
  title: ''
  type: GettingStarted
  url: https://public-api.justworks.com/v1/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.justworks.com/pricing
- group: other
  title: ''
  type: Products
  url: https://www.justworks.com/products
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.justworks.com/partners
- group: company
  title: ''
  type: PartnerBlog
  url: https://www.justworks.com/partners/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.justworks.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.justworks.com
- group: company
  title: ''
  type: Blog
  url: https://www.justworks.com/blog
- group: company
  title: ''
  type: Careers
  url: https://www.justworks.com/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/justworkshr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/justworks
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/JustworksHR
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Justworks
- group: commercial
  title: ''
  type: Plans
  url: plans/justworks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/justworks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/justworks-finops.yml
created: '2026-05-25'
description: 'Justworks is a New York City-based Professional Employer Organization (PEO) and small-business HR platform. It bundles payroll, tax filing, multi-state compliance, large-group medical/dental/vision benefits, 401(k) administration, workers comp, time tracking, and HR consulting into a single per-employee-per-month subscription. Justworks operates four primary products: Justworks Payroll (standalone payroll), Justworks PEO Basic, Justworks PEO Plus (PEO with included benefits package), and Justworks EOR International for hiring full-time employees abroad without a local entity. Justworks exposes a Partner API at public-api.justworks.com for approved integration partners, covering Members, Company, Payroll, Paystubs, Deductions, Time Off, and Webhooks. The API uses OAuth 2.0 authorization-code grant, cursor pagination, signed at-least-once webhooks, and zero-decimal currency representation. Deductions is the primary write surface; everything else is read-only.'
features:
- Justworks PEO Basic — co-employment PEO with payroll, HR support, and access to large-group benefits
- Justworks PEO Plus — PEO Basic plus medical, dental, vision, life, AD&D, disability, and 401(k) administration
- Justworks Payroll — standalone small-business payroll, time tracking, and HR tooling for companies that source their own benefits
- Justworks EOR International — employer-of-record service for hiring full-time employees abroad without a local entity
- Justworks Partner API at public-api.justworks.com with OAuth 2.0 authorization-code flow
- Members endpoints (list, get, custom field values, tax-id/SSN) with cursor pagination and updated_at filtering
- Company endpoints (identity, bank account, business info, custom fields, jurisdictions)
- Payroll endpoints (list runs by date range, list fees, list paystubs, get paystub with earnings + deductions + employer contributions)
- Deductions endpoints (list types, list, create, update, cancel) with per-row operation_id idempotency
- Time Off endpoints (asynchronous balance reports, policies, requests)
- Signed webhooks for member.profile.created/updated, member.employment_state.termination_scheduled/canceled, and department.created/updated/deleted
- Webhook simulator endpoint for partner-listener validation in the Tour environment
- 24-hour access tokens and 30-day refresh tokens
- Hierarchical OAuth scopes (e.g., member.detail:read implies member.basic:read implies member.dob/sex:read)
- Zero-decimal currency representation for all monetary fields
- Partner program with revenue share, co-marketing, dedicated relationship managers
- Integrations marketplace covering Greenhouse, Lever, JazzHR, CultureAmp, 15Five, QuickBooks, NetSuite, Xero, Sage Intacct, Brex, Ramp
- Available via aggregator platforms Finch, Merge, and Apideck for cross-HRIS access
finops:
- name: Justworks Finops
  service_category: Human Capital Management
  slug: justworks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/justworks.png
json_schemas:
- name: Justworks Deduction
  property_count: 10
  slug: justworks-deduction
- name: Justworks Member
  property_count: 27
  slug: justworks-member
- name: Justworks Payroll
  property_count: 10
  slug: justworks-payroll
- name: Justworks Paystub
  property_count: 12
  slug: justworks-paystub
- name: Justworks Time Off Request
  property_count: 11
  slug: justworks-time-off-request
- name: Justworks Webhook Event
  property_count: 5
  slug: justworks-webhook-event
jsonld:
- class_count: 0
  name: Justworks Context
  property_count: 8
  slug: justworks-context
layout: provider
modified: '2026-05-25'
name: Justworks
nav: Providers
network: true
overview: 'Justworks publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Members API, Company API, Deductions API, and 8 more. Tagged areas include PEO, Payroll, HR, Human Resources, and Benefits.


  The Justworks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Justworks'' developer surface includes authentication, documentation, developer portal, getting-started guide, pricing, engineering blog, YouTube channel, and 17 more developer resources.'
plans:
- name: Justworks Plans Pricing
  plan_count: 5
  slug: justworks-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 2
  name: Justworks Rate Limits
  slug: justworks-rate-limits
rules:
- name: Justworks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: justworks-jsonschema-spectral-rules
scopes:
- name: Justworks Scopes
  scope_count: 15
  slug: justworks-scopes
  summary_line: 15 scopes · authorizationCode
score:
  band: strong
  composite: 57.4
  delta: -1.9
  facets:
    commercial_clarity: 57.9
    contract_quality: 71.5
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 68.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/justworks/refs/heads/main/screenshots/justworks-2026-06-20T183846.png
security:
- kind: authentication
  name: Justworks Authentication
  slug: justworks-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Justworks Domain Security
  slug: justworks-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Justworks Vulnerability Disclosure
  slug: justworks-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: justworks
tags:
- PEO
- Payroll
- HR
- Human Resources
- Benefits
- Health Insurance
- 401(k)
- Time Off
- Compliance
- Small Business
- Employer of Record
- HRIS
website: https://www.justworks.com
---
