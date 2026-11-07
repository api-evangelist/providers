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
    agentic_access: derived
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
  score: 18.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bookthetee Com Agentic Access
  operation_count: 3
  slug: bookthetee-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://bookthetee.com
  baseurl_source: declared
  description: The Courses API from BookTheTee — 1 operation(s) for courses.
  name: BookTheTee Courses API
  slug: bookthetee-com-courses-api
- baseURL: https://bookthetee.com
  baseurl_source: declared
  description: The Courses.json API from BookTheTee — 1 operation(s) for courses.json.
  name: BookTheTee Courses.json API
  slug: bookthetee-com-courses-json-api
- baseURL: https://bookthetee.com
  baseurl_source: declared
  description: The Regions API from BookTheTee — 1 operation(s) for regions.
  name: BookTheTee Regions API
  slug: bookthetee-com-regions-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/bookthetee-com/agentic-access/bookthetee-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bookthetee-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bookthetee-com/rules/bookthetee-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bookthetee-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bookthetee-com/json-ld/bookthetee-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bookthetee-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bookthetee-com/vocabulary/bookthetee-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bookthetee-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bookthetee-com/data-model/bookthetee-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bookthetee-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bookthetee-com/conformance/bookthetee-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bookthetee-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bookthetee-com/llms/bookthetee-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bookthetee-com-llms.txt
- group: build
  href: https://artifacts.apis.io/bookthetee-com/mcp/bookthetee-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bookthetee-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bookthetee-com/mcp/bookthetee-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bookthetee-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bookthetee-com/well-known/bookthetee-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bookthetee-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bookthetee-com/hosts/bookthetee-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bookthetee-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bookthetee-com/vendors/bookthetee-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bookthetee-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bookthetee-com/security/bookthetee-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bookthetee-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bookthetee.com/
created: '2026-11-02'
description: BookTheTee provides a public API that aggregates official tee time booking links for public golf courses in the New York City area. The service offers a read‑only JSON feed of course details, fees, and links to the courses’ own booking pages, enabling developers to build applications that help golfers find and book tee times without resellers or markups.
json_schemas:
- name: Course
  property_count: 34
  slug: bookthetee-com-course
jsonld:
- class_count: 1
  name: Bookthetee Com Context
  property_count: 34
  slug: bookthetee-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at bookthetee.com.
  name: BookTheTee MCP Server
  slug: bookthetee-com-mcp-yml
modified: '2026-11-02'
name: BookTheTee
nav: Providers
network: true
overview: 'BookTheTee publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Courses API, Courses.json API, and Regions API. Tagged areas include Golf, Public Data, NYC, and Booking.


  The BookTheTee catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: BookTheTee API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: bookthetee-com-rules
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.2
    catalog_earned_first_party: 0.0
    catalog_gap: 65.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 47.7
    developer_ergonomics: 0.0
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bookthetee Com Domain Security
  slug: bookthetee-com-domain-security
  summary_line: TLSv1.3
slug: bookthetee-com
tags:
- Golf
- Public Data
- NYC
- Booking
website: https://bookthetee.com/
---
