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
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Astra Agentic Access
  operation_count: 45
  slug: astra-agentic-access
  summary_line: 45 operations · 24 acting
api_count: 1
apis:
- baseURL: https://api.astra.finance/v1
  baseurl_source: declared
  description: The Accounts API from Astra — 4 operation(s) for accounts.
  name: Astra Accounts API
  slug: astra-accounts-api
- baseURL: https://api.astra.finance/v1
  baseurl_source: declared
  description: The Authorization API from Astra — 3 operation(s) for authorization.
  name: Astra Authorization API
  slug: astra-authorization-api
- baseURL: https://api.astra.finance/v1
  baseurl_source: declared
  description: The Cards API from Astra — 6 operation(s) for cards.
  name: Astra Cards API
  slug: astra-cards-api
- baseURL: https://api.astra.finance/v1
  baseurl_source: declared
  description: The Instant Payment Eligibility API from Astra — 1 operation(s) for instant payment eligibility.
  name: Astra Instant Payment Eligibility API
  slug: astra-instant-payment-eligibility-api
- baseURL: https://api.astra.finance/v1
  baseurl_source: declared
  description: The Payment Instruments API from Astra — 2 operation(s) for payment instruments.
  name: Astra Payment Instruments API
  slug: astra-payment-instruments-api
- baseURL: https://api.astra.finance/v1
  baseurl_source: declared
  description: The Routines API from Astra — 7 operation(s) for routines.
  name: Astra Routines API
  slug: astra-routines-api
- baseURL: https://api.astra.finance/v1
  baseurl_source: declared
  description: The Transfers API from Astra — 5 operation(s) for transfers.
  name: Astra Transfers API
  slug: astra-transfers-api
- baseURL: https://api.astra.finance/v1
  baseurl_source: declared
  description: The User API from Astra — 11 operation(s) for user.
  name: Astra User API
  slug: astra-user-api
artifact_total: 16
asyncapis:
- description: ''
  name: Astra Webhooks
  slug: astra-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/agentic-access/astra-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/astra-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/rules/astra-rules.yml
  title: ''
  type: Spectral
  url: rules/astra-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/json-ld/astra-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/astra-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/vocabulary/astra-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/astra-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/data-model/astra-data-model.yml
  title: ''
  type: DataModel
  url: data-model/astra-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/conventions/astra-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/astra-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/security/astra-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/astra-trust-center.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/lifecycle/astra-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/astra-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/errors/astra-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/astra-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/hosts/astra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astra-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/vendors/astra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astra-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://astra.finance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/security/astra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astra-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.astra.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.astra.finance/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.astra.finance/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.astra.finance/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://astrafi.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://dashboard-sandbox.astra.finance/support
- group: start
  title: ''
  type: SignUp
  url: https://dashboard-sandbox.astra.finance/login
- group: start
  title: ''
  type: Login
  url: https://dashboard.astra.finance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astrafi.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astrafi.com/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.astrafi.com/
- group: auth
  title: ''
  type: Compliance
  url: https://astrafi.com/security-and-privacy/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/llms/astra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astra-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/authentication/astra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/astra-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/conventions/astra-conventions.yml
  title: ''
  type: Conventions
  url: conventions/astra-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/errors/astra-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/astra-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/asyncapi/astra-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/astra-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/lifecycle/astra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/astra-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/sandbox/astra-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/astra-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/conformance/astra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astra-conformance.yml
created: '2026-07-17'
description: Astra (Astra Finance, Inc.) is a financial technology company providing an all-in-one instant payments API that lets product teams embed real-time money movement between bank accounts and debit cards. The platform powers instant disbursements and payouts, instant account funding, accelerated bank transfers, card-to-account movement, cross-border payments, and automated "Routines," with built-in compliance, fraud detection, and chargeback management. Developers integrate over a versioned REST API (v1) using OAuth 2.0 authorization for end-user money movement plus client-credential authorization for administrative operations, with webhooks for asynchronous updates and a full sandbox environment for testing.
image: https://astrafi.com/static/images/favicons/apple-touch-icon.png
json_schemas:
- name: oauth_success_response
  property_count: 4
  slug: astra-oauth-success-response
jsonld:
- class_count: 5
  name: Astra Context
  property_count: 10
  slug: astra-context
layout: provider
modified: '2026-09-16'
name: Astra
nav: Providers
network: true
overview: 'Astra publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Authorization API, Cards API, and 5 more. Tagged areas include Company, Payments, Fintech, Money Movement, and ACH.


  The Astra catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Astra''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 26 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Astra API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 1
  slug: astra-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 59.2
    catalog_earned_first_party: 0.0
    catalog_gap: 55.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.1
  facets:
    access_clarity: 35.5
    contract_governance: 35.6
    contract_quality: 69.6
    developer_ergonomics: 40.5
    discoverability: 73.2
    operational_transparency: 15.8
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/screenshots/astra-2026-07-25T201458.png
security:
- kind: authentication
  name: Astra Authentication
  slug: astra-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Astra Domain Security
  slug: astra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Astra Trust Center
  slug: astra-trust-center
  summary_line: SOC 2, PCI DSS, GDPR, CCPA/CPRA
slug: astra
tags:
- Company
- Payments
- Fintech
- Money Movement
- ACH
- Instant Payments
- Bank Transfers
- Disbursements
website: https://astra.finance
---
