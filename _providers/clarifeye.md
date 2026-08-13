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
  band_gated_from: agent-native
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
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Clarifeye Agentic Access
  operation_count: 75
  slug: clarifeye-agentic-access
  summary_line: 75 operations · 46 acting
api_count: 13
apis:
- description: Manage AI agent configurations
  name: Clarifeye Agent Settings API
  slug: clarifeye-agent-settings-api
- description: Create and interact with AI-powered conversations
  name: Clarifeye Conversations API
  slug: clarifeye-conversations-api
- description: Manage documents within a project
  name: Clarifeye Documents API
  slug: clarifeye-documents-api
- description: Manage extraction flows (auto-sync DAGs) — list, run, inspect statistics, update, and publish
  name: Clarifeye Extraction Flows API
  slug: clarifeye-extraction-flows-api
- description: Submit feedback on conversation messages
  name: Clarifeye Feedback API
  slug: clarifeye-feedback-api
- description: Assign and review structured interview conversations
  name: Clarifeye Interviews API
  slug: clarifeye-interviews-api
- description: Manage project invitations
  name: Clarifeye Invitations API
  slug: clarifeye-invitations-api
- description: Manage project-scoped notifications for users
  name: Clarifeye Notifications API
  slug: clarifeye-notifications-api
- description: Inspect pipeline runs queued by extraction flows or other pipeline triggers — list runs and fetch the details/status of a single run
  name: Clarifeye Pipeline Runs API
  slug: clarifeye-pipeline-runs-api
- description: Submit signals about the project's content for domain experts to review
  name: Clarifeye Signals API
  slug: clarifeye-signals-api
- description: Perform CRUD operations on warehouse tables
  name: Clarifeye Tables API
  slug: clarifeye-tables-api
- description: Execute configured AI tools with custom parameters
  name: Clarifeye Tools API
  slug: clarifeye-tools-api
- description: Manage users within a project
  name: Clarifeye Users API
  slug: clarifeye-users-api
artifact_total: 18
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/clarifeye-backoffice-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.clarifeye.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.clarifeye.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clarifeye.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clarifeye.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clarifeye.ai/guides/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.clarifeye.ai/guides/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.clarifeye.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.clarifeye.ai/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clarifeye.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://us.app.clarifeye.ai/
- group: start
  title: ''
  type: Login
  url: https://us.app.clarifeye.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clarifeye.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clarifeye.ai/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clarifeyeai/
- group: auth
  title: ''
  type: Compliance
  url: https://www.clarifeye.ai/technology
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clarifeye-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clarifeye-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clarifeye-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clarifeye-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clarifeye-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clarifeye-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clarifeye-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clarifeye-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clarifeye-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clarifeye-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clarifeye-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clarifeye-agentic-access.yml
created: '2026-07-17'
description: Clarifeye is an AI-native knowledge infrastructure platform that captures the undocumented knowledge locked in people's heads. Its AI interviewer, Clara, runs document-aware interviews with subject-matter experts, surfaces contradictions, and structures the results into versioned, reusable knowledge artifacts — briefs, playbooks, mental maps, and ontologies. That captured knowledge is exposed to AI clients such as Claude, ChatGPT, and Microsoft Copilot through a hosted Model Context Protocol (MCP) server and a REST API, so agents answer grounded in an organization's own logic with references back to source. Clarifeye targets regulated industries where undocumented processes create key-person risk, offers EU and US data localization with PII redaction at ingestion, and is SOC 2 Type II certified. Backed by EQT Ventures.
image: https://www.clarifeye.ai/_astro/og-default.BHhQt8Bo.png
layout: provider
mcp_servers:
- description: ''
  name: clarifeye-mcp.yml
  slug: clarifeye-mcpyml
modified: '2026-07-18'
name: Clarifeye
nav: Providers
network: true
overview: 'Clarifeye publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Agent Settings API, Conversations API, Documents API, and 10 more. Tagged areas include Company, Artificial Intelligence, Knowledge Management, Model Context Protocol, and Document Intelligence.


  Clarifeye''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, support, pricing, and 22 more developer resources.'
random_paper: 108
scopes:
- name: Clarifeye Scopes
  scope_count: 3
  slug: clarifeye-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 62.7
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clarifeye/refs/heads/main/screenshots/clarifeye-2026-07-25T205502.png
security:
- kind: authentication
  name: Clarifeye Authentication
  slug: clarifeye-authentication
  summary_line: apiKey/http/oauth2 · 2 schemes
- kind: domain-security
  name: Clarifeye Domain Security
  slug: clarifeye-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clarifeye
tags:
- Company
- Artificial Intelligence
- Knowledge Management
- Model Context Protocol
- Document Intelligence
- Agents
- Enterprise AI
- Retrieval
website: https://www.clarifeye.ai/
---
