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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The Cakewalk Open API is a REST API for building custom access-governance workflows and integrations. It exposes users, user groups, work apps, accesses, permission levels, requests, tasks, policies, '
  name: Cakewalk Open API
  slug: cakewalk-open-api
artifact_total: 8
asyncapis:
- description: ''
  name: Cakewalk Webhooks
  slug: cakewalk-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.cakewalk.security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cakewalk.security/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.cakewalk.security/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.cakewalk.security/docs/open-api-and-mcp/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cakewalk.security/docs/open-api-and-mcp/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/cakewalk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cakewalk-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cakewalk-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cakewalk-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cakewalk-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cakewalk-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cakewalk-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cakewalk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/cakewalk-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cakewalk-trust-center.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cakewalk-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cakewalk-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cakewalk-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cakewalk-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cakewalk.security/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cakewalk-security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cakewalk.security/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.cakewalk.security/book-demo
- group: start
  title: ''
  type: Login
  url: https://app.getcakewalk.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cakewalk-security/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@getcakewalk
created: '2026-07-17'
description: 'Cakewalk is the agentic access management platform for fast-moving companies, combining a granular identity governance and administration (IGA) platform with AI-driven workflows. Cakewalk governs access for both human identities and AI agents: its MCP Gateway routes every AI agent tool call through a runtime policy engine with credential mediation, least-privilege enforcement, and a complete audit trail, while its human access management handles joiner-mover-leaver lifecycle, access requests, access reviews, and auto-provisioning via its Agent Cake provisioning agent. The Cakewalk Open API and hosted MCP server let developers manage users, groups, work apps, accesses, requests, and tasks programmatically. Founded in 2022 and backed by Seedcamp, Fly Ventures, and Possible Ventures.'
image: https://www.getcakewalk.io/favicon-v2.png
layout: provider
mcp_servers:
- description: ''
  name: Cakewalk MCP Server
  slug: cakewalk-mcp-server
modified: '2026-07-18'
name: Cakewalk
nav: Providers
network: true
overview: 'Cakewalk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Access Management, Identity Governance, IGA, and AI Agents.


  The Cakewalk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cakewalk''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, YouTube channel, and 20 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 1
  name: Cakewalk Rate Limits
  slug: cakewalk-rate-limits
scopes:
- name: Cakewalk Scopes
  scope_count: 4
  slug: cakewalk-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 39.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cakewalk/refs/heads/main/screenshots/cakewalk-2026-07-25T204223.png
security:
- kind: authentication
  name: Cakewalk Authentication
  slug: cakewalk-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Cakewalk Domain Security
  slug: cakewalk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cakewalk Trust Center
  slug: cakewalk-trust-center
  summary_line: ISO 27001:2022
slug: cakewalk
tags:
- Company
- Access Management
- Identity Governance
- IGA
- AI Agents
- Security
- Access Control
- MCP
- Provisioning
- SaaS Management
- Authentication
website: https://www.cakewalk.security/
---
