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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://www.litmushiring.com/api/v1
  baseurl_source: declared
  description: Candidate invitations
  name: Litmus Hiring Invites API
  slug: litmus-hiring-invites-api
- baseURL: https://www.litmushiring.com/api/v1
  baseurl_source: declared
  description: Open roles within your organization
  name: Litmus Hiring Roles API
  slug: litmus-hiring-roles-api
- baseURL: https://www.litmushiring.com/api/v1
  baseurl_source: declared
  description: Candidate assessment submissions
  name: Litmus Hiring Submissions API
  slug: litmus-hiring-submissions-api
artifact_total: 13
collections:
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
  href: https://artifacts.apis.io/litmus-hiring/capabilities/litmus-hiring-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/litmus-hiring-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/litmus-hiring/overlays/litmus-hiring-overlay.yaml
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
  href: https://artifacts.apis.io/litmus-hiring/mcp/litmus-hiring-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/litmus-hiring-mcp.yml
- group: auth
  href: https://artifacts.apis.io/litmus-hiring/authentication/litmus-hiring-authentication.yml
  title: ''
  type: Authentication
  url: authentication/litmus-hiring-authentication.yml
- group: auth
  href: https://artifacts.apis.io/litmus-hiring/scopes/litmus-hiring-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/litmus-hiring-scopes.yml
- group: design
  href: https://artifacts.apis.io/litmus-hiring/conventions/litmus-hiring-conventions.yml
  title: ''
  type: Conventions
  url: conventions/litmus-hiring-conventions.yml
- group: design
  href: https://artifacts.apis.io/litmus-hiring/errors/litmus-hiring-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/litmus-hiring-problem-types.yml
- group: design
  href: https://artifacts.apis.io/litmus-hiring/lifecycle/litmus-hiring-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/litmus-hiring-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/litmus-hiring/conformance/litmus-hiring-conformance.yml
  title: ''
  type: Conformance
  url: conformance/litmus-hiring-conformance.yml
- group: design
  href: https://artifacts.apis.io/litmus-hiring/data-model/litmus-hiring-data-model.yml
  title: ''
  type: DataModel
  url: data-model/litmus-hiring-data-model.yml
- group: agent
  href: https://artifacts.apis.io/litmus-hiring/well-known/litmus-hiring-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/litmus-hiring-well-known.yml
- group: agent
  href: https://artifacts.apis.io/litmus-hiring/llms/litmus-hiring-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/litmus-hiring-llms.txt
- group: agent
  href: https://artifacts.apis.io/litmus-hiring/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/litmus-hiring/security/litmus-hiring-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/litmus-hiring-domain-security.yml
created: '2026-07-17'
description: Litmus is a Y Combinator-backed technical hiring platform that turns repositories, engineering tickets, and job descriptions into structured, project-based technical assessments and interview pipelines tailored to how a team actually ships. It evaluates candidates on both code quality and development process, lets them work in their own IDE or terminal, and captures AI-tool usage (Claude Code, Copilot CLI) transparently. Candidate management syncs with the Ashby, Greenhouse, and Lever applicant-tracking systems. Litmus exposes a bearer-key REST API (roles, invites, submissions) and an official hosted Model Context Protocol (MCP) server for agent-driven access to submissions, candidates, pipeline status, and assessment authoring.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/litmus-hiring.png
layout: provider
mcp_servers:
- description: Official hosted Model Context Protocol server for the Litmus hiring platform. Connects Claude Desktop, Claude Code, or Cursor (via Clerk OAuth) and headless/automation clients (via a `litmus_sk_...` A
  name: Litmus Hiring MCP Server
  slug: litmus
modified: '2026-07-20'
name: Litmus Hiring
nav: Providers
network: true
overview: 'Litmus Hiring publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Invites API, Roles API, and Submissions API. Tagged areas include Company, Hiring, Recruiting, Technical Assessment, and Developer Hiring.


  The Litmus Hiring catalog on APIs.io includes 1 Spectral governance ruleset.


  Litmus Hiring''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 17 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Litmus Hiring API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: litmus-hiring-rules
scopes:
- name: Litmus Hiring Scopes
  scope_count: 7
  slug: litmus-hiring-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 56.5
    discoverability: 68.3
    operational_transparency: 0.0
  previous_composite: 39.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/litmus-hiring/litmus-hiring-2026-07-25T225341.png
security:
- kind: authentication
  name: Litmus Hiring Authentication
  slug: litmus-hiring-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Litmus Hiring Domain Security
  slug: litmus-hiring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Author an assessment and invite a candidate
  slug: litmus-hiring-invite-and-assess
- name: Track Litmus submissions for a role
  slug: litmus-hiring-track-submissions
slug: litmus-hiring
tags:
- Company
- Hiring
- Recruiting
- Technical Assessment
- Developer Hiring
- MCP
- Interviewing
- Y Combinator
website: https://litmushiring.com
---
