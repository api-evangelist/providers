---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.acme.com
  baseurl_source: declared
  description: 'Octri API as documented publicly: 71 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Octri API
  slug: octri-dev-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/octri-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/octri-dev/plans/octri-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/octri-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/rules/octri-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/octri-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/json-ld/octri-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/octri-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/octri-dev/vocabulary/octri-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/octri-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/data-model/octri-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/octri-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/conventions/octri-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/octri-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/octri-dev/authentication/octri-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/octri-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/conformance/octri-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/octri-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/octri-dev/llms/octri-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/octri-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/octri-dev/hosts/octri-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octri-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/octri-dev/vendors/octri-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/octri-dev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://octri.dev/security
- group: company
  title: ''
  type: Newsroom
  url: https://octri.dev/press
- group: start
  title: ''
  type: Login
  url: https://app.octri.dev/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://octri.dev/developers/guides/monitoring/releases
- group: auth
  href: https://artifacts.apis.io/octri-dev/security/octri-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octri-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octri.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://octri.dev/developers
- group: docs
  title: ''
  type: Documentation
  url: https://octri.dev/developers/guides/api-docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://octri.dev/developers/guides/api-docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://octri.dev/developers/guides/api-docs/overview
- group: operate
  title: ''
  type: Support
  url: https://octri.dev/support
- group: company
  title: ''
  type: Blog
  url: https://octri.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/octridev
- group: commercial
  title: ''
  type: Pricing
  url: https://octri.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://octri.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octri.dev/privacy
coverage:
  checked: '2026-10-31'
  detail: Documentation is rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://octri.dev/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Octri provides a platform that generates API documentation, SDKs in ten programming languages, a Monitoring and Control Plane (MCP) server, and tools for AI agents. Users can upload an OpenAPI spec and receive a full documentation site, automatically generated client libraries, real‑time SDK health monitoring, and an MCP that exposes the API as callable tools for agents. Octri also offers free utilities for spec conversion, auditing, and a marketplace of sample APIs. The service includes pricing plans for individuals and enterprises, a blog with product updates, and open source SDKs.
image: https://octri.dev/opengraph-image
json_schemas:
- name: GetV1BatchesIdResponse
  property_count: 1
  slug: octri-dev-get-v1-batches-id-response
- name: PostCustomersRequest
  property_count: 3
  slug: octri-dev-post-customers-request
- name: PostCustomersResponse
  property_count: 3
  slug: octri-dev-post-customers-response
- name: PostRefundsResponse
  property_count: 1
  slug: octri-dev-post-refunds-response
- name: PostV1BatchesRequest
  property_count: 1
  slug: octri-dev-post-v1-batches-request
- name: PostV1BatchesResponse
  property_count: 3
  slug: octri-dev-post-v1-batches-response
jsonld:
- class_count: 6
  name: Octri Dev Context
  property_count: 7
  slug: octri-dev-context
layout: provider
modified: '2026-10-28'
name: Octri
nav: Providers
network: true
overview: 'Octri is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Documentation, SDK, and Monitoring.


  The Octri catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Octri''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
plans:
- name: Octri Dev Plans Pricing
  plan_count: 5
  slug: octri-dev-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Octri API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: octri-dev-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 23.7
    developer_ergonomics: 63.6
    discoverability: 67.9
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 39
      marker_coverage: 100.0
      total: 39
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Octri Dev Authentication
  slug: octri-dev-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Octri Dev Domain Security
  slug: octri-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-assistants
  slug: octri-dev-get_assistants-skill
slug: octri-dev
tags:
- Company
- API
- Documentation
- SDK
- Monitoring
- MCP
website: https://octri.dev
---
