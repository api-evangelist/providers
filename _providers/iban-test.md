---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: IBAN Validation API provides endpoints to validate IBAN numbers, retrieve bank details, and generate test IBANs.
  name: IBAN Validation API
  slug: iban-validation-api
- description: 'ToadTec API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: ToadTec API
  slug: iban-test-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/iban-test/rules/iban-test-rules.yml
  title: ''
  type: Spectral
  url: rules/iban-test-rules.yml
- group: design
  href: https://artifacts.apis.io/iban-test/json-ld/iban-test-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/iban-test-context.jsonld
- group: design
  href: https://artifacts.apis.io/iban-test/vocabulary/iban-test-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/iban-test-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/iban-test/data-model/iban-test-data-model.yml
  title: ''
  type: DataModel
  url: data-model/iban-test-data-model.yml
- group: auth
  href: https://artifacts.apis.io/iban-test/authentication/iban-test-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iban-test-authentication.yml
- group: design
  href: https://artifacts.apis.io/iban-test/conformance/iban-test-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iban-test-conformance.yml
- group: agent
  href: https://artifacts.apis.io/iban-test/well-known/iban-test-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/iban-test-well-known.yml
- group: other
  href: https://artifacts.apis.io/iban-test/hosts/iban-test-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iban-test-hosts.yml
- group: auth
  href: https://artifacts.apis.io/iban-test/security/iban-test-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iban-test-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iban-test.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://www.iban-test.eu/API-Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.iban-test.eu/api/docs/IbanTest/html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.iban-test.eu/guides
- group: operate
  title: ''
  type: Support
  url: https://www.iban-test.eu/Contact
- group: company
  title: ''
  type: Blog
  url: https://www.iban-test.eu/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iban-test.eu/Registration
- group: start
  title: ''
  type: SignUp
  url: https://www.iban-test.eu/Registration
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iban-test.eu/Terms-and-Conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iban-test.eu/Privacy-Policy
coverage:
  checked: '2026-10-18'
  detail: The provider's documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract could be found after probing common spec locations.
  evidence:
  - status: 404
    url: https://iban-test.eu/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: ToadTec provides a free IBAN validation service and API, allowing developers to verify IBAN formats, check digits, and retrieve bank details for over 115 formats across 40 countries. The platform offers both online checking and API access with 10 free requests daily, plus paid plans for higher volume. Features include IBAN generation, bank directory lookup, and integration guides for various programming environments.
image: https://www.iban-test.eu/media/cache/ibanTest/6a325c12ebe869_11416744-iban-test-social-sharing-en.png
json_schemas:
- name: GetApiV2IbanValidateResponse
  property_count: 4
  slug: iban-test-get-api-v2-iban-validate-response
- name: GetV2BankAccountValidateResponse
  property_count: 4
  slug: iban-test-get-v2-bank-account-validate-response
- name: GetV2BicValidateBicResponse
  property_count: 4
  slug: iban-test-get-v2-bic-validate-bic-response
- name: GetV2IbanGenerateResponse
  property_count: 4
  slug: iban-test-get-v2-iban-generate-response
- name: GetV2IbanValidateIbanResponse
  property_count: 4
  slug: iban-test-get-v2-iban-validate-iban-response
- name: GetV2IbanValidateResponse
  property_count: 4
  slug: iban-test-get-v2-iban-validate-response
jsonld:
- class_count: 10
  name: Iban Test Context
  property_count: 8
  slug: iban-test-context
layout: provider
modified: '2026-10-17'
name: ToadTec
nav: Providers
network: true
overview: 'ToadTec is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Payments, and Validation.


  The ToadTec catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ToadTec''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 12 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: ToadTec API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: iban-test-rules
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 22.8
    developer_ergonomics: 29.8
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 32.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/iban-test/iban-test-2026-11-03T133603.png
security:
- kind: authentication
  name: Iban Test Authentication
  slug: iban-test-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Iban Test Domain Security
  slug: iban-test-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iban-test
tags:
- Company
- Finance
- Payments
- Validation
website: https://iban-test.eu/
---
