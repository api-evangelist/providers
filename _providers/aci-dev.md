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
    agent_skills: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Aci Dev Agentic Access
  operation_count: 15
  slug: aci-dev-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 4
apis:
- description: The app-configurations API from ACI.dev — 2 operation(s) for app-configurations.
  name: ACI.dev app-configurations API
  slug: aci-dev-app-configurations-api
- description: The apps API from ACI.dev — 2 operation(s) for apps.
  name: ACI.dev apps API
  slug: aci-dev-apps-api
- description: The functions API from ACI.dev — 3 operation(s) for functions.
  name: ACI.dev functions API
  slug: aci-dev-functions-api
- description: The linked-accounts API from ACI.dev — 4 operation(s) for linked-accounts.
  name: ACI.dev linked-accounts API
  slug: aci-dev-linked-accounts-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ACI.dev app-configurations API
  slug: open-aci-dev-app-configurations-api
- collection_type: open
  name: ACI.dev app-configurations apps API
  slug: open-aci-dev-apps-api
- collection_type: open
  name: ACI.dev app-configurations functions API
  slug: open-aci-dev-functions-api
- collection_type: open
  name: ACI.dev app-configurations linked-accounts API
  slug: open-aci-dev-linked-accounts-api
- collection_type: open
  name: ACI.dev API
  slug: open-aci-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aci-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aci-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aci-dev-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aci.dev
- group: docs
  title: ''
  type: Documentation
  url: https://aci.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://aci.dev/docs/introduction/quickstart.md
- group: docs
  title: ''
  type: Documentation
  url: https://aci.dev/docs/api-reference/overview.md
- group: docs
  title: ''
  type: Documentation
  url: https://aci.dev/docs/api-reference/openapi.json
- group: docs
  title: ''
  type: Documentation
  url: https://aci.dev/docs/sdk/intro.md
- group: docs
  title: ''
  type: Documentation
  url: https://aci.dev/docs/sdk/custom-functions.md
- group: docs
  title: ''
  type: Documentation
  url: https://aci.dev/docs/mcp-servers/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://aci.dev/docs/agent-playground/introduction.md
- group: docs
  title: ''
  type: Documentation
  url: https://aci.dev/docs/advanced/oauth2-whitelabel.md
- group: docs
  title: ''
  type: Documentation
  url: https://aci.dev/docs/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aipotheosis-labs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aipotheosis-labs/aci
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aipotheosis-labs/aci-mcp
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aipotheosis-labs/aci-mcp-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aipotheosis-labs/aci-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aipotheosis-labs/aci-typescript-sdk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aipotheosis-labs/aci-agents
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aipotheosis-labs/aci-developer-docs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aipotheosis-labs/gate22
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aipotheosis-labs/gate22-docs
- group: docs
  title: ''
  type: Documentation
  url: https://platform.aci.dev
- group: docs
  title: ''
  type: Documentation
  url: https://discord.gg/nnqFSzq2ne
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aipotheosis-labs-aipolabs
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AipoLabs
- group: docs
  title: ''
  type: Documentation
  url: https://www.youtube.com/@AipotheosisLabs
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aci-dev-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/aci-dev-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/aci-dev-context.jsonld
created: '2026-05-25'
description: ACI.dev (Aipolabs Agent-Computer Interface) is an open-source tool-calling platform that hooks AI agents into 600+ pre-built tools through direct function calling or a unified Model Context Protocol server. Maintained by Aipotheosis Labs (Aipolabs) under Apache 2.0, ACI provides multi-tenant OAuth2 and API-key authentication, per-project App Configurations, natural-language permission guardrails, OpenAI- and Anthropic-compatible function definitions, Python and TypeScript SDKs, and the unified aci-mcp server with ACI_SEARCH_FUNCTIONS and ACI_EXECUTE_FUNCTION meta-tools. The sister project Gate22 adds an open-source MCP gateway and control plane for governing which tools agents can use, what they can do, and how it is audited.
examples:
- key_count: 2
  name: Aci Dev Execute Function Example
  slug: aci-dev-execute-function-example
- key_count: 2
  name: Aci Dev Link Oauth2 Account Example
  slug: aci-dev-link-oauth2-account-example
- key_count: 2
  name: Aci Dev Search Functions Example
  slug: aci-dev-search-functions-example
features:
- 600+ pre-built App integrations (Slack, Gmail, Zendesk, GitHub, Notion, Stripe, and more)
- Unified MCP server (aci-mcp) exposing ACI_SEARCH_FUNCTIONS and ACI_EXECUTE_FUNCTION meta-tools
- Apps MCP mode that surfaces a specific set of Apps as named MCP tools
- Node port (aci-mcp-node) for TypeScript-native MCP integration
- OpenAI-compatible and Anthropic-compatible function-definition output formats
- Multi-tenant end-user OAuth2 link flow, white-label OAuth2 for production branding
- Per-project App Configurations with function-level enable/disable and security-scheme overrides
- Natural-language permission filters that guardrail tool executions
- Custom functions SDK for registering proprietary tools alongside the catalog
- Agent Playground for prompting against the unified catalog before wiring it into production
- Python and TypeScript SDKs (aci-python-sdk, aci-typescript-sdk)
- Sister project gate22 — open-source MCP gateway and control plane for governance and audit across Cursor and other agentic IDEs
- Self-hostable backend, frontend portal, and SDKs under Apache 2.0
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aci-dev.png
integrations:
- Anthropic Claude (function definitions returned in Anthropic tool-use format)
- OpenAI (function definitions returned in OpenAI tool-use format)
- Model Context Protocol (Cursor, Claude Desktop, Claude Code, and other MCP clients)
- GitHub, Gmail, Slack, Zendesk, Notion, Stripe and 600+ other apps via the ACI catalog
json_schemas:
- name: AnthropicFunctionDefinition
  property_count: 3
  slug: aci-dev-anthropic-function-definition
- name: AppConfigurationPublic
  property_count: 10
  slug: aci-dev-app-configuration
- name: AppBasic
  property_count: 2
  slug: aci-dev-app
- name: AppBasicWithFunctions
  property_count: 3
  slug: aci-dev-app-with-functions
- name: FunctionExecute
  property_count: 2
  slug: aci-dev-function-execute
- name: FunctionExecutionResult
  property_count: 3
  slug: aci-dev-function-execution-result
- name: FunctionBasic
  property_count: 2
  slug: aci-dev-function
- name: LinkedAccountPublic
  property_count: 8
  slug: aci-dev-linked-account
- name: OpenAIFunctionDefinition
  property_count: 2
  slug: aci-dev-openai-function-definition
jsonld:
- class_count: 0
  name: Aci Dev Context
  property_count: 5
  slug: aci-dev-context
layout: provider
modified: '2026-05-25'
name: ACI.dev
nav: Providers
network: true
overview: 'ACI.dev publishes 4 APIs on the [APIs.io](https://apis.io/) network, including app-configurations API, apps API, functions API, and 1 more. Tagged areas include Agent Infrastructure, Agents, Artificial Intelligence, Function Calling, and MCP.


  The ACI.dev catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ACI.dev''s developer surface includes authentication, developer portal, documentation, getting-started guide, and 29 more developer resources.'
random_paper: 14
rules:
- effective_rule_count: 5
  extends: []
  name: ACI.dev API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aci-dev-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: ACI.dev API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: aci-dev-rules
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 73.3
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 2.6
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aci-dev/refs/heads/main/screenshots/aci-dev-2026-06-20T163831.png
security:
- kind: authentication
  name: Aci Dev Authentication
  slug: aci-dev-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aci Dev Domain Security
  slug: aci-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aci-dev
tags:
- Agent Infrastructure
- Agents
- Artificial Intelligence
- Function Calling
- MCP
- Authentication
- Open-Source
- Tool Calling
- VibeOps
website: https://aci.dev
---
