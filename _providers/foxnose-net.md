---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Management API provides administrative endpoints for managing resources, limits, and collections.
  name: Management API
  slug: management-api-2
- baseURL: https://api.foxnose.net
  baseurl_source: declared
  description: 'foxnose-net flux API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: foxnose-net flux API
  slug: flux-api
- baseURL: https://api.foxnose.net
  baseurl_source: declared
  description: 'foxnose-net management API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: foxnose-net management API
  slug: management-api
artifact_total: 17
common:
- group: commercial
  href: https://artifacts.apis.io/foxnose-net/plans/foxnose-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/foxnose-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/foxnose-net/rules/foxnose-net-rules.yml
  title: ''
  type: Spectral
  url: rules/foxnose-net-rules.yml
- group: design
  href: https://artifacts.apis.io/foxnose-net/json-ld/foxnose-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/foxnose-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/foxnose-net/vocabulary/foxnose-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/foxnose-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/foxnose-net/data-model/foxnose-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/foxnose-net-data-model.yml
- group: operate
  href: https://artifacts.apis.io/foxnose-net/changelog/foxnose-net-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/foxnose-net-changelog.yml
- group: design
  href: https://artifacts.apis.io/foxnose-net/conventions/foxnose-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/foxnose-net-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://foxnose.net/security
- group: design
  href: https://artifacts.apis.io/foxnose-net/conformance/foxnose-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/foxnose-net-conformance.yml
- group: other
  href: https://artifacts.apis.io/foxnose-net/hosts/foxnose-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/foxnose-net-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://foxnose.net/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foxnose.net/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://foxnose.net/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://foxnose.net/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://foxnose.net/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://foxnose.net/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://foxnose.net/docs/quick-start
- group: auth
  href: https://artifacts.apis.io/foxnose-net/security/foxnose-net-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/foxnose-net-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/foxnose-net/security/foxnose-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foxnose-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foxnose.net/
coverage:
  checked: '2026-10-31'
  detail: Documentation pages exist but no OpenAPI or other machine-readable contract was found.
  evidence:
  - status: 404
    url: https://foxnose.net/docs/management-api/v1/openapi.json
  - status: 404
    url: https://api.foxnose.net/openapi.yaml
  - status: 404
    url: https://foxnose.net/docs/flux-api/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: foxnose-net is a technology company that provides innovative networking solutions and API services. Founded with a focus on secure, scalable, and developer-friendly interfaces, the company offers a suite of products ranging from API gateways to data integration tools. Their platform emphasizes robust security, comprehensive documentation, and community support, aiming to simplify API consumption and management for enterprises of all sizes. Through continuous development and open collaboration, foxnose-net strives to empower developers to build, deploy, and monitor APIs efficiently and reliably.
image: https://foxnose.net/og-image.jpeg
json_schemas:
- name: GetCommerceCatalogItems9D2Hx6Qpzml0Response
  property_count: 2
  slug: foxnose-net-get-commerce-catalog-items9-d2-hx6-qpzml0-response
- name: GetV1EnvApiApiCurlResponse
  property_count: 10
  slug: foxnose-net-get-v1-env-api-api-curl-response
- name: GetV17C9H4PwuApiDw2Qc5QrwxuzResponse
  property_count: 10
  slug: foxnose-net-get-v17-c9-h4-pwu-api-dw2-qc5-qrwxuz-response
- name: PostBlogMcpRequest
  property_count: 4
  slug: foxnose-net-post-blog-mcp-request
- name: PostBlogMcpResponse
  property_count: 2
  slug: foxnose-net-post-blog-mcp-response
- name: PostV1EnvApiApiCollectionsCurlRequest
  property_count: 6
  slug: foxnose-net-post-v1-env-api-api-collections-curl-request
- name: PutV1EnvApiApiCurlRequest
  property_count: 5
  slug: foxnose-net-put-v1-env-api-api-curl-request
- name: PutV17C9H4PwuApiDw2Qc5QrwxuzCollectionsMk8Np3TyvbcxRequest
  property_count: 5
  slug: foxnose-net-put-v17-c9-h4-pwu-api-dw2-qc5-qrwxuz-collections-mk8-np3-tyvbcx-request
- name: PutV17C9H4PwuApiResponse
  property_count: 10
  slug: foxnose-net-put-v17-c9-h4-pwu-api-response
jsonld:
- class_count: 22
  name: Foxnose Net Context
  property_count: 29
  slug: foxnose-net-context
layout: provider
modified: '2026-10-30'
name: foxnose-net
nav: Providers
network: true
overview: 'foxnose-net is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including flux API, management API, and 1 more. Tagged areas include Company, Networking, Security, and Integration.


  The foxnose-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  foxnose-net''s developer surface includes changelog, pricing, documentation, engineering blog, getting-started guide, and 15 more developer resources.'
plans:
- name: Foxnose Net Plans Pricing
  plan_count: 4
  slug: foxnose-net-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: foxnose-net API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: foxnose-net-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 13.2
  previous_composite: 37.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/foxnose-net/foxnose-net-2026-11-03T132315.png
security:
- kind: domain-security
  name: Foxnose Net Domain Security
  slug: foxnose-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Foxnose Net Trust Center
  slug: foxnose-net-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: foxnose-net
tags:
- Company
- Networking
- Security
- Integration
website: https://foxnose.net/
---
