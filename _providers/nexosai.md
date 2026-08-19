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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Nexosai Agentic Access
  operation_count: 55
  slug: nexosai-agentic-access
  summary_line: 55 operations · 34 acting
api_count: 16
apis:
- description: Manage agents.
  name: nexos.ai Agent Management API
  slug: nexosai-agent-management-api
- description: Manage assistants.
  name: nexos.ai Assistant Management API
  slug: nexosai-assistant-management-api
- description: Generate audio or text from audio or text input.
  name: nexos.ai Audio API
  slug: nexosai-audio-api
- description: Create and run large groups of requests asynchronously. Batches are only available for OpenAI models.
  name: nexos.ai Batches API
  slug: nexosai-batches-api
- description: Manage company budget limits.
  name: nexos.ai Budget Limit Management API
  slug: nexosai-budget-limit-management-api
- description: Generate a response from conversation messages.
  name: nexos.ai Chat API
  slug: nexosai-chat-api
- description: List company API keys and their usage.
  name: nexos.ai Company Management API
  slug: nexosai-company-management-api
- description: Create vector embeddings for input text.
  name: nexos.ai Embeddings API
  slug: nexosai-embeddings-api
- description: Upload and manage files used by other endpoints.
  name: nexos.ai Files API
  slug: nexosai-files-api
- description: Generate images from image or text input.
  name: nexos.ai Images API
  slug: nexosai-images-api
- description: Anthropic-native Messages API for prompt-cache-preserving passthrough.
  name: nexos.ai Messages API
  slug: nexosai-messages-api
- description: List available models.
  name: nexos.ai Models API
  slug: nexosai-models-api
- description: Create and manage model responses.
  name: nexos.ai Responses API
  slug: nexosai-responses-api
- description: Upload and manage media files.
  name: nexos.ai Storage API
  slug: nexosai-storage-api
- description: Manage teams, API keys, and models.
  name: nexos.ai Team Management API
  slug: nexosai-team-management-api
- description: Manage user API keys.
  name: nexos.ai User Management API
  slug: nexosai-user-management-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nexos AI Public API Production Agent Management API
  slug: open-nexosai-agent-management-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Assistant Management API
  slug: open-nexosai-assistant-management-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Audio API
  slug: open-nexosai-audio-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Batches API
  slug: open-nexosai-batches-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Budget Limit Management API
  slug: open-nexosai-budget-limit-management-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Chat API
  slug: open-nexosai-chat-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Company Management API
  slug: open-nexosai-company-management-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Embeddings API
  slug: open-nexosai-embeddings-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Files API
  slug: open-nexosai-files-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Images API
  slug: open-nexosai-images-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Messages API
  slug: open-nexosai-messages-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Models API
  slug: open-nexosai-models-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Responses API
  slug: open-nexosai-responses-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Storage API
  slug: open-nexosai-storage-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management Team Management API
  slug: open-nexosai-team-management-api
- collection_type: open
  name: Nexos AI Public API Production Agent Management User Management API
  slug: open-nexosai-user-management-api
common:
- group: company
  title: ''
  type: Website
  url: https://nexos.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nexos.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nexos.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nexos.ai/gateway-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nexos.ai/readme.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nexos.ai/changelog/changelog/latest-updates
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nexos-ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexosai-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/nexosai-gateway-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nexosai-gateway-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexosai-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nexosai-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexosai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nexosai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nexosai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nexosai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nexosai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nexos.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/nexosai-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nexosai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nexosai-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexosai-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: nexos.ai is an enterprise AI platform and OpenAI-compatible AI gateway that unifies many large language model providers behind a single API key and governed workspace. Its Gateway API exposes chat completions, responses, messages, embeddings, images, audio (speech, transcription, translation), batches, files, and storage, alongside management surfaces for models and fallbacks, teams, users, agents, assistants, companies, API keys, and per-company/team/user budget limits. Organizations get guardrails, observability, smart routing across models, agents (Agent Builder with human-in-the-loop approvals), and integrations with tools like Slack, Atlassian, GitHub, Google Workspace, and Microsoft 365. Founded by the team behind Nord Security and backed by Index Ventures and Creandum. This profile was enriched from the provider's public docs at docs.nexos.ai.
image: https://nexos.ai/
layout: provider
mcp_servers:
- description: ''
  name: nexosai-mcp.yml
  slug: nexosai-mcpyml
modified: '2026-07-20'
name: nexos.ai
nav: Providers
network: true
overview: 'nexos.ai publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Agent Management API, Assistant Management API, Audio API, and 13 more. Tagged areas include Company, Artificial Intelligence, LLM, AI Gateway, and Machine Learning.


  nexos.ai''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 18 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 39.9
  delta: 0.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 16.7
    contract_quality: 55.5
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexosai/refs/heads/main/screenshots/nexosai-2026-08-07T185156.png
security:
- kind: authentication
  name: Nexosai Authentication
  slug: nexosai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Nexosai Domain Security
  slug: nexosai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Nexosai Trust Center
  slug: nexosai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: nexosai
tags:
- Company
- Artificial Intelligence
- LLM
- AI Gateway
- Machine Learning
- Embeddings
- Agents
- Developer Tools
- OpenAI Compatible
website: https://nexos.ai/
---
