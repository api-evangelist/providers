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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Candidate invitations
  name: Litmus Hiring Invites API
  slug: litmus-hiring-invites-api
- description: Open roles within your organization
  name: Litmus Hiring Roles API
  slug: litmus-hiring-roles-api
- description: Candidate assessment submissions
  name: Litmus Hiring Submissions API
  slug: litmus-hiring-submissions-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Litmus Hiring REST Invites API
  slug: open-litmus-hiring-invites-api
- collection_type: open
  name: Litmus Hiring REST Invites Roles API
  slug: open-litmus-hiring-roles-api
- collection_type: open
  name: Litmus Hiring REST Invites Submissions API
  slug: open-litmus-hiring-submissions-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/litmus-hiring-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://litmushiring.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://litmushiring.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://litmushiring.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://litmushiring.com/docs/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://litmushiring.com/docs/mcp/quickstart
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://litmushiring.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://litmushiring.com/terms
- group: operate
  title: ''
  type: Support
  url: mailto:support@litmushiring.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/litmus-hiring-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/litmus-hiring-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/litmus-hiring-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/litmus-hiring-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/litmus-hiring-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/litmus-hiring-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/litmus-hiring-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/litmus-hiring-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/litmus-hiring-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/litmus-hiring-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/litmus-hiring-domain-security.yml
created: '2026-07-17'
description: Litmus is a Y Combinator-backed technical hiring platform that turns repositories, engineering tickets, and job descriptions into structured, project-based technical assessments and interview pipelines tailored to how a team actually ships. It evaluates candidates on both code quality and development process, lets them work in their own IDE or terminal, and captures AI-tool usage (Claude Code, Copilot CLI) transparently. Candidate management syncs with the Ashby, Greenhouse, and Lever applicant-tracking systems. Litmus exposes a bearer-key REST API (roles, invites, submissions) and an official hosted Model Context Protocol (MCP) server for agent-driven access to submissions, candidates, pipeline status, and assessment authoring.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/litmus-hiring.png
layout: provider
mcp_servers:
- description: ''
  name: litmus-hiring-mcp.yml
  slug: litmus-hiring-mcpyml
modified: '2026-07-20'
name: Litmus Hiring
nav: Providers
network: true
overview: 'Litmus Hiring publishes 3 APIs on the [APIs.io](https://apis.io/) network: Invites API, Roles API, and Submissions API. Tagged areas include Company, Hiring, Recruitment, Technical Assessment, and Developer Hiring.


  Litmus Hiring''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 16 more developer resources.'
random_paper: 12
scopes:
- name: Litmus Hiring Scopes
  scope_count: 7
  slug: litmus-hiring-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 40.3
  delta: -1.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 58.7
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 41.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/litmus-hiring/refs/heads/main/screenshots/litmus-hiring-2026-07-25T225341.png
security:
- kind: authentication
  name: Litmus Hiring Authentication
  slug: litmus-hiring-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Litmus Hiring Domain Security
  slug: litmus-hiring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: litmus-hiring
tags:
- Company
- Hiring
- Recruitment
- Technical Assessment
- Developer Hiring
- MCP
- Interviewing
- Y Combinator
website: https://litmushiring.com
---
