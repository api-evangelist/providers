---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Synchrony Financial Agentic Access
  operation_count: 9
  slug: synchrony-financial-agentic-access
  summary_line: 9 operations · 8 acting
api_count: 9
apis:
- description: The Synchrony Account Management API provides access to cardholder account information, enabling partners to retrieve account details, balance information, transaction history, and manage account serv
  name: Synchrony Account Management API
  slug: account-management
- description: Full credit card application submissions.
  name: Synchrony Financial Applications API
  slug: synchrony-financial-applications-api
- description: Retrieve application decisions.
  name: Synchrony Financial Decisions API
  slug: synchrony-financial-decisions-api
- description: Process customer account payments.
  name: Synchrony Financial Payments API
  slug: synchrony-financial-payments-api
- description: Soft-pull preapproval operations.
  name: Synchrony Financial Preapprovals API
  slug: synchrony-financial-preapprovals-api
- description: Place holds on credit for future purchase completions.
  name: Synchrony Financial Preauthorizations API
  slug: synchrony-financial-preauthorizations-api
- description: Authorize and capture purchase transactions.
  name: Synchrony Financial Purchases API
  slug: synchrony-financial-purchases-api
- description: Process refunds and credit adjustments.
  name: Synchrony Financial Refunds API
  slug: synchrony-financial-refunds-api
- description: Reverse and void transactions.
  name: Synchrony Financial Reversals API
  slug: synchrony-financial-reversals-api
artifact_total: 26
collections:
- collection_type: open
  name: Synchrony Financial Credit Authorization API
  slug: open-synchrony-financial-credit-authorization
- collection_type: open
  name: Synchrony Financial Quickscreen Apply API
  slug: open-synchrony-financial-quickscreen-apply
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/synchrony-financial-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/synchrony-financial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synchrony-financial-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synchrony-financial-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synchrony-financial
- group: company
  title: ''
  type: Website
  url: https://www.synchrony.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.syf.com/
- group: start
  title: ''
  type: PortalProducts
  url: https://developer.syf.com/our-products
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.syf.com/terms-of-use
- group: start
  title: ''
  type: Sandbox
  url: https://developer.syf.com/
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/synchrony-financial-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/synchrony-financial-vocabulary.yml
created: '2026-05-03'
description: Synchrony Financial is one of the nation's premier consumer financial services companies, providing a range of credit products through programs established with retailers, manufacturers, and merchants. Synchrony offers APIs enabling partners and retailers to integrate credit applications, authorizations, payments, loyalty, and account management into their digital commerce experiences.
examples:
- key_count: 2
  name: Synchrony Financial Credit Authorization Createpurchase Example
  slug: synchrony-financial-credit-authorization-createPurchase-example
- key_count: 2
  name: Synchrony Financial Quickscreen Apply Submitpreapproval Example
  slug: synchrony-financial-quickscreen-apply-submitPreapproval-example
finops:
- name: Synchrony Financial Finops
  service_category: Consumer Credit / Retail Finance
  slug: synchrony-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synchrony-financial.png
json_schemas:
- name: Credit Application
  property_count: 8
  slug: synchrony-financial-credit-application
- name: Transaction
  property_count: 11
  slug: synchrony-financial-transaction
json_structures:
- name: Synchrony Financial Transaction Structure
  property_count: 0
  slug: synchrony-financial-transaction-structure
jsonld:
- class_count: 24
  name: Synchrony Financial Context
  property_count: 2
  slug: synchrony-financial-context
layout: provider
modified: '2026-05-19'
name: Synchrony Financial
nav: Providers
network: true
overview: 'Synchrony Financial publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Decisions API, Payments API, and 5 more. Tagged areas include Financial Services, Credit, Payments, Consumer Finance, and Retail Finance.


  The Synchrony Financial catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Synchrony Financial''s developer surface includes authentication, sandbox, and 10 more developer resources.'
plans:
- name: Synchrony Financial Plans Pricing
  plan_count: 1
  slug: synchrony-financial-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 1
  name: Synchrony Financial Rate Limits
  slug: synchrony-financial-rate-limits
rules:
- name: Synchrony Financial API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: synchrony-financial-jsonschema-spectral-rules
- name: Synchrony Financial API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 7
  slug: synchrony-financial-rules
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.3
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synchrony-financial/refs/heads/main/screenshots/synchrony-financial-2026-06-20T194826.png
security:
- kind: authentication
  name: Synchrony Financial Authentication
  slug: synchrony-financial-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Synchrony Financial Domain Security
  slug: synchrony-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Synchrony Financial Vulnerability Disclosure
  slug: synchrony-financial-vulnerability-disclosure
  summary_line: Bugcrowd
slug: synchrony-financial
tags:
- Financial Services
- Credit
- Payments
- Consumer Finance
- Retail Finance
website: https://www.synchrony.com
---
