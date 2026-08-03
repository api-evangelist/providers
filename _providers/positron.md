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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Positron Agentic Access
  operation_count: 23
  slug: positron-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 2
apis:
- description: OpenAI API-compatible inference endpoint served by Positron's Olivaw serving layer. Lists available models, retrieves a single model, and creates chat completions and raw text completions against mode
  name: Positron Olivaw OpenAI-Compatible Inference API
  slug: positron-olivaw-openai-compatible-inference-api
- description: Administrative API for the Olivaw layer that fronts Positron Atlas hardware. Manages the model catalog (list/create/read/update/delete), the service nodes that back it (Giskard, vLLM or OpenAI backend
  name: Positron Olivaw Admin API
  slug: positron-olivaw-admin-api
artifact_total: 5
common:
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
  url: openapi/positron-inference-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/positron-admin-openapi.yml
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
modified: '2026-08-02'
name: Positron
nav: Providers
network: true
overview: 'Positron publishes 2 APIs on the [APIs.io](https://apis.io/) network: Olivaw OpenAI-Compatible Inference API and Olivaw Admin API. Tagged areas include artificial-intelligence, ai-inference, inference-hardware, ai-accelerators, and large-language-models.


  Positron''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, and 23 more developer resources.'
random_paper: 39
score:
  band: thin
  composite: 37.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 55.4
    developer_ergonomics: 51.6
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
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
