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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for ConsentStack consent management platform
  name: ConsentStack API
  slug: consentstack-api
- baseURL: https://origins.consentstack.io
  baseurl_source: declared
  description: 'ConsentStack API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ConsentStack API
  slug: consentstack-io-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/consentstack-io/plans/consentstack-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consentstack-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/consentstack-io/rules/consentstack-io-rules.yml
  title: ''
  type: Spectral
  url: rules/consentstack-io-rules.yml
- group: design
  href: https://artifacts.apis.io/consentstack-io/json-ld/consentstack-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/consentstack-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/consentstack-io/vocabulary/consentstack-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/consentstack-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/consentstack-io/data-model/consentstack-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/consentstack-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/consentstack-io/changelog/consentstack-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/consentstack-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/consentstack-io/authentication/consentstack-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/consentstack-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/consentstack-io/errors/consentstack-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/consentstack-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/consentstack-io/conformance/consentstack-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consentstack-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/consentstack-io/llms/consentstack-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/consentstack-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/consentstack-io/well-known/consentstack-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/consentstack-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/consentstack-io/hosts/consentstack-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/consentstack-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/consentstack-io/vendors/consentstack-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/consentstack-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.consentstack.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.consentstack.io/docs/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://www.consentstack.io/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.consentstack.io/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/consentstack-io/security/consentstack-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consentstack-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://consentstack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.consentstack.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.consentstack.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.consentstack.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.consentstack.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.consentstack.io/privacy-policy
coverage:
  checked: '2026-11-04'
  detail: API reference page is a JavaScript‑rendered site with no machine‑readable OpenAPI spec discovered
  evidence:
  - status: 200
    url: https://www.consentstack.io/docs/api-reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: ConsentStack provides a modern consent management platform for websites, supporting over 195 privacy laws including GDPR, CCPA, and ePrivacy. It offers script blocking, Google Consent Mode v2 integration, real‑time analytics, and a customizable consent banner to help businesses stay compliant and respect user privacy.
image: https://www.consentstack.io/opengraph-image-c43v9f?707e7de40cc2c668
json_schemas:
- name: GetFunctionsV1ConfigResponse
  property_count: 10
  slug: consentstack-io-get-functions-v1-config-response
- name: PostFunctionsV1ConsentRequest
  property_count: 18
  slug: consentstack-io-post-functions-v1-consent-request
- name: PostFunctionsV1ConsentResponse
  property_count: 1
  slug: consentstack-io-post-functions-v1-consent-response
- name: PostFunctionsV1ScriptsRequest
  property_count: 5
  slug: consentstack-io-post-functions-v1-scripts-request
- name: PostFunctionsV1ScriptsResponse
  property_count: 1
  slug: consentstack-io-post-functions-v1-scripts-response
jsonld:
- class_count: 5
  name: Consentstack Io Context
  property_count: 32
  slug: consentstack-io-context
layout: provider
modified: '2026-11-04'
name: ConsentStack
nav: Providers
network: true
overview: 'ConsentStack is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consent Management, Privacy, GDPR, and CCPA.


  The ConsentStack catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ConsentStack''s developer surface includes changelog, authentication, API reference, getting-started guide, documentation, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Consentstack Io Plans Pricing
  plan_count: 3
  slug: consentstack-io-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: ConsentStack API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: consentstack-io-rules
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 26.5
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Consentstack Io Authentication
  slug: consentstack-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Consentstack Io Domain Security
  slug: consentstack-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: consentstack-io
tags:
- Company
- Consent Management
- Privacy
- GDPR
- CCPA
- Cookie
website: https://consentstack.io/
---
