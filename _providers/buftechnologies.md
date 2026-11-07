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
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Buf provides a Schema Registry API and Connect RPC services, but no public OpenAPI spec is available.
  name: Buf API
  slug: buf-api
- baseURL: https://demo.connectrpc.com
  baseurl_source: declared
  description: The Connectrpc API from Buftechnologies — 2 operation(s) for connectrpc.
  name: Buftechnologies Connectrpc API
  slug: buftechnologies-connectrpc-api
- baseURL: https://demo.connectrpc.com
  baseurl_source: declared
  description: The Foo API from Buftechnologies — 1 operation(s) for foo.
  name: Buftechnologies Foo API
  slug: buftechnologies-foo-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/buftechnologies/plans/buftechnologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buftechnologies-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buftechnologies/rules/buftechnologies-rules.yml
  title: ''
  type: Spectral
  url: rules/buftechnologies-rules.yml
- group: design
  href: https://artifacts.apis.io/buftechnologies/json-ld/buftechnologies-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buftechnologies-context.jsonld
- group: design
  href: https://artifacts.apis.io/buftechnologies/vocabulary/buftechnologies-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buftechnologies-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buftechnologies/data-model/buftechnologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buftechnologies-data-model.yml
- group: build
  href: https://artifacts.apis.io/buftechnologies/cli/buftechnologies-cli.yml
  title: ''
  type: CLI
  url: cli/buftechnologies-cli.yml
- group: design
  href: https://artifacts.apis.io/buftechnologies/conformance/buftechnologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buftechnologies-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buftechnologies/well-known/buftechnologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buftechnologies-well-known.yml
- group: other
  href: https://artifacts.apis.io/buftechnologies/hosts/buftechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buftechnologies-hosts.yml
- group: other
  href: https://artifacts.apis.io/buftechnologies/vendors/buftechnologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buftechnologies-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://buf.build/docs/bsr/admin/on-prem/release-notes/
- group: auth
  href: https://artifacts.apis.io/buftechnologies/security/buftechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buftechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buf.build
- group: docs
  title: ''
  type: Documentation
  url: https://buf.build/docs
- group: docs
  title: ''
  type: APIReference
  url: https://buf.build/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://buf.build/docs/cli/quickstart
- group: operate
  title: ''
  type: Support
  url: https://buf.build/contact
- group: company
  title: ''
  type: Blog
  url: https://buf.build/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bufbuild
- group: commercial
  title: ''
  type: Pricing
  url: https://buf.build/pricing
- group: start
  title: ''
  type: SignUp
  url: https://buf.build/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buf.build/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buf.build/legal/privacy-policy
coverage:
  checked: '2026-10-06'
  detail: Documentation at https://buf.build/docs provides guides but no public OpenAPI or other machine‑readable contract is available.
  evidence:
  - status: 200
    url: https://buf.build/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Buf Technologies provides modern tools for working with Protocol Buffers and gRPC, including the Buf Schema Registry, Buf CLI, and Connect RPC. Their platform enables developers to generate SDKs, create API documentation, enforce policy checks, and manage plugins, streamlining protobuf development and governance across languages and services.
finops:
- has_sources: true
  method: derived
  name: Buftechnologies Finops
  primary_unit: subscription
  service_category: ''
  slug: buftechnologies-finops
  template: false
image: https://buf.build/images/buf-og-image-v1.png
json_schemas:
- name: PostConnectrpcElizaV1ElizaserviceConnectrpcelizav1Elizaservi
  property_count: 1
  slug: buftechnologies-post-connectrpc-eliza-v1-elizaservice-connectrpcelizav1-elizaservi
jsonld:
- class_count: 1
  name: Buftechnologies Context
  property_count: 1
  slug: buftechnologies-context
layout: provider
modified: '2026-10-06'
name: Buftechnologies
nav: Providers
network: true
overview: 'Buftechnologies is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Connectrpc API, Foo API, and 1 more. Tagged areas include Company, Protobuf, gRPC, and Developer Tools.


  The Buftechnologies catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Buftechnologies'' developer surface includes CLI, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Buftechnologies Plans Pricing
  plan_count: 4
  slug: buftechnologies-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Buftechnologies API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: buftechnologies-rules
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 61.2
    catalog_earned_first_party: 12.0
    catalog_gap: 53.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 77.6
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 34.5
    discoverability: 53.6
    operational_transparency: 10.5
  previous_composite: 41.3
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/buftechnologies/buftechnologies-2026-11-03T122730.png
security:
- kind: domain-security
  name: Buftechnologies Domain Security
  slug: buftechnologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buftechnologies
tags:
- Company
- Protobuf
- gRPC
- Developer Tools
website: https://buf.build
---
