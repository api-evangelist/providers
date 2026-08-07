---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 96
  human_in_the_loop: 0
  name: Aleph Alpha Agentic Access
  operation_count: 194
  slug: aleph-alpha-agentic-access
  summary_line: 194 operations · 96 acting
api_count: 6
apis:
- description: Access and interact with Aleph Alpha models and functionality over HTTP endpoints. Provides completion, chat completions, embeddings, semantic and batch semantic embeddings, tokenization and detokeniz
  name: PhariaInference API
  slug: pharia-inference
- description: The PhariaData API provides a comprehensive suite of endpoints to manage data workflows within the Pharia Data Platform — repositories, datasets, datapoints, stages, files, downloads, connectors, tran
  name: PhariaData API
  slug: pharia-data
- description: The Document Index is a service that provides semantic search over your knowledge base. It handles chunking and embedding of documents and keeps embeddings in sync, and exposes namespaces, collections
  name: PhariaSearch / Document Index API
  slug: pharia-search
- description: PhariaStudio is the collaborative development environment for building, debugging, evaluating and deploying organisation-specific AI solutions. Its API covers projects, traces, spans and events, evalu
  name: PhariaStudio API
  slug: pharia-studio
- description: PhariaOS is a resource management system that oversees the entire lifecycle of AI resources, from inception to maintenance. The Manager API covers cluster GPUs, nodes and taints, use cases and deploym
  name: PhariaOS Manager API
  slug: pharia-os
- description: 'A stateful, OpenAI-compatible Responses API for building agentic applications on PhariaAI. Supports conversations, response persistence and retrieval, guardrail checks, client-executed function tools '
  name: Responses API (Stateful Responses)
  slug: responses
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aleph-alpha-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aleph-alpha-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aleph-alpha-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aleph-alpha.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aleph-alpha.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/pharia-openapi/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/phariaai-applications/quick-start-custom-apps.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/get-token.html
- group: operate
  title: ''
  type: Support
  url: https://supportportal.aleph-alpha.com/
- group: company
  title: ''
  type: Blog
  url: https://aleph-alpha.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aleph-Alpha
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aleph-alpha.com/phariaai-home/latest/release-notes/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aleph-alpha.com/data-privacy/
- group: other
  title: ''
  type: Imprint
  url: https://aleph-alpha.com/imprint/
- group: other
  title: ''
  type: Research
  url: https://aleph-alpha.com/research/
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/Aleph-Alpha
- group: build
  title: ''
  type: Packages
  url: packages/aleph-alpha-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aleph-alpha-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/aleph-alpha-cli.yml
- group: design
  title: ''
  type: Components
  url: components/aleph-alpha-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aleph-alpha-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aleph-alpha-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aleph-alpha-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/aleph-alpha-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aleph-alpha-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aleph-alpha-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.aleph-alpha.com/phariaai-home/latest/release-notes/index.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aleph-alpha-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aleph-alpha-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dqsglobal.com/en/customer-database/aleph-alpha-gmbh
- group: auth
  title: ''
  type: TrustCenter
  url: security/aleph-alpha-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aleph-alpha-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aleph-alpha-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-inference-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-responses-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-search-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-studio-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aleph-alpha-pharia-os-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aleph-alpha-sandbox.yml
- group: other
  title: ''
  type: Playground
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/pharia-studio/playground.html
- group: operate
  title: ''
  type: Contact
  url: https://aleph-alpha.com/en/contact/
created: '2026-08-02'
description: Aleph Alpha is a Heidelberg, Germany based sovereign AI company building PhariaAI, an end-to-end, customizable AI suite for enterprises and governments that can be deployed on-premise or hosted. The stack combines leading open-source and proprietary large language models with Aleph Alpha's own Pharia-1-LLM model family and its research into transparency, explainability and domain-specific performance. PhariaAI is exposed through six documented HTTP APIs — PhariaInference (completion, chat, embeddings, tokenization), PhariaData (repositories, datasets, transformations), PhariaSearch / Document Index (semantic search over a knowledge base), PhariaStudio (projects, traces, evaluation, benchmarks), PhariaOS (cluster, use case and model lifecycle management) and a stateful, OpenAI-compatible Responses API with MCP tool calling — each published as an OpenAPI or Swagger definition on the Aleph Alpha documentation site. First-party SDKs ship for Python and Rust, alongside a CLI for
  publishing WebAssembly skills to the Pharia Kernel.
image: https://aleph-alpha.com/og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: aleph-alpha-mcp.yml
  slug: aleph-alpha-mcpyml
modified: '2026-08-02'
name: Aleph Alpha
nav: Providers
network: true
overview: 'Aleph Alpha publishes 6 APIs on the [APIs.io](https://apis.io/) network, including PhariaInference API, PhariaData API, PhariaSearch / Document Index API, and 3 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, Large Language Models, and Generative AI.


  Aleph Alpha''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 37 more developer resources.'
random_paper: 68
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 54.4
    developer_ergonomics: 82.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 48.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Aleph Alpha Authentication
  slug: aleph-alpha-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Aleph Alpha Domain Security
  slug: aleph-alpha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aleph Alpha Trust Center
  slug: aleph-alpha-trust-center
  summary_line: trust center published
slug: aleph-alpha
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Large Language Models
- Generative AI
- Sovereign AI
- Inference
- Embeddings
- Semantic Search
- Vector Search
- Agents
- Model Context Protocol
- Germany
- Enterprise Software
- Government
website: https://aleph-alpha.com/en/
---
