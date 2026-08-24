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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Abacus Agentic Access
  operation_count: 8
  slug: abacus-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 3
apis:
- description: OAuth 2.0 authentication operations
  name: Abacus Authentication API
  slug: abacus-authentication-api
- description: Expense report management and operations
  name: Abacus Expenses API
  slug: abacus-expenses-api
- description: Member management operations for inviting and managing expense users
  name: Abacus Members API
  slug: abacus-members-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Abacus Authentication API
  slug: open-abacus-authentication-api
- collection_type: open
  name: Abacus Authentication Expenses API
  slug: open-abacus-expenses-api
- collection_type: open
  name: Abacus Authentication Members API
  slug: open-abacus-members-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/abacus-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/abacus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abacus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abacus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/abacus-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.abacus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.abacus.com/hc/en-us/articles/12493681200269-Abacus-API
- group: operate
  title: ''
  type: Support
  url: https://support.abacus.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.emburse.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.emburse.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/rules/abacus-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/vocabulary/abacus-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/json-ld/abacus-api-context.jsonld
created: '2024-01-15'
description: Abacus (now part of Emburse Spend) is an expense management platform that allows businesses to streamline expense reporting, receipts, and reimbursements. The Abacus API is available to partners and enterprise customers, providing programmatic access to member management and expense operations using OAuth 2.0 authentication.
examples:
- key_count: 11
  name: Abacus Expense Example
  slug: abacus-expense-example
- key_count: 4
  name: Abacus Expense List Response Example
  slug: abacus-expense-list-response-example
- key_count: 5
  name: Abacus Invite Member Request Example
  slug: abacus-invite-member-request-example
- key_count: 8
  name: Abacus Member Example
  slug: abacus-member-example
- key_count: 4
  name: Abacus Member List Response Example
  slug: abacus-member-list-response-example
- key_count: 3
  name: Abacus Oauth Token Request Example
  slug: abacus-oauth-token-request-example
- key_count: 3
  name: Abacus Oauth Token Response Example
  slug: abacus-oauth-token-response-example
- key_count: 3
  name: Abacus Update Member Request Example
  slug: abacus-update-member-request-example
features:
- description: Invite, update, and suspend organization members programmatically
  name: Member Management
- description: Retrieve and filter expense reports by status, member, and date range
  name: Expense Tracking
- description: Secure API access using client credentials grant flow
  name: OAuth 2.0 Authentication
- description: Link receipts to expense reports via URL references
  name: Receipt Management
- description: Categorize expenses across meals, travel, lodging, office supplies, and software
  name: Multi-category Expenses
- description: Paginated API responses with configurable page sizes
  name: Paginated Results
finops:
- name: Abacus Finops
  service_category: API
  slug: abacus-finops
image: /assets/icons/abacus.png
integrations:
- description: Sync expense data with QuickBooks for accounting reconciliation
  name: QuickBooks
- description: Integrate with Xero for automated expense accounting
  name: Xero
- description: Connect expense reports with NetSuite ERP
  name: NetSuite
- description: Sync expenses with Sage Intacct for financial management
  name: Sage Intacct
json_schemas:
- name: ExpenseListResponse
  property_count: 4
  slug: abacus-expense-list-response
- name: Expense
  property_count: 11
  slug: abacus-expense
- name: InviteMemberRequest
  property_count: 5
  slug: abacus-invite-member-request
- name: MemberListResponse
  property_count: 4
  slug: abacus-member-list-response
- name: Member
  property_count: 8
  slug: abacus-member
- name: OAuthTokenRequest
  property_count: 3
  slug: abacus-oauth-token-request
- name: OAuthTokenResponse
  property_count: 3
  slug: abacus-oauth-token-response
- name: UpdateMemberRequest
  property_count: 3
  slug: abacus-update-member-request
json_structures:
- name: Abacus Expense List Response Structure
  property_count: 4
  slug: abacus-expense-list-response-structure
- name: Abacus Expense Structure
  property_count: 11
  slug: abacus-expense-structure
- name: Abacus Invite Member Request Structure
  property_count: 5
  slug: abacus-invite-member-request-structure
- name: Abacus Member List Response Structure
  property_count: 4
  slug: abacus-member-list-response-structure
- name: Abacus Member Structure
  property_count: 8
  slug: abacus-member-structure
- name: Abacus Oauth Token Request Structure
  property_count: 3
  slug: abacus-oauth-token-request-structure
- name: Abacus Oauth Token Response Structure
  property_count: 3
  slug: abacus-oauth-token-response-structure
- name: Abacus Update Member Request Structure
  property_count: 3
  slug: abacus-update-member-request-structure
jsonld:
- class_count: 8
  name: Abacus Api Context
  property_count: 27
  slug: abacus-api-context
layout: provider
modified: '2026-05-19'
name: Abacus
nav: Providers
network: true
overview: 'Abacus publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Expenses API, and Members API. Tagged areas include Accounting, Expense Management, Finance, and Reimbursement.


  The Abacus catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Abacus'' developer surface includes authentication, documentation, support, and 10 more developer resources.'
plans:
- name: Abacus Plans Pricing
  plan_count: 3
  slug: abacus-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Abacus Rate Limits
  slug: abacus-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Abacus API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: abacus-jsonschema-spectral-rules
- effective_rule_count: 87
  extends:
  - spectral:oas
  name: Abacus API Rules
  rule_count: 46
  severity_counts:
    error: 13
    hint: 0
    info: 7
    warn: 26
  slug: abacus-spectral-rules
scopes:
- name: Abacus Scopes
  scope_count: 3
  slug: abacus-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 27.7
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 28.8
    contract_quality: 29.9
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abacus/refs/heads/main/screenshots/abacus-2026-06-20T163056.png
security:
- kind: authentication
  name: Abacus Authentication
  slug: abacus-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Abacus Domain Security
  slug: abacus-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Abacus Vulnerability Disclosure
  slug: abacus-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: abacus
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
use_cases:
- description: Automatically invite new employees to the expense platform via API
  name: Employee Onboarding
- description: Programmatically suspend departed employees from expense access
  name: Employee Offboarding
- description: Retrieve and reconcile expense reports for accounting integration
  name: Expense Reconciliation
- description: Pull expense data by category, member, or date range for reporting
  name: Spend Analytics
- description: Connect Abacus expense data with ERP and accounting systems
  name: Third-party Integration
website: https://www.abacus.com/
---
