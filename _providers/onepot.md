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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.6
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Programmatic access to onepot CORE for make-on-demand molecule discovery and synthesis. Run similarity (Tanimoto) and substructure (SMILES/SMARTS) search, optional retrosynthetic decomposition with bu
  name: Onepot API
  slug: onepot-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.onepot.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.onepot.ai/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.onepot.ai/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.onepot.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.onepot.ai/api
- group: company
  title: ''
  type: Blog
  url: https://www.onepot.ai/blog
- group: other
  title: ''
  type: Research
  url: https://www.onepot.ai/research
- group: build
  title: ''
  type: Packages
  url: packages/onepot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/onepot-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onepot-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/onepot-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onepot-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onepot-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onepot-domain-security.yml
created: '2026-07-17'
description: Onepot (onepot.ai) is a San Francisco-based startup building an AI-powered, fully automated custom synthesis platform for small-molecule drug discovery. It combines ultra-high-throughput lab automation in its POT-1 lab with an AI organic chemist ("Phil") and reaction foundation models to search, quote, and synthesize make-on-demand molecules end to end, aiming to replace slow, error-prone CRO workflows. Onepot exposes a developer API and a Python client (published on PyPI as "onepot") that lets teams run Tanimoto similarity and SMILES/SMARTS substructure search over the full onepot CORE compound space, perform retrosynthetic decomposition with building-block and price/risk filters, stream real-time results over server-sent events, and place synthesis orders programmatically from their own pipelines using an API key.
image: https://www.onepot.ai/onepot_logo_color.svg
layout: provider
mcp_servers:
- description: ''
  name: onepot-mcp.yml
  slug: onepot-mcpyml
modified: '2026-07-20'
name: Onepot
nav: Providers
network: true
overview: 'Onepot publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chemistry, Cheminformatics, Drug Discovery, and Small Molecule Synthesis.


  Onepot''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, and 10 more developer resources.'
random_paper: 65
score:
  band: emerging
  composite: 19.3
  delta: 0.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.6
  provenance:
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onepot/refs/heads/main/screenshots/onepot-2026-08-07T190333.png
security:
- kind: authentication
  name: Onepot Authentication
  slug: onepot-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Onepot Domain Security
  slug: onepot-domain-security
  summary_line: TLSv1.3 · HSTS
slug: onepot
tags:
- Company
- Chemistry
- Cheminformatics
- Drug Discovery
- Small Molecule Synthesis
- Contract Research Organization
- Artificial Intelligence
- Machine Learning
- Lab Automation
- Life Sciences
- API
website: https://www.onepot.ai
---
