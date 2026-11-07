---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: self
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: GraphQL API for EcoCitizenz platform providing identity and trust operations.
  name: EcoCitizenz GraphQL API
  slug: ecocitizenz-graphql-api
- baseURL: https://trustops.ecocitizenz.com
  baseurl_source: declared
  description: 'EcoCitizenz API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: EcoCitizenz API
  slug: ecocitizenz-com-api
artifact_total: 9
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ecocitizenz.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ecocitizenz.com/policies/privacy-policy
- group: design
  href: https://artifacts.apis.io/ecocitizenz-com/rules/ecocitizenz-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ecocitizenz-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ecocitizenz-com/json-ld/ecocitizenz-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ecocitizenz-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ecocitizenz-com/vocabulary/ecocitizenz-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ecocitizenz-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ecocitizenz-com/data-model/ecocitizenz-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ecocitizenz-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ecocitizenz-com/conformance/ecocitizenz-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ecocitizenz-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ecocitizenz-com/llms/ecocitizenz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecocitizenz-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ecocitizenz-com/well-known/ecocitizenz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecocitizenz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecocitizenz-com/hosts/ecocitizenz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecocitizenz-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecocitizenz-com/vendors/ecocitizenz-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecocitizenz-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/ecocitizenz-com/packages/ecocitizenz-com-packages.yml
  title: ''
  type: SDKs
  url: packages/ecocitizenz-com-packages.yml
- group: build
  href: https://artifacts.apis.io/ecocitizenz-com/packages/ecocitizenz-com-packages.yml
  title: ''
  type: Packages
  url: packages/ecocitizenz-com-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.ecocitizenz.com/blogs/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.ecocitizenz.com/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ecocitizenz
- group: auth
  href: https://artifacts.apis.io/ecocitizenz-com/security/ecocitizenz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecocitizenz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ecocitizenz.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ecocitizenz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ecocitizenz.com/pages/why-ecz-id
- group: docs
  title: ''
  type: APIReference
  url: https://developers.ecocitizenz.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ecocitizenz.com/pages/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://www.ecocitizenz.com/pages/website-security-review
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ecocitizenz.com/pages/for-businesses
created: '2026-11-06'
description: EcoCitizenz provides the ECZ-ID platform, a neutral identity and authority reference layer that enables businesses to create, manage, and verify digital passports for entities, devices, and services. The platform offers tools for trust verification, governance, and security reviews, targeting enterprises, CIOs, and developers seeking automated identity assurance and compliance. It integrates with developer gateways, trust‑ops, and ecosystem partners to deliver end‑to‑end provenance and accountability across the machine economy.
image: http://www.ecocitizenz.com/cdn/shop/files/Logo.png?v=1770328906
json_schemas:
- name: GetApiV1AcquisitionFamiliesResponse
  property_count: 1
  slug: ecocitizenz-com-get-api-v1-acquisition-families-response
- name: GetWellKnownEczMcpJsonResponse
  property_count: 2
  slug: ecocitizenz-com-get-well-known-ecz-mcp-json-response
- name: PostApiV1ResolveNativeRequest
  property_count: 3
  slug: ecocitizenz-com-post-api-v1-resolve-native-request
- name: PostApiV1ResolveNativeResponse
  property_count: 4
  slug: ecocitizenz-com-post-api-v1-resolve-native-response
jsonld:
- class_count: 4
  name: Ecocitizenz Com Context
  property_count: 10
  slug: ecocitizenz-com-context
layout: provider
modified: '2026-11-06'
name: EcoCitizenz
nav: Providers
network: true
overview: 'EcoCitizenz is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Trust, Security, Platform, and Enterprise.


  The EcoCitizenz catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EcoCitizenz''s developer surface includes changelog, documentation, API reference, getting-started guide, support, pricing, and 18 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: EcoCitizenz API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: ecocitizenz-com-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 22.3
    developer_ergonomics: 50.0
    discoverability: 67.9
    operational_transparency: 21.1
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
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ecocitizenz Com Domain Security
  slug: ecocitizenz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ecocitizenz-com
tags:
- Identity
- Trust
- Security
- Platform
- Enterprise
website: https://www.ecocitizenz.com/
---
