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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 8
  name: Backresto Com Agentic Access
  operation_count: 28
  slug: backresto-com-agentic-access
  summary_line: 28 operations · 10 acting · 8 human-in-the-loop
api_count: 2
apis:
- baseURL: https://www.backresto.com
  baseurl_source: declared
  description: Agent-oriented representations of the site
  name: BackResto Agent API
  slug: backresto-com-agent-api
- baseURL: https://www.backresto.com
  baseurl_source: declared
  description: EU allergen table generator (14 regulated allergens)
  name: BackResto Allergens API
  slug: backresto-com-allergens-api
- baseURL: https://www.backresto.com
  baseurl_source: declared
  description: Free HACCP express audit
  name: BackResto Audit API
  slug: backresto-com-audit-api
- baseURL: https://api.backresto.com
  baseurl_source: declared
  description: The Health API from BackResto — 3 operation(s) for health.
  name: BackResto Health API
  slug: backresto-com-health-api
- baseURL: https://www.backresto.com
  baseurl_source: declared
  description: Service metadata
  name: BackResto Meta API
  slug: backresto-com-meta-api
- baseURL: https://api.backresto.com
  baseurl_source: declared
  description: The mobile API from BackResto — 1 operation(s) for mobile.
  name: BackResto Mobile API
  slug: backresto-com-mobile-api
- baseURL: https://api.backresto.com
  baseurl_source: declared
  description: The module assets API from BackResto — 3 operation(s) for module assets.
  name: BackResto module assets API
  slug: backresto-com-module-assets-api
- baseURL: https://api.backresto.com
  baseurl_source: declared
  description: The module shadow ingestion API from BackResto — 1 operation(s) for module shadow ingestion.
  name: BackResto module shadow ingestion API
  slug: backresto-com-module-shadow-ingestion-api
- baseURL: https://api.backresto.com
  baseurl_source: declared
  description: The partner restaurants API from BackResto — 1 operation(s) for partner restaurants.
  name: BackResto partner restaurants API
  slug: backresto-com-partner-restaurants-api
- baseURL: https://api.backresto.com
  baseurl_source: declared
  description: The received module snapshots API from BackResto — 3 operation(s) for received module snapshots.
  name: BackResto received module snapshots API
  slug: backresto-com-received-module-snapshots-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/backresto-com/agentic-access/backresto-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/backresto-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/backresto-com/rules/backresto-com-rules.yml
  title: ''
  type: Spectral
  url: rules/backresto-com-rules.yml
- group: design
  href: https://artifacts.apis.io/backresto-com/json-ld/backresto-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/backresto-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/backresto-com/vocabulary/backresto-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/backresto-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/backresto-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/backresto-com/data-model/backresto-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/backresto-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/backresto-com/conventions/backresto-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/backresto-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/backresto-com/conventions/backresto-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/backresto-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/backresto-com/errors/backresto-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/backresto-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/backresto-com/conformance/backresto-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/backresto-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/backresto-com/llms/backresto-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backresto-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/backresto-com/mcp/backresto-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/backresto-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/backresto-com/well-known/backresto-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backresto-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/backresto-com/hosts/backresto-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backresto-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/backresto-com/vendors/backresto-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backresto-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.backresto.com/fr
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.backresto.com/fr/privacy
- group: auth
  href: https://artifacts.apis.io/backresto-com/security/backresto-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backresto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backresto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.backresto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.backresto.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.backresto.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.backresto.com/
- group: company
  title: ''
  type: Blog
  url: https://www.backresto.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.backresto.com/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://backresto.com/openapi.json
  - status: null
    url: https://api.backresto.com/openapi.json
  - status: 401
    url: https://api.backresto.com/mcp
  - status: 200
    url: https://backresto.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BackResto provides a modern, cloud‑based HACCP (Hazard Analysis Critical Control Points) solution for restaurants and food service businesses. The platform offers real‑time hygiene tracking, automated register generation, temperature monitoring, cleaning schedules, and traceability tools, all accessible via a mobile app. Designed by restaurateur Thomas, it eliminates paper logs, reduces daily compliance time from 30 minutes to 5, and ensures readiness for inspections. BackResto supports connected sensors for cold‑room monitoring and generates printable labels for product shelf‑life, helping teams collaborate across multiple locations.
image: https://www.backresto.com/opengraph-image
json_schemas:
- name: AllergenMenu
  property_count: 1
  slug: backresto-com-allergen-menu
- name: AllergenParseRequest
  property_count: 1
  slug: backresto-com-allergen-parse-request
- name: HaccpAuditRequest
  property_count: 12
  slug: backresto-com-haccp-audit-request
- name: HaccpAuditResponse
  property_count: 2
  slug: backresto-com-haccp-audit-response
jsonld:
- class_count: 7
  name: Backresto Com Context
  property_count: 39
  slug: backresto-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.backresto.com.
  name: BackResto MCP Server
  slug: backresto-com-mcp-yml
modified: '2026-11-02'
name: BackResto
nav: Providers
network: true
overview: 'BackResto publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Allergens API, Audit API, and 7 more. Tagged areas include Food, Restaurant, HACCP, Compliance, and Safety.


  The BackResto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BackResto''s developer surface includes support, documentation, API reference, getting-started guide, engineering blog, pricing, and 19 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: BackResto API Rules
  rule_count: 53
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 2
  slug: backresto-com-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 60.1
    developer_ergonomics: 29.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 40.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Backresto Com Domain Security
  slug: backresto-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: partner-restaurants
  slug: backresto-com-partner-restaurants
slug: backresto-com
tags:
- Food
- Restaurant
- HACCP
- Compliance
- Safety
- French
website: https://backresto.com/
---
