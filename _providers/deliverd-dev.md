---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 85
  human_in_the_loop: 3
  name: Deliverd Dev Agentic Access
  operation_count: 142
  slug: deliverd-dev-agentic-access
  summary_line: 142 operations · 85 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: Remote MCP server (Streamable HTTP) at https://deliverd.dev/api/mcp; OAuth 2.1 with PKCE and dynamic client registration per https://deliverd.dev/llms.txt. Anonymous probe returns 401 (gated).
  name: Deliverd MCP Server
  slug: deliverd-mcp-server
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Actions API from Deliverd — 1 operation(s) for actions.
  name: Deliverd Actions API
  slug: deliverd-dev-actions-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Agents API from Deliverd — 2 operation(s) for agents.
  name: Deliverd Agents API
  slug: deliverd-dev-agents-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Ai Systems API from Deliverd — 4 operation(s) for ai systems.
  name: Deliverd Ai Systems API
  slug: deliverd-dev-ai-systems-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Analytics API from Deliverd — 1 operation(s) for analytics.
  name: Deliverd Analytics API
  slug: deliverd-dev-analytics-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Approvals API from Deliverd — 5 operation(s) for approvals.
  name: Deliverd Approvals API
  slug: deliverd-dev-approvals-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Audiences API from Deliverd — 1 operation(s) for audiences.
  name: Deliverd Audiences API
  slug: deliverd-dev-audiences-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Audit Events API from Deliverd — 1 operation(s) for audit events.
  name: Deliverd Audit Events API
  slug: deliverd-dev-audit-events-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Collections API from Deliverd — 3 operation(s) for collections.
  name: Deliverd Collections API
  slug: deliverd-dev-collections-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Comments API from Deliverd — 2 operation(s) for comments.
  name: Deliverd Comments API
  slug: deliverd-dev-comments-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Decision Sessions API from Deliverd — 2 operation(s) for decision sessions.
  name: Deliverd Decision Sessions API
  slug: deliverd-dev-decision-sessions-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Drafts API from Deliverd — 1 operation(s) for drafts.
  name: Deliverd Drafts API
  slug: deliverd-dev-drafts-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Evidence API from Deliverd — 1 operation(s) for evidence.
  name: Deliverd Evidence API
  slug: deliverd-dev-evidence-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Flows API from Deliverd — 5 operation(s) for flows.
  name: Deliverd Flows API
  slug: deliverd-dev-flows-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Gates API from Deliverd — 7 operation(s) for gates.
  name: Deliverd Gates API
  slug: deliverd-dev-gates-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Governance API from Deliverd — 10 operation(s) for governance.
  name: Deliverd Governance API
  slug: deliverd-dev-governance-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Knowledge API from Deliverd — 5 operation(s) for knowledge.
  name: Deliverd Knowledge API
  slug: deliverd-dev-knowledge-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Playbooks API from Deliverd — 6 operation(s) for playbooks.
  name: Deliverd Playbooks API
  slug: deliverd-dev-playbooks-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Policies API from Deliverd — 6 operation(s) for policies.
  name: Deliverd Policies API
  slug: deliverd-dev-policies-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Reports API from Deliverd — 15 operation(s) for reports.
  name: Deliverd Reports API
  slug: deliverd-dev-reports-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Reviews API from Deliverd — 3 operation(s) for reviews.
  name: Deliverd Reviews API
  slug: deliverd-dev-reviews-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Risk Indicators API from Deliverd — 2 operation(s) for risk indicators.
  name: Deliverd Risk Indicators API
  slug: deliverd-dev-risk-indicators-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Schedules API from Deliverd — 2 operation(s) for schedules.
  name: Deliverd Schedules API
  slug: deliverd-dev-schedules-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Screen API from Deliverd — 1 operation(s) for screen.
  name: Deliverd Screen API
  slug: deliverd-dev-screen-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Tasks API from Deliverd — 20 operation(s) for tasks.
  name: Deliverd Tasks API
  slug: deliverd-dev-tasks-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Templates API from Deliverd — 1 operation(s) for templates.
  name: Deliverd Templates API
  slug: deliverd-dev-templates-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Uploads API from Deliverd — 1 operation(s) for uploads.
  name: Deliverd Uploads API
  slug: deliverd-dev-uploads-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Webhook Endpoints API from Deliverd — 3 operation(s) for webhook endpoints.
  name: Deliverd Webhook Endpoints API
  slug: deliverd-dev-webhook-endpoints-api
- baseURL: https://deliverd.dev
  baseurl_source: declared
  description: The Workspaces API from Deliverd — 1 operation(s) for workspaces.
  name: Deliverd Workspaces API
  slug: deliverd-dev-workspaces-api
artifact_total: 49
common:
- group: agent
  href: https://artifacts.apis.io/deliverd-dev/agentic-access/deliverd-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deliverd-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/deliverd-dev/rate-limits/deliverd-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deliverd-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/deliverd-dev/plans/deliverd-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deliverd-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deliverd-dev/rules/deliverd-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/deliverd-dev-rules.yml
- group: agent
  href: https://artifacts.apis.io/deliverd-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/deliverd-dev/components/deliverd-dev-components.yml
  title: ''
  type: Components
  url: components/deliverd-dev-components.yml
- group: build
  href: https://artifacts.apis.io/deliverd-dev/cli/deliverd-dev-cli.yml
  title: ''
  type: CLI
  url: cli/deliverd-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/deliverd-dev/changelog/deliverd-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/deliverd-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/deliverd-dev/conventions/deliverd-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/deliverd-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/deliverd-dev/conventions/deliverd-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deliverd-dev-conventions.yml
- group: start
  href: https://artifacts.apis.io/deliverd-dev/sandbox/deliverd-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/deliverd-dev-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://deliverd.dev/security
- group: auth
  href: https://artifacts.apis.io/deliverd-dev/scopes/deliverd-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/deliverd-dev-scopes.yml
- group: design
  href: https://artifacts.apis.io/deliverd-dev/lifecycle/deliverd-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/deliverd-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/deliverd-dev/errors/deliverd-dev-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/deliverd-dev-error-codes.yml
- group: design
  href: https://artifacts.apis.io/deliverd-dev/errors/deliverd-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deliverd-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deliverd-dev/conformance/deliverd-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deliverd-dev-conformance.yml
- group: other
  href: https://artifacts.apis.io/deliverd-dev/overlays/deliverd-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deliverd-dev-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/deliverd-dev/llms/deliverd-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deliverd-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/deliverd-dev/a2a/deliverd-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deliverd-dev-a2a.yml
- group: build
  href: https://artifacts.apis.io/deliverd-dev/mcp/deliverd-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/deliverd-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/deliverd-dev/mcp/deliverd-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deliverd-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/deliverd-dev/well-known/deliverd-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deliverd-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/deliverd-dev/well-known/deliverd-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deliverd-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/deliverd-dev/hosts/deliverd-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deliverd-dev-hosts.yml
- group: build
  href: https://artifacts.apis.io/deliverd-dev/integrations/deliverd-dev-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/deliverd-dev-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/deliverd-dev/vendors/deliverd-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deliverd-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/deliverd-dev/packages/deliverd-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/deliverd-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/deliverd-dev/packages/deliverd-dev-packages.yml
  title: ''
  type: Packages
  url: packages/deliverd-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/deliverd-dev/authentication/deliverd-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deliverd-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/deliverd-dev/security/deliverd-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deliverd-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/deliverd-dev/security/deliverd-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deliverd-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deliverd-dev/security/deliverd-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deliverd-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deliverd.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://deliverd.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://deliverd.dev/docs/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://deliverd.dev/docs/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://deliverd.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://deliverd.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://deliverd.dev/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://deliverd.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://deliverd.dev/sign-up
- group: start
  title: ''
  type: Login
  url: https://deliverd.dev/sign-in
- group: operate
  title: ''
  type: Support
  url: https://deliverd.dev/contact
- group: auth
  title: ''
  type: Security
  url: https://deliverd.dev/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deliverd.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deliverd.dev/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deliverd-dev
- group: company
  title: ''
  type: About
  url: https://deliverd.dev/about
- group: other
  title: ''
  type: X
  url: https://x.com/deliverd_dev
created: '2026-11-05'
description: 'Deliverd is human-in-the-loop infrastructure for AI agents. When an agent needs a person - for an approval, a decision, missing information or a review - it makes one call: Deliverd can check the agent''s action against policy or ask the right person under your rules about who may decide, returns the answer to the agent, and keeps evidence of who decided what. It works with any agent or tool over MCP, a REST API, TypeScript and Python SDKs and a CLI, with products for approvals, gates, tasks, publishing and compliance.'
image: https://deliverd.dev/opengraph-image-pwu6ef?9de8ef7e68eaf9b5
layout: provider
mcp_servers:
- description: Remote MCP server at deliverd.dev over streamable HTTP requiring OAuth; 100 tools listed.
  name: Deliverd MCP Server
  slug: deliverd
modified: '2026-11-05'
name: Deliverd
nav: Providers
network: true
overview: 'Deliverd publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Agents API, Ai Systems API, and 26 more. Tagged areas include Company, AI Agents, Human-in-the-Loop, Approvals, and MCP.


  The Deliverd catalog on APIs.io includes 1 Spectral governance ruleset.


  Deliverd''s developer surface includes CLI, changelog, sandbox, authentication, documentation, API reference, getting-started guide, and 43 more developer resources.'
plans:
- name: Deliverd Dev Plans Pricing
  plan_count: 5
  slug: deliverd-dev-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Deliverd Dev Rate Limits
  slug: deliverd-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Deliverd API Rules
  rule_count: 41
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 5
  slug: deliverd-dev-rules
scopes:
- name: Deliverd Dev Scopes
  scope_count: 29
  slug: deliverd-dev-scopes
  summary_line: 29 scopes
score:
  band: exemplar
  composite: 68.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 45.3
    developer_ergonomics: 85.7
    discoverability: 65.0
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deliverd Dev Authentication
  slug: deliverd-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deliverd Dev Domain Security
  slug: deliverd-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deliverd Dev Vulnerability Disclosure
  slug: deliverd-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Deliverd Dev Trust Center
  slug: deliverd-dev-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 10
skills:
- name: approval
  slug: deliverd-dev-approval
- name: artifact
  slug: deliverd-dev-artifact
- name: checkpoint
  slug: deliverd-dev-checkpoint
- name: compliance
  slug: deliverd-dev-compliance
- name: ethics-rules
  slug: deliverd-dev-ethics-rules
- name: ethics
  slug: deliverd-dev-ethics
- name: policy
  slug: deliverd-dev-policy
- name: prompts
  slug: deliverd-dev-prompts
- name: screen
  slug: deliverd-dev-screen
- name: tasks
  slug: deliverd-dev-tasks
slug: deliverd-dev
tags:
- Company
- AI Agents
- Human-in-the-Loop
- Approvals
- MCP
- Agent Governance
- Compliance
- Workflows
website: https://deliverd.dev/
---
