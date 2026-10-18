---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Openpayments Io Agentic Access
  operation_count: 57
  slug: openpayments-io-agentic-access
  summary_line: 57 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: 'The Account Information Service (AIS) offers the following services: * Transaction reports for a given account or card account including balances if applicable * Balances of a given account or card ac'
  name: Open Payments Account Information Service (AIS) API
  slug: openpayments-io-account-information-service-ais-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: 'The ASPSP (Account Servicing Payment Service Providers) Information Service allows looking up information about banks and other account providers. The service offers the following services: * List All'
  name: Open Payments ASPSP Information Service API
  slug: openpayments-io-aspsp-information-service-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: Bankgiro Lookup APIs provide enhanced data and pre-payment validation on top of our core APIs. These services enable you to build more reliable, user-friendly payment experiences by accessing and veri
  name: Open Payments Bankgiro Lookup API
  slug: openpayments-io-bankgiro-lookup-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: 'The Consent Service offers the following services: * Create and authorize consents between the PSU and the TPP for use in the AIS services * Get status of consent and retrieve previously authorized co'
  name: Open Payments Consent Service API
  slug: openpayments-io-consent-service-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: FX Connect enables you to execute cross-border payments without integrating the Payment Initiation Service (PIS), operating seamlessly on top of your own existing bank integrations. With FX Connect, y
  name: Open Payments FX Connect API
  slug: openpayments-io-fx-connect-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: ISO Payments offers a direct and intuitive interface to the banks ISO 20022 products. By leveraging ISO 20022, you can automate and streamline a wide range of payment processes, including both domesti
  name: Open Payments ISO Payments API
  slug: openpayments-io-iso-payments-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: 'KYC Service offers the following services: * Initiation of a KYC process to access our KYC webform * KYC status of a corporation'
  name: Open Payments KYC Service API
  slug: openpayments-io-kyc-service-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: 'Payment Initiation Service (PIS) offers the following services: * Create and authorize payments * Status information of payments and authorizations * Create and authorize baskets to efficiently sign m'
  name: Open Payments Payment Initiation Service (PIS) API
  slug: openpayments-io-payment-initiation-service-pis-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: The Payout Service brings efficiency and security to a wide range of payment processes, including supplier invoices, payroll, refunds, and other forms of disbursement. The solution automates the entir
  name: Open Payments Payout Service API
  slug: openpayments-io-payout-service-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: The SEPA Direct Debit API allows you to initiate EUR-denominated collections directly from your customer's bank account in the Netherlands by submitting debit instructions in JSON format, from which a
  name: Open Payments SEPA Direct Debit API
  slug: openpayments-io-sepa-direct-debit-api
- baseURL: https://api.openbankingplatform.com
  baseurl_source: declared
  description: The Verification of Payee (VoP) API allows you to instantly verify that a creditor's name matches the provided account details (IBAN) and display the result to your PSU, e.g. when they create a new su
  name: Open Payments Verification of Payee (VoP) API
  slug: openpayments-io-verification-of-payee-vop-api
artifact_total: 23
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/agentic-access/openpayments-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openpayments-io-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/rules/openpayments-io-rules.yml
  title: ''
  type: Spectral
  url: rules/openpayments-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/json-ld/openpayments-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openpayments-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/vocabulary/openpayments-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openpayments-io-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/data-model/openpayments-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openpayments-io-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/changelog/openpayments-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/openpayments-io-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/sandbox/openpayments-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/openpayments-io-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/authentication/openpayments-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openpayments-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/errors/openpayments-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/openpayments-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/conformance/openpayments-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openpayments-io-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/llms/openpayments-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openpayments-io-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/hosts/openpayments-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openpayments-io-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/vendors/openpayments-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openpayments-io-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openpayments.io/privacypolicy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openpayments.io/docs/getstarted
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/scopes/openpayments-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/openpayments-io-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openpayments-io/refs/heads/main/security/openpayments-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openpayments-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openpayments.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.openpayments.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openpayments.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openpayments.io/pricing
- group: company
  title: ''
  type: About
  url: https://www.openpayments.io/company
- group: company
  title: ''
  type: Blog
  url: https://www.openpayments.io/news-press
- group: other
  title: ''
  type: Cases
  url: https://www.openpayments.io/cases
- group: other
  title: ''
  type: Whitepaper
  url: https://www.openpayments.io/whitepaper
created: '2026-10-15'
description: Open Payments provides a unified API platform that connects businesses to multiple banks, enabling payments, account data access, cross‑border transactions, and financial data aggregation. Their solution simplifies integration, reduces friction, and offers real‑time cash‑flow visibility, compliance with PSD2 and GDPR, and customizable branding for enterprises seeking to build modern financial services.
image: https://cdn.prod.website-files.com/62334f93c837ab072ce54cd5/62544bad42bb186a71cba7e0_OGI%201.jpg
json_schemas:
- name: ConfirmIsoPaymentResponse
  property_count: 3
  slug: openpayments-io-confirm-iso-payment-response
- name: ConfirmPayoutResponse
  property_count: 3
  slug: openpayments-io-confirm-payout-response
- name: CreatePayoutRequest
  property_count: 12
  slug: openpayments-io-create-payout-request
- name: CreatePayoutResponse
  property_count: 10
  slug: openpayments-io-create-payout-response
- name: GetPayoutResponse
  property_count: 14
  slug: openpayments-io-get-payout-response
- name: SEPA Direct Debit Payment
  property_count: 26
  slug: openpayments-io-payment-initiation-sepa-direct-debit-json
jsonld:
- class_count: 120
  name: Openpayments Io Context
  property_count: 248
  slug: openpayments-io-context
layout: provider
modified: '2026-10-15'
name: Open Payments
nav: Providers
network: true
overview: 'Open Payments publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Information Service (AIS) API, ASPSP Information Service API, Bankgiro Lookup API, and 8 more. Tagged areas include Company, Payments, Banking, and Fintech.


  The Open Payments catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Open Payments'' developer surface includes changelog, sandbox, authentication, getting-started guide, documentation, pricing, engineering blog, and 19 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Open Payments API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 3
  slug: openpayments-io-rules
scopes:
- name: Openpayments Io Scopes
  scope_count: 13
  slug: openpayments-io-scopes
  summary_line: 13 scopes · clientCredentials
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 66.1
    developer_ergonomics: 54.2
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 33.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Openpayments Io Authentication
  slug: openpayments-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Openpayments Io Domain Security
  slug: openpayments-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openpayments-io
tags:
- Company
- Payments
- Banking
- Fintech
website: https://openpayments.io/
---
