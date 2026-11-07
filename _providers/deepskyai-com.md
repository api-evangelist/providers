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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Deepskyai Com Agentic Access
  operation_count: 11
  slug: deepskyai-com-agentic-access
  summary_line: 11 operations · 4 acting
api_count: 1
apis:
- baseURL: https://www.deepskyai.com
  baseurl_source: declared
  description: The Compliance API from Deepsky — 1 operation(s) for compliance.
  name: Deepsky Compliance API
  slug: deepskyai-com-compliance-api
- baseURL: https://www.deepskyai.com
  baseurl_source: declared
  description: The Deepsky Aviation Agent API API from Deepsky — 2 operation(s) for deepsky aviation agent api.
  name: Deepsky Deepsky Aviation Agent API
  slug: deepskyai-com-deepsky-aviation-agent-api-api
- baseURL: https://www.deepskyai.com
  baseurl_source: declared
  description: The Mcp API from Deepsky — 1 operation(s) for mcp.
  name: Deepsky MCP API
  slug: deepskyai-com-mcp-api
- baseURL: https://www.deepskyai.com
  baseurl_source: declared
  description: The Search API from Deepsky — 3 operation(s) for search.
  name: Deepsky Search API
  slug: deepskyai-com-search-api
- baseURL: https://www.deepskyai.com
  baseurl_source: declared
  description: The Skills API from Deepsky — 2 operation(s) for skills.
  name: Deepsky Skills API
  slug: deepskyai-com-skills-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/deepskyai-com/agentic-access/deepskyai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deepskyai-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/deepskyai-com/rules/deepskyai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/deepskyai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/deepskyai-com/json-ld/deepskyai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deepskyai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/deepskyai-com/vocabulary/deepskyai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deepskyai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deepskyai-com/data-model/deepskyai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deepskyai-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/deepskyai-com/errors/deepskyai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deepskyai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deepskyai-com/conformance/deepskyai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deepskyai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deepskyai-com/llms/deepskyai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deepskyai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/deepskyai-com/mcp/deepskyai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deepskyai-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/deepskyai-com/well-known/deepskyai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deepskyai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/deepskyai-com/hosts/deepskyai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepskyai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepskyai-com/vendors/deepskyai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepskyai-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.deepskyai.com/app/login
- group: auth
  href: https://artifacts.apis.io/deepskyai-com/authentication/deepskyai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deepskyai-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/deepskyai-com/security/deepskyai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepskyai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deepskyai.com/
- group: company
  title: ''
  type: Blog
  url: https://www.deepskyai.com/newsletter
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deepskyai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deepskyai.com/privacy
created: '2026-11-05'
description: Deepsky provides AI‑driven automation for Aircraft Entry Into Service (EIS) documentation, helping operators accelerate regulatory approval by generating manuals, forms and compliance documents. Their platform streamlines the creation of Operational Manuals, OMELs, and other required paperwork, reducing delays that can cost thousands of dollars per aircraft. By integrating operator data with regulatory requirements, Deepsky aims to cut document turnaround from months to days, improving efficiency for airlines and manufacturers.
image: https://www.deepskyai.com/deepsky-logo.png
json_schemas:
- name: SearchRequest
  property_count: 2
  slug: deepskyai-com-search-request
- name: SearchResponse
  property_count: 5
  slug: deepskyai-com-search-response
jsonld:
- class_count: 4
  name: Deepskyai Com Context
  property_count: 15
  slug: deepskyai-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.deepskyai.com.
  name: Deepsky MCP Server
  slug: deepskyai-com-mcp-yml
modified: '2026-11-05'
name: Deepsky
nav: Providers
network: true
overview: 'Deepsky publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Compliance API, Deepsky Aviation Agent API, MCP API, and 2 more. Tagged areas include Aviation, Artificial Intelligence, Automation, Documentation, and Compliance.


  The Deepsky catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Deepsky''s developer surface includes authentication, engineering blog, and 17 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Deepsky API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: deepskyai-com-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 55.3
    developer_ergonomics: 14.3
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deepskyai Com Authentication
  slug: deepskyai-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deepskyai Com Domain Security
  slug: deepskyai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deepskyai-com
tags:
- Aviation
- Artificial Intelligence
- Automation
- Documentation
- Compliance
- Company
website: https://www.deepskyai.com/
---
