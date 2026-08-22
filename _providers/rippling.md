---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Rippling Agentic Access
  operation_count: 29
  slug: rippling-agentic-access
  summary_line: 29 operations · 10 acting
api_count: 22
apis:
- description: The Rippling Platform API exposes core HRIS resources — companies, employees, departments, work locations, custom fields, employment types, and compensation history — for partners building HR-data int
  name: Rippling Platform API
  slug: rippling-platform-api
- description: Read and write employee records — personal information, employment details, manager hierarchy, work email, work location, and custom employee fields — for active and terminated workers.
  name: Rippling Employees API
  slug: rippling-employees-api
- description: Retrieve company-level metadata, legal entities, business addresses, and account-wide configuration scoped to the authenticated tenant.
  name: Rippling Companies API
  slug: rippling-companies-api
- description: List and manage departments and the hierarchical org structure used to group employees and route approvals.
  name: Rippling Departments API
  slug: rippling-departments-api
- description: Manage cross-functional teams that group employees independently of the department hierarchy.
  name: Rippling Teams API
  slug: rippling-teams-api
- description: Read and manage company work locations including office addresses and remote-work designations referenced by employee records.
  name: Rippling Work Locations API
  slug: rippling-work-locations-api
- description: Push earnings, deductions, and reimbursements into Rippling Payroll for off-cycle and on-cycle pay runs, and read pay-history events.
  name: Rippling Payroll API
  slug: rippling-payroll-api
- description: Submit and manage time-off requests, leave balances, and policies for vacation, sick leave, and other absence categories.
  name: Rippling Time Off API
  slug: rippling-time-off-api
- description: Capture clock-in / clock-out events, hourly timesheets, breaks, and shift schedules for hourly and shift-based workers.
  name: Rippling Time Tracking API
  slug: rippling-time-tracking-api
- description: Retrieve employee benefits enrollments, dependents, and plan details across health, dental, vision, and other insurance lines.
  name: Rippling Benefits API
  slug: rippling-benefits-api
- description: Submit and approve employee expense reports, attach receipts, and reimburse approved expenses through Rippling Spend.
  name: Rippling Expenses API
  slug: rippling-expenses-api
- description: Issue, manage, and reconcile corporate cards, spend limits, and transactions for Rippling Spend customers.
  name: Rippling Corporate Cards API
  slug: rippling-corporate-cards-api
- description: Manage vendor invoices, approvals, and payments through Rippling Bill Pay for accounts-payable workflows.
  name: Rippling Bill Pay API
  slug: rippling-bill-pay-api
- description: Sync candidates, applications, and offers between external ATS platforms and Rippling's recruiting and onboarding flows.
  name: Rippling Recruiting API
  slug: rippling-recruiting-api
- description: Trigger new-hire onboarding, capture personal details, distribute offer letters and policy documents, and provision day-one access.
  name: Rippling Onboarding API
  slug: rippling-onboarding-api
- description: Manage company-owned devices, MDM enrollment, ownership assignment, and lifecycle status across macOS, Windows, iOS, and Android.
  name: Rippling Devices API
  slug: rippling-devices-api
- description: Manage SaaS app provisioning, role assignment, and de-provisioning across the Rippling Apps catalog for IT teams.
  name: Rippling Apps API
  slug: rippling-apps-api
- description: SCIM 2.0 endpoints for inbound user, group, and role provisioning from identity providers (Okta, Azure AD, Google) and outbound to partner SaaS applications.
  name: Rippling SCIM API
  slug: rippling-scim-api
- description: Configure SAML/OIDC single sign-on between Rippling as an IdP and external service providers, plus SP integrations into Rippling.
  name: Rippling SSO API
  slug: rippling-sso-api
- description: Define and read custom fields attached to employees, departments, and other Rippling resources for tenant-specific metadata.
  name: Rippling Custom Fields API
  slug: rippling-custom-fields-api
- description: Subscribe to Rippling events (employee created/updated/terminated, time-off approved, payroll finalized, device assigned) for near real-time downstream integration.
  name: Rippling Webhooks API
  slug: rippling-webhooks-api
- description: The Platform API from Rippling — 24 operation(s) for platform.
  name: Rippling Platform API
  slug: rippling-platform-api
artifact_total: 43
asyncapis:
- description: 'Rippling Partner Applications listed in the Rippling App Shop can register a webhook URL to receive event-triggered notifications when relevant changes occur in a customer''s Rippling tenant. Rippling '
  name: Rippling Partner Webhooks
  slug: rippling-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rippling API (Base API) Platform API
  slug: open-rippling-platform-api
- collection_type: open
  name: Rippling Platform API (Base API)
  slug: open-rippling
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rippling-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rippling-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rippling-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rippling
- group: company
  title: ''
  type: Website
  url: https://www.rippling.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.rippling.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.rippling.com/docs/rippling-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rippling.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.rippling.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rippling.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rippling.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.rippling.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rippling
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rippling.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rippling.com/terms
- group: commercial
  title: ''
  type: Plans
  url: plans/rippling-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rippling-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rippling-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.rippling.com/llms.txt
created: '2026-05-08'
description: Rippling is a unified workforce platform spanning HR, IT, and Finance with programmable APIs for employees, payroll, devices, apps, time tracking, benefits, expenses, and SCIM identity provisioning.
features:
- Unified HR, IT, and Finance platform with composable products
- Per-employee-per-month pricing across all modules (custom-quoted)
- Platform API for HRIS data partners
- SCIM 2.0 inbound and outbound for IdP and SaaS provisioning
- Devices and MDM across macOS, Windows, iOS, Android
- Apps catalog for SaaS provisioning and de-provisioning
- Webhooks for HRIS, payroll, time-off, and device events
- OAuth2 Marketplace apps for partner integrations
- SAML / OIDC SSO as IdP and SP
finops:
- name: Rippling Finops
  service_category: HR
  slug: rippling-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Rippling unified workforce platform. Rippling provides REST APIs across HR, IT, and Finance domains. The GraphQL schema presented here model
  name: Rippling GraphQL Schema
  slug: rippling-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rippling.png
layout: provider
modified: '2026-05-30'
name: Rippling
nav: Providers
network: true
overview: 'Rippling publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Platform API, Webhooks API, and 1 more. Tagged areas include HR, HCM, Payroll, IT, and Identity.


  The Rippling catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Rippling''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, and 13 more developer resources.'
plans:
- name: Rippling Plans Pricing
  plan_count: 8
  slug: rippling-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Rippling Rate Limits
  slug: rippling-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Rippling API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: rippling-asyncapi-spectral-rules
score:
  band: thin
  composite: 35.9
  delta: -14.4
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 11.4
    contract_quality: 68.2
    developer_ergonomics: 14.3
    discoverability: 46.3
    governance: 11.4
    operational_transparency: 26.3
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rippling/refs/heads/main/screenshots/rippling-2026-06-20T193125.png
security:
- kind: authentication
  name: Rippling Authentication
  slug: rippling-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rippling Domain Security
  slug: rippling-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rippling
tags:
- HR
- HCM
- Payroll
- IT
- Identity
- SCIM
- Devices
- Spend Management
website: https://www.rippling.com/
---
