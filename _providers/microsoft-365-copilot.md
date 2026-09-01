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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Microsoft 365 Copilot Agentic Access
  operation_count: 13
  slug: microsoft-365-copilot-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- description: Microsoft Copilot Studio allows developers to create, customize, and extend Copilot experiences with custom plugins and connectors to integrate business-specific data and workflows.
  name: Microsoft Copilot Studio API
  slug: microsoft-copilot-studio-api
- description: API for extending Microsoft 365 Copilot with custom skills, plugins, and connectors to integrate third-party services and enterprise data sources.
  name: Microsoft 365 Copilot Extensibility API
  slug: microsoft-365-copilot-extensibility-api
- description: Azure OpenAI Service provides REST API access to OpenAI's language models, which power Microsoft 365 Copilot's AI capabilities with enterprise-grade security and compliance.
  name: Azure OpenAI Service API
  slug: azure-openai-service-api
- description: The Connectors API from Microsoft 365 Copilot — 3 operation(s) for connectors.
  name: Microsoft 365 Copilot Connectors API
  slug: microsoft-365-copilot-connectors-api
- description: The External Items API from Microsoft 365 Copilot — 1 operation(s) for external items.
  name: Microsoft 365 Copilot External Items API
  slug: microsoft-365-copilot-external-items-api
- description: The Search API from Microsoft 365 Copilot — 1 operation(s) for search.
  name: Microsoft 365 Copilot Search API
  slug: microsoft-365-copilot-search-api
- description: The User Content API from Microsoft 365 Copilot — 4 operation(s) for user content.
  name: Microsoft 365 Copilot User Content API
  slug: microsoft-365-copilot-user-content-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft 365 Copilot (Microsoft Graph) Connectors API
  slug: open-microsoft-365-copilot-connectors-api
- collection_type: open
  name: Microsoft 365 Copilot (Microsoft Graph) Connectors External Items API
  slug: open-microsoft-365-copilot-external-items-api
- collection_type: open
  name: Microsoft 365 Copilot (Microsoft Graph) Connectors Search API
  slug: open-microsoft-365-copilot-search-api
- collection_type: open
  name: Microsoft 365 Copilot (Microsoft Graph) Connectors User Content API
  slug: open-microsoft-365-copilot-user-content-api
- collection_type: open
  name: Microsoft 365 Copilot (Microsoft Graph)
  slug: open-microsoft-365-copilot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-365-copilot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-365-copilot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-365-copilot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-365-copilot-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/copilot-for-microsoft-365
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/microsoft-365/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/microsoft/skills-for-copilot-studio
created: '2024-01-15'
description: Microsoft 365 Copilot is an AI-powered productivity tool that combines large language models (LLMs) with Microsoft 365 apps and business data to enhance creativity, productivity, and skills across Microsoft 365 applications.
finops:
- name: Microsoft 365 Copilot Finops
  service_category: API
  slug: microsoft-365-copilot-finops
image: https://www.microsoft.com/en-us/microsoft-365/copilot/copilot-logo.png
layout: provider
modified: '2026-05-19'
name: Microsoft 365 Copilot
nav: Providers
network: true
overview: 'Microsoft 365 Copilot publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connectors API, External Items API, Search API, and 1 more. Tagged areas include Artificial Intelligence, Copilot, Enterprise, LLM, and Microsoft-365.


  Microsoft 365 Copilot''s developer surface includes authentication, developer portal, support, engineering blog, and 10 more developer resources.'
plans:
- name: Microsoft 365 Copilot Plans Pricing
  plan_count: 3
  slug: microsoft-365-copilot-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Microsoft 365 Copilot Rate Limits
  slug: microsoft-365-copilot-rate-limits
scopes:
- name: Microsoft 365 Copilot Scopes
  scope_count: 7
  slug: microsoft-365-copilot-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 49.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-365-copilot/refs/heads/main/screenshots/microsoft-365-copilot-2026-06-20T185342.png
security:
- kind: authentication
  name: Microsoft 365 Copilot Authentication
  slug: microsoft-365-copilot-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft 365 Copilot Domain Security
  slug: microsoft-365-copilot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 31
skills:
- name: add-action
  slug: add-action
- name: add-adaptive-card
  slug: add-adaptive-card
- name: add-generative-answers
  slug: add-generative-answers
- name: add-global-variable
  slug: add-global-variable
- name: add-knowledge
  slug: add-knowledge
- name: add-node
  slug: add-node
- name: add-other-agents
  slug: add-other-agents
- name: analyze-evals
  slug: analyze-evals
- name: chat-directline
  slug: chat-directline
- name: chat-sdk
  slug: chat-sdk
- name: chat-with-agent
  slug: chat-with-agent
- name: clone-agent
  slug: clone-agent
- name: create-eval-set
  slug: create-eval-set
- name: create-eval
  slug: create-eval
- name: detect-mode
  slug: detect-mode
- name: directline-chat
  slug: directline-chat
- name: edit-action
  slug: edit-action
- name: edit-agent
  slug: edit-agent
- name: edit-triggers
  slug: edit-triggers
- name: int-patterns
  slug: int-patterns
- name: int-project-context
  slug: int-project-context
- name: int-reference
  slug: int-reference
- name: list-kinds
  slug: list-kinds
- name: list-topics
  slug: list-topics
slug: microsoft-365-copilot
tags:
- Artificial Intelligence
- Copilot
- Enterprise
- LLM
- Microsoft-365
- Natural Language Processing
- Productivity
website: https://developer.microsoft.com/
---
