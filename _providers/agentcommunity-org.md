---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public read‑only API for agentcommunity.org providing directory data, search and MCP endpoints.
  name: Agent Community Public API
  slug: agent-community-public-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/agentcommunity-org/authentication/agentcommunity-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentcommunity-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentcommunity-org/conformance/agentcommunity-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentcommunity-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentcommunity-org/llms/agentcommunity-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentcommunity-org-llms.txt
- group: other
  href: https://artifacts.apis.io/agentcommunity-org/a2a/agentcommunity-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentcommunity-org-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentcommunity-org/mcp/agentcommunity-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentcommunity-org-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentcommunity-org/well-known/agentcommunity-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentcommunity-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentcommunity-org/hosts/agentcommunity-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentcommunity-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentcommunity-org/vendors/agentcommunity-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentcommunity-org-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://agentcommunity.org/lists/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentcommunity.org/terms
- group: auth
  title: ''
  type: Security
  url: https://agentcommunity.org/lists/security
- group: start
  title: ''
  type: Sandbox
  url: https://agentcommunity.org/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentcommunity.org/privacy
- group: other
  title: ''
  type: Leadership
  url: https://agentcommunity.org/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentcommunity
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentcommunity.org/developers
- group: company
  title: ''
  type: Blog
  url: https://agentcommunity.org/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://agentcommunity.org/docs/agent-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentcommunity.org/
- group: docs
  title: ''
  type: APIReference
  url: https://agentcommunity.org/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/agentcommunity-org/security/agentcommunity-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentcommunity-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentcommunity.org/
created: '2026-10-31'
description: Agent Community is an open, collaborative network for builders of autonomous agents. It provides a public directory of member organizations, shared standards, governance frameworks, and resources such as events, documentation, and community discussions. The platform aims to promote accountability, openness, fairness, and stewardship in the agentic web, offering tools, specifications, and a space for collaboration among companies, labs, and independent developers.
image: https://agentcommunity.org/opengraph-image?97cf73dea83b04ed
layout: provider
mcp_servers:
- description: Remote MCP server at agentcommunity.org.
  name: Agent Community MCP Server
  slug: agentcommunity-org-mcp-yml
modified: '2026-10-31'
name: Agent Community
nav: Providers
network: true
overview: 'Agent Community is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Community, Open Source, Agents, Governance, and Collaboration.


  Agent Community''s developer surface includes authentication, sandbox, engineering blog, getting-started guide, documentation, API reference, and 16 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 14.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 65.8
    operational_transparency: 7.9
  previous_composite: 29.1
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentcommunity Org Authentication
  slug: agentcommunity-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentcommunity Org Domain Security
  slug: agentcommunity-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agentcommunity-org
tags:
- Community
- Open Source
- Agents
- Governance
- Collaboration
website: https://agentcommunity.org/
---
