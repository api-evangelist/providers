---
agent_readiness:
  band: human-only
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Explore Impact Engines tools for survey teams, including the Survey Solutions MCP Server, Simple BYOK, specialised AI, and dashboard prototypes.
  name: Impact Engines Tools API
  slug: impact-engines-tools-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/impactengines-ai/llms/impactengines-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/impactengines-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/impactengines-ai/mcp/impactengines-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/impactengines-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/impactengines-ai/hosts/impactengines-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/impactengines-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/impactengines-ai/vendors/impactengines-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/impactengines-ai-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lbruce-wq
- group: auth
  href: https://artifacts.apis.io/impactengines-ai/security/impactengines-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/impactengines-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://impactengines.ai/
- group: company
  title: ''
  type: Blog
  url: https://impactengines.ai/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://impactengines.ai/tools/
- group: operate
  title: ''
  type: Support
  url: https://impactengines.ai/contact/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's documented tools page.
  evidence:
  - status: 200
    url: https://impactengines.ai/tools/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Impact Engines is a specialist AI consulting practice for global development data, national statistics, and survey systems. They help organisations use AI across the full data lifecycle, from field collection and cleaning to analysis, statistics, and reporting, offering services such as AI‑driven survey quality control, data cleaning workflows, responsible AI implementation, and bespoke application development.
image: https://impactengines.ai/assets/impact-engines-og.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at classifications.impactengines.ai.
  name: impactengines-ai MCP Server
  slug: impactengines-ai-mcp-yml
modified: '2026-10-30'
name: impactengines-ai
nav: Providers
network: true
overview: 'impactengines-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Consulting, Development Data, and Official Statistics.


  impactengines-ai''s developer surface includes engineering blog, documentation, support, and 7 more developer resources.'
random_paper: 22
scopes:
- name: Impactengines Ai Scopes
  scope_count: 0
  slug: impactengines-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Impactengines Ai Authentication
  slug: impactengines-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Impactengines Ai Domain Security
  slug: impactengines-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: impactengines-ai
tags:
- Company
- AI
- Consulting
- Development Data
- Official Statistics
- Survey Quality
website: https://impactengines.ai/
---
