---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Hypto Agentic Access
  operation_count: 65
  slug: hypto-agentic-access
  summary_line: 65 operations · 31 acting
api_count: 1
apis:
- baseURL: https://partners.hypto.in
  baseurl_source: declared
  description: This section explains how to create virtual accounts that can be used to receive collections and deposits using any fund transfer mode.
  name: Hypto Banking API
  slug: hypto-banking-api
- baseURL: https://partners.hypto.in
  baseurl_source: declared
  description: This section explains the steps to generate a QR code using any given UPI ID on web (.js) and android (Java/Kotlin)
  name: Hypto Generate QR API
  slug: hypto-generate-qr-api
- baseURL: https://partners.hypto.in
  baseurl_source: declared
  description: This section explains how to initiate a fund transfer to any bank account and check the status of the transaction.
  name: Hypto Payments API
  slug: hypto-payments-api
- baseURL: https://partners.hypto.in
  baseurl_source: declared
  description: This section explains how to fetch status details of partner services.
  name: Hypto Status API
  slug: hypto-status-api
- baseURL: https://partners.hypto.in
  baseurl_source: declared
  description: Create customized UPI IDs to accept payments through any UPI app.
  name: Hypto UPI API
  slug: hypto-upi-api
- baseURL: https://partners.hypto.in
  baseurl_source: declared
  description: Initiate collection requests to any UPI ID and receive payments through any UPI app
  name: Hypto UPI Collections API
  slug: hypto-upi-collections-api
- baseURL: https://partners.hypto.in
  baseurl_source: declared
  description: This section explains the steps to configure callback urls for receiving transactions (collections) into virtual accounts and UPI IDs.
  name: Hypto Webhooks API
  slug: hypto-webhooks-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/hypto/agentic-access/hypto-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hypto-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/hypto/rules/hypto-rules.yml
  title: ''
  type: Spectral
  url: rules/hypto-rules.yml
- group: design
  href: https://artifacts.apis.io/hypto/json-ld/hypto-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hypto-context.jsonld
- group: design
  href: https://artifacts.apis.io/hypto/vocabulary/hypto-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hypto-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hypto/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hypto/data-model/hypto-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hypto-data-model.yml
- group: design
  href: https://artifacts.apis.io/hypto/errors/hypto-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hypto-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hypto/conformance/hypto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hypto-conformance.yml
- group: other
  href: https://artifacts.apis.io/hypto/hosts/hypto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hypto-hosts.yml
- group: other
  href: https://artifacts.apis.io/hypto/vendors/hypto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hypto-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hypto.in/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hypto.in/privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://www.hypto.in/docs
- group: auth
  href: https://artifacts.apis.io/hypto/security/hypto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hypto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hypto.in/
created: '2026-10-20'
description: Hypto provides a developer-friendly payment gateway platform offering APIs for collections, payouts, and UPI transactions in India. Their services enable businesses to automate fund transfers via IMPS, NEFT, RTGS, and UPI, create virtual accounts for seamless collections, and integrate payment solutions quickly with low pricing and high scalability. Hypto processes over $100M daily, supporting use cases such as supplier payments, loan disbursements, online gaming rewards, and more, with robust security and extensive documentation.
json_schemas:
- name: Account
  property_count: 19
  slug: hypto-account
- name: Bank_Verification
  property_count: 3
  slug: hypto-bank-verification
- name: Received_UPI
  property_count: 3
  slug: hypto-received-upi
- name: Received_VA
  property_count: 3
  slug: hypto-received-va
- name: UPI
  property_count: 16
  slug: hypto-upi
- name: UPI_Verification
  property_count: 3
  slug: hypto-upi-verification
jsonld:
- class_count: 6
  name: Hypto Context
  property_count: 30
  slug: hypto-context
layout: provider
modified: '2026-10-20'
name: Hypto
nav: Providers
network: true
overview: 'Hypto publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Banking API, Generate QR API, Payments API, and 4 more. Tagged areas include Company, Payments, Fintech, and Collection.


  The Hypto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hypto''s developer surface includes API reference and 14 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Hypto API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: hypto-rules
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 56.0
    developer_ergonomics: 8.9
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hypto Domain Security
  slug: hypto-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: hypto-create-and-fetch-virtual-account
  slug: hypto-create-and-fetch-virtual-account
- name: hypto-fund-transfer-and-status
  slug: hypto-fund-transfer-and-status
slug: hypto
tags:
- Company
- Payments
- Fintech
- Collection
website: https://hypto.in/
---
