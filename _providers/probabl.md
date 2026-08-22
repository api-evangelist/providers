---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Public REST API for Skore Hub, Probabl's hosted collaboration platform for machine-learning experiments. Covers identity (OAuth authorization-code and device flows, token refresh, user profile, per-wo
  name: Skore Hub API
  slug: skore-hub-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://probabl.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skore.probabl.ai/stable/
- group: docs
  title: ''
  type: APIReference
  url: https://api.skore.probabl.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skore.probabl.ai/stable/install.html
- group: company
  title: ''
  type: Blog
  url: https://blog.probabl.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/probabl-ai
- group: operate
  title: ''
  type: Support
  url: https://discord.probabl.ai/
- group: operate
  title: ''
  type: Contact
  url: https://www.probabl.ai/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.probabl.ai/legal/skore-eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.probabl.ai/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.probabl.ai/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/probabl-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/probabl-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/probabl-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/probabl-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/probabl-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/probabl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/probabl-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/probabl-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/probabl-domain-security.yml
created: '2026-08-17'
description: 'Probabl (styled ":probabl.") is the French, Inria-spun-out company behind scikit-learn — "the Tabular AI company by the creators of scikit-learn" — founded in 2023 to develop, maintain and commercially sustain the open-source Python data-science stack (scikit-learn, skrub, skore). Its commercial product is Skore: an open-source Python library (`skore`) that turns model training into structured, auditable artifacts — estimator reports, cross-validation reports, comparison reports, data and metric diagnostics — plus Skore Hub, a hosted collaboration platform where teams push, compare and track those artifacts across workspaces and projects. Skore Hub exposes a public REST API (Skore Hub, OpenAPI 3.1.0, 67 operations) covering identity/OAuth, workspaces, members and API keys, projects, estimator/cross-validation/comparison reports, artifacts, project goals, and OpenAI/Anthropic-compatible agent endpoints. Probabl also publishes a first-party Agent Skills package (probabl-skills,
  BSD-3-Clause) of 14 data-science skills for coding agents such as Claude Code and Cursor, a `skore` CLI, training via Skolar, and the Scikit-learn Central ecosystem explorer.'
image: https://avatars.githubusercontent.com/u/135336812?v=4
layout: provider
mcp_servers:
- description: ''
  name: probabl-mcp.yml
  slug: probabl-mcpyml
modified: '2026-08-17'
name: Probabl
nav: Providers
network: true
overview: 'Probabl publishes 1 API on the [APIs.io](https://apis.io/) network: Skore Hub API. Tagged areas include Company, Open Source, machine-learning, data-science, and scikit-learn.


  Probabl''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, CLI, and 14 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 38.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 49.3
    developer_ergonomics: 52.4
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 18.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: domain-security
  name: Probabl Domain Security
  slug: probabl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: probabl
tags:
- Company
- Open Source
- machine-learning
- data-science
- scikit-learn
- mlops
- model-evaluation
- experiment-tracking
- agent-skills
- artificial-intelligence
- python
- france
website: https://probabl.ai/
---
