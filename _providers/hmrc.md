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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Hmrc Agentic Access
  operation_count: 5
  slug: hmrc-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 8
apis:
- description: The HMRC Self Assessment APIs enable software to submit and manage self assessment tax returns, income sources, and tax calculations for individuals and sole traders under Making Tax Digital for Incom
  name: HMRC Self Assessment API
  slug: hmrc-self-assessment-api
- description: The HMRC PAYE APIs enable payroll software to submit employer payroll data, retrieve tax codes and employee records, and manage PAYE submissions for Real Time Information (RTI) reporting.
  name: HMRC PAYE (Pay As You Earn) API
  slug: hmrc-paye-api
- description: The HMRC Customs Declarations APIs enable customs software to submit import and export declarations, manage authorizations, and integrate with the UK Customs Declaration Service (CDS) for trade compli
  name: HMRC Customs Declarations API
  slug: hmrc-customs-declarations-api
- description: The HMRC Corporation Tax APIs enable accounting software to submit corporation tax returns, retrieve liabilities, manage payments, and access tax calculation data for UK businesses.
  name: HMRC Corporation Tax API
  slug: hmrc-corporation-tax-api
- description: VAT financial liabilities
  name: HMRC UK Tax Authority Liabilities API
  slug: hmrc-liabilities-api
- description: VAT return filing obligations
  name: HMRC UK Tax Authority Obligations API
  slug: hmrc-obligations-api
- description: VAT payments made to HMRC
  name: HMRC UK Tax Authority Payments API
  slug: hmrc-payments-api
- description: VAT return submission
  name: HMRC UK Tax Authority Returns API
  slug: hmrc-returns-api
artifact_total: 40
collections:
- collection_type: postman
  name: HMRC VAT (Making Tax Digital) Liabilities API
  slug: postman-hmrc-liabilities-api
- collection_type: postman
  name: HMRC VAT (Making Tax Digital) Liabilities Obligations API
  slug: postman-hmrc-obligations-api
- collection_type: postman
  name: HMRC VAT (Making Tax Digital) Liabilities Payments API
  slug: postman-hmrc-payments-api
- collection_type: postman
  name: HMRC VAT (Making Tax Digital) Liabilities Returns API
  slug: postman-hmrc-returns-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HMRC VAT (Making Tax Digital) Liabilities API
  slug: open-hmrc-liabilities-api
- collection_type: open
  name: HMRC VAT (Making Tax Digital) Liabilities Obligations API
  slug: open-hmrc-obligations-api
- collection_type: open
  name: HMRC VAT (Making Tax Digital) Liabilities Payments API
  slug: open-hmrc-payments-api
- collection_type: open
  name: HMRC VAT (Making Tax Digital) Liabilities Returns API
  slug: open-hmrc-returns-api
- collection_type: open
  name: HMRC VAT (Making Tax Digital) API
  slug: open-hmrc-vat-mtd
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hmrc-uk-tax-authority/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hmrc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hmrc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hmrc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hmrc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hmrc-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hmrc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hmrc
- group: start
  title: ''
  type: Portal
  url: https://developer.service.hmrc.gov.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
- group: auth
  title: ''
  type: Authentication
  url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.service.hmrc.gov.uk/api-documentation/docs/using-the-hub
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gov.uk/api-documentation/docs/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://api-platform-status.production.tax.service.gov.uk/
- group: operate
  title: ''
  type: Support
  url: https://developer.service.hmrc.gov.uk/
- group: company
  title: ''
  type: Website
  url: https://www.gov.uk/government/organisations/hm-revenue-customs
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/hmrc-vat-mtd-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hmrc-vat-return-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/hmrc-context.jsonld
created: '2025'
description: HM Revenue and Customs (HMRC) provides over 115 APIs through the HMRC Developer Hub for UK tax compliance including Making Tax Digital for VAT and Income Tax, PAYE, customs declarations, corporation tax, and construction industry scheme. APIs use OAuth 2.0 and support both REST and XML protocols with a sandbox testing environment.
finops:
- name: Hmrc Finops
  service_category: Government / Tax
  slug: hmrc-finops
image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
json_schemas:
- name: Error
  property_count: 3
  slug: hmrc-error
- name: LiabilitiesResponse
  property_count: 1
  slug: hmrc-liabilitiesresponse
- name: Obligation
  property_count: 6
  slug: hmrc-obligation
- name: ObligationsResponse
  property_count: 1
  slug: hmrc-obligationsresponse
- name: PaymentsResponse
  property_count: 1
  slug: hmrc-paymentsresponse
- name: HMRC VAT Return
  property_count: 11
  slug: hmrc-vat-return
- name: VatLiability
  property_count: 5
  slug: hmrc-vatliability
- name: VatPayment
  property_count: 2
  slug: hmrc-vatpayment
- name: VatReturn
  property_count: 0
  slug: hmrc-vatreturn
- name: VatReturnConfirmation
  property_count: 4
  slug: hmrc-vatreturnconfirmation
- name: VatReturnRequest
  property_count: 11
  slug: hmrc-vatreturnrequest
json_structures:
- name: Hmrc Structure
  property_count: 0
  slug: hmrc-structure
jsonld:
- class_count: 4
  name: Hmrc Context
  property_count: 21
  slug: hmrc-context
layout: provider
modified: '2026-05-19'
name: HMRC UK Tax Authority
nav: Providers
network: true
overview: 'HMRC UK Tax Authority publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Liabilities API, Obligations API, Payments API, and 1 more. Tagged areas include Government, Making Tax Digital, Regulatory, Tax, and UK.


  The HMRC UK Tax Authority catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HMRC UK Tax Authority''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, and 14 more developer resources.'
plans:
- name: Hmrc Plans Pricing
  plan_count: 2
  slug: hmrc-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Hmrc Rate Limits
  slug: hmrc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: HMRC UK Tax Authority API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hmrc-jsonschema-spectral-rules
scopes:
- name: Hmrc Scopes
  scope_count: 2
  slug: hmrc-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 47.9
  delta: 1.4
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 59.5
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 61.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/screenshots/hmrc-2026-06-20T182805.png
security:
- kind: authentication
  name: Hmrc Authentication
  slug: hmrc-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hmrc Domain Security
  slug: hmrc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hmrc Vulnerability Disclosure
  slug: hmrc-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hmrc
tags:
- Government
- Making Tax Digital
- Regulatory
- Tax
- UK
website: https://www.gov.uk/government/organisations/hm-revenue-customs
---
