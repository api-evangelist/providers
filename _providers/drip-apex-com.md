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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.drip-apex.com
  baseurl_source: declared
  description: 'DRIP Apex API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: DRIP Apex API
  slug: drip-apex-com-api
artifact_total: 13
asyncapis:
- description: ''
  name: Drip Apex Com Webhooks
  slug: drip-apex-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/drip-apex-com/rules/drip-apex-com-rules.yml
  title: ''
  type: Spectral
  url: rules/drip-apex-com-rules.yml
- group: design
  href: https://artifacts.apis.io/drip-apex-com/json-ld/drip-apex-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/drip-apex-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/drip-apex-com/vocabulary/drip-apex-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/drip-apex-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/drip-apex-com/asyncapi/drip-apex-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/drip-apex-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/drip-apex-com/data-model/drip-apex-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drip-apex-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/drip-apex-com/conventions/drip-apex-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/drip-apex-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/drip-apex-com/conventions/drip-apex-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/drip-apex-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.drip-apex.com/
- group: auth
  href: https://artifacts.apis.io/drip-apex-com/authentication/drip-apex-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drip-apex-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/drip-apex-com/conformance/drip-apex-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drip-apex-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/drip-apex-com/llms/drip-apex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drip-apex-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/drip-apex-com/well-known/drip-apex-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/drip-apex-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/drip-apex-com/well-known/drip-apex-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drip-apex-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/drip-apex-com/hosts/drip-apex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drip-apex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/drip-apex-com/vendors/drip-apex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drip-apex-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drip-apex.com/terms
- group: auth
  title: ''
  type: Security
  url: https://www.drip-apex.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.drip-apex.com/legal/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://docs.drip-apex.com/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.drip-apex.com/docs/getting-started/what-is-apex
- group: docs
  title: ''
  type: Documentation
  url: https://docs.drip-apex.com/
- group: auth
  href: https://artifacts.apis.io/drip-apex-com/security/drip-apex-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/drip-apex-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/drip-apex-com/security/drip-apex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drip-apex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drip-apex.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.drip-apex.com/api/mcp
  - status: 200
    url: https://drip-apex.com/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DRIP Apex provides an A/B testing platform that leverages AI to predict experiment outcomes before traffic exposure. The service offers features such as multi‑test experimentation, likelihood‑to‑win scoring, a genome of millions of past tests, feature‑flag management, personalization with holdback, and integrations with Shopify, Shopware, WooCommerce and more. It supplies a versioned REST API, webhooks, a CLI, MCP and SDKs, along with comprehensive documentation and security & privacy compliance.
image: https://www.drip-apex.com/images/apex-site/og.png?v=2
json_schemas:
- name: GetHealthResponse
  property_count: 9
  slug: drip-apex-com-get-health-response
- name: PatchApiV1FlagsIdCodeRequest
  property_count: 3
  slug: drip-apex-com-patch-api-v1-flags-id-code-request
- name: PostApiV1AdminClientLinksRequest
  property_count: 15
  slug: drip-apex-com-post-api-v1-admin-client-links-request
- name: PostApiV1AdminClientLinksResponse
  property_count: 7
  slug: drip-apex-com-post-api-v1-admin-client-links-response
- name: PostSosRequest
  property_count: 11
  slug: drip-apex-com-post-sos-request
- name: PostSosResponse
  property_count: 7
  slug: drip-apex-com-post-sos-response
jsonld:
- class_count: 16
  name: Drip Apex Com Context
  property_count: 49
  slug: drip-apex-com-context
layout: provider
modified: '2026-11-05'
name: DRIP Apex
nav: Providers
network: true
overview: 'DRIP Apex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include A/B Testing, Artificial Intelligence, Marketing, Feature Flags, and Personalization.


  The DRIP Apex catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DRIP Apex''s developer surface includes authentication, API reference, getting-started guide, documentation, and 20 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: DRIP Apex API Rules
  rule_count: 47
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 5
  slug: drip-apex-com-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 33.7
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Drip Apex Com Authentication
  slug: drip-apex-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Drip Apex Com Domain Security
  slug: drip-apex-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Drip Apex Com Trust Center
  slug: drip-apex-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: drip-apex-com
tags:
- A/B Testing
- Artificial Intelligence
- Marketing
- Feature Flags
- Personalization
website: https://drip-apex.com/
---
