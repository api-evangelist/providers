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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.skore.probabl.ai
  baseurl_source: declared
  description: The Anthropic Compatible Agent API from Probabl — 1 operation(s) for anthropic compatible agent.
  name: Probabl Anthropic Compatible Agent API
  slug: probabl-anthropic-compatible-agent-api
- baseURL: https://api.skore.probabl.ai
  baseurl_source: declared
  description: The Health API from Probabl — 1 operation(s) for health.
  name: Probabl Health API
  slug: probabl-health-api
- baseURL: https://api.skore.probabl.ai
  baseurl_source: declared
  description: The identity API from Probabl — 22 operation(s) for identity.
  name: Probabl Identity API
  slug: probabl-identity-api
- baseURL: https://api.skore.probabl.ai
  baseurl_source: declared
  description: The Liveness API from Probabl — 1 operation(s) for liveness.
  name: Probabl Liveness API
  slug: probabl-liveness-api
- baseURL: https://api.skore.probabl.ai
  baseurl_source: declared
  description: The LLM Provider API from Probabl — 3 operation(s) for llm provider.
  name: Probabl LLM Provider API
  slug: probabl-llm-provider-api
- baseURL: https://api.skore.probabl.ai
  baseurl_source: declared
  description: The OpenAI Compatible Agent API from Probabl — 3 operation(s) for openai compatible agent.
  name: Probabl OpenAI Compatible Agent API
  slug: probabl-openai-compatible-agent-api
- baseURL: https://api.skore.probabl.ai
  baseurl_source: declared
  description: The projects API from Probabl — 19 operation(s) for projects.
  name: Probabl Projects API
  slug: probabl-projects-api
- baseURL: https://api.skore.probabl.ai
  baseurl_source: declared
  description: The Readiness API from Probabl — 1 operation(s) for readiness.
  name: Probabl Readiness API
  slug: probabl-readiness-api
artifact_total: 10
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/probabl-skore-hub-overlay.yaml
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
  name: Probabl MCP Server
  slug: probabl-mcp-server
modified: '2026-08-17'
name: Probabl
nav: Providers
network: true
overview: 'Probabl publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Anthropic Compatible Agent API, Health API, Identity API, and 5 more. Tagged areas include Company, Open-Source, Machine-Learning, Data Science, and scikit-learn.


  Probabl''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, CLI, and 15 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 46.4
    developer_ergonomics: 71.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 39.3
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/probabl/refs/heads/main/screenshots/probabl-2026-09-02T152057.png
security:
- kind: domain-security
  name: Probabl Domain Security
  slug: probabl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: probabl
tags:
- Company
- Open-Source
- Machine-Learning
- Data Science
- scikit-learn
- MLOps
- Model Evaluation
- Experiment Tracking
- Agent Skills
- Artificial Intelligence
- Python
- France
website: https://probabl.ai/
---
