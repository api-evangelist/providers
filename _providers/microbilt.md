---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Microbilt provides various verification APIs such as Bank Account Verification, as listed on their developer portal.
  name: Microbilt API
  slug: microbilt-api-2
- baseURL: https://apitest.microbilt.com
  baseurl_source: declared
  description: 'Microbilt API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Microbilt API
  slug: microbilt-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/microbilt/rules/microbilt-rules.yml
  title: ''
  type: Spectral
  url: rules/microbilt-rules.yml
- group: design
  href: https://artifacts.apis.io/microbilt/json-ld/microbilt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microbilt-context.jsonld
- group: design
  href: https://artifacts.apis.io/microbilt/vocabulary/microbilt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microbilt-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microbilt/data-model/microbilt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microbilt-data-model.yml
- group: auth
  href: https://artifacts.apis.io/microbilt/authentication/microbilt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microbilt-authentication.yml
- group: design
  href: https://artifacts.apis.io/microbilt/conformance/microbilt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microbilt-conformance.yml
- group: other
  href: https://artifacts.apis.io/microbilt/hosts/microbilt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microbilt-hosts.yml
- group: other
  href: https://artifacts.apis.io/microbilt/vendors/microbilt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microbilt-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.microbilt.com/legal-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.microbilt.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.microbilt.com/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://developer.microbilt.com/
- group: auth
  href: https://artifacts.apis.io/microbilt/security/microbilt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microbilt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://microbilt.com/
created: '2026-10-20'
description: 'Microbilt is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: PostOauthGetaccesstokenRequest
  property_count: 3
  slug: microbilt-post-oauth-getaccesstoken-request
- name: PostOauthGetaccesstokenResponse
  property_count: 5
  slug: microbilt-post-oauth-getaccesstoken-response
- name: PostOauthTokenRequest
  property_count: 3
  slug: microbilt-post-oauth-token-request
- name: PostOauthTokenResponse
  property_count: 5
  slug: microbilt-post-oauth-token-response
jsonld:
- class_count: 4
  name: Microbilt Context
  property_count: 8
  slug: microbilt-context
layout: provider
modified: '2026-10-20'
name: Microbilt
nav: Providers
network: true
overview: 'Microbilt is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Credit Decisioning, Identity Verification, Background Screening, Business Credentialing, and Risk Management.


  The Microbilt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microbilt''s developer surface includes authentication, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Microbilt API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: microbilt-rules
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 44.8
    catalog_earned_first_party: 0.0
    catalog_gap: 70.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 21.8
    developer_ergonomics: 22.6
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 21.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microbilt/microbilt-2026-11-03T135549.png
security:
- kind: authentication
  name: Microbilt Authentication
  slug: microbilt-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Microbilt Domain Security
  slug: microbilt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microbilt
tags:
- Credit Decisioning
- Identity Verification
- Background Screening
- Business Credentialing
- Risk Management
- Alternative Credit Data
- Compliance
website: https://microbilt.com/
---
