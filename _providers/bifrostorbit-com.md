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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for Bifröst Orbit's platform, covering CMS, travel booking, commerce and presence services.
  name: Bifröst Orbit API
  slug: bifr-st-orbit-api
- baseURL: https://api.bifrostorbit.com
  baseurl_source: declared
  description: 'Bifröst Orbit API as documented publicly: 26 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Bifröst Orbit API
  slug: bifrostorbit-com-api
artifact_total: 13
asyncapis:
- description: ''
  name: Bifrostorbit Com Webhooks
  slug: bifrostorbit-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/bifrostorbit-com/rules/bifrostorbit-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bifrostorbit-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bifrostorbit-com/json-ld/bifrostorbit-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bifrostorbit-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bifrostorbit-com/vocabulary/bifrostorbit-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bifrostorbit-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bifrostorbit-com/asyncapi/bifrostorbit-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bifrostorbit-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bifrostorbit-com/data-model/bifrostorbit-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bifrostorbit-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bifrostorbit-com/changelog/bifrostorbit-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bifrostorbit-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/bifrostorbit-com/conformance/bifrostorbit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bifrostorbit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bifrostorbit-com/llms/bifrostorbit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bifrostorbit-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/bifrostorbit-com/well-known/bifrostorbit-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bifrostorbit-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bifrostorbit-com/well-known/bifrostorbit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bifrostorbit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bifrostorbit-com/hosts/bifrostorbit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bifrostorbit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bifrostorbit-com/vendors/bifrostorbit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bifrostorbit-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bifrostorbit.com/legal/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.bifrostorbit.com/status/
- group: auth
  title: ''
  type: Security
  url: https://bifrostorbit.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bifrostorbit.com/legal/privacy/
- group: start
  title: ''
  type: Login
  url: https://app.bifrostorbit.com/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bifrost-orbit
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bifrostorbit.com/developers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bifrostorbit.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://bifrostorbit.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.bifrostorbit.com/orbit/admins/plans-and-billing/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bifrostorbit.com/orbit/everyone/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bifrostorbit.com/
- group: auth
  href: https://artifacts.apis.io/bifrostorbit-com/security/bifrostorbit-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bifrostorbit-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bifrostorbit-com/security/bifrostorbit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bifrostorbit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bifrostorbit.com/
coverage:
  checked: '2026-11-02'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found after exhaustive probing.
  evidence:
  - status: 404
    url: https://api.bifrostorbit.com/openapi.json
  - status: 404
    url: https://api.bifrostorbit.com/openapi.yaml
  - status: 404
    url: https://api.bifrostorbit.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bifröst Orbit provides a unified sign‑in platform that connects an organization’s tools, roles and AI agents behind a single authentication. It offers modular products for CMS, travel booking, commerce and presence, enabling teams to integrate and manage services with shared identity and AI‑driven automation.
image: https://api.bifrostorbit.com/cms/uploads/6ad4a6d7f731235918cb3dd1/6ad4a6d8f731235918cb3dd4/share-2a87d51f.webp?format=jpeg
json_schemas:
- name: GetContentResponse
  property_count: 9
  slug: bifrostorbit-com-get-content-response
- name: GetGlobalResponse
  property_count: 6
  slug: bifrostorbit-com-get-global-response
- name: GetListResponse
  property_count: 4
  slug: bifrostorbit-com-get-list-response
- name: GetProductsResponse
  property_count: 4
  slug: bifrostorbit-com-get-products-response
- name: GetResolveResponse
  property_count: 5
  slug: bifrostorbit-com-get-resolve-response
- name: PostTravelApiCdnGraphqlRequest
  property_count: 2
  slug: bifrostorbit-com-post-travel-api-cdn-graphql-request
jsonld:
- class_count: 14
  name: Bifrostorbit Com Context
  property_count: 25
  slug: bifrostorbit-com-context
layout: provider
modified: '2026-11-02'
name: Bifröst Orbit
nav: Providers
network: true
overview: 'Bifröst Orbit is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Authentication, Software-as-a-Service, and Platform.


  The Bifröst Orbit catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bifröst Orbit''s developer surface includes changelog, engineering blog, pricing, getting-started guide, documentation, and 22 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Bifröst Orbit API Rules
  rule_count: 46
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 3
  slug: bifrostorbit-com-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 33.7
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 31.6
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bifrostorbit Com Domain Security
  slug: bifrostorbit-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bifrostorbit Com Vulnerability Disclosure
  slug: bifrostorbit-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bifrostorbit-com
tags:
- Company
- Identity
- Authentication
- Software-as-a-Service
- Platform
website: https://bifrostorbit.com/
---
