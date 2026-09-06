---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 83
  human_in_the_loop: 0
  name: Pleo Agentic Access
  operation_count: 142
  slug: pleo-agentic-access
  summary_line: 142 operations · 83 acting
api_count: 11
apis:
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: 'The Accounting Entries API endpoints enable you to perform the following: - Apply filters and search for accounting entries and accounting receipts. - Retrieve list of accounting entries and accountin'
  name: Pleo accounting-entries API
  slug: pleo-accounting-entries-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The accounting-entries-external API from Pleo — 3 operation(s) for accounting-entries-external.
  name: Pleo accounting-entries-external API
  slug: pleo-accounting-entries-external-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The AccountingEntryEnrichmentV2 API from Pleo — 1 operation(s) for accountingentryenrichmentv2.
  name: Pleo AccountingEntryEnrichmentV2 API
  slug: pleo-accountingentryenrichmentv2-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: This API enables you to create an account in Pleo, search for an account by its specific ID, update details of an account recorded in Pleo, delete an account from Pleo, or apply specific filters to re
  name: Pleo Accounts API
  slug: pleo-accounts-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: 'The Companies API enables you to search for company records that are managed in Pleo. You can perform the following: - Search for multiple companies - Search for a specific company record by company I'
  name: Pleo Companies API
  slug: pleo-companies-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: 'The Employees API enables you to search for employee records that are managed in Pleo. You can perform the following: - Search for multiple employees - Search for a specific employee record by employe'
  name: Pleo Employees API
  slug: pleo-employees-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The Export API (v0) API from Pleo — 4 operation(s) for export api (v0).
  name: Pleo Export API (v0) API
  slug: pleo-export-api-v0-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The Export API (v1) API from Pleo — 4 operation(s) for export api (v1).
  name: Pleo Export API (v1) API
  slug: pleo-export-api-v1-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The Export API (v2) API from Pleo — 4 operation(s) for export api (v2).
  name: Pleo Export API (v2) API
  slug: pleo-export-api-v2-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The Export API (v3) API from Pleo — 6 operation(s) for export api (v3).
  name: Pleo Export API (v3) API
  slug: pleo-export-api-v3-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The Export Items (v0) API from Pleo — 1 operation(s) for export items (v0).
  name: Pleo Export Items (v0) API
  slug: pleo-export-items-v0-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The Export Items (v1) API from Pleo — 1 operation(s) for export items (v1).
  name: Pleo Export Items (v1) API
  slug: pleo-export-items-v1-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The Export Items (v2) API from Pleo — 1 operation(s) for export items (v2).
  name: Pleo Export Items (v2) API
  slug: pleo-export-items-v2-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The Export Items (v3) API from Pleo — 1 operation(s) for export items (v3).
  name: Pleo Export Items (v3) API
  slug: pleo-export-items-v3-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The External Clients API from Pleo — 1 operation(s) for external clients.
  name: Pleo External Clients API
  slug: pleo-external-clients-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The external-vendors API from Pleo — 13 operation(s) for external-vendors.
  name: Pleo external-vendors API
  slug: pleo-external-vendors-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: Installations of applications. An installation is a representation of an application being installed for a resource. Currently we support companies and organizations, future support might include user
  name: Pleo Installations API
  slug: pleo-installations-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The Subscriptions API from Pleo — 4 operation(s) for subscriptions.
  name: Pleo Subscriptions API
  slug: pleo-subscriptions-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The tag-groups API from Pleo — 6 operation(s) for tag-groups.
  name: Pleo tag-groups API
  slug: pleo-tag-groups-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: The tags API from Pleo — 8 operation(s) for tags.
  name: Pleo tags API
  slug: pleo-tags-api
- baseURL: https://external.pleo.io
  baseurl_source: declared
  description: Tax Codes API
  name: Pleo tax-codes API
  slug: pleo-tax-codes-api
artifact_total: 77
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: App Marketplace accounting-entries API
  slug: open-pleo-accounting-entries-api
- collection_type: open
  name: App Marketplace accounting-entries accounting-entries-external API
  slug: open-pleo-accounting-entries-external-api
- collection_type: open
  name: App Marketplace accounting-entries AccountingEntryEnrichmentV2 API
  slug: open-pleo-accountingentryenrichmentv2-api
- collection_type: open
  name: App Marketplace accounting-entries Accounts API
  slug: open-pleo-accounts-api
- collection_type: open
  name: App Marketplace accounting-entries Companies API
  slug: open-pleo-companies-api
- collection_type: open
  name: App Marketplace accounting-entries Employees API
  slug: open-pleo-employees-api
- collection_type: open
  name: App Marketplace accounting-entries Export API (v0) API
  slug: open-pleo-export-api-v0-api
- collection_type: open
  name: App Marketplace accounting-entries Export API (v1) API
  slug: open-pleo-export-api-v1-api
- collection_type: open
  name: App Marketplace accounting-entries Export API (v2) API
  slug: open-pleo-export-api-v2-api
- collection_type: open
  name: App Marketplace accounting-entries Export API (v3) API
  slug: open-pleo-export-api-v3-api
- collection_type: open
  name: App Marketplace accounting-entries Export Items (v0) API
  slug: open-pleo-export-items-v0-api
- collection_type: open
  name: App Marketplace accounting-entries Export Items (v1) API
  slug: open-pleo-export-items-v1-api
- collection_type: open
  name: App Marketplace accounting-entries Export Items (v2) API
  slug: open-pleo-export-items-v2-api
- collection_type: open
  name: App Marketplace accounting-entries Export Items (v3) API
  slug: open-pleo-export-items-v3-api
- collection_type: open
  name: App Marketplace accounting-entries External Clients API
  slug: open-pleo-external-clients-api
- collection_type: open
  name: App Marketplace accounting-entries external-vendors API
  slug: open-pleo-external-vendors-api
- collection_type: open
  name: App Marketplace accounting-entries Installations API
  slug: open-pleo-installations-api
- collection_type: open
  name: App Marketplace accounting-entries Subscriptions API
  slug: open-pleo-subscriptions-api
- collection_type: open
  name: App Marketplace accounting-entries tag-groups API
  slug: open-pleo-tag-groups-api
- collection_type: open
  name: App Marketplace accounting-entries tags API
  slug: open-pleo-tags-api
- collection_type: open
  name: App Marketplace accounting-entries tax-codes API
  slug: open-pleo-tax-codes-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pleo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pleo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pleo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.pleo.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pleo.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pleo-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pleo-company
- group: other
  title: ''
  type: X
  url: https://x.com/pleo
- group: company
  title: ''
  type: Blog
  url: https://blog.pleo.io/en
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pleo.io/en/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pleo.io
- group: commercial
  title: ''
  type: Plans
  url: plans/pleo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pleo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pleo-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/pleo-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/pleo-context.jsonld
created: 2026-06-12
description: Pleo is a business spend management platform that issues smart company cards to employees, enabling real-time expense tracking, receipt capture, and automated bookkeeping. The Pleo REST API lets developers automate workflows, sync accounting data, manage users and cards, and build custom integrations against accounting systems. The API supports OAuth 2.0 (with PKCE) and API key authentication with a scopes-based permission model, and offers both a sandbox and production environment. Pleo also runs an App Marketplace where partners can publish integrations available to thousands of businesses across Europe.
examples:
- key_count: 18
  name: Pleo Accounting Entry Example
  slug: pleo-accounting-entry-example
- key_count: 8
  name: Pleo Bookkeeping Account Example
  slug: pleo-bookkeeping-account-example
- key_count: 10
  name: Pleo Export Job Example
  slug: pleo-export-job-example
- key_count: 13
  name: Pleo Vendor Example
  slug: pleo-vendor-example
- key_count: 9
  name: Pleo Webhook Subscription Example
  slug: pleo-webhook-subscription-example
finops:
- name: Pleo Finops
  service_category: ''
  slug: pleo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pleo.png
json_schemas:
- name: Account
  property_count: 2
  slug: pleo-account
- name: AccountingEntryBaseSearchRequest
  property_count: 24
  slug: pleo-accounting-entry-base-search-request
- name: AccountingEntryCoreV6
  property_count: 32
  slug: pleo-accounting-entry-core-v6
- name: AccountingEntryEnrichmentResponse
  property_count: 3
  slug: pleo-accounting-entry-enrichment-response
- name: AccountingEntryEnrichmentV2BodyRequest
  property_count: 2
  slug: pleo-accounting-entry-enrichment-v2-body-request
- name: ActivateVendorEventRequest
  property_count: 2
  slug: pleo-activate-vendor-event-request
- name: AggregatedTagGroupModel
  property_count: 8
  slug: pleo-aggregated-tag-group-model
- name: AggregatedTagModel
  property_count: 9
  slug: pleo-aggregated-tag-model
- name: BookkeepingAccountBatchCreateRequestV1
  property_count: 2
  slug: pleo-bookkeeping-account-batch-create-request-v1
- name: BookkeepingAccountCreateRequestV1
  property_count: 7
  slug: pleo-bookkeeping-account-create-request-v1
- name: BookkeepingAccountCreateRequestV4
  property_count: 7
  slug: pleo-bookkeeping-account-create-request-v4
- name: BookkeepingAccountRestModelV4
  property_count: 8
  slug: pleo-bookkeeping-account-rest-model-v4
- name: BookkeepingAccountSearchRequestV4
  property_count: 6
  slug: pleo-bookkeeping-account-search-request-v4
- name: BookkeepingMethodV2
  property_count: 0
  slug: pleo-bookkeeping-method-v2
- name: CreateCsvImportJobRequestV1
  property_count: 5
  slug: pleo-create-csv-import-job-request-v1
- name: CursorPaginatedResponseExternalCompanyResponseModel
  property_count: 2
  slug: pleo-cursor-paginated-response-external-company-response-model
- name: CursorPaginatedResponseExternalEmployeeResponseModel
  property_count: 2
  slug: pleo-cursor-paginated-response-external-employee-response-model
- name: CursorPaginatedResponseTaxCodeModel
  property_count: 2
  slug: pleo-cursor-paginated-response-tax-code-model
- name: InstallationResponse
  property_count: 8
  slug: pleo-installation-response
- name: SubscriptionResponse
  property_count: 1
  slug: pleo-subscription-response
- name: TaxCodeCreateUpdateModel
  property_count: 8
  slug: pleo-tax-code-create-update-model
jsonld:
- class_count: 40
  name: Pleo Context
  property_count: 18
  slug: pleo-context
layout: provider
modified: 2026-06-12
name: Pleo
nav: Providers
network: true
overview: 'Pleo publishes 21 APIs on the [APIs.io](https://apis.io/) network, including accounting-entries API, accounting-entries-external API, AccountingEntryEnrichmentV2 API, and 18 more. Tagged areas include Expense Management, Company Cards, Spend Management, Reimbursement, and Accounting.


  The Pleo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pleo''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Pleo Plans Pricing
  plan_count: 4
  slug: pleo-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Pleo Rate Limits
  slug: pleo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pleo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: pleo-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 86.3
    catalog_earned_first_party: 0.0
    catalog_gap: 28.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 61.8
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pleo/refs/heads/main/screenshots/pleo-2026-06-20T191811.png
security:
- kind: authentication
  name: Pleo Authentication
  slug: pleo-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Pleo Domain Security
  slug: pleo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pleo
tags:
- Expense Management
- Company Cards
- Spend Management
- Reimbursement
- Accounting
- Fintech
- Finance
website: https://www.pleo.io
---
