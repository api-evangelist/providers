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
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Token API from ParkourSC — 1 operation(s) for token.
  name: ParkourSC Token API
  slug: cloudleaf-token-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/cloudleaf/rules/cloudleaf-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudleaf-rules.yml
- group: design
  href: https://artifacts.apis.io/cloudleaf/json-ld/cloudleaf-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudleaf-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudleaf/vocabulary/cloudleaf-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudleaf-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cloudleaf/data-model/cloudleaf-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudleaf-data-model.yml
- group: design
  href: https://artifacts.apis.io/cloudleaf/conformance/cloudleaf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudleaf-conformance.yml
- group: other
  href: https://artifacts.apis.io/cloudleaf/hosts/cloudleaf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudleaf-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloudleaf/vendors/cloudleaf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudleaf-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parkoursc.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parkoursc.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://prod.parkoursc.com/cloudos/login
- group: company
  title: ''
  type: Blog
  url: https://www.parkoursc.com/blog
- group: auth
  href: https://artifacts.apis.io/cloudleaf/security/cloudleaf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudleaf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.parkoursc.com
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, Swagger, or Redoc spec found at common API host paths.
  evidence:
  - status: 404
    url: https://api.parkoursc.com/openapi.json
  - status: 404
    url: https://prod.parkoursc.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: ParkourSC, formerly Cloudleaf, provides an AI-native Decision Intelligence platform for real‑time supply chain operations. The platform offers digital twins, dynamic decision intelligence, and low‑code workbenches to monitor inventory, cold‑chain logistics, and manufacturing processes. It serves industries such as logistics, pharma, consumer goods, and food & beverage, helping companies anticipate disruptions, optimize demand fulfillment, and ensure quality compliance across global supply chains.
image: https://www.parkoursc.com/wp-content/themes/parkour/img/fbThumb.jpg
json_schemas:
- name: PostApi2TokenRequest
  property_count: 2
  slug: cloudleaf-post-api2-token-request
- name: PostApi2TokenResponse
  property_count: 2
  slug: cloudleaf-post-api2-token-response
jsonld:
- class_count: 2
  name: Cloudleaf Context
  property_count: 4
  slug: cloudleaf-context
layout: provider
modified: '2026-10-09'
name: ParkourSC
nav: Providers
network: true
overview: 'ParkourSC is listed with 1 API on the [APIs.io](https://apis.io/) network: Token API. Tagged areas include Supply Chain, Artificial Intelligence, Digital Twin, Decision Intelligence, and Logistics.


  The ParkourSC catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ParkourSC''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: ParkourSC API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: cloudleaf-rules
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 19.9
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 20.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cloudleaf/cloudleaf-2026-11-03T124524.png
security:
- kind: domain-security
  name: Cloudleaf Domain Security
  slug: cloudleaf-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cloudleaf
tags:
- Supply Chain
- Artificial Intelligence
- Digital Twin
- Decision Intelligence
- Logistics
- Cloud
website: https://www.parkoursc.com
---
