---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.0
  scored_at: '2026-09-15'
api_count: 1
apis:
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: One is the current successor brand to IntegrationOS and Pica. It provides agent infrastructure with a unified CLI for 250+ platforms and 50,000+ tools, managed OAuth (AuthKit), multi-step Flows, memor
  name: One (successor to IntegrationOS / Pica)
  slug: successor
artifact_total: 10
asyncapis:
- description: ''
  name: Integration Os Webhooks
  slug: integration-os-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/scopes/integration-os-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/integration-os-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/authentication/integration-os-authentication.yml
  title: ''
  type: Authentication
  url: authentication/integration-os-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.withone.ai/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/withoneai/knowledge/issues
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/a2a/integration-os-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/integration-os-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/security/integration-os-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/integration-os-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/integrationos
- group: start
  title: ''
  type: Portal
  url: https://withone.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.withone.ai/docs/welcome
- group: company
  title: ''
  type: Blog
  url: https://www.withone.ai/blog
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.withone.ai/knowledge
- group: start
  title: ''
  type: Signup
  url: https://app.withone.ai
- group: start
  title: ''
  type: Login
  url: https://app.withone.ai
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/withoneai
- group: other
  title: ''
  type: HistoricalSite
  url: https://www.picaos.com/
- group: build
  title: ''
  type: HistoricalGitHub
  url: https://github.com/integration-os
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/openapi/integration-os-one-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/integration-os-one-api-openapi.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/mcp/integration-os-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/integration-os-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/mcp/integration-os-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/integration-os-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/asyncapi/integration-os-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/integration-os-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/llms/integration-os-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/integration-os-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/well-known/integration-os-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/integration-os-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/packages/integration-os-packages.yml
  title: ''
  type: Packages
  url: packages/integration-os-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/packages/integration-os-packages.yml
  title: ''
  type: SDKs
  url: packages/integration-os-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/cli/integration-os-cli.yml
  title: ''
  type: CLI
  url: cli/integration-os-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/components/integration-os-components.yml
  title: ''
  type: Components
  url: components/integration-os-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/sandbox/integration-os-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/integration-os-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/conventions/integration-os-conventions.yml
  title: ''
  type: Conventions
  url: conventions/integration-os-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/conventions/integration-os-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/integration-os-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/errors/integration-os-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/integration-os-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/data-model/integration-os-data-model.yml
  title: ''
  type: DataModel
  url: data-model/integration-os-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/conformance/integration-os-conformance.yml
  title: ''
  type: Conformance
  url: conformance/integration-os-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/lifecycle/integration-os-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/integration-os-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withone.ai/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/changelog/integration-os-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/integration-os-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/plans/integration-os-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/integration-os-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/rate-limits/integration-os-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/integration-os-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/finops/integration-os-finops.yml
  title: ''
  type: FinOps
  url: finops/integration-os-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/rules/integration-os-rules.yml
  title: ''
  type: Rules
  url: rules/integration-os-rules.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/overlays/integration-os-one-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/integration-os-one-api-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://www.withone.ai/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.withone.ai/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.withone.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withone.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withone.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.withone.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withoneai
created: '2026-03-27'
description: 'IntegrationOS was a unified API platform that let developers add third-party integrations to their products with a single API call. The company rebranded as Pica (picaos.com) and then, on 2026-03-25, as One (withone.ai) — the provider''s own changelog records the step as "Pica is now One". One is an agent infrastructure platform: authenticated access to 789 platforms and 111,176 actions through a unified CLI, managed OAuth (AuthKit), multi-step Flows, inbound webhook Relay, and both a hosted and a local Model Context Protocol server. This record preserves the IntegrationOS history and profiles the active successor''s published surface, including its OpenAPI 3.1.0 contract (248 operations), its four-tool MCP server, its llms.txt and its agent.json.'
finops:
- name: Integration Os Finops
  service_category: API
  slug: integration-os-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: One ships BOTH a hosted remote MCP server and a local-stdio server, and the provider documents them as two ways to reach the same four tools. The remote endpoint is reachable and OAuth-gated; the loca
  name: IntegrationOS MCP Server
  slug: integrationos-mcp-server
modified: '2026-09-13'
name: IntegrationOS
nav: Providers
network: true
overview: 'IntegrationOS publishes 1 API on the [APIs.io](https://apis.io/) network: One (successor to IntegrationOS / Pica). Tagged areas include Agent Infrastructure, AI Agents, Connectors, Historical, and Integration.


  The IntegrationOS catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  IntegrationOS''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, CLI, sandbox, and 41 more developer resources.'
plans:
- name: Integration Os Plans Pricing
  plan_count: 4
  slug: integration-os-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Integration Os Rate Limits
  slug: integration-os-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: IntegrationOS API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: integration-os-rules
scopes:
- name: Integration Os Scopes
  scope_count: 38
  slug: integration-os-scopes
  summary_line: 38 scopes · authorizationCode
score:
  band: strong
  composite: 64.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 47.6
    developer_ergonomics: 85.7
    discoverability: 75.9
    operational_transparency: 76.3
  previous_composite: 64.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/screenshots/integration-os-2026-06-20T183438.png
security:
- kind: authentication
  name: Integration Os Authentication
  slug: integration-os-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Integration Os Domain Security
  slug: integration-os-domain-security
  summary_line: TLSv1.3 · HSTS
slug: integration-os
tags:
- Agent Infrastructure
- AI Agents
- Connectors
- Historical
- Integration
- iPaaS
- MCP
- Rebrand
- Unified-API
website: https://www.withone.ai/
---
