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
    mcp_server: documented
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
  score: 16.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for the Care Leader Guide platform, providing access to guide metadata and resources.
  name: Care Leader Guide API
  slug: care-leader-guide-api
- description: 'Care Leader Guide API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Care Leader Guide API
  slug: careleader-guide-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/careleader-guide/rules/careleader-guide-rules.yml
  title: ''
  type: Spectral
  url: rules/careleader-guide-rules.yml
- group: design
  href: https://artifacts.apis.io/careleader-guide/json-ld/careleader-guide-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/careleader-guide-context.jsonld
- group: design
  href: https://artifacts.apis.io/careleader-guide/vocabulary/careleader-guide-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/careleader-guide-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/careleader-guide/data-model/careleader-guide-data-model.yml
  title: ''
  type: DataModel
  url: data-model/careleader-guide-data-model.yml
- group: design
  href: https://artifacts.apis.io/careleader-guide/conformance/careleader-guide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/careleader-guide-conformance.yml
- group: agent
  href: https://artifacts.apis.io/careleader-guide/llms/careleader-guide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/careleader-guide-llms.txt
- group: build
  href: https://artifacts.apis.io/careleader-guide/mcp/careleader-guide-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/careleader-guide-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/careleader-guide/mcp/careleader-guide-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/careleader-guide-mcp.yml
- group: other
  href: https://artifacts.apis.io/careleader-guide/hosts/careleader-guide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/careleader-guide-hosts.yml
- group: other
  href: https://artifacts.apis.io/careleader-guide/vendors/careleader-guide-vendors.yml
  title: ''
  type: Vendors
  url: vendors/careleader-guide-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://careleader.guide/terms
- group: operate
  title: ''
  type: Support
  url: https://careleader.guide/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://careleader.guide/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://careleader.guide/guides
- group: docs
  title: ''
  type: APIReference
  url: https://careleader.guide/llms.txt
- group: auth
  href: https://artifacts.apis.io/careleader-guide/security/careleader-guide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/careleader-guide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://careleader.guide/
coverage:
  checked: '2026-11-03'
  detail: OpenAPI spec at https://careleader.guide/openapi.json describes a different product, so no owned contract.
  evidence:
  - status: 200
    url: https://careleader.guide/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Care Leader Guide is a platform that provides curated guides and resources for individuals leading care work. It focuses on the challenges faced by care leaders, offering practical advice, best practices, and community support to help them navigate their roles effectively. The site includes articles, guides, and tools aimed at improving care leadership and fostering better outcomes for those they serve.
image: https://careleader.guide/opengraph-image-1oy18k?29435694197f5727
json_schemas:
- name: GetApiV1GuidesResponse
  property_count: 3
  slug: careleader-guide-get-api-v1-guides-response
jsonld:
- class_count: 1
  name: Careleader Guide Context
  property_count: 0
  slug: careleader-guide-context
layout: provider
mcp_servers:
- description: Remote MCP server at careleader.guide.
  name: Care Leader Guide MCP Server
  slug: careleader-guide-mcp-yml
modified: '2026-11-03'
name: Care Leader Guide
nav: Providers
network: true
overview: 'Care Leader Guide is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Care, Leadership, Guides, Community, and Healthcare.


  The Care Leader Guide catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Care Leader Guide''s developer surface includes support, documentation, API reference, and 14 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Care Leader Guide API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: careleader-guide-rules
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 17.4
    developer_ergonomics: 10.7
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Careleader Guide Domain Security
  slug: careleader-guide-domain-security
  summary_line: TLSv1.3 · HSTS
slug: careleader-guide
tags:
- Care
- Leadership
- Guides
- Community
- Healthcare
website: https://careleader.guide/
---
