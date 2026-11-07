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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/agile-today-org/llms/agile-today-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agile-today-org-llms.txt
- group: build
  href: https://artifacts.apis.io/agile-today-org/mcp/agile-today-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agile-today-org-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agile-today-org/mcp/agile-today-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agile-today-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/agile-today-org/hosts/agile-today-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agile-today-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/agile-today-org/vendors/agile-today-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agile-today-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agile-today-org/security/agile-today-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agile-today-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agile-today.org/
- group: docs
  title: ''
  type: Documentation
  url: https://agile-today.org/en/
- group: docs
  title: ''
  type: APIReference
  url: https://agile-today.org/api/mcp
- group: company
  title: ''
  type: Blog
  url: https://agile-today.org/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agile-today.org/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agile-today.org/en/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://agile-today.org/en/about
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract found despite documentation page at https://agile-today.org/api returning 404.
  evidence:
  - status: 404
    url: https://agile-today.org/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agile Today provides a methodology graph for AI agents to manage projects through a structured set of gates and stages. The platform integrates practices from PMBOK®, PRINCE2®, Scrum, Kanban, and BABOK®, offering reproducible, traceable decision support for hybrid delivery, complex scopes, and fixed‑price contracts. It is a public beta, free, with no sign‑up required, and includes an MCP endpoint with read‑only tools for AI integration.
image: https://agile-today.org/opengraph-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at agile-today.org.
  name: Agile Today MCP Server
  slug: agile-today-org-mcp-yml
modified: '2026-11-01'
name: Agile Today
nav: Providers
network: true
overview: 'Agile Today is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Project Management, AI Integration, Methodology, Open Source, and Public Beta.


  Agile Today''s developer surface includes documentation, API reference, engineering blog, getting-started guide, and 9 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 15.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agile Today Org Domain Security
  slug: agile-today-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agile-today-org
tags:
- Project Management
- AI Integration
- Methodology
- Open Source
- Public Beta
website: https://agile-today.org/
---
