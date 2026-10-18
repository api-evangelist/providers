---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-10-17'
api_count: 9
apis:
- description: Banking API version 4 providing account, transaction, and payment operations.
  name: Banking API v4
  slug: banking-api-v4
- baseURL: https://bankservice.zdata.no
  baseurl_source: declared
  description: The Accounts API from Aritma — 1 operation(s) for accounts.
  name: Aritma Accounts API
  slug: aritma-accounts-api
- baseURL: https://bankservice.zdata.no
  baseurl_source: declared
  description: The Aritma API API from Aritma — 1 operation(s) for aritma api.
  name: Aritma Aritma API
  slug: aritma-aritma-api-api
- baseURL: https://bankservice.zdata.no
  baseurl_source: declared
  description: The Banks API from Aritma — 2 operation(s) for banks.
  name: Aritma Banks API
  slug: aritma-banks-api
- baseURL: https://bankservice.zdata.no
  baseurl_source: declared
  description: The Bulk Payments API from Aritma — 1 operation(s) for bulk payments.
  name: Aritma Bulk Payments API
  slug: aritma-bulk-payments-api
- baseURL: https://bankservice.zdata.no
  baseurl_source: declared
  description: The Companies API from Aritma — 1 operation(s) for companies.
  name: Aritma Companies API
  slug: aritma-companies-api
- baseURL: https://bankservice.zdata.no
  baseurl_source: declared
  description: The Consents API from Aritma — 5 operation(s) for consents.
  name: Aritma Consents API
  slug: aritma-consents-api
- baseURL: https://bankservice.zdata.no
  baseurl_source: declared
  description: The Events API from Aritma — 1 operation(s) for events.
  name: Aritma Events API
  slug: aritma-events-api
- baseURL: https://bankservice.zdata.no
  baseurl_source: declared
  description: The Mock API from Aritma — 2 operation(s) for mock.
  name: Aritma Mock API
  slug: aritma-mock-api
artifact_total: 20
asyncapis:
- description: ''
  name: Aritma Webhooks
  slug: aritma-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/rules/aritma-rules.yml
  title: ''
  type: Spectral
  url: rules/aritma-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/json-ld/aritma-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aritma-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/vocabulary/aritma-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aritma-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/asyncapi/aritma-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aritma-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/data-model/aritma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aritma-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/authentication/aritma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aritma-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/lifecycle/aritma-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aritma-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/lifecycle/aritma-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aritma-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/conformance/aritma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aritma-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/llms/aritma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aritma-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/well-known/aritma-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aritma-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/well-known/aritma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aritma-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/hosts/aritma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aritma-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/vendors/aritma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aritma-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aritma.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.aritma.com/log-in
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aritma/refs/heads/main/security/aritma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aritma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aritma.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aritma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.aritma.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.aritma.com/apis/banking/v4
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.aritma.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.aritma.com/en
- group: company
  title: ''
  type: Blog
  url: https://www.aritma.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aritma.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aritma.com/
coverage:
  checked: '2026-10-16'
  detail: The Banking API documentation page is a JavaScript‑rendered SPA with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://developer.aritma.com/apis/banking/v4
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Aritma provides a finance automation platform for B2B enterprises, enabling seamless payments, reconciliation, and integration with multiple ERP systems. Their API connects banks, ERP solutions like Microsoft Dynamics 365, Business NXT, Visma, and more, allowing developers to build custom workflows for CFOs, accountants, and IT teams. The platform supports multi‑bank transactions, ISO‑20022 compliance, and offers extensive documentation for developers to integrate financial data across systems.
image: https://cdn.prod.website-files.com/6373dc3023ac2e946464f5b3/65805757fee228b9b87f2434_6572e8614112a5e3b5553b67_Open%20banking1.svg
json_schemas:
- name: GetApiV3EventsDeadlettersResponse
  property_count: 12
  slug: aritma-get-api-v3-events-deadletters-response
- name: GetConsentsConsentidResponse
  property_count: 1
  slug: aritma-get-consents-consentid-response
- name: PostApiBulkPaymentsCreditTransferRequest
  property_count: 14
  slug: aritma-post-api-bulk-payments-credit-transfer-request
- name: PostMockApisBankingV4OpenapiBankingOpenapiBulkPaymentsCredit
  property_count: 4
  slug: aritma-post-mock-apis-banking-v4-openapi-banking-openapi-bulk-payments-credit
- name: PutApiV3CompaniesCompanyidSubscriptionsSubscriptionnameReque
  property_count: 5
  slug: aritma-put-api-v3-companies-companyid-subscriptions-subscriptionname-reque
- name: PutConsentsIdRefreshResponse
  property_count: 1
  slug: aritma-put-consents-id-refresh-response
jsonld:
- class_count: 9
  name: Aritma Context
  property_count: 25
  slug: aritma-context
layout: provider
modified: '2026-10-16'
name: Aritma
nav: Providers
network: true
overview: 'Aritma is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Aritma API, Banks API, and 6 more. Tagged areas include Company, Finance, Automation, B2B, and Payments.


  The Aritma catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Aritma''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Aritma API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: aritma-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 35.8
    developer_ergonomics: 63.6
    discoverability: 69.6
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aritma Authentication
  slug: aritma-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aritma Domain Security
  slug: aritma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aritma
tags:
- Company
- Finance
- Automation
- B2B
- Payments
website: https://aritma.com/
---
