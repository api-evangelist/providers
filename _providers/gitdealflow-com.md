---
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.8
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Gitdealflow Com Agentic Access
  operation_count: 37
  slug: gitdealflow-com-agentic-access
  summary_line: 37 operations · 1 acting
api_count: 1
apis:
- baseURL: https://signals.gitdealflow.com
  baseurl_source: declared
  description: 'Free, no-auth REST API over the weekly startup engineering-acceleration panel: bulk signals (JSON/CSV/NDJSON), single-startup lookups, sector rankings, citation-ready Q&A retrieval, site search, Scout'
  name: VC Deal Flow Signal API
  slug: vc-deal-flow-signal-api
- description: Hosted Model Context Protocol server (protocol 2025-06-18, Streamable HTTP) exposing 12 read-only tools, 3 resources and 7 prompts over the same signal panel; also shipped as the npm stdio package @gi
  name: VC Deal Flow Signal MCP Server
  slug: vc-deal-flow-signal-mcp-server
- description: Agent-to-Agent (A2A 0.3.0) JSON-RPC 2.0 endpoint implementing message/send, tasks/get and tasks/cancel over the signal panel, executing synchronously; discovered via the agent card served at /.well-kn
  name: GitDealFlow A2A Agent
  slug: gitdealflow-a2a-agent
- description: 'Microsoft NLWeb-compatible conversational endpoint: POST a natural-language query and receive schema.org-typed JSON-LD (ItemList, Organization, Article, Dataset or WebPage). GET returns the request-sc'
  name: GitDealFlow NLWeb Endpoint
  slug: gitdealflow-nlweb-endpoint
artifact_total: 12
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/security/gitdealflow-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gitdealflow-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/security/gitdealflow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gitdealflow-com-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/agentic-access/gitdealflow-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gitdealflow-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/authentication/gitdealflow-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gitdealflow-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://gitdealflow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://signals.gitdealflow.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://signals.gitdealflow.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://signals.gitdealflow.com/api/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://signals.gitdealflow.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://signals.gitdealflow.com/support
- group: company
  title: ''
  type: Blog
  url: https://signals.gitdealflow.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://signals.gitdealflow.com/feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kindrat86
- group: commercial
  title: ''
  type: Pricing
  url: https://signals.gitdealflow.com/pricing
- group: start
  title: ''
  type: Login
  url: https://signals.gitdealflow.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gitdealflow.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gitdealflow.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://signals.gitdealflow.com/agents/postman-collection.json
- group: operate
  title: ''
  type: StatusPage
  url: https://signals.gitdealflow.com/uptime
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/changelog/gitdealflow-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gitdealflow-com-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/lifecycle/gitdealflow-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gitdealflow-com-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/packages/gitdealflow-com-packages.yml
  title: ''
  type: Packages
  url: packages/gitdealflow-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/packages/gitdealflow-com-packages.yml
  title: ''
  type: SDKs
  url: packages/gitdealflow-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/well-known/gitdealflow-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gitdealflow-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/well-known/gitdealflow-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gitdealflow-com-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/a2a/gitdealflow-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gitdealflow-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/llms/gitdealflow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gitdealflow-com-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/conformance/gitdealflow-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gitdealflow-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/conventions/gitdealflow-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gitdealflow-com-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/components/gitdealflow-com-components.yml
  title: ''
  type: Components
  url: components/gitdealflow-com-components.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/plans/gitdealflow-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gitdealflow-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/rate-limits/gitdealflow-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gitdealflow-com-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/regulatory/gitdealflow-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/gitdealflow-com-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/well-known/gitdealflow-com-compliance.json
  title: ''
  type: Subprocessors
  url: well-known/gitdealflow-com-compliance.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/well-known/gitdealflow-com-compliance.json
  title: ''
  type: DataResidency
  url: well-known/gitdealflow-com-compliance.json
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/well-known/gitdealflow-com-compliance.json
  title: ''
  type: IncidentNotification
  url: well-known/gitdealflow-com-compliance.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/well-known/gitdealflow-com-ai-policy.json
  title: ''
  type: AITransparency
  url: well-known/gitdealflow-com-ai-policy.json
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://gitdealflow.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/security/gitdealflow-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/gitdealflow-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/scopes/gitdealflow-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gitdealflow-com-scopes.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gitdealflow-com/refs/heads/main/well-known/gitdealflow-com-compliance.json
  title: ''
  type: ExitAssistance
  url: well-known/gitdealflow-com-compliance.json
created: '2026-09-19'
description: GitDealFlow (also published as VC Deal Flow Signal) is a deal-flow signal tool for angel, scout and seed investors that reads public GitHub engineering activity across 400+ venture-backed startup organizations in 15 sectors and ranks the ones accelerating, historically 3-6 weeks before a fundraise announcement. The data is published free under CC BY 4.0 through a no-auth REST API described by an OpenAPI 3.1 document, a hosted MCP server (Streamable HTTP plus an npm stdio package), an A2A JSON-RPC agent with a published agent card, an NLWeb endpoint, JSON/CSV/ NDJSON bulk exports and an RSS feed, with one paid deep-signal endpoint metered by credit-pack key or x402 USDC micropayments. Operated pseudonymously from Cyprus by "The Data Nerd"; methodology published on SSRN.
image: https://signals.gitdealflow.com/icon.png
layout: provider
mcp_servers:
- description: ''
  name: GitDealFlow MCP Server
  slug: gitdealflow-mcp-server
modified: '2026-09-19'
name: GitDealFlow
nav: Providers
network: true
overview: 'GitDealFlow publishes 1 API on the [APIs.io](https://apis.io/) network: VC Deal Flow Signal API. Tagged areas include Venture Capital, Deal Flow, Startups, GitHub, and Alternative Data.


  GitDealFlow''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 35 more developer resources.'
plans:
- name: Gitdealflow Com Plans Pricing
  plan_count: 11
  slug: gitdealflow-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Gitdealflow Com Rate Limits
  slug: gitdealflow-com-rate-limits
scopes:
- name: Gitdealflow Com Scopes
  scope_count: 1
  slug: gitdealflow-com-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 52.5
    developer_ergonomics: 76.2
    discoverability: 75.9
    operational_transparency: 78.9
  previous_composite: 63.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Gitdealflow Com Authentication
  slug: gitdealflow-com-authentication
  summary_line: none/http-bearer/x402-payment/oauth2-client-credentials · 4 schemes
- kind: domain-security
  name: Gitdealflow Com Domain Security
  slug: gitdealflow-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gitdealflow Com Vulnerability Disclosure
  slug: gitdealflow-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: gitdealflow-com
tags:
- Venture Capital
- Deal Flow
- Startups
- GitHub
- Alternative Data
- Investing
- MCP
- Agents
- Developer Tools
- A2A
website: https://gitdealflow.com/
---
