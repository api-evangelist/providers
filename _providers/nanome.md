---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: REST API to create workspaces, load molecular structures, create and rename scenes, and add visualization components. Bearer-token auth. Powers the MARA workspace builder, the official Nanome MCP serv
  name: Nanome Workspaces API
  slug: nanome-workspaces-api
- description: Account and session API (e.g. GET /user/session to validate a token).
  name: Nanome Account API
  slug: nanome-account-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://nanome.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nanome.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nanome.ai
- group: company
  title: ''
  type: Blog
  url: https://nanome.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nanome.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mara.nanome.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nanome.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nanome.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nanome-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://nanome.statuspage.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/nanome-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/nanome-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nanome-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nanome-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nanome-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nanome-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nanome-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nanome-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nanome-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nanome-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nanome-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nanome-llms.txt
created: '2026-07-17'
description: Nanome is a collaborative workspace for drug discovery — molecular visualization and design in VR/XR and the browser, backed by an in-session AI assistant called MARA. Scientists and agents load protein and small-molecule structures from public databases (RCSB PDB, AlphaFold, PubChem, ChEMBL, SWISS-MODEL, COD), organize them into scenes with rich visual representations (cartoons, surfaces, ball-and-stick, interactions), and collaborate inside shared 3D workspaces. Nanome exposes a REST Workspaces API (workspaces.nanome.ai) and an official Model Context Protocol (MCP) server so agents can build and populate workspaces programmatically, plus a Python library (nanome-lib) for authoring plugins. Surfaced as a portfolio company of Bullpen Capital and enriched into the API Evangelist network.
image: https://nanome.ai/MR_preview.jpg
layout: provider
mcp_servers:
- description: ''
  name: nanome-mcp.yml
  slug: nanome-mcpyml
modified: '2026-07-20'
name: Nanome
nav: Providers
network: true
overview: 'Nanome publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drug Discovery, Molecular Visualization, Life Sciences, and Cheminformatics.


  Nanome''s developer surface includes documentation, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 30.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 30.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nanome/refs/heads/main/screenshots/nanome-2026-08-07T184617.png
security:
- kind: authentication
  name: Nanome Authentication
  slug: nanome-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nanome Domain Security
  slug: nanome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nanome
tags:
- Company
- Drug Discovery
- Molecular Visualization
- Life Sciences
- Cheminformatics
- Structural Biology
- Virtual Reality
- Collaboration
- Artificial Intelligence
website: https://nanome.ai
---
