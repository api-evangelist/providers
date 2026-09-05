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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Clarifeye Agentic Access
  operation_count: 75
  slug: clarifeye-agentic-access
  summary_line: 75 operations · 46 acting
api_count: 2
apis:
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage AI agent configurations
  name: Clarifeye Agent Settings API
  slug: clarifeye-agent-settings-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Create and interact with AI-powered conversations
  name: Clarifeye Conversations API
  slug: clarifeye-conversations-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage documents within a project
  name: Clarifeye Documents API
  slug: clarifeye-documents-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage extraction flows (auto-sync DAGs) — list, run, inspect statistics, update, and publish
  name: Clarifeye Extraction Flows API
  slug: clarifeye-extraction-flows-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Submit feedback on conversation messages
  name: Clarifeye Feedback API
  slug: clarifeye-feedback-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Assign and review structured interview conversations
  name: Clarifeye Interviews API
  slug: clarifeye-interviews-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage project invitations
  name: Clarifeye Invitations API
  slug: clarifeye-invitations-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage project-scoped notifications for users
  name: Clarifeye Notifications API
  slug: clarifeye-notifications-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Inspect pipeline runs queued by extraction flows or other pipeline triggers — list runs and fetch the details/status of a single run
  name: Clarifeye Pipeline Runs API
  slug: clarifeye-pipeline-runs-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Submit signals about the project's content for domain experts to review
  name: Clarifeye Signals API
  slug: clarifeye-signals-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Perform CRUD operations on warehouse tables
  name: Clarifeye Tables API
  slug: clarifeye-tables-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Execute configured AI tools with custom parameters
  name: Clarifeye Tools API
  slug: clarifeye-tools-api
- baseURL: https://eu.app.clarifeye.ai/api/v1
  baseurl_source: declared
  description: Manage users within a project
  name: Clarifeye Users API
  slug: clarifeye-users-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clarifeye Platform Agent Settings API
  slug: open-clarifeye-agent-settings-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Conversations API
  slug: open-clarifeye-conversations-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Documents API
  slug: open-clarifeye-documents-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Extraction Flows API
  slug: open-clarifeye-extraction-flows-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Feedback API
  slug: open-clarifeye-feedback-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Interviews API
  slug: open-clarifeye-interviews-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Invitations API
  slug: open-clarifeye-invitations-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Notifications API
  slug: open-clarifeye-notifications-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Pipeline Runs API
  slug: open-clarifeye-pipeline-runs-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Signals API
  slug: open-clarifeye-signals-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Tables API
  slug: open-clarifeye-tables-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Tools API
  slug: open-clarifeye-tools-api
- collection_type: open
  name: Clarifeye Platform Agent Settings Users API
  slug: open-clarifeye-users-api
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
- description: Clarifeye publishes a hosted, per-knowledge-store MCP server that exposes an organization's captured knowledge (briefs, playbooks, mental maps, tags, objects) to AI clients (Claude, ChatGPT, Microsoft
  name: Clarifeye MCP Server
  slug: clarifeye-mcp-server
modified: '2026-07-18'
name: Clarifeye
nav: Providers
network: true
overview: 'Clarifeye publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Agent Settings API, Conversations API, Documents API, and 10 more. Tagged areas include Company, Artificial Intelligence, Knowledge-Management, MCP, and Document Intelligence.


  Clarifeye''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, support, pricing, and 22 more developer resources.'
random_paper: 3
scopes:
- name: Clarifeye Scopes
  scope_count: 3
  slug: clarifeye-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 58.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 44.2
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Knowledge-Management
- MCP
- Document Intelligence
- Agents
- Enterprise AI
- Retrieval
website: https://www.clarifeye.ai/
---
