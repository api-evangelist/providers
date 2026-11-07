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
    agentic_commerce: platform
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Metered API for automated color separation services
  name: Separation API
  slug: separation-api
- description: 'AI Separations API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AI Separations API
  slug: aiseparations-com-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/aiseparations-com/rules/aiseparations-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aiseparations-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aiseparations-com/json-ld/aiseparations-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aiseparations-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aiseparations-com/vocabulary/aiseparations-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiseparations-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aiseparations-com/data-model/aiseparations-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiseparations-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/aiseparations-com/conformance/aiseparations-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiseparations-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiseparations-com/llms/aiseparations-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiseparations-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aiseparations-com/mcp/aiseparations-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiseparations-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aiseparations-com/well-known/aiseparations-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiseparations-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiseparations-com/hosts/aiseparations-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiseparations-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiseparations-com/vendors/aiseparations-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiseparations-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aiseparations.com/learn/getting-started/
- group: auth
  href: https://artifacts.apis.io/aiseparations-com/security/aiseparations-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiseparations-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiseparations.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aiseparations.com/learn/
- group: docs
  title: ''
  type: APIReference
  url: https://www.aiseparations.com/separation-api/
- group: company
  title: ''
  type: Blog
  url: https://www.aiseparations.com/blog/
coverage:
  checked: '2026-11-01'
  detail: API documentation page renders a JavaScript-heavy site with no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://www.aiseparations.com/separation-api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AI Separations provides AI‑powered color separation and quoting software for screen printing and DTF workflows. Their web app offers instant quotes, pre‑flight checks, profit mode calculations, and ink matching without Photoshop. The platform includes a free separation tool, bulk mockup generator, gang‑sheet builder, and a metered API for developers to integrate automated color separations into their services.
image: https://www.aiseparations.com/og-image.png
json_schemas:
- name: GetApiCreditsResponse
  property_count: 1
  slug: aiseparations-com-get-api-credits-response
- name: PostApiSeparateRequest
  property_count: 3
  slug: aiseparations-com-post-api-separate-request
- name: PostApiSeparateResponse
  property_count: 23
  slug: aiseparations-com-post-api-separate-response
jsonld:
- class_count: 3
  name: Aiseparations Com Context
  property_count: 25
  slug: aiseparations-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.aiseparations.com.
  name: AI Separations MCP Server
  slug: aiseparations-com-mcp-yml
modified: '2026-11-01'
name: AI Separations
nav: Providers
network: true
overview: 'AI Separations is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Screen Printing, DTF, Prepress Software, Color Separation, and Quoting Tool.


  The AI Separations catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Separations'' developer surface includes getting-started guide, documentation, API reference, engineering blog, and 12 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AI Separations API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: aiseparations-com-rules
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 22.4
    developer_ergonomics: 15.5
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 19.5
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
security:
- kind: domain-security
  name: Aiseparations Com Domain Security
  slug: aiseparations-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiseparations-com
tags:
- Screen Printing
- DTF
- Prepress Software
- Color Separation
- Quoting Tool
- Ink Matching
- Print Ready Output
website: https://aiseparations.com/
---
