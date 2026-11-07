---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Bowmark Ai Agentic Access
  operation_count: 13
  slug: bowmark-ai-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.bowmark.ai
  baseurl_source: declared
  description: The Library API from Bowmark AI — 1 operation(s) for library.
  name: Bowmark AI Library API
  slug: bowmark-ai-library-api
- baseURL: https://api.bowmark.ai
  baseurl_source: declared
  description: The Recipes API from Bowmark AI — 2 operation(s) for recipes.
  name: Bowmark AI Recipes API
  slug: bowmark-ai-recipes-api
- baseURL: https://api.bowmark.ai
  baseurl_source: declared
  description: The Run API from Bowmark AI — 1 operation(s) for run.
  name: Bowmark AI Run API
  slug: bowmark-ai-run-api
- baseURL: https://api.bowmark.ai
  baseurl_source: declared
  description: The Scripts API from Bowmark AI — 3 operation(s) for scripts.
  name: Bowmark AI Scripts API
  slug: bowmark-ai-scripts-api
- baseURL: https://api.bowmark.ai
  baseurl_source: declared
  description: The Sites API from Bowmark AI — 3 operation(s) for sites.
  name: Bowmark AI Sites API
  slug: bowmark-ai-sites-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/bowmark-ai/agentic-access/bowmark-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bowmark-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bowmark-ai/rules/bowmark-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bowmark-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bowmark-ai/json-ld/bowmark-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bowmark-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bowmark-ai/vocabulary/bowmark-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bowmark-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bowmark-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bowmark-ai/data-model/bowmark-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bowmark-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bowmark-ai/authentication/bowmark-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bowmark-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/bowmark-ai/errors/bowmark-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bowmark-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bowmark-ai/conformance/bowmark-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bowmark-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bowmark-ai/llms/bowmark-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bowmark-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bowmark-ai/mcp/bowmark-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bowmark-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bowmark-ai/well-known/bowmark-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bowmark-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bowmark-ai/hosts/bowmark-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bowmark-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bowmark-ai/vendors/bowmark-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bowmark-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/bowmark-ai/packages/bowmark-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/bowmark-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/bowmark-ai/packages/bowmark-ai-packages.yml
  title: ''
  type: Packages
  url: packages/bowmark-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bowmark.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://bowmark.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bowmark.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://bowmark.ai/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://bowmark.ai/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/bowmark-ai/mcp/releases/latest/download/bowmark.mcpb
- group: commercial
  title: ''
  type: Pricing
  url: https://bowmark.ai/docs/pricing.md
- group: start
  title: ''
  type: GettingStarted
  url: https://bowmark.ai/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://bowmark.ai/docs/http-api.md
- group: auth
  href: https://artifacts.apis.io/bowmark-ai/security/bowmark-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bowmark-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bowmark.ai/
created: '2026-11-02'
description: Bowmark AI reorganizes web functionality into a typed capability library that AI agents call by writing code, instead of driving a browser page by page. It provides an MCP server and skill that gives an AI agent a typed library of website functions, enabling agents to retrieve structured data from any website without manual browsing. The service covers search boxes, filters, quote forms, product configurators, availability lookups, checkout and booking flows, and pages behind login, offering a free tier with usage‑based pricing.
image: https://bowmark.ai/opengraph-image?afaa719fdee20bfc
json_schemas:
- name: Recipe
  property_count: 6
  slug: bowmark-ai-recipe
- name: RunEnvelope
  property_count: 15
  slug: bowmark-ai-run-envelope
- name: SavedScript
  property_count: 7
  slug: bowmark-ai-saved-script
jsonld:
- class_count: 3
  name: Bowmark Ai Context
  property_count: 26
  slug: bowmark-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.bowmark.ai.
  name: Bowmark AI MCP Server
  slug: bowmark-ai-mcp-yml
modified: '2026-11-02'
name: Bowmark AI
nav: Providers
network: true
overview: 'Bowmark AI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Library API, Recipes API, Run API, and 2 more. Tagged areas include Artificial Intelligence, Automation, Web, Data Extraction, and Platform.


  The Bowmark AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bowmark AI''s developer surface includes authentication, support, documentation, changelog, pricing, getting-started guide, API reference, and 20 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Bowmark AI API Rules
  rule_count: 58
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 2
  slug: bowmark-ai-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 62.2
    developer_ergonomics: 37.5
    discoverability: 65.0
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bowmark Ai Authentication
  slug: bowmark-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bowmark Ai Domain Security
  slug: bowmark-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: bowmark-ai-run-script
  slug: bowmark-ai-run-script
slug: bowmark-ai
tags:
- Artificial Intelligence
- Automation
- Web
- Data Extraction
- Platform
- Company
website: https://bowmark.ai/
---
