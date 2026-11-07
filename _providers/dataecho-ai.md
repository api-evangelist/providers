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
    agent_card: flavored
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Dataecho Ai Agentic Access
  operation_count: 56
  slug: dataecho-ai-agentic-access
  summary_line: 56 operations · 36 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Analytics API from DataEcho — 2 operation(s) for analytics.
  name: DataEcho Analytics API
  slug: dataecho-ai-analytics-api
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Auth API from DataEcho — 2 operation(s) for auth.
  name: DataEcho Auth API
  slug: dataecho-ai-auth-api
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Domains API from DataEcho — 2 operation(s) for domains.
  name: DataEcho Domains API
  slug: dataecho-ai-domains-api
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Drives API from DataEcho — 9 operation(s) for drives.
  name: DataEcho Drives API
  slug: dataecho-ai-drives-api
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Handles API from DataEcho — 1 operation(s) for handles.
  name: DataEcho Handles API
  slug: dataecho-ai-handles-api
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Links API from DataEcho — 2 operation(s) for links.
  name: DataEcho Links API
  slug: dataecho-ai-links-api
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Profile API from DataEcho — 4 operation(s) for profile.
  name: DataEcho Profile API
  slug: dataecho-ai-profile-api
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Site Data API from DataEcho — 2 operation(s) for site data.
  name: DataEcho Site Data API
  slug: dataecho-ai-site-data-api
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Sites API from DataEcho — 10 operation(s) for sites.
  name: DataEcho Sites API
  slug: dataecho-ai-sites-api
- baseURL: https://dataecho.ai
  baseurl_source: declared
  description: The Variables API from DataEcho — 2 operation(s) for variables.
  name: DataEcho Variables API
  slug: dataecho-ai-variables-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/dataecho-ai/agentic-access/dataecho-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dataecho-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dataecho-ai/rules/dataecho-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/dataecho-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/dataecho-ai/vocabulary/dataecho-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dataecho-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dataecho-ai/errors/dataecho-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dataecho-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dataecho-ai/conformance/dataecho-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataecho-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dataecho-ai/llms/dataecho-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataecho-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/dataecho-ai/a2a/dataecho-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dataecho-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dataecho-ai/mcp/dataecho-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dataecho-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dataecho-ai/well-known/dataecho-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataecho-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dataecho-ai/hosts/dataecho-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataecho-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataecho-ai/vendors/dataecho-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataecho-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dataecho-ai/authentication/dataecho-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dataecho-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dataecho-ai/security/dataecho-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataecho-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataecho.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://dataecho.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dataecho.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://dataecho.ai/docs#getting-started
created: '2026-11-04'
description: DataEcho provides free, instant web hosting and private cloud storage designed specifically for AI agents. Users can publish any file or folder to a live, edge‑served URL in seconds without creating an account or signing up. The platform also offers versioned cloud Drives for agent memory, context, and handoff, enabling seamless integration of AI agents with persistent storage.
layout: provider
mcp_servers:
- description: Remote MCP server at dataecho.ai.
  name: DataEcho MCP Server
  slug: dataecho-ai-mcp-yml
modified: '2026-11-04'
name: DataEcho
nav: Providers
network: true
overview: 'DataEcho publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Auth API, Domains API, and 7 more. Tagged areas include Artificial Intelligence, Hosting, Cloud Storage, and Free.


  The DataEcho catalog on APIs.io includes 1 Spectral governance ruleset.


  DataEcho''s developer surface includes authentication, documentation, getting-started guide, and 14 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: DataEcho API Rules
  rule_count: 36
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 3
  slug: dataecho-ai-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 47.8
    developer_ergonomics: 42.9
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dataecho Ai Authentication
  slug: dataecho-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dataecho Ai Domain Security
  slug: dataecho-ai-domain-security
  summary_line: TLSv1.3
slug: dataecho-ai
tags:
- Artificial Intelligence
- Hosting
- Cloud Storage
- Free
website: https://dataecho.ai/
---
