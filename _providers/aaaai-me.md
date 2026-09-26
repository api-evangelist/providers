---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 63
  human_in_the_loop: 3
  name: Aaaai Me Agentic Access
  operation_count: 102
  slug: aaaai-me-agentic-access
  summary_line: 102 operations · 63 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://web.aaaai.me
  baseurl_source: declared
  description: REST API of the AAA AI workspace, published as Swagger 2.0 "AAAAI API" 1.1.0 (host web.aaaai.me, 79 paths, 102 operations, no operationIds, empty definitions) at https://web.aaaai.me/api/spec.json — t
  name: AAAAI Platform API
  slug: aaaai-platform-api
- description: The provider-documented purchase surface for autonomous agents, described in https://aaaai.me/pay.md and machine-readably in https://aaaai.me/.well-known/agent-payments.json but absent from the Swagge
  name: AAA AI Agent Checkout (Billing) API
  slug: aaaai-agent-checkout-api
artifact_total: 8
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/agentic-access/aaaai-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aaaai-me-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://aaaai.me/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://web.aaaai.me/
- group: docs
  title: ''
  type: Documentation
  url: https://aaaai.me/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://web.aaaai.me/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://aaaai.me/auth.md
- group: start
  title: ''
  type: Login
  url: https://web.aaaai.me/
- group: start
  title: ''
  type: SignUp
  url: https://aaaai.me/register.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aaaai.me/pay/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aaaai.me/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aaaai.me/privacy.html
- group: operate
  title: ''
  type: Support
  url: mailto:support@aaaai.me
- group: company
  title: ''
  type: Blog
  url: https://aaaai.me/blog.html
- group: company
  title: ''
  type: BlogRSS
  url: https://aaaai.me/blog/feed.xml
- group: company
  title: ''
  type: Newsroom
  url: https://aaaai.me/news.html
- group: other
  title: ''
  type: Downloads
  url: https://aaaai.me/downloads.html
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/llms/aaaai-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aaaai-me-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://aaaai.me/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/well-known/aaaai-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aaaai-me-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://aaaai.me/.well-known/api-catalog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/authentication/aaaai-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aaaai-me-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/scopes/aaaai-me-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aaaai-me-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/conventions/aaaai-me-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aaaai-me-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/errors/aaaai-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aaaai-me-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/lifecycle/aaaai-me-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aaaai-me-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/changelog/aaaai-me-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aaaai-me-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://aaaai.me/news/feed.xml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/conformance/aaaai-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aaaai-me-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/plans/aaaai-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aaaai-me-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/rate-limits/aaaai-me-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aaaai-me-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/packages/aaaai-me-packages.yml
  title: ''
  type: Packages
  url: packages/aaaai-me-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/cli/aaaai-me-cli.yml
  title: ''
  type: CLI
  url: cli/aaaai-me-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/data-model/aaaai-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aaaai-me-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/security/aaaai-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aaaai-me-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://aaaai.me/privacy.html
- group: other
  title: ''
  type: AITransparency
  url: https://web.aaaai.me/meet
- group: other
  title: ''
  type: ExitAssistance
  url: https://aaaai.me/docs.html
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aaaai-me/refs/heads/main/regulatory/aaaai-me-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/aaaai-me-regulatory-posture.yml
created: '2026-09-19'
description: 'AAA AI (Autonomous Agents Automations; product spelling AAAAI) is a Montenegro-based multi-agent AI platform operated by Kirill Pokidov: a workspace at web.aaaai.me that routes questions through a panel of expert models with debate and verification modes, runs visual workflows with human-approval nodes across a catalog of integrations, pairs desktop "agents" on a user''s own machines, and adds Meet — voice and video calls with live AI notes. Sold as a $20/month Pro cloud plan (card, crypto or SBP) or self-hosted. The API is a 102-operation Swagger 2.0 contract on web.aaaai.me (chat, streaming queries, an OpenAI-compatible /v1/chat/completions, approvals, cron jobs, goal jobs, experts, settings) authenticated by an X-User-Login header, plus a documented crypto checkout API that lets an agent buy the subscription autonomously. The static site aaaai.me publishes an unusually complete agent-discovery layer — RFC 9727 api-catalog, OAuth/OIDC/RFC 9728 metadata, ai-plugin.json, an
  MCP server card, an agentskills.io index, agent-payments.json, llms.txt and the full ai-visibility.org.uk file set — several of whose targets (the named OpenAPI URL, the MCP endpoint, the JWKS) do not exist.'
image: https://aaaai.me/og-image.png
layout: provider
modified: '2026-09-19'
name: AAA AI
nav: Providers
network: true
overview: 'AAA AI publishes 2 APIs on the [APIs.io](https://apis.io/) network, including AAAAI Platform API, and 1 more. Tagged areas include Artificial Intelligence, Agents, Multi-Agent, LLM Orchestration, and Meetings.


  AAA AI''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 32 more developer resources.'
plans:
- name: Aaaai Me Plans Pricing
  plan_count: 2
  slug: aaaai-me-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Aaaai Me Rate Limits
  slug: aaaai-me-rate-limits
scopes:
- name: Aaaai Me Scopes
  scope_count: 5
  slug: aaaai-me-scopes
  summary_line: 5 scopes · authorizationCode/refreshToken/password
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 34.5
    developer_ergonomics: 66.1
    discoverability: 85.7
    operational_transparency: 15.8
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 42.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aaaai Me Authentication
  slug: aaaai-me-authentication
  summary_line: apiKey/cookie · 4 schemes
- kind: domain-security
  name: Aaaai Me Domain Security
  slug: aaaai-me-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aaaai-me
tags:
- Artificial Intelligence
- Agents
- Multi-Agent
- LLM Orchestration
- Meetings
- Voice
- Video
- Workflows
- MCP
- Agentic Commerce
- OpenAI-Compatible
- Self-Hosted
- Agent-Native
- Montenegro
website: https://aaaai.me/
---
