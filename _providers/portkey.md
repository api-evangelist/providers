---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 122
  human_in_the_loop: 1
  name: Portkey Agentic Access
  operation_count: 231
  slug: portkey-agentic-access
  summary_line: 231 operations · 122 acting · 1 human-in-the-loop
api_count: 51
apis:
- description: Get data points for graphical representation.
  name: Portkey Analytics > Graphs API
  slug: portkey-analytics-graphs-api
- description: Get grouped metrics for the selected time bucket.
  name: Portkey Analytics > Groups API
  slug: portkey-analytics-groups-api
- description: Get overall summary for the selected time bucket.
  name: Portkey Analytics > Summary API
  slug: portkey-analytics-summary-api
- description: Create, List, Retrieve, Update, and Delete your Portkey API keys.
  name: Portkey Api-Keys API
  slug: portkey-api-keys-api
- description: Build Assistants that can call models and use tools.
  name: Portkey Assistants API
  slug: portkey-assistants-api
- description: Turn audio into text or text into audio.
  name: Portkey Audio API
  slug: portkey-audio-api
- description: Get audit logs for your Portkey account.
  name: Portkey Audit Logs API
  slug: portkey-audit-logs-api
- description: Create large batches of API requests to run asynchronously.
  name: Portkey Batch API
  slug: portkey-batch-api
- description: Given a list of messages comprising a conversation, the model will return a response.
  name: Portkey Chat API
  slug: portkey-chat-api
- description: Create, List, Retrieve, Update, and Delete collections of prompts.
  name: Portkey Collections API
  slug: portkey-collections-api
- description: Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position.
  name: Portkey Completions API
  slug: portkey-completions-api
- description: Create, List, Retrieve, and Update your Portkey Configs.
  name: Portkey Configs API
  slug: portkey-configs-api
- description: Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.
  name: Portkey Embeddings API
  slug: portkey-embeddings-api
- description: Send and Update any feedback.
  name: Portkey Feedback API
  slug: portkey-feedback-api
- description: Files are used to upload documents that can be used with features like Assistants and Fine-tuning.
  name: Portkey Files API
  slug: portkey-files-api
- description: Manage fine-tuning jobs to tailor a model to your specific training data.
  name: Portkey Fine-tuning API
  slug: portkey-fine-tuning-api
- description: The Finetune API from Portkey — 1 operation(s) for finetune.
  name: Portkey Finetune API
  slug: portkey-finetune-api
- description: Create, List, Retrieve, Update, and Delete prompt Guardrails.
  name: Portkey Guardrails API
  slug: portkey-guardrails-api
- description: Given a prompt and/or an input image, the model will generate a new image.
  name: Portkey Images API
  slug: portkey-images-api
- description: Create, List, Retrieve, Update, and Delete your Portkey Integrations.
  name: Portkey Integrations API
  slug: portkey-integrations-api
- description: Manage model access for your Portkey Integrations.
  name: Portkey Integrations > Models API
  slug: portkey-integrations-models-api
- description: Manage workspace access for your Portkey Integrations.
  name: Portkey Integrations > Workspaces API
  slug: portkey-integrations-workspaces-api
- description: Create, List, Retrieve, Update, and Delete labels.
  name: Portkey Labels API
  slug: portkey-labels-api
- description: Custom Logger to add external logs to Portkey.
  name: Portkey Logs API
  slug: portkey-logs-api
- description: Exports logs service.
  name: Portkey Logs Export API
  slug: portkey-logs-export-api
- description: Create, List, Retrieve, Update, and Delete MCP Integrations.
  name: Portkey MCP Integrations API
  slug: portkey-mcp-integrations-api
- description: List and manage capabilities for MCP Integrations.
  name: Portkey MCP Integrations > Capabilities API
  slug: portkey-mcp-integrations-capabilities-api
- description: Get MCP Integration metadata and sync info.
  name: Portkey MCP Integrations > Metadata API
  slug: portkey-mcp-integrations-metadata-api
- description: Manage workspace access for MCP Integrations.
  name: Portkey MCP Integrations > Workspaces API
  slug: portkey-mcp-integrations-workspaces-api
- description: Create, List, Retrieve, Update, and Delete MCP Servers (workspace instances of MCP Integrations).
  name: Portkey MCP Servers API
  slug: portkey-mcp-servers-api
- description: List and manage capabilities for MCP Servers.
  name: Portkey MCP Servers > Capabilities API
  slug: portkey-mcp-servers-capabilities-api
- description: List and manage user connections for MCP Servers.
  name: Portkey MCP Servers > Connections API
  slug: portkey-mcp-servers-connections-api
- description: List and manage user access for MCP Servers.
  name: Portkey MCP Servers > User Access API
  slug: portkey-mcp-servers-user-access-api
- description: Model pricing configurations for 2300+ LLMs across 40+ providers
  name: Portkey Model Pricing API
  slug: portkey-model-pricing-api
- description: List and describe the various models available in the API.
  name: Portkey Models API
  slug: portkey-models-api
- description: Given a input text, outputs if the model classifies it as potentially harmful.
  name: Portkey Moderations API
  slug: portkey-moderations-api
- description: Create, List, Retrieve, Update, and Delete prompt partials.
  name: Portkey PromptPartials API
  slug: portkey-promptpartials-api
- description: Given a prompt template ID and variables, will run the saved prompt template and return a response.
  name: Portkey Prompts API
  slug: portkey-prompts-api
- description: Create, List, Retrieve, Update, and Delete your Portkey Providers.
  name: Portkey Providers API
  slug: portkey-providers-api
- description: Manage rate limits policies to control request or token rates
  name: Portkey Rate Limits Policies API
  slug: portkey-rate-limits-policies-api
- description: WebSocket proxy for provider Realtime APIs
  name: Portkey Realtime API
  slug: portkey-realtime-api
- description: Rerank a list of documents based on their relevance to a query. Supported providers include Cohere, Voyage, Jina, Pinecone, Bedrock, and Azure AI.
  name: Portkey Rerank API
  slug: portkey-rerank-api
- description: The Responses API from Portkey — 3 operation(s) for responses.
  name: Portkey Responses API
  slug: portkey-responses-api
- description: Create, List, Retrieve, Update, and Delete secret references to external secret managers.
  name: Portkey Secret-References API
  slug: portkey-secret-references-api
- description: Manage usage limits policies to control total usage over time
  name: Portkey Usage Limits Policies API
  slug: portkey-usage-limits-policies-api
- description: Create and manage user invites.
  name: Portkey User-invites API
  slug: portkey-user-invites-api
- description: Create and manage users.
  name: Portkey Users API
  slug: portkey-users-api
- description: The Vector Stores API from Portkey — 8 operation(s) for vector stores.
  name: Portkey Vector Stores API
  slug: portkey-vector-stores-api
- description: Create, List, Retrieve, Update, and Delete your Portkey Virtual keys.
  name: Portkey Virtual-keys API
  slug: portkey-virtual-keys-api
- description: Create and manage workspaces.
  name: Portkey Workspaces API
  slug: portkey-workspaces-api
- description: Create and manage workspace members.
  name: Portkey Workspaces > Members API
  slug: portkey-workspaces-members-api
artifact_total: 110
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Portkey Analytics > Graphs API
  slug: open-portkey-analytics-graphs-api
- collection_type: open
  name: Portkey Analytics > Graphs Analytics > Groups API
  slug: open-portkey-analytics-groups-api
- collection_type: open
  name: Portkey Analytics > Graphs Analytics > Summary API
  slug: open-portkey-analytics-summary-api
- collection_type: open
  name: Portkey Analytics > Graphs Api-Keys API
  slug: open-portkey-api-keys-api
- collection_type: open
  name: Portkey Analytics > Graphs Assistants API
  slug: open-portkey-assistants-api
- collection_type: open
  name: Portkey Analytics > Graphs Audio API
  slug: open-portkey-audio-api
- collection_type: open
  name: Portkey Analytics > Graphs Audit Logs API
  slug: open-portkey-audit-logs-api
- collection_type: open
  name: Portkey Analytics > Graphs Batch API
  slug: open-portkey-batch-api
- collection_type: open
  name: Portkey Analytics > Graphs Chat API
  slug: open-portkey-chat-api
- collection_type: open
  name: Portkey Analytics > Graphs Collections API
  slug: open-portkey-collections-api
- collection_type: open
  name: Portkey Analytics > Graphs Completions API
  slug: open-portkey-completions-api
- collection_type: open
  name: Portkey Analytics > Graphs Configs API
  slug: open-portkey-configs-api
- collection_type: open
  name: Portkey Analytics > Graphs Embeddings API
  slug: open-portkey-embeddings-api
- collection_type: open
  name: Portkey Analytics > Graphs Feedback API
  slug: open-portkey-feedback-api
- collection_type: open
  name: Portkey Analytics > Graphs Files API
  slug: open-portkey-files-api
- collection_type: open
  name: Portkey Analytics > Graphs Fine-tuning API
  slug: open-portkey-fine-tuning-api
- collection_type: open
  name: Portkey Analytics > Graphs Finetune API
  slug: open-portkey-finetune-api
- collection_type: open
  name: Portkey Analytics > Graphs Guardrails API
  slug: open-portkey-guardrails-api
- collection_type: open
  name: Portkey Analytics > Graphs Images API
  slug: open-portkey-images-api
- collection_type: open
  name: Portkey Analytics > Graphs Integrations API
  slug: open-portkey-integrations-api
- collection_type: open
  name: Portkey Analytics > Graphs Integrations > Models API
  slug: open-portkey-integrations-models-api
- collection_type: open
  name: Portkey Analytics > Graphs Integrations > Workspaces API
  slug: open-portkey-integrations-workspaces-api
- collection_type: open
  name: Portkey Analytics > Graphs Labels API
  slug: open-portkey-labels-api
- collection_type: open
  name: Portkey Analytics > Graphs Logs API
  slug: open-portkey-logs-api
- collection_type: open
  name: Portkey Analytics > Graphs Logs Export API
  slug: open-portkey-logs-export-api
- collection_type: open
  name: Portkey Analytics > Graphs MCP Integrations API
  slug: open-portkey-mcp-integrations-api
- collection_type: open
  name: Portkey Analytics > Graphs MCP Integrations > Capabilities API
  slug: open-portkey-mcp-integrations-capabilities-api
- collection_type: open
  name: Portkey Analytics > Graphs MCP Integrations > Metadata API
  slug: open-portkey-mcp-integrations-metadata-api
- collection_type: open
  name: Portkey Analytics > Graphs MCP Integrations > Workspaces API
  slug: open-portkey-mcp-integrations-workspaces-api
- collection_type: open
  name: Portkey Analytics > Graphs MCP Servers API
  slug: open-portkey-mcp-servers-api
- collection_type: open
  name: Portkey Analytics > Graphs MCP Servers > Capabilities API
  slug: open-portkey-mcp-servers-capabilities-api
- collection_type: open
  name: Portkey Analytics > Graphs MCP Servers > Connections API
  slug: open-portkey-mcp-servers-connections-api
- collection_type: open
  name: Portkey Analytics > Graphs MCP Servers > User Access API
  slug: open-portkey-mcp-servers-user-access-api
- collection_type: open
  name: Portkey Analytics > Graphs Model Pricing API
  slug: open-portkey-model-pricing-api
- collection_type: open
  name: Portkey Analytics > Graphs Models API
  slug: open-portkey-models-api
- collection_type: open
  name: Portkey Analytics > Graphs Moderations API
  slug: open-portkey-moderations-api
- collection_type: open
  name: Portkey Analytics > Graphs PromptPartials API
  slug: open-portkey-promptpartials-api
- collection_type: open
  name: Portkey Analytics > Graphs Prompts API
  slug: open-portkey-prompts-api
- collection_type: open
  name: Portkey Analytics > Graphs Providers API
  slug: open-portkey-providers-api
- collection_type: open
  name: Portkey Analytics > Graphs Rate Limits Policies API
  slug: open-portkey-rate-limits-policies-api
- collection_type: open
  name: Portkey Analytics > Graphs Realtime API
  slug: open-portkey-realtime-api
- collection_type: open
  name: Portkey Analytics > Graphs Rerank API
  slug: open-portkey-rerank-api
- collection_type: open
  name: Portkey Analytics > Graphs Responses API
  slug: open-portkey-responses-api
- collection_type: open
  name: Portkey Analytics > Graphs Secret-References API
  slug: open-portkey-secret-references-api
- collection_type: open
  name: Portkey Analytics > Graphs Usage Limits Policies API
  slug: open-portkey-usage-limits-policies-api
- collection_type: open
  name: Portkey Analytics > Graphs User-invites API
  slug: open-portkey-user-invites-api
- collection_type: open
  name: Portkey Analytics > Graphs Users API
  slug: open-portkey-users-api
- collection_type: open
  name: Portkey Analytics > Graphs Vector Stores API
  slug: open-portkey-vector-stores-api
- collection_type: open
  name: Portkey Analytics > Graphs Virtual-keys API
  slug: open-portkey-virtual-keys-api
- collection_type: open
  name: Portkey Analytics > Graphs Workspaces API
  slug: open-portkey-workspaces-api
- collection_type: open
  name: Portkey Analytics > Graphs Workspaces > Members API
  slug: open-portkey-workspaces-members-api
- collection_type: open
  name: Portkey API
  slug: open-portkey
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/portkey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/portkey-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/Portkey-AI/cli
- group: company
  title: ''
  type: Website
  url: https://portkey.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://portkey.ai/docs/introduction/what-is-portkey
- group: operate
  title: ''
  type: ChangeLog
  url: https://portkey.ai/docs/changelog/2025/july
- group: company
  title: ''
  type: Blog
  url: https://portkey.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.portkey.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://portkey.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://portkey.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://portkey.ai/terms
- group: start
  title: ''
  type: Login
  url: https://new.portkey.ai/login
- group: start
  title: ''
  type: GettingStarted
  url: https://portkey.ai/docs/guides/getting-started/getting-started-with-ai-gateway
- group: docs
  title: ''
  type: APIReference
  url: https://portkey.ai/docs/api-reference/inference-api/chat
- group: docs
  title: ''
  type: APIReference
  url: https://portkey.ai/docs/api-reference/admin-api/introduction
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/Portkey-AI/openapi
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Portkey-AI/gateway
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Portkey-AI/portkey-python-sdk
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Portkey-AI/portkey-node-sdk
- group: build
  title: ''
  type: PythonPackage
  url: https://pypi.org/project/portkey-ai/
- group: build
  title: ''
  type: NodePackage
  url: https://www.npmjs.com/package/portkey-ai
- group: build
  title: ''
  type: SDKs
  url: https://portkey.ai/docs/api-reference/portkey-sdk-client
- group: operate
  title: ''
  type: Forums
  url: https://portkey.ai/docs/support/developer-forum
- group: auth
  title: ''
  type: Security
  url: https://portkey.ai/features/security-compliance
- group: other
  title: ''
  type: Observability
  url: https://portkey.ai/features/observability
- group: other
  title: ''
  type: Guardrails
  url: https://portkey.ai/features/guardrails
- group: docs
  title: ''
  type: Documentation
  url: https://portkey.ai/docs/product/guardrails
- group: other
  title: ''
  type: Providers
  url: https://portkey.ai/docs/api-reference/inference-api/supported-providers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/portkey-ai
created: '2025-08-19'
description: Portkey equips AI teams with everything they need to go to production - Gateway, Observability, Guardrails, Governance, and Prompt Management, all in one platform.
finops:
- name: Portkey Finops
  service_category: AI Infrastructure
  slug: portkey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portkey.png
layout: provider
modified: '2026-05-19'
name: Portkey
nav: Providers
network: true
overview: 'Portkey publishes 51 APIs on the [APIs.io](https://apis.io/) network, including Analytics > Graphs API, Analytics > Groups API, Analytics > Summary API, and 48 more. Tagged areas include AI Gateways, Gateways, Governance, Guardrails, and Observability.


  Portkey''s developer surface includes authentication, documentation, changelog, engineering blog, pricing, getting-started guide, API reference, and 23 more developer resources.'
plans:
- name: Portkey Plans Pricing
  plan_count: 4
  slug: portkey-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Portkey Rate Limits
  slug: portkey-rate-limits
score:
  band: developing
  composite: 49.8
  delta: 1.4
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 56.4
    developer_ergonomics: 61.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 51
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/portkey/refs/heads/main/screenshots/portkey-2026-06-20T191938.png
security:
- kind: authentication
  name: Portkey Authentication
  slug: portkey-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Portkey Domain Security
  slug: portkey-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: portkey
tags:
- AI Gateways
- Gateways
- Governance
- Guardrails
- Observability
- Prompt Management
website: https://portkey.ai/
---
