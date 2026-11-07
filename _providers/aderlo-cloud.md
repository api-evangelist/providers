---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
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
  score: 39.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Customer API for managing domains, DNS, email, databases, and other hosting resources.
  name: Aderlo Cloud Customer API
  slug: aderlo-cloud-customer-api
- baseURL: https://aderlo.cloud
  baseurl_source: declared
  description: 'Hosted MCP endpoint (JSON-RPC 2.0 over Streamable HTTP), its OAuth 2.1 authorization server, and the public domain availability check. Plans and prices: https://aderlo.cloud/llms.txt'
  name: Aderlo Cloud public API API
  slug: aderlo-cloud-public-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/aderlo-cloud/rules/aderlo-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/aderlo-cloud-rules.yml
- group: design
  href: https://artifacts.apis.io/aderlo-cloud/json-ld/aderlo-cloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aderlo-cloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/aderlo-cloud/vocabulary/aderlo-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aderlo-cloud-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/aderlo-cloud/plans/aderlo-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aderlo-cloud-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aderlo-cloud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aderlo-cloud/data-model/aderlo-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aderlo-cloud-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aderlo-cloud/authentication/aderlo-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aderlo-cloud-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aderlo-cloud/scopes/aderlo-cloud-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aderlo-cloud-scopes.yml
- group: design
  href: https://artifacts.apis.io/aderlo-cloud/lifecycle/aderlo-cloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aderlo-cloud-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aderlo-cloud/errors/aderlo-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aderlo-cloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aderlo-cloud/conformance/aderlo-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aderlo-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aderlo-cloud/llms/aderlo-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aderlo-cloud-llms.txt
- group: auth
  href: https://artifacts.apis.io/aderlo-cloud/well-known/aderlo-cloud-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aderlo-cloud-www-security.txt
- group: agent
  href: https://artifacts.apis.io/aderlo-cloud/well-known/aderlo-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aderlo-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/aderlo-cloud/hosts/aderlo-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aderlo-cloud-hosts.yml
- group: build
  href: https://artifacts.apis.io/aderlo-cloud/packages/aderlo-cloud-packages.yml
  title: ''
  type: SDKs
  url: packages/aderlo-cloud-packages.yml
- group: build
  href: https://artifacts.apis.io/aderlo-cloud/packages/aderlo-cloud-packages.yml
  title: ''
  type: Packages
  url: packages/aderlo-cloud-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aderlo.cloud/status
- group: start
  title: ''
  type: Login
  url: https://aderlo.cloud/login/forgot
- group: auth
  href: https://artifacts.apis.io/aderlo-cloud/security/aderlo-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aderlo-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aderlo.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://aderlo.cloud/docs/api
- group: operate
  title: ''
  type: Support
  url: https://aderlo.cloud/support
- group: commercial
  title: ''
  type: Pricing
  url: https://aderlo.cloud/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aderlo.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aderlo.cloud/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://aderlo.cloud/openapi.json
  - status: 401
    url: https://aderlo.cloud/api/mcp
  - status: 200
    url: https://aderlo.cloud/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Aderlo Cloud provides managed WooCommerce and WordPress hosting on its own enterprise‑grade NVMe and ECC hardware in the European Union. Powered by LiteSpeed Enterprise, dedicated PHP workers, and Redis object cache, it offers a real uptime SLA. The company, ADERLO PROSTA SPÓŁKA AKCYJNA, is based in Warsaw, Poland and serves customers across EU, offering secure, high‑performance hosting solutions.
image: https://aderlo.cloud/brand/icon-512.png
json_schemas:
- name: JsonRpcRequest
  property_count: 4
  slug: aderlo-cloud-json-rpc-request
jsonld:
- class_count: 1
  name: Aderlo Cloud Context
  property_count: 4
  slug: aderlo-cloud-context
layout: provider
modified: '2026-10-31'
name: Aderlo Cloud
nav: Providers
network: true
overview: 'Aderlo Cloud publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including public API API, and 1 more. Tagged areas include Hosting, WooCommerce, WordPress, EU, and Managed.


  The Aderlo Cloud catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aderlo Cloud''s developer surface includes authentication, documentation, support, pricing, and 22 more developer resources.'
plans:
- name: Aderlo Cloud Plans Pricing
  plan_count: 4
  slug: aderlo-cloud-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Aderlo Cloud API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: aderlo-cloud-rules
scopes:
- name: Aderlo Cloud Scopes
  scope_count: 6
  slug: aderlo-cloud-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.2
    catalog_earned_first_party: 12.0
    catalog_gap: 49.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 46.9
    developer_ergonomics: 32.6
    discoverability: 66.1
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 50.5
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aderlo Cloud Authentication
  slug: aderlo-cloud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aderlo Cloud Domain Security
  slug: aderlo-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aderlo-cloud
tags:
- Hosting
- WooCommerce
- WordPress
- EU
- Managed
- Cloud
website: https://aderlo.cloud/
---
