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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 21
common:
- group: company
  title: ''
  type: Blog
  url: https://microsoft.github.io/autogen/0.2/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://microsoft.github.io/autogen/
- group: docs
  title: ''
  type: Documentation
  url: https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html
- group: other
  title: ''
  type: Installation
  url: https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/installation.html
- group: other
  title: ''
  type: Usage
  url: https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/usage.html
- group: other
  title: ''
  type: ExperimentalFeatures
  url: https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/experimental.html
- group: operate
  title: ''
  type: FAQ
  url: https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/faq.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/autogen
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/microsoft/autogen/tree/main/python/packages/autogen-studio
- group: build
  title: ''
  type: PackagePyPI
  url: https://pypi.org/project/autogenstudio/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: operate
  title: ''
  type: Discord
  url: https://aka.ms/autogen-discord
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/pyautogen
- group: learn
  title: ''
  type: VideoTutorial
  url: https://youtu.be/oum6EI7wohM
- group: other
  title: ''
  type: ResearchPaper
  url: https://aclanthology.org/2024.emnlp-demo.8/
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/microsoft/autogen/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/microsoft/autogen/blob/main/LICENSE-CODE
- group: other
  title: ''
  type: Companion
  url: https://github.com/api-evangelist/microsoft-autogen
created: '2026-05-24'
description: AutoGen Studio is a low-code / no-code developer GUI from Microsoft Research for rapidly prototyping, composing, and debugging multi-agent AI workflows built on the AutoGen framework. Shipped as the `autogenstudio` Python package and launched with `autogenstudio ui`, it serves a FastAPI + React (Gatsby) web app on localhost that exposes four primary interfaces — Team Builder, Playground, Gallery, and Deployment — backed by a SQLModel persistence layer (SQLite by default; any SQLAlchemy-compatible backend such as PostgreSQL, MySQL, MSSQL via `--database-uri`). The Team Builder offers drag-and-drop and JSON authoring of teams, agents, models, tools, and termination conditions fully aligned with AutoGen AgentChat's declarative component spec; the Playground streams live inter-agent messages and renders the control transition graph; the Gallery imports community components; and the Deployment view exports a team to Python, exposes it as an endpoint, and packages it for Docker. AutoGen
  Studio is built on AutoGen AgentChat / Core / Extensions and supports any OpenAI-compatible model endpoint (OpenAI, Azure OpenAI, Anthropic, local vLLM/Ollama, etc.) via declarative `model_client` configuration, plus MCP tool integration. Authentication is experimental (GitHub OAuth + JWT only). Microsoft explicitly positions AutoGen Studio as a research prototype — not production-ready — and encourages teams that need authn/z, multi-tenancy, sandboxing rigor, or hardened deployment to build directly on the AutoGen framework instead. Companion to the broader AutoGen multi-agent framework, distributed under the Microsoft microsoft/autogen monorepo (CC-BY-4.0 docs, MIT code).
features:
- Installable via `pip install -U autogenstudio` (Python 3.10+); current PyPI release 0.4.2.2
- Launched as a local web app with `autogenstudio ui --port 8081` (FastAPI backend + Gatsby/React frontend)
- Configurable via `--host`, `--port`, `--appdir`, `--reload`, `--database-uri`, `--upgrade-database`, `--auth-config`
- Team Builder visual canvas with drag-and-drop assembly of teams, agents, models, tools, and termination conditions, plus equivalent direct JSON editing
- Component Library backed by AutoGen AgentChat's declarative component spec (teams, agents, models, tools, termination conditions)
- Playground with live inter-agent message streaming, control transition graph visualization, UserProxyAgent sessions, and pause/stop run control
- Gallery for discovering and importing community-created components and third-party integrations
- Deployment view that exports a team to Python code, exposes it as a runnable endpoint, and supports containerized execution via Docker
- Bring-your-own model — any OpenAI-compatible endpoint (OpenAI, Azure OpenAI, Anthropic, vLLM, Ollama, local models) via declarative `model_client` config; AutoGen Extensions provides first-party clients
- Define agents in Python with AutoGen AgentChat, dump to JSON via `dump_component().model_dump_json()`, and import into Studio's JSON editor
- MCP (Model Context Protocol) tool integration via `autogenstudio/mcp` and `/api/mcp` routes
- SQLModel-based persistence (Pydantic + SQLAlchemy) — defaults to SQLite, supports PostgreSQL, MySQL, MSSQL, Oracle, and other SQLAlchemy dialects
- Internal FastAPI surface (not a public API) under `/api/` with routes for teams, sessions, runs, gallery, mcp, settings, validation, and a `/api/ws` WebSocket for streaming
- Experimental GitHub OAuth authentication with JWT (`--auth-config auth.yaml`); disabled by default, WebSockets require `?token=` query param when enabled
- Default app directory `~/.autogenstudio/` for database and generated user files
- Dev container shipped under `python/packages/autogen-studio/.devcontainer/` for source builds
- Frontend stack: React + Gatsby (built with `yarn build`); backend served by `autogenstudio.web.serve`
- Explicitly positioned by Microsoft as a research prototype — not production-ready; lacks production-grade authn/z, multi-tenancy, jailbreak hardening, and least-privilege key scoping
- Companion to the broader AutoGen framework (AgentChat, Core, Extensions, .NET) under the microsoft/autogen monorepo (~58k GitHub stars)
- Original research prototype (Oct 2023) by Dibia, Bansal, Fourney, Choudhury, Amershi, Awadallah, Wang; EMNLP 2024 System Demonstrations paper
- License: MIT for code, CC-BY-4.0 for documentation
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autogen-studio.png
layout: provider
modified: '2026-05-24'
name: AutoGen Studio
nav: Providers
network: true
overview: 'AutoGen Studio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AutoGen, AutoGen Studio, Multi-Agent, Agent Framework, and Agentic AI.


  AutoGen Studio''s developer surface includes engineering blog, documentation, FAQ, and 15 more developer resources.'
random_paper: 39
score:
  band: minimal
  composite: 8.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autogen-studio/refs/heads/main/screenshots/autogen-studio-2026-06-20T172642.png
slug: autogen-studio
tags:
- AutoGen
- AutoGen Studio
- Multi-Agent
- Agent Framework
- Agentic AI
- Low-Code
- No-Code
- GUI
- Visual Builder
- Drag and Drop
- Prototyping
- AgentChat
- Microsoft Research
- Python
- FastAPI
- React
- SQLModel
- MCP
- Open Source
website: https://microsoft.github.io/autogen/
---
