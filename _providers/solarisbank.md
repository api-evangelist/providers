---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.solaris-sandbox.de
  baseurl_source: declared
  description: 'solarisBank AG API as documented publicly: 48 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: solarisBank AG API
  slug: solarisbank-api
artifact_total: 16
asyncapis:
- description: ''
  name: Solarisbank Webhooks
  slug: solarisbank-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/solarisbank/well-known/solarisbank-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/solarisbank-status-security.txt
- group: agent
  href: https://artifacts.apis.io/solarisbank/well-known/solarisbank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/solarisbank-well-known.yml
- group: design
  href: https://artifacts.apis.io/solarisbank/rules/solarisbank-rules.yml
  title: ''
  type: Spectral
  url: rules/solarisbank-rules.yml
- group: design
  href: https://artifacts.apis.io/solarisbank/json-ld/solarisbank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/solarisbank-context.jsonld
- group: design
  href: https://artifacts.apis.io/solarisbank/vocabulary/solarisbank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/solarisbank-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/solarisbank/asyncapi/solarisbank-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/solarisbank-webhooks.yml
- group: design
  href: https://artifacts.apis.io/solarisbank/data-model/solarisbank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/solarisbank-data-model.yml
- group: operate
  href: https://artifacts.apis.io/solarisbank/changelog/solarisbank-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/solarisbank-changelog.yml
- group: design
  href: https://artifacts.apis.io/solarisbank/conventions/solarisbank-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/solarisbank-conventions.yml
- group: design
  href: https://artifacts.apis.io/solarisbank/conventions/solarisbank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/solarisbank-conventions.yml
- group: auth
  href: https://artifacts.apis.io/solarisbank/authentication/solarisbank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/solarisbank-authentication.yml
- group: design
  href: https://artifacts.apis.io/solarisbank/conformance/solarisbank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/solarisbank-conformance.yml
- group: agent
  href: https://artifacts.apis.io/solarisbank/llms/solarisbank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/solarisbank-llms.txt
- group: other
  href: https://artifacts.apis.io/solarisbank/hosts/solarisbank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/solarisbank-hosts.yml
- group: other
  href: https://artifacts.apis.io/solarisbank/vendors/solarisbank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/solarisbank-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solarisgroup.com/en/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.solarisgroup.com
- group: auth
  title: ''
  type: Security
  url: https://www.solarisgroup.com/en/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solarisgroup.com/en/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.solarisgroup.com/en/press/
- group: auth
  href: https://artifacts.apis.io/solarisbank/security/solarisbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/solarisbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solarisgroup.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.solarisgroup.com/en/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.solarisgroup.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.solarisgroup.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.solarisgroup.com/guides/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.solarisgroup.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.solarisgroup.com/hc/en-us
- group: auth
  href: https://artifacts.apis.io/solarisbank/security/solarisbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/solarisbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://solarisbank.com/
created: '2026-10-21'
description: solarisBank AG is a German technology company offering embedded finance solutions through a Banking-as-a-Service platform. It provides digital banking services such as accounts, cards, payments, lending, and compliance tools, enabling businesses to embed regulated financial products. The company operates across Europe with a full banking license, focusing on SaaS providers, accounting software, and other enterprises seeking white‑label banking capabilities.
image: https://www.solarisgroup.com/assets/images/share/solarisshareimage_og.png
json_schemas:
- name: GetV1PersonsPersonidConsumerLoanApplicationsApplicationidRes
  property_count: 2
  slug: solarisbank-get-v1-persons-personid-consumer-loan-applications-applicationid-res
- name: PostOauthTokenRequest
  property_count: 3
  slug: solarisbank-post-oauth-token-request
- name: PostV1BusinessesBusinessidFrontingLoanApplicationsApplicatio
  property_count: 1
  slug: solarisbank-post-v1-businesses-businessid-fronting-loan-applications-applicatio
- name: PostV1BusinessesBusinessidFrontingLoansLoanidPayoutsRequest
  property_count: 1
  slug: solarisbank-post-v1-businesses-businessid-fronting-loans-loanid-payouts-request
- name: PostV1WebhooksRequest
  property_count: 2
  slug: solarisbank-post-v1-webhooks-request
- name: PostV1WebhooksResponse
  property_count: 4
  slug: solarisbank-post-v1-webhooks-response
- name: PutV1PersonsPersonidConsumerLoanApplicationsApplicationidUpl
  property_count: 1
  slug: solarisbank-put-v1-persons-personid-consumer-loan-applications-applicationid-upl
jsonld:
- class_count: 23
  name: Solarisbank Context
  property_count: 25
  slug: solarisbank-context
layout: provider
modified: '2026-10-21'
name: solarisBank AG
nav: Providers
network: true
overview: 'solarisBank AG is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Banking-as-a-Service, Embedded Finance, and Europe.


  The solarisBank AG catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  solarisBank AG''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, support, and 23 more developer resources.'
plans:
- name: Solarisbank Plans Pricing
  plan_count: 0
  slug: solarisbank-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Solarisbank Rate Limits
  slug: solarisbank-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: solarisBank AG API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: solarisbank-rules
scopes:
- name: Solarisbank Scopes
  scope_count: 0
  slug: solarisbank-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 36.1
    developer_ergonomics: 57.1
    discoverability: 67.9
    operational_transparency: 50.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 33.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Solarisbank Authentication
  slug: solarisbank-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Solarisbank Domain Security
  slug: solarisbank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: solarisbank
tags:
- Company
- Finance
- Banking-as-a-Service
- Embedded Finance
- Europe
website: https://www.solarisgroup.com/en/
---
