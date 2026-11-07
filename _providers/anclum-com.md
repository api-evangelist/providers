---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Anclum provides a directory of MCP servers, agent skills, and AI tools; the API is documented at the MCP directory documentation page.
  name: Anclum API
  slug: anclum-api
- description: 'Anclum API as documented publicly: 30 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Anclum API
  slug: anclum-com-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/anclum-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anclum-com/rules/anclum-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anclum-com-rules.yml
- group: design
  href: https://artifacts.apis.io/anclum-com/json-ld/anclum-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anclum-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/anclum-com/vocabulary/anclum-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anclum-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/anclum-com/data-model/anclum-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anclum-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/anclum-com/changelog/anclum-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/anclum-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/anclum-com/conformance/anclum-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anclum-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anclum-com/llms/anclum-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anclum-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anclum-com/mcp/anclum-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anclum-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anclum-com/well-known/anclum-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anclum-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anclum-com/hosts/anclum-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anclum-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://anclum.com/en/mcp-directory/security/
- group: build
  title: ''
  type: SDKs
  url: https://anclum.com/zh/mcp-directory/dev/sdk/
- group: company
  title: ''
  type: Newsroom
  url: https://anclum.com/en/mcp-directory/media/
- group: operate
  title: ''
  type: ChangeLog
  url: https://anclum.com/en/changelog/
- group: auth
  href: https://artifacts.apis.io/anclum-com/security/anclum-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anclum-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anclum.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anclum.com/en/
- group: operate
  title: ''
  type: Support
  url: https://anclum.com/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://anclum.com/en/r/bloggers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wdfdaivd/skilltide-mcp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anclum.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anclum.com/en/privacy/
coverage:
  checked: '2026-11-01'
  detail: Public documentation pages exist but no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract was found.
  evidence:
  - status: 404
    url: https://anclum.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Anclum is an independent index of MCP servers, agent skills, and open‑source AI tools for developers and AI agents. The site provides a searchable directory, browsing by category, and links to the underlying GitHub repositories. It aggregates data from public sources, offers a multilingual interface (English and Chinese), and includes pages for terms, privacy, contact, and community blogs.
image: https://anclum.com/og.png
json_schemas:
- name: PostFetchResponse
  property_count: 1
  slug: anclum-com-post-fetch-response
- name: PostSearchResponse
  property_count: 3
  slug: anclum-com-post-search-response
jsonld:
- class_count: 2
  name: Anclum Com Context
  property_count: 4
  slug: anclum-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at anclum.com.
  name: Anclum MCP Server
  slug: anclum-com-mcp-yml
modified: '2026-11-01'
name: Anclum
nav: Providers
network: true
overview: 'Anclum is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include MCP, Artificial Intelligence, Tools, Directory, and Open Source.


  The Anclum catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anclum''s developer surface includes changelog, documentation, support, engineering blog, and 19 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Anclum API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: anclum-com-rules
scopes:
- name: Anclum Com Scopes
  scope_count: 0
  slug: anclum-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 21.9
    discoverability: 57.5
    operational_transparency: 15.8
  previous_composite: 29.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anclum Com Authentication
  slug: anclum-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anclum Com Domain Security
  slug: anclum-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anclum-com
tags:
- MCP
- Artificial Intelligence
- Tools
- Directory
- Open Source
- Community
website: https://anclum.com/
---
