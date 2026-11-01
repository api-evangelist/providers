---
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Provides cloud‑based memory management platform APIs.
  name: xmemory API
  slug: xmemory-api-2
- baseURL: https://api.xmemory.ai
  baseurl_source: declared
  description: 'xmemory API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: xmemory API
  slug: xmemory-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/xmemory/rate-limits/xmemory-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xmemory-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/xmemory/plans/xmemory-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xmemory-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/xmemory/rules/xmemory-rules.yml
  title: ''
  type: Spectral
  url: rules/xmemory-rules.yml
- group: design
  href: https://artifacts.apis.io/xmemory/json-ld/xmemory-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/xmemory-context.jsonld
- group: design
  href: https://artifacts.apis.io/xmemory/vocabulary/xmemory-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xmemory-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/xmemory/data-model/xmemory-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xmemory-data-model.yml
- group: build
  href: https://artifacts.apis.io/xmemory/cli/xmemory-cli.yml
  title: ''
  type: CLI
  url: cli/xmemory-cli.yml
- group: design
  href: https://artifacts.apis.io/xmemory/conformance/xmemory-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xmemory-conformance.yml
- group: agent
  href: https://artifacts.apis.io/xmemory/llms/xmemory-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xmemory-llms.txt
- group: agent
  href: https://artifacts.apis.io/xmemory/well-known/xmemory-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xmemory-well-known.yml
- group: other
  href: https://artifacts.apis.io/xmemory/hosts/xmemory-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xmemory-hosts.yml
- group: other
  href: https://artifacts.apis.io/xmemory/vendors/xmemory-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xmemory-vendors.yml
- group: build
  href: https://artifacts.apis.io/xmemory/packages/xmemory-packages.yml
  title: ''
  type: SDKs
  url: packages/xmemory-packages.yml
- group: build
  href: https://artifacts.apis.io/xmemory/packages/xmemory-packages.yml
  title: ''
  type: Packages
  url: packages/xmemory-packages.yml
- group: start
  title: ''
  type: Login
  url: https://console.xmemory.ai/login/google
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.xmemory.ai`
- group: auth
  href: https://artifacts.apis.io/xmemory/security/xmemory-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xmemory-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xmemory.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://xmemory.ai/integration-overview/
- group: docs
  title: ''
  type: APIReference
  url: https://xmemory.ai/integration-overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://xmemory.ai/integration-overview/
- group: commercial
  title: ''
  type: Pricing
  url: https://xmemory.ai/pricing-deployment/
- group: company
  title: ''
  type: Blog
  url: https://xmemory.ai/#our-blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xmemory.ai/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xmemory.ai/privacy-policy.html
coverage:
  checked: '2026-10-19'
  detail: Documentation is HTML only and no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://xmemory.ai/integration-overview/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: xmemory provides a cloud‑based memory management platform that helps enterprises optimise data storage, improve performance, and reduce costs. Leveraging advanced analytics and AI‑driven recommendations, xmemory enables seamless integration across on‑premise and multi‑cloud environments, offering real‑time insights, automated tiering, and secure data lifecycle management. The solution supports a wide range of workloads, from databases to backup archives, and is designed for scalability, compliance, and high availability, empowering organisations to maximise the value of their data assets while minimising operational overhead.
json_schemas:
- name: PostClustersClusteridInstancesRequest
  property_count: 5
  slug: xmemory-post-clusters-clusterid-instances-request
- name: PostInstancesInstanceidReadRequest
  property_count: 9
  slug: xmemory-post-instances-instanceid-read-request
- name: PostInstancesInstanceidReadResponse
  property_count: 5
  slug: xmemory-post-instances-instanceid-read-response
- name: PostInstancesInstanceidSuggestionsApplyResponse
  property_count: 6
  slug: xmemory-post-instances-instanceid-suggestions-apply-response
- name: PostInstancesInstanceidWriteAsyncRequest
  property_count: 7
  slug: xmemory-post-instances-instanceid-write-async-request
- name: PostInstancesInstanceidWriteRequest
  property_count: 7
  slug: xmemory-post-instances-instanceid-write-request
jsonld:
- class_count: 43
  name: Xmemory Context
  property_count: 87
  slug: xmemory-context
layout: provider
modified: '2026-10-19'
name: xmemory
nav: Providers
network: true
overview: 'xmemory is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Memory, Cloud, and Data Management.


  The xmemory catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  xmemory''s developer surface includes CLI, documentation, API reference, getting-started guide, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Xmemory Plans Pricing
  plan_count: 4
  slug: xmemory-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Xmemory Rate Limits
  slug: xmemory-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: xmemory API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: xmemory-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 75.8
    catalog_earned_first_party: 20.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.3
    developer_ergonomics: 54.8
    discoverability: 53.6
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Xmemory Domain Security
  slug: xmemory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xmemory
tags:
- Company
- Artificial Intelligence
- Memory
- Cloud
- Data Management
- Platform
website: https://xmemory.ai/
---
