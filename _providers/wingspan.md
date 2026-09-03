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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 92
  human_in_the_loop: 0
  name: Wingspan Agentic Access
  operation_count: 172
  slug: wingspan-agentic-access
  summary_line: 172 operations · 92 acting
api_count: 1
apis:
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Includes endpoints for managing 1099 forms.
  name: Wingspan 1099 Operations API
  slug: wingspan-1099-operations-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: These endpoints cater to fetching, storing, and managing documents related to electronic signatures, including retrieval of signing URLs and saving e-signed documents.
  name: Wingspan Banking Management API
  slug: wingspan-banking-management-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: This category includes endpoints for managing bulk operations like bulk payables, bulk invoices, and bulk collaborator management.
  name: Wingspan Bulk Operations API
  slug: wingspan-bulk-operations-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Encompasses endpoints for banking-related operations such as managing bank cards, statements, instant payouts, and banking institutions..
  name: Wingspan Client Management API
  slug: wingspan-client-management-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: This category includes endpoints that manage relationships and interactions with collaborators. This includes collaborator settings, and various operations related to collaborators.
  name: Wingspan Collaborator Management API
  slug: wingspan-collaborator-management-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Focuses on endpoints for managing custom fields related to payments and collaborators.
  name: Wingspan Custom Field Management API
  slug: wingspan-custom-field-management-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Deprecated Endpoints.
  name: Wingspan Deprecated API
  slug: wingspan-deprecated-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Focuses on endpoints for managing eligibility requirements and custom fields related to payments.
  name: Wingspan Document Signing and Eligibility API
  slug: wingspan-document-signing-and-eligibility-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: 'Covers endpoints related to invoice creation, retrieval, and management. This includes both member and client invoices, along with specific actions like sending invoices by email and managing invoice '
  name: Wingspan Invoice Management API
  slug: wingspan-invoice-management-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Endpoint that provides a comprehensive list of available Merchant Category Codes.
  name: Wingspan Merchant Category Codes API
  slug: wingspan-merchant-category-codes-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Endpoints dealing with payables, including creating, listing, updating, and deleting payables. It also includes summary endpoints and immediate payroll payables.
  name: Wingspan Payables Management API
  slug: wingspan-payables-management-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Covers endpoints that manage payout settings and related configurations.
  name: Wingspan Payroll Settings API
  slug: wingspan-payroll-settings-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Includes endpoints for generating various reports and analytics, such as payables reports, collaborators reports, and aging reports.
  name: Wingspan Reporting and Analytics API
  slug: wingspan-reporting-and-analytics-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Covers endpoints that manage service statuses and related configurations.
  name: Wingspan Service Settings API
  slug: wingspan-service-settings-api
- baseURL: https://api.wingspan.app
  baseurl_source: declared
  description: Operations related to Wingspan Wallet
  name: Wingspan Wingspan Wallet API
  slug: wingspan-wingspan-wallet-api
artifact_total: 53
asyncapis:
- description: ''
  name: Wingspan Webhooks
  slug: wingspan-webhooks
collections:
- collection_type: postman
  name: Wingspan Payments 1099 Operations API
  slug: postman-wingspan-1099-operations-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Banking Management API
  slug: postman-wingspan-banking-management-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Bulk Operations API
  slug: postman-wingspan-bulk-operations-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Client Management API
  slug: postman-wingspan-client-management-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Collaborator Management API
  slug: postman-wingspan-collaborator-management-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Custom Field Management API
  slug: postman-wingspan-custom-field-management-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Deprecated API
  slug: postman-wingspan-deprecated-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Document Signing and Eligibility API
  slug: postman-wingspan-document-signing-and-eligibility-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Invoice Management API
  slug: postman-wingspan-invoice-management-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Merchant Category Codes API
  slug: postman-wingspan-merchant-category-codes-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Payables Management API
  slug: postman-wingspan-payables-management-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Payroll Settings API
  slug: postman-wingspan-payroll-settings-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Reporting and Analytics API
  slug: postman-wingspan-reporting-and-analytics-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Service Settings API
  slug: postman-wingspan-service-settings-api
- collection_type: postman
  name: Wingspan Payments 1099 Operations Wingspan Wallet API
  slug: postman-wingspan-wingspan-wallet-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wingspan Payments 1099 Operations API
  slug: open-wingspan-1099-operations-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Banking Management API
  slug: open-wingspan-banking-management-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Bulk Operations API
  slug: open-wingspan-bulk-operations-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Client Management API
  slug: open-wingspan-client-management-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Collaborator Management API
  slug: open-wingspan-collaborator-management-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Custom Field Management API
  slug: open-wingspan-custom-field-management-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Deprecated API
  slug: open-wingspan-deprecated-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Document Signing and Eligibility API
  slug: open-wingspan-document-signing-and-eligibility-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Invoice Management API
  slug: open-wingspan-invoice-management-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Merchant Category Codes API
  slug: open-wingspan-merchant-category-codes-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Payables Management API
  slug: open-wingspan-payables-management-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Payroll Settings API
  slug: open-wingspan-payroll-settings-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Reporting and Analytics API
  slug: open-wingspan-reporting-and-analytics-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Service Settings API
  slug: open-wingspan-service-settings-api
- collection_type: open
  name: Wingspan Payments 1099 Operations Wingspan Wallet API
  slug: open-wingspan-wingspan-wallet-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/wingspan-payments-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wingspan/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wingspan.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wingspan.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wingspan.app/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wingspan.app/docs/get-started-with-the-wingspan-api
- group: operate
  title: ''
  type: Support
  url: https://www.wingspan.app/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.wingspan.app/en/
- group: company
  title: ''
  type: Blog
  url: https://www.wingspan.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wingspanHQ
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wingspan.app/pricing
- group: start
  title: ''
  type: Login
  url: https://my.wingspan.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wingspan.app/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wingspan.app/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wingspan.app/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wingspan-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wingspan-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wingspan-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wingspan-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.wingspan.app/security
- group: design
  title: ''
  type: Conformance
  url: conformance/wingspan-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wingspan-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/wingspan-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wingspan-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wingspan-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wingspan-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wingspan-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wingspan-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wingspan-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wingspan-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wingspan-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/wingspan-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wingspan-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Wingspan is a contractor payments and payroll platform built for the independent workforce, giving enterprises a single system to onboard 1099 contractors, collect W-9 and compliance documents, run approval-based payroll, pay collaborators by ACH or instant payout, and file 1099 tax forms. Its REST Payments API (OpenAPI 3.1) covers payables, invoicing, collaborators and groups, payable/invoice/1099 batches, deductions, eligibility requirements, custom fields, reporting, and webhooks, with embeddable onboarding and payout-settings UIs.
image: https://www.wingspan.app/images/wingspan-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Wingspan MCP Server
  slug: wingspan-mcp-server
modified: '2026-07-21'
name: Wingspan
nav: Providers
network: true
overview: 'Wingspan publishes 15 APIs on the [APIs.io](https://apis.io/) network, including 1099 Operations API, Banking Management API, Bulk Operations API, and 12 more. Tagged areas include Company, Payments, Payroll, Contractors, and Invoicing.


  The Wingspan catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wingspan''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 27 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 2
  name: Wingspan Rate Limits
  slug: wingspan-rate-limits
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 23
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 64.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wingspan/refs/heads/main/screenshots/wingspan-2026-08-17T082930.png
security:
- kind: authentication
  name: Wingspan Authentication
  slug: wingspan-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wingspan Domain Security
  slug: wingspan-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Wingspan Trust Center
  slug: wingspan-trust-center
  summary_line: SOC 2, HIPAA
slug: wingspan
tags:
- Company
- Payments
- Payroll
- Contractors
- Invoicing
- Taxes
- Fintech
- Freelance Economy
website: https://docs.wingspan.app/
---
