---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.staircase.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://elephant.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/elephant-xyz/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elephant-xyz
- group: company
  title: ''
  type: Blog
  url: https://www.staircase.co/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/elephant-xyz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.staircase.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.staircase.co/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/staircase-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/staircase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/staircase-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/staircase-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/staircase-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/staircase-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/staircase-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/staircase-llms.txt
created: '2026-07-17'
description: 'Staircase, Inc. operates the Elephant Protocol (elephant.xyz), a decentralized property-data network that aggregates and cryptographically verifies fragmented county property and address records into trusted, agent-consumable data. It publishes 500,000+ enriched property data points and an unusually agent-native developer surface: a Model Context Protocol (MCP) server (@elephant-xyz/mcp, both stdio and hosted), an Elephant CLI (@elephant-xyz/cli) for oracle data transformation and on-chain proof submission to Polygon, a fact-sheet generator, and a library of 14 published Agent Skills for county-data ingestion. An Enterprise API is offered to organizations at scale. Backed by Bessemer Venture Partners; originally a mortgage-technology API company, now focused on real estate data infrastructure.'
image: https://www.staircase.co/favicon.ico
layout: provider
mcp_servers:
- description: Exposes the Elephant property data graph — county datasets, oracle property records, JSON Schemas, geospatial lookups, and read-only SQL — to AI agents.
  name: Elephant MCP server
  slug: elephant-mcp-server
modified: '2026-07-21'
name: Staircase
nav: Providers
network: true
overview: 'Staircase is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Real-Estate, Property Data, and Data.


  Staircase''s developer surface includes documentation, engineering blog, support, CLI, and 13 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 15.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/staircase/refs/heads/main/screenshots/staircase-2026-09-02T160720.png
security:
- kind: domain-security
  name: Staircase Domain Security
  slug: staircase-domain-security
  summary_line: TLSv1.3 · HSTS
slug: staircase
tags:
- Company
- Fintech
- Real-Estate
- Property Data
- Data
- MCP
- Agents
- Blockchain
website: https://www.staircase.co/
---
