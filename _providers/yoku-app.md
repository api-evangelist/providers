---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.yoku.app
  baseurl_source: declared
  description: 'yoku-app API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: yoku-app API
  slug: yoku-app-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/yoku-app/plans/yoku-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yoku-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/yoku-app/rules/yoku-app-rules.yml
  title: ''
  type: Spectral
  url: rules/yoku-app-rules.yml
- group: design
  href: https://artifacts.apis.io/yoku-app/json-ld/yoku-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/yoku-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/yoku-app/vocabulary/yoku-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/yoku-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/yoku-app/data-model/yoku-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yoku-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/yoku-app/conventions/yoku-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/yoku-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/yoku-app/authentication/yoku-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yoku-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/yoku-app/conformance/yoku-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yoku-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/yoku-app/mcp/yoku-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/yoku-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/yoku-app/hosts/yoku-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yoku-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/yoku-app/vendors/yoku-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yoku-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/yoku-app/packages/yoku-app-packages.yml
  title: ''
  type: SDKs
  url: packages/yoku-app-packages.yml
- group: build
  href: https://artifacts.apis.io/yoku-app/packages/yoku-app-packages.yml
  title: ''
  type: Packages
  url: packages/yoku-app-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yoku.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yoku.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yoku.app/pricing
- group: start
  title: ''
  type: Login
  url: https://www.yoku.app/auth/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://www.yoku.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.yoku.app/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/yoku-app/security/yoku-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yoku-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yoku.app/
created: '2026-10-31'
description: Yoku provides a developer‑first brand identity API delivering real‑time company data, logos, colors, industry classifications and social profiles. By supplying a domain, company name, ticker or transaction descriptor, developers receive structured brand information ready for integration into SaaS, fintech and AI applications. The platform emphasizes speed, reliability and ease of use, offering a free tier without credit‑card requirements and extensive documentation for quick onboarding.
image: https://www.yoku.app/og/main.png
json_schemas:
- name: PostRequest
  property_count: 4
  slug: yoku-app-post-request
- name: PostResponse
  property_count: 3
  slug: yoku-app-post-response
jsonld:
- class_count: 2
  name: Yoku App Context
  property_count: 7
  slug: yoku-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.yoku.app requiring an API key.
  name: yoku-app MCP Server
  slug: yoku-app-mcp-yml
modified: '2026-10-31'
name: yoku-app
nav: Providers
network: true
overview: 'yoku-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Brands, Data, and Software-as-a-Service.


  The yoku-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  yoku-app''s developer surface includes authentication, pricing, documentation, API reference, and 17 more developer resources.'
plans:
- name: Yoku App Plans Pricing
  plan_count: 4
  slug: yoku-app-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: yoku-app API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: yoku-app-rules
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 21.7
    developer_ergonomics: 27.4
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 38.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Yoku App Authentication
  slug: yoku-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Yoku App Domain Security
  slug: yoku-app-domain-security
  summary_line: TLSv1.3
slug: yoku-app
tags:
- Company
- Brands
- Data
- Software-as-a-Service
website: https://www.yoku.app/
---
