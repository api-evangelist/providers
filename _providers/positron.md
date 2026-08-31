---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Positron Agentic Access
  operation_count: 23
  slug: positron-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 3
apis:
- description: The access_tokens API from Positron — 3 operation(s) for access_tokens.
  name: Positron Access Tokens API
  slug: positron-access-tokens-api
- description: The completion API from Positron — 2 operation(s) for completion.
  name: Positron Completion API
  slug: positron-completion-api
- description: The models API from Positron — 5 operation(s) for models.
  name: Positron Models API
  slug: positron-models-api
- description: The service_nodes API from Positron — 2 operation(s) for service_nodes.
  name: Positron Service Nodes API
  slug: positron-service-nodes-api
- description: The users API from Positron — 3 operation(s) for users.
  name: Positron Users API
  slug: positron-users-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Olivaw Admin Access Tokens API
  slug: open-positron-access-tokens-api
- collection_type: open
  name: Olivaw Admin API
  slug: open-positron-admin
- collection_type: open
  name: Olivaw OpenAI Completion API
  slug: open-positron-completion-api
- collection_type: open
  name: Olivaw OpenAI API
  slug: open-positron-inference
- collection_type: open
  name: Positron Models API
  slug: open-positron-models-api
- collection_type: open
  name: Olivaw Admin Service Nodes API
  slug: open-positron-service-nodes-api
- collection_type: open
  name: Olivaw Admin Users API
  slug: open-positron-users-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/positron-ai/admin-api-docs/issues
- group: agent
  title: ''
  type: MCPServer
  url: mcp/positron-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/positron-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/positron-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.positron.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.positron.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://support.positron.ai/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://support.positron.ai/api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://support.positron.ai/user-guide
- group: operate
  title: ''
  type: Support
  url: https://www.positron.ai/contact-sales
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/positron-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.positron.ai/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/positron-changelog.yml
- group: company
  title: ''
  type: Press
  url: https://www.positron.ai/press
- group: company
  title: ''
  type: Careers
  url: https://www.positron.ai/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/positron-ai/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/positron_ai
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/positron-inference-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/positron-admin-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/positron-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/positron-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/positron-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/positron-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/positron-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/positron-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/positron-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/positron-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/positron-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/positron-inference-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/positron-admin-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'Positron AI is a US-based generative-AI hardware company founded in 2023 and headquartered in Reno, Nevada, building purpose-built Transformer inference accelerators as an alternative to GPU-based inference infrastructure. Its shipping product, Atlas, is a rack inference appliance built on eight in-house Archer accelerators (256 GB HBM) and dual AMD EPYC Genoa processors, with the next-generation Asimov silicon and Titan system slated for 2027. Positron exposes its inference fleet through "Olivaw", a serving and administration layer that publishes two documented HTTP APIs: an OpenAI-compatible completions API (models, chat completions, text completions, with server-sent-event streaming) so existing OpenAI client code can be repointed at a Positron endpoint, and an administrative API for managing models, service nodes, users, and access tokens on an appliance or hosted cluster. The company raised a $230M Series B in February 2026 at a valuation above $1B from ARENA, Jump Trading,
  Unless, the Qatar Investment Authority, Arm, Helena, DFJ Growth, Atreides, Valor, Resilience Reserve, Flume Ventures and 1517 Fund.'
image: https://www.positron.ai/opengraph-image-pwu6ef.png
layout: provider
mcp_servers:
- description: ''
  name: Positron MCP Server
  slug: positron-mcp-server
modified: '2026-08-02'
name: Positron
nav: Providers
network: true
overview: 'Positron publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Access Tokens API, Completion API, Models API, and 2 more. Tagged areas include artificial-intelligence, ai-inference, inference-hardware, ai-accelerators, and large-language-models.


  Positron''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, and 25 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 53.0
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 0.0
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 42.9
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Positron Authentication
  slug: positron-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Positron Domain Security
  slug: positron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: positron
tags:
- artificial-intelligence
- ai-inference
- inference-hardware
- ai-accelerators
- large-language-models
- transformers
- openai-compatible
- machine-learning
- semiconductors
- data-center
- llm-serving
- model-hosting
website: https://www.positron.ai/
---
