---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Tessio Eu Agentic Access
  operation_count: 12
  slug: tessio-eu-agentic-access
  summary_line: 12 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.tessio.eu
  baseurl_source: declared
  description: The Age Verification API from tessio-eu — 2 operation(s) for age verification.
  name: tessio-eu Age Verification API
  slug: tessio-eu-age-verification-api
- baseURL: https://api.tessio.eu
  baseurl_source: declared
  description: The Stats API from tessio-eu — 5 operation(s) for stats.
  name: tessio-eu Stats API
  slug: tessio-eu-stats-api
- baseURL: https://api.tessio.eu
  baseurl_source: declared
  description: The Webhooks API from tessio-eu — 2 operation(s) for webhooks.
  name: tessio-eu Webhooks API
  slug: tessio-eu-webhooks-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/tessio-eu/agentic-access/tessio-eu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tessio-eu-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/tessio-eu/plans/tessio-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tessio-eu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tessio-eu/rules/tessio-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/tessio-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/tessio-eu/json-ld/tessio-eu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tessio-eu-context.jsonld
- group: design
  href: https://artifacts.apis.io/tessio-eu/vocabulary/tessio-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tessio-eu-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tessio-eu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tessio-eu/data-model/tessio-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tessio-eu-data-model.yml
- group: design
  href: https://artifacts.apis.io/tessio-eu/conventions/tessio-eu-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tessio-eu-conventions.yml
- group: design
  href: https://artifacts.apis.io/tessio-eu/conventions/tessio-eu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tessio-eu-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://tessio.eu/security/
- group: auth
  title: ''
  type: Security
  url: https://tessio.eu/security
- group: auth
  href: https://artifacts.apis.io/tessio-eu/authentication/tessio-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tessio-eu-authentication.yml
- group: auth
  href: https://artifacts.apis.io/tessio-eu/scopes/tessio-eu-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tessio-eu-scopes.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tessio.eu
- group: design
  href: https://artifacts.apis.io/tessio-eu/lifecycle/tessio-eu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tessio-eu-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tessio-eu/errors/tessio-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tessio-eu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tessio-eu/conformance/tessio-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tessio-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tessio-eu/llms/tessio-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tessio-eu-llms.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-pid-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-pid-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-pid-sdjwt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-pid-sdjwt-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-photoid-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-photoid-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-labs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-labs-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-interop-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-interop-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-conformance-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-conformance-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-cloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-cloud-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-av-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-av-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-api-security.txt
- group: auth
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-annexc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tessio-eu-annexc-security.txt
- group: agent
  href: https://artifacts.apis.io/tessio-eu/well-known/tessio-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tessio-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/tessio-eu/hosts/tessio-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tessio-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/tessio-eu/vendors/tessio-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tessio-eu-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://cloud.tessio.eu/login
- group: auth
  href: https://artifacts.apis.io/tessio-eu/security/tessio-eu-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tessio-eu-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tessio-eu/security/tessio-eu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tessio-eu-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tessio-eu/security/tessio-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tessio-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tessio.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://tessio.eu/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://tessio.eu/docs/api/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tessio.eu/for/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://tessio.eu/docs/
- group: operate
  title: ''
  type: Support
  url: https://tessio.eu/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://tessio.eu/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tessio.eu/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tessio.eu/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tripledownab
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.tessio.eu/v1/openapi.json
  - status: null
    url: https://cloud.tessio.eu/openapi.json
  - status: 401
    url: https://api.tessio.eu/mcp
  - status: 401
    url: https://cloud.tessio.eu/api/mcp
  - status: 200
    url: https://tessio.eu/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Tessio.Cloud provides an age verification API for the EU digital wallet ecosystem. It enables applications to verify that users are over 18 via the EU age verification app, returning a signed yes or no without storing personal ID data. The service is built by Triple Down AB in Stockholm, Sweden, and offers webhook callbacks and statistical endpoints.
image: https://tessio.eu/favicon.svg
json_schemas:
- name: AgeCheckCreated
  property_count: 5
  slug: tessio-eu-age-check-created
- name: AgeCheck
  property_count: 7
  slug: tessio-eu-age-check
- name: AgeCheckStatsSeries
  property_count: 5
  slug: tessio-eu-age-check-stats-series
- name: CreateAgeCheckRequest
  property_count: 3
  slug: tessio-eu-create-age-check-request
- name: SetWebhookRequest
  property_count: 2
  slug: tessio-eu-set-webhook-request
- name: WebhookCreated
  property_count: 3
  slug: tessio-eu-webhook-created
jsonld:
- class_count: 26
  name: Tessio Eu Context
  property_count: 59
  slug: tessio-eu-context
layout: provider
modified: '2026-10-31'
name: tessio-eu
nav: Providers
network: true
overview: 'tessio-eu publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Age Verification API, Stats API, and Webhooks API. Tagged areas include Company, Age Verification, EU, and Identity.


  The tessio-eu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tessio-eu''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 40 more developer resources.'
plans:
- name: Tessio Eu Plans Pricing
  plan_count: 4
  slug: tessio-eu-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: tessio-eu API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: tessio-eu-rules
scopes:
- name: Tessio Eu Scopes
  scope_count: 2
  slug: tessio-eu-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.4
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 63.2
    developer_ergonomics: 39.8
    discoverability: 57.1
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 64.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tessio-eu/tessio-eu-2026-11-03T144501.png
security:
- kind: authentication
  name: Tessio Eu Authentication
  slug: tessio-eu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tessio Eu Domain Security
  slug: tessio-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tessio Eu Vulnerability Disclosure
  slug: tessio-eu-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tessio Eu Trust Center
  slug: tessio-eu-trust-center
  summary_line: SOC 2, ISO 27001
slug: tessio-eu
tags:
- Company
- Age Verification
- EU
- Identity
website: https://tessio.eu/
---
