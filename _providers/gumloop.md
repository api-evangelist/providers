---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 24
  human_in_the_loop: 5
  name: Gumloop Agentic Access
  operation_count: 49
  slug: gumloop-agentic-access
  summary_line: 49 operations · 24 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Agents API from Gumloop — 5 operation(s) for agents.
  name: Gumloop Agents API
  slug: gumloop-agents-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Artifacts API from Gumloop — 2 operation(s) for artifacts.
  name: Gumloop Artifacts API
  slug: gumloop-artifacts-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Brain API from Gumloop — 1 operation(s) for brain.
  name: Gumloop Brain API
  slug: gumloop-brain-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Chat completions API from Gumloop — 1 operation(s) for chat completions.
  name: Gumloop Chat completions API
  slug: gumloop-chat-completions-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Data Access API from Gumloop — 5 operation(s) for data access.
  name: Gumloop Data Access API
  slug: gumloop-data-access-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Evaluations API from Gumloop — 4 operation(s) for evaluations.
  name: Gumloop Evaluations API
  slug: gumloop-evaluations-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Execution API from Gumloop — 2 operation(s) for execution.
  name: Gumloop Execution API
  slug: gumloop-execution-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The File Handling API from Gumloop — 4 operation(s) for file handling.
  name: Gumloop File Handling API
  slug: gumloop-file-handling-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The MCP API from Gumloop — 4 operation(s) for mcp.
  name: Gumloop MCP API
  slug: gumloop-mcp-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Models API from Gumloop — 1 operation(s) for models.
  name: Gumloop Models API
  slug: gumloop-models-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Organization API from Gumloop — 5 operation(s) for organization.
  name: Gumloop Organization API
  slug: gumloop-organization-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Sessions API from Gumloop — 4 operation(s) for sessions.
  name: Gumloop Sessions API
  slug: gumloop-sessions-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Skills API from Gumloop — 3 operation(s) for skills.
  name: Gumloop Skills API
  slug: gumloop-skills-api
- baseURL: https://api.gumloop.com/api/v1
  baseurl_source: declared
  description: The Teams API from Gumloop — 1 operation(s) for teams.
  name: Gumloop Teams API
  slug: gumloop-teams-api
artifact_total: 36
asyncapis:
- description: ''
  name: Gumloop Webhooks
  slug: gumloop-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Public Agents API
  slug: open-gumloop-agents-api
- collection_type: open
  name: Public Agents Artifacts API
  slug: open-gumloop-artifacts-api
- collection_type: open
  name: Public Agents Brain API
  slug: open-gumloop-brain-api
- collection_type: open
  name: Public Agents Chat completions API
  slug: open-gumloop-chat-completions-api
- collection_type: open
  name: Public Agents Data Access API
  slug: open-gumloop-data-access-api
- collection_type: open
  name: Public Agents Evaluations API
  slug: open-gumloop-evaluations-api
- collection_type: open
  name: Public Agents Execution API
  slug: open-gumloop-execution-api
- collection_type: open
  name: Public Agents File Handling API
  slug: open-gumloop-file-handling-api
- collection_type: open
  name: Public Agents MCP API
  slug: open-gumloop-mcp-api
- collection_type: open
  name: Public Agents Models API
  slug: open-gumloop-models-api
- collection_type: open
  name: Public Agents Organization API
  slug: open-gumloop-organization-api
- collection_type: open
  name: Public Agents Sessions API
  slug: open-gumloop-sessions-api
- collection_type: open
  name: Public Agents Skills API
  slug: open-gumloop-skills-api
- collection_type: open
  name: Public Agents Teams API
  slug: open-gumloop-teams-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/gumloop-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gumloop.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gumloop.com/getting-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gumloop.com/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gumloop.com/api-reference/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/gumloop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gumloop-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/gumloop-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gumloop-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/gumloop-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gumloop-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gumloop-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gumloop-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/gumloop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gumloop-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gumloop-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gumloop-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gumloop-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gumloop.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gumloop-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gumloop-webhooks.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gumloop.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gumloop-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gumloop-agentic-access.yml
- group: company
  title: ''
  type: Blog
  url: https://gumloop.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://gumloop.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.gumloop.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@gumloop.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gumloop.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gumloop.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.gumloop.com
created: '2026-07-17'
description: Gumloop is an AI-agent automation platform for building, deploying, and governing agents that automate real work — data analysis, customer support, CRM management, and back-office tasks — across tools like Slack, Microsoft Teams, and Gmail. Its public REST API (https://api.gumloop.com/api/v1) exposes 49 operations spanning flow execution, agents and sessions, an OpenAI-compatible chat/completions endpoint, Company Brain search, agent skills, artifacts, MCP server management, evaluations, file handling, teams, and organization administration. Gumloop ships first-party Python and JavaScript SDKs, a `gumloop` CLI, a hosted MCP server for Claude/Cursor/ VS Code, OAuth 2.0 with PKCE, webhook/schedule/event triggers, and enterprise controls (SSO/SAML/SCIM, audit logging, app policies).
image: https://gumloop.com/images/link-preview.webp
layout: provider
mcp_servers:
- description: ''
  name: Gumloop MCP Server
  slug: gumloop-mcp-server
modified: '2026-07-19'
name: Gumloop
nav: Providers
network: true
overview: 'Gumloop publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Artifacts API, Brain API, and 11 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Automation, and Workflow-Automation.


  The Gumloop catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gumloop''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, engineering blog, and 25 more developer resources.'
random_paper: 15
scopes:
- name: Gumloop Scopes
  scope_count: 5
  slug: gumloop-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 62.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gumloop/refs/heads/main/screenshots/gumloop-2026-07-25T220434.png
security:
- kind: authentication
  name: Gumloop Authentication
  slug: gumloop-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gumloop Domain Security
  slug: gumloop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gumloop Trust Center
  slug: gumloop-trust-center
  summary_line: trust center published
slug: gumloop
tags:
- Company
- Artificial Intelligence
- AI Agents
- Automation
- Workflow-Automation
- Agent Platform
- MCP
- LLM
- No-Code
- Developer Tools
website: https://www.gumloop.com
---
