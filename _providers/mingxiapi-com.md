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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MingXi Export Control API providing data export control operations.
  name: MingXi Export Control API
  slug: mingxi-export-control-api
- description: 'MingXi Export Control API API: 4 operations.'
  name: MingXi Export Control API API
  slug: mingxi-export-control-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/mingxiapi-com/rules/mingxiapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/mingxiapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/mingxiapi-com/json-ld/mingxiapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mingxiapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/mingxiapi-com/vocabulary/mingxiapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mingxiapi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mingxiapi-com/data-model/mingxiapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mingxiapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/mingxiapi-com/errors/mingxiapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mingxiapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mingxiapi-com/conformance/mingxiapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mingxiapi-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/mingxiapi-com/hosts/mingxiapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mingxiapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/mingxiapi-com/vendors/mingxiapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mingxiapi-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mingxiapi-com/security/mingxiapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mingxiapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mingxiapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mingxiapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.mingxiapi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://mingxiapi.com/#pricing
created: '2026-10-30'
description: Mingxi API (mingxiapi.com) is a technology company offering a suite of APIs for data integration, analytics, and automation. The company focuses on providing developers with robust endpoints for accessing real-time data streams, managing resources, and integrating third-party services. Their platform emphasizes security, scalability, and ease of use, targeting enterprises and developers seeking to build data-driven applications. The API catalog includes endpoints for authentication, data retrieval, and operational controls, all documented with comprehensive guides and examples.
jsonld:
- class_count: 2
  name: Mingxiapi Com Context
  property_count: 6
  slug: mingxiapi-com-context
layout: provider
modified: '2026-10-30'
name: mingxiapi-com
nav: Providers
network: true
overview: 'mingxiapi-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including MingXi Export Control API API, and 1 more. Tagged areas include Data Integration, Analytics, Automation, Enterprise, and Developer Platform.


  The mingxiapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mingxiapi-com''s developer surface includes documentation, API reference, pricing, and 10 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: mingxiapi-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: mingxiapi-com-rules
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 37.1
    developer_ergonomics: 8.3
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 22.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mingxiapi-com/mingxiapi-com-2026-11-03T135626.png
security:
- kind: domain-security
  name: Mingxiapi Com Domain Security
  slug: mingxiapi-com-domain-security
  summary_line: TLSv1.3
slug: mingxiapi-com
tags:
- Data Integration
- Analytics
- Automation
- Enterprise
- Developer Platform
website: https://mingxiapi.com/
---
