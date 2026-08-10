---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Truv Agentic Access
  operation_count: 68
  slug: truv-agentic-access
  summary_line: 68 operations · 25 acting
api_count: 20
apis:
- description: Administrative access key management.
  name: Truv Admin API
  slug: truv-admin-api
- description: Verification-of-assets banking data for a connected link.
  name: Truv Banking API
  slug: truv-banking-api
- description: Mint tokens that initialize the Truv Bridge widget and connect flows.
  name: Truv Bridge Tokens API
  slug: truv-bridge-tokens-api
- description: Employer companies, mappings, and data providers.
  name: Truv Companies & Providers API
  slug: truv-companies-providers-api
- description: Direct deposit and deposit switch reports.
  name: Truv Direct Deposit API
  slug: truv-direct-deposit-api
- description: Verification of employment data and reports.
  name: Truv Employment API
  slug: truv-employment-api
- description: Consumer identity data for a connected link.
  name: Truv Identity API
  slug: truv-identity-api
- description: Income reports, transactions, and income insights.
  name: Truv Income API
  slug: truv-income-api
- description: Insurance reports including auto and home.
  name: Truv Insurance API
  slug: truv-insurance-api
- description: Manage connections between a consumer and a payroll or financial data source.
  name: Truv Links API
  slug: truv-links-api
- description: Verification orders and their lifecycle.
  name: Truv Orders API
  slug: truv-orders-api
- description: Individual pay statement documents.
  name: Truv Pay Statements API
  slug: truv-pay-statements-api
- description: Shift-level payroll data.
  name: Truv Payroll & Shifts API
  slug: truv-payroll-shifts-api
- description: Pre-qualification lending logic reports.
  name: Truv PLL API
  slug: truv-pll-api
- description: Scoring attribute reports.
  name: Truv Scoring API
  slug: truv-scoring-api
- description: Asynchronous task tracking.
  name: Truv Tasks API
  slug: truv-tasks-api
- description: Tax document data for a connected link.
  name: Truv Tax API
  slug: truv-tax-api
- description: Reusable configuration templates.
  name: Truv Templates API
  slug: truv-templates-api
- description: Manage the end users (consumers) whose data is connected through Truv.
  name: Truv Users API
  slug: truv-users-api
- description: Webhook endpoint registration and delivery history.
  name: Truv Webhooks API
  slug: truv-webhooks-api
artifact_total: 29
collections:
- collection_type: open
  name: Truv API
  slug: open-truv
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truv-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/truv-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/truv-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truv-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truvhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truvhq
- group: company
  title: ''
  type: Website
  url: https://truv.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.truv.com
- group: commercial
  title: ''
  type: Plans
  url: plans/truv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truv-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/truv-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://truv.com/blog/
created: '2026-07-01'
description: Truv provides consumer-permissioned access to payroll, income, and employment data. Its platform lets applicants connect their payroll accounts to instantly verify income and employment, retrieve pay statements, and switch direct deposit, replacing manual document collection and legacy verification services across lending, background screening, and fintech workflows.
finops:
- name: Truv Finops
  service_category: Financial Data and Verification
  slug: truv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truv.png
layout: provider
modified: '2026-07-01'
name: Truv
nav: Providers
network: true
overview: 'Truv publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Banking API, Bridge Tokens API, and 17 more. Tagged areas include Income Verification, Employment Verification, Payroll, Direct Deposit, and Consumer Permissioned Data.


  Truv''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Truv Plans Pricing
  plan_count: 3
  slug: truv-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Truv Rate Limits
  slug: truv-rate-limits
score:
  band: thin
  composite: 40.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Truv Authentication
  slug: truv-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Truv Domain Security
  slug: truv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Truv Vulnerability Disclosure
  slug: truv-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Truv Trust Center
  slug: truv-trust-center
  summary_line: SOC 2, GDPR
slug: truv
tags:
- Income Verification
- Employment Verification
- Payroll
- Direct Deposit
- Consumer Permissioned Data
- Fintech
website: https://truv.com
---
