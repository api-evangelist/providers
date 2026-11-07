---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'ContainerMath API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ContainerMath API
  slug: containermath-com-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/containermath-com/plans/containermath-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/containermath-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/containermath-com/rules/containermath-com-rules.yml
  title: ''
  type: Spectral
  url: rules/containermath-com-rules.yml
- group: design
  href: https://artifacts.apis.io/containermath-com/json-ld/containermath-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/containermath-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/containermath-com/vocabulary/containermath-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/containermath-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/containermath-com/data-model/containermath-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/containermath-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/containermath-com/security/containermath-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/containermath-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/containermath-com/conformance/containermath-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/containermath-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/containermath-com/llms/containermath-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/containermath-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/containermath-com/well-known/containermath-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/containermath-com-security.txt
- group: agent
  href: https://artifacts.apis.io/containermath-com/well-known/containermath-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/containermath-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/containermath-com/hosts/containermath-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/containermath-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/containermath-com/vendors/containermath-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/containermath-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://containermath.com/news
- group: auth
  href: https://artifacts.apis.io/containermath-com/security/containermath-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/containermath-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/containermath-com/security/containermath-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/containermath-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://containermath.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://containermath.com/developer-api
- group: docs
  title: ''
  type: Documentation
  url: https://containermath.com/developer-api
- group: docs
  title: ''
  type: APIReference
  url: https://containermath.com/developer-api
- group: commercial
  title: ''
  type: Pricing
  url: https://containermath.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://containermath.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://containermath.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://containermath.com/privacy
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite accessible documentation.
  evidence:
  - status: 200
    url: https://containermath.com/guide
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: ContainerMath provides a 3D container load planning platform that helps businesses optimize the packing of cartons into shipping containers. Users can paste cargo lists, generate optimized loading plans, and export them. The service offers tools for carton fit, container dimensions, load calculators, and integrates via a developer API for automated workflows. It targets logistics, manufacturing, and freight forwarding companies seeking efficient, data‑driven load planning.
image: https://containermath.com/opengraph-v2.jpg
json_schemas:
- name: GetApiV1ContainersResponse
  property_count: 1
  slug: containermath-com-get-api-v1-containers-response
- name: PostApiV1LoadplansCalculateRequest
  property_count: 3
  slug: containermath-com-post-api-v1-loadplans-calculate-request
jsonld:
- class_count: 2
  name: Containermath Com Context
  property_count: 4
  slug: containermath-com-context
layout: provider
modified: '2026-11-04'
name: ContainerMath
nav: Providers
network: true
overview: 'ContainerMath is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Shipping, Load Planning, 3D Visualization, and Software-as-a-Service.


  The ContainerMath catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ContainerMath''s developer surface includes documentation, API reference, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Containermath Com Plans Pricing
  plan_count: 3
  slug: containermath-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: ContainerMath API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: containermath-com-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Containermath Com Domain Security
  slug: containermath-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Containermath Com Vulnerability Disclosure
  slug: containermath-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: containermath-com
tags:
- Logistics
- Shipping
- Load Planning
- 3D Visualization
- Software-as-a-Service
website: https://containermath.com/
---
