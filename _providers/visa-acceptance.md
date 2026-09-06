---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Visa Acceptance Agentic Access
  operation_count: 13
  slug: visa-acceptance-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.visaacceptance.com
  baseurl_source: spec
  description: Capture previously authorized payments
  name: Visa Acceptance Captures API
  slug: visa-acceptance-captures-api
- baseURL: https://api.visaacceptance.com
  baseurl_source: spec
  description: Create and manage invoices for payment collection
  name: Visa Acceptance Invoices API
  slug: visa-acceptance-invoices-api
- baseURL: https://api.visaacceptance.com
  baseurl_source: spec
  description: Generate and manage payment links
  name: Visa Acceptance Pay by Link API
  slug: visa-acceptance-pay-by-link-api
- baseURL: https://api.visaacceptance.com
  baseurl_source: spec
  description: Payment authorization, capture, sale, and reversal
  name: Visa Acceptance Payments API
  slug: visa-acceptance-payments-api
- baseURL: https://api.visaacceptance.com
  baseurl_source: spec
  description: Refund and credit operations
  name: Visa Acceptance Refunds API
  slug: visa-acceptance-refunds-api
- baseURL: https://api.visaacceptance.com
  baseurl_source: spec
  description: Void authorized, captured, or credited transactions
  name: Visa Acceptance Voids API
  slug: visa-acceptance-voids-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Visa Acceptance Payments Captures API
  slug: open-visa-acceptance-captures-api
- collection_type: open
  name: Visa Acceptance Payments Captures Invoices API
  slug: open-visa-acceptance-invoices-api
- collection_type: open
  name: Visa Acceptance Payments Captures Pay by Link API
  slug: open-visa-acceptance-pay-by-link-api
- collection_type: open
  name: Visa Acceptance Captures Payments API
  slug: open-visa-acceptance-payments-api
- collection_type: open
  name: Visa Acceptance Payments API
  slug: open-visa-acceptance-payments
- collection_type: open
  name: Visa Acceptance Payments Captures Refunds API
  slug: open-visa-acceptance-refunds-api
- collection_type: open
  name: Visa Acceptance Payments Captures Voids API
  slug: open-visa-acceptance-voids-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/visa-acceptance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/visa-acceptance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/visa-acceptance-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/visaacceptance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/visa-acceptance-solutions
- group: company
  title: ''
  type: Website
  url: https://developer.visaacceptance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.visaacceptance.com/docs.html
- group: start
  title: ''
  type: Sandbox
  url: https://developer.visaacceptance.com/hello-world/sandbox.html
- group: operate
  title: ''
  type: Support
  url: https://developer.visaacceptance.com/support/contact-us.html
- group: build
  title: ''
  type: ResponseCodes
  url: https://developer.visaacceptance.com/api/reference/response-codes.html
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/visa-acceptance-payment-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/visa-acceptance-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/visa-acceptance-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/visa-acceptance-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.visaacceptance.com/llms.txt
created: '2025-02-17'
description: Visa Acceptance Solutions (powered by CyberSource) is the developer platform for accepting payments online, in-person, and via mobile. The platform provides REST APIs for payment authorization, capture, refund, void, reversal, invoicing, and pay-by-link. Authentication uses JWT with RSA key pairs, with support for Intelligent Commerce APIs enabling AI agent-initiated payments.
examples:
- key_count: 2
  name: Visa Acceptance Authorize Payment Example
  slug: visa-acceptance-authorize-payment-example
- key_count: 2
  name: Visa Acceptance Capture Payment Example
  slug: visa-acceptance-capture-payment-example
- key_count: 2
  name: Visa Acceptance Create Invoice Example
  slug: visa-acceptance-create-invoice-example
- key_count: 2
  name: Visa Acceptance Create Pay By Link Example
  slug: visa-acceptance-create-pay-by-link-example
- key_count: 2
  name: Visa Acceptance Refund Payment Example
  slug: visa-acceptance-refund-payment-example
finops:
- name: Visa Acceptance Finops
  service_category: Payments
  slug: visa-acceptance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/visa-acceptance.png
json_schemas:
- name: Visa Acceptance Payment
  property_count: 7
  slug: visa-acceptance-payment
json_structures:
- name: Visa Acceptance Payment Structure
  property_count: 0
  slug: visa-acceptance-payment-structure
jsonld:
- class_count: 0
  name: Visa Acceptance Context
  property_count: 25
  slug: visa-acceptance-context
layout: provider
modified: '2026-05-19'
name: Visa Acceptance
nav: Providers
network: true
overview: 'Visa Acceptance publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Captures API, Invoices API, Pay by Link API, and 3 more. Tagged areas include Payments, E-Commerce, Fintech, Credit Cards, and Invoicing.


  The Visa Acceptance catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Visa Acceptance''s developer surface includes authentication, documentation, sandbox, support, and 11 more developer resources.'
plans:
- name: Visa Acceptance Plans Pricing
  plan_count: 1
  slug: visa-acceptance-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Visa Acceptance Rate Limits
  slug: visa-acceptance-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Visa Acceptance API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: visa-acceptance-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Visa Acceptance API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: visa-acceptance-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 63.2
    developer_ergonomics: 45.2
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/visa-acceptance/refs/heads/main/screenshots/visa-acceptance-2026-06-20T201047.png
security:
- kind: authentication
  name: Visa Acceptance Authentication
  slug: visa-acceptance-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Visa Acceptance Domain Security
  slug: visa-acceptance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: visa-acceptance
tags:
- Payments
- E-Commerce
- Fintech
- Credit Cards
- Invoicing
- Payment Links
- Digital Wallet
website: https://developer.visaacceptance.com/
---
