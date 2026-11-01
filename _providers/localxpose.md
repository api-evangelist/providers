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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'xLab API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: xLab API
  slug: localxpose-api
artifact_total: 7
asyncapis:
- description: ''
  name: Localxpose Webhooks
  slug: localxpose-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/localxpose/plans/localxpose-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/localxpose-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/localxpose/rules/localxpose-rules.yml
  title: ''
  type: Spectral
  url: rules/localxpose-rules.yml
- group: design
  href: https://artifacts.apis.io/localxpose/json-ld/localxpose-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/localxpose-context.jsonld
- group: design
  href: https://artifacts.apis.io/localxpose/vocabulary/localxpose-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/localxpose-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/localxpose/asyncapi/localxpose-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/localxpose-webhooks.yml
- group: design
  href: https://artifacts.apis.io/localxpose/data-model/localxpose-data-model.yml
  title: ''
  type: DataModel
  url: data-model/localxpose-data-model.yml
- group: build
  href: https://artifacts.apis.io/localxpose/cli/localxpose-cli.yml
  title: ''
  type: CLI
  url: cli/localxpose-cli.yml
- group: design
  href: https://artifacts.apis.io/localxpose/conformance/localxpose-conformance.yml
  title: ''
  type: Conformance
  url: conformance/localxpose-conformance.yml
- group: other
  href: https://artifacts.apis.io/localxpose/hosts/localxpose-hosts.yml
  title: ''
  type: Hosts
  url: hosts/localxpose-hosts.yml
- group: other
  href: https://artifacts.apis.io/localxpose/vendors/localxpose-vendors.yml
  title: ''
  type: Vendors
  url: vendors/localxpose-vendors.yml
- group: build
  href: https://artifacts.apis.io/localxpose/packages/localxpose-packages.yml
  title: ''
  type: SDKs
  url: packages/localxpose-packages.yml
- group: build
  href: https://artifacts.apis.io/localxpose/packages/localxpose-packages.yml
  title: ''
  type: Packages
  url: packages/localxpose-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://localxpose.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://localxpose.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LocalXpose
- group: auth
  href: https://artifacts.apis.io/localxpose/security/localxpose-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/localxpose-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://localxpose.io/
- group: docs
  title: ''
  type: Documentation
  url: https://localxpose.io/docs
- group: company
  title: ''
  type: Blog
  url: https://localxpose.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://localxpose.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://localxpose.io/signup
- group: start
  title: ''
  type: Login
  url: https://localxpose.io/login
coverage:
  checked: '2026-10-18'
  detail: Documentation pages exist but provide no machine‑readable OpenAPI/AsyncAPI/GraphQL/WSDL contracts.
  evidence:
  - status: 200
    url: https://localxpose.io/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: LocalXpose, developed by xLab, provides secure tunneling and localhost exposure software, enabling developers to safely expose local servers, IoT devices, and applications to the internet via encrypted tunnels. The platform emphasizes security, speed, and ease of use for remote access and testing.
image: https://localxpose.io/image/localxpose-product.png
json_schemas:
- name: GetApiCollectionsPostsRecordsResponse
  property_count: 4
  slug: localxpose-get-api-collections-posts-records-response
jsonld:
- class_count: 1
  name: Localxpose Context
  property_count: 4
  slug: localxpose-context
layout: provider
modified: '2026-10-18'
name: xLab
nav: Providers
network: true
overview: 'xLab is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tunneling, Developer Tools, Security, Cloud, and Networking.


  The xLab catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  xLab''s developer surface includes CLI, documentation, engineering blog, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Localxpose Plans Pricing
  plan_count: 3
  slug: localxpose-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: xLab API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: localxpose-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 24.9
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 37.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Localxpose Domain Security
  slug: localxpose-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: localxpose
tags:
- Tunneling
- Developer Tools
- Security
- Cloud
- Networking
website: https://localxpose.io/
---
