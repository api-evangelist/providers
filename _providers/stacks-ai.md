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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Stacks Ai Agentic Access
  operation_count: 13
  slug: stacks-ai-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- description: The analytics API from Stacks Ai — 2 operation(s) for analytics.
  name: Stacks Ai analytics API
  slug: stacks-ai-analytics-api
- description: The Knowledge Base Resources API from Stacks Ai — 2 operation(s) for knowledge base resources.
  name: Stacks Ai Knowledge Base Resources API
  slug: stacks-ai-knowledge-base-resources-api
- description: The Knowledge Base Sync API from Stacks Ai — 1 operation(s) for knowledge base sync.
  name: Stacks Ai Knowledge Base Sync API
  slug: stacks-ai-knowledge-base-sync-api
- description: The Knowledge Bases API from Stacks Ai — 5 operation(s) for knowledge bases.
  name: Stacks Ai Knowledge Bases API
  slug: stacks-ai-knowledge-bases-api
- description: The Run Flow API from Stacks Ai — 1 operation(s) for run flow.
  name: Stacks Ai Run Flow API
  slug: stacks-ai-run-flow-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: StackAI analytics API
  slug: open-stacks-ai-analytics-api
- collection_type: open
  name: StackAI analytics Knowledge Base Resources API
  slug: open-stacks-ai-knowledge-base-resources-api
- collection_type: open
  name: StackAI analytics Knowledge Base Sync API
  slug: open-stacks-ai-knowledge-base-sync-api
- collection_type: open
  name: StackAI analytics Knowledge Bases API
  slug: open-stacks-ai-knowledge-bases-api
- collection_type: open
  name: StackAI analytics Run Flow API
  slug: open-stacks-ai-run-flow-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/stacks-ai-build-knowledge-base.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stacks-ai-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/stacks-ai-openapi-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stacks-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stacks-ai-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stacks-ai-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.stackai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stackai.com/interface-and-deployment/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stackai.com/getting-started/start-here
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stackai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.stackai.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stackai.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stackai.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.stackai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stack-ai.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.stackai.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stacks-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stacks-ai-llms.txt
created: '2026-07-17'
description: StackAI (Stack AI, Inc.) is an enterprise AI agent platform that lets teams build, deploy, and govern no-code agentic workflows at scale. Its visual Workflow Builder chains LLMs, knowledge bases, connections, and logic nodes into production agents that can be deployed as a REST API, chat assistant, form, or batch job. The public StackAI API runs deployed flows, manages Knowledge Bases and their file resources (upload, index, sync, cursor-paginated listing), and reads flow-run analytics. The platform targets regulated industries with SOC 2 Type II and ISO 27001 certifications, RBAC/SCIM governance, and multi-tenant, VPC, and on-premise deployment options. Backed by Lightspeed Venture Partners.
image: https://www.stackai.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Stacks Ai MCP Server
  slug: stacks-ai-mcp-server
modified: '2026-07-21'
name: Stacks Ai
nav: Providers
network: true
overview: 'Stacks Ai publishes 5 APIs on the [APIs.io](https://apis.io/) network, including analytics API, Knowledge Base Resources API, Knowledge Base Sync API, and 2 more. Tagged areas include Company, Artificial Intelligence, Agents, LLM, and No-Code.


  Stacks Ai''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 14 more developer resources.'
random_paper: 14
scopes:
- name: Stacks Ai Scopes
  scope_count: 0
  slug: stacks-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 54.3
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stacks-ai/refs/heads/main/screenshots/stacks-ai-2026-08-17T082059.png
security:
- kind: authentication
  name: Stacks Ai Authentication
  slug: stacks-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Stacks Ai Domain Security
  slug: stacks-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stacks Ai Trust Center
  slug: stacks-ai-trust-center
  summary_line: SOC 2, ISO 27001
slug: stacks-ai
tags:
- Company
- Artificial Intelligence
- Agents
- LLM
- No-Code
- Automation
- Workflows
- RAG
- Knowledge Base
- Enterprise
website: https://docs.stackai.com/
---
