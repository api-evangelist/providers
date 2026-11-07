---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: API for AIVA cloud platform to manage and execute automated web‑app tests.
  name: AIVA Cloud API
  slug: aiva-cloud-api
- baseURL: https://api.aiva.works
  baseurl_source: declared
  description: 'AIVA API Reference API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AIVA API Reference API
  slug: api-api
- baseURL: https://api.aiva.works
  baseurl_source: declared
  description: 'AIVA How to... API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AIVA How to... API
  slug: how-to-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/aiva-works/plans/aiva-works-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiva-works-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aiva-works/rules/aiva-works-rules.yml
  title: ''
  type: Spectral
  url: rules/aiva-works-rules.yml
- group: design
  href: https://artifacts.apis.io/aiva-works/json-ld/aiva-works-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aiva-works-context.jsonld
- group: design
  href: https://artifacts.apis.io/aiva-works/vocabulary/aiva-works-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiva-works-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aiva-works/data-model/aiva-works-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiva-works-data-model.yml
- group: operate
  href: https://artifacts.apis.io/aiva-works/changelog/aiva-works-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aiva-works-changelog.yml
- group: auth
  href: https://artifacts.apis.io/aiva-works/authentication/aiva-works-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiva-works-authentication.yml
- group: design
  href: https://artifacts.apis.io/aiva-works/conformance/aiva-works-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiva-works-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiva-works/mcp/aiva-works-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiva-works-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aiva-works/well-known/aiva-works-sso-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aiva-works-sso-security.txt
- group: agent
  href: https://artifacts.apis.io/aiva-works/well-known/aiva-works-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiva-works-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiva-works/hosts/aiva-works-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiva-works-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiva-works/vendors/aiva-works-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiva-works-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://app.aiva.works/docs/release-notes
- group: auth
  href: https://artifacts.apis.io/aiva-works/security/aiva-works-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiva-works-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiva.works/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.aiva.works/
- group: docs
  title: ''
  type: Documentation
  url: https://app.aiva.works/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.aiva.works/docs/api/aiva-cloud-api
- group: start
  title: ''
  type: GettingStarted
  url: https://app.aiva.works/docs#getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://aiva.works/
- group: start
  title: ''
  type: SignUp
  url: https://app.aiva.works/signup?context=landing_page
coverage:
  checked: '2026-11-01'
  detail: API spec endpoints require an API key, returning 401 Unauthorized.
  evidence:
  - status: 401
    url: https://api.aiva.works/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-01'
description: AIVA is a no‑code tool for automated testing of web applications. Users record a test once manually and AIVA learns to replay it without requiring code, selectors, or scripts. It visually identifies elements, keeping tests stable across UI changes, and highlights broken steps for quick repair. Built by Y Soft, AIVA offers a cloud‑based platform for reliable, maintainable web‑app testing.
image: https://aiva.works/AIVA.svg
json_schemas:
- name: PostV2BatchExecutionsRequest
  property_count: 6
  slug: aiva-works-post-v2-batch-executions-request
- name: PostV2TestsTestidRunsResponse
  property_count: 1
  slug: aiva-works-post-v2-tests-testid-runs-response
jsonld:
- class_count: 2
  name: Aiva Works Context
  property_count: 7
  slug: aiva-works-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.aiva.works.
  name: AIVA MCP Server
  slug: aiva-works-mcp-yml
modified: '2026-11-01'
name: AIVA
nav: Providers
network: true
overview: 'AIVA is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including API Reference API, How to... API, and 1 more. Tagged areas include Automation, Testing, No-Code, Web, and Artificial Intelligence.


  The AIVA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIVA''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Aiva Works Plans Pricing
  plan_count: 4
  slug: aiva-works-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AIVA API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: aiva-works-rules
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.2
    catalog_earned_first_party: 12.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 19.5
    developer_ergonomics: 31.0
    discoverability: 61.7
    operational_transparency: 18.4
  previous_composite: 38.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aiva Works Authentication
  slug: aiva-works-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aiva Works Domain Security
  slug: aiva-works-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aiva-works
tags:
- Automation
- Testing
- No-Code
- Web
- Artificial Intelligence
website: https://aiva.works/
---
