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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Kubit's hosted Model Context Protocol server. Exposes five tools — getUserContext, getSchema, createReport, getRawData, and searchKubit — that let an MCP-compatible IDE or assistant explore schemas, e
  name: Kubit MCP Server
  slug: mcp
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Kubit-AI/mcp-server/issues
- group: company
  title: ''
  type: Website
  url: https://www.kubit.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kubit.ai/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kubit.ai/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kubit.ai/docs/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://guide.kubit.ai/article/get-started-overview
- group: company
  title: ''
  type: Blog
  url: https://kubit.ai/company/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kubit-AI
- group: commercial
  title: ''
  type: Pricing
  url: https://kubit.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://agent.kubit.ai/
- group: start
  title: ''
  type: Login
  url: https://app.kubit.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kubit.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kubit.ai/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://kubit.ai/about/#contact-block
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kubit-ai-inc-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/kubit-ai-inc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kubit-ai-inc-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kubit-ai-inc-cli.yml
- group: design
  title: ''
  type: Components
  url: components/kubit-ai-inc-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kubit-ai-inc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kubit-ai-inc-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kubit-ai-inc-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kubit-ai-inc-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/kubit-ai-inc-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kubit-ai-inc-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kubit-ai-inc-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://kubit.ai/gdpr-compliance-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: security/kubit-ai-inc-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubit-ai-inc-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kubit-ai-inc-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kubit-ai-inc-changelog.yml
created: '2026-07-17'
description: Kubit is a warehouse-native digital analytics platform that runs product analytics directly against a customer's cloud data warehouse with no ETL, and bridges that behavioral data with LLM observability. Kubit maps clickstream behavior, intent, and sentiment onto LLM traces so teams building AI agents can debug and optimize them where they already work. Its semantic layer applies business definitions, data models, and governance policies before any query reaches the warehouse. Kubit's programmatic surface is a hosted Model Context Protocol server at mcp.kubit.ai, protected by OAuth 2.1 with PKCE, plus first-party OpenTelemetry exporters and a set of published agent skills for Claude Code and Cursor. Kubit is backed by Insight Partners.
image: https://kubit.ai/wp-content/uploads/2024/04/cropped-Kubit-Social-Profile-Image-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: KubitMCP
  slug: kubitmcp
modified: '2026-07-19'
name: Kubit AI, Inc.
nav: Providers
network: true
overview: 'Kubit AI, Inc. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Product Analytics, Data Warehouse, and LLM Observability.


  Kubit AI, Inc.''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, CLI, and 25 more developer resources.'
random_paper: 15
scopes:
- name: Kubit Ai Inc Scopes
  scope_count: 0
  slug: kubit-ai-inc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 34.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubit-ai-inc/refs/heads/main/screenshots/kubit-ai-inc-2026-07-25T224318.png
security:
- kind: authentication
  name: Kubit Ai Inc Authentication
  slug: kubit-ai-inc-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Kubit Ai Inc Domain Security
  slug: kubit-ai-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kubit Ai Inc Trust Center
  slug: kubit-ai-inc-trust-center
  summary_line: enumerated, note
slug: kubit-ai-inc
tags:
- Company
- Analytics
- Product Analytics
- Data Warehouse
- LLM Observability
- MCP
- Agent Analytics
- OpenTelemetry
- DevOps
website: https://www.kubit.ai/
---
