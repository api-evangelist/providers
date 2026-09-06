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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Laurence MCP is a hosted, remote Model Context Protocol server that exposes a read-only set of nine tools over a customer''s Amazon Advertising and Amazon Marketing Stream data — allowed ads profiles, '
  name: Laurence MCP
  slug: mcp
artifact_total: 7
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/laurence-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/laurence-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/laurence-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/laurence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/laurence-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/laurence-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/laurence-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/laurence-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/laurence-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/laurence-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/laurence-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/laurence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/laurence-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.laurence.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.laurence.com/how-it-works
- group: company
  title: ''
  type: Blog
  url: https://www.laurence.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.laurence.com/blog/feed.xml
- group: start
  title: ''
  type: SignUp
  url: https://www.laurence.com/audit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.laurence.com/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.laurence.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.laurence.com/demo
- group: start
  title: ''
  type: Login
  url: https://www.laurence.com/auth/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Laurence-AI
- group: other
  title: ''
  type: Sitemap
  url: https://www.laurence.com/sitemap.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/laurence-ai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/trylaurence
created: '2026-07-17'
description: Laurence is a New York City based Y Combinator (Winter 2026) company that automates Amazon advertising and marketplace management for brands. The platform applies quantitative-trading methodology — hierarchical Bayesian bid optimization over Amazon Marketing Stream data landed in ClickHouse — to maximize contribution margin after margin and ad spend rather than optimizing to rules-of-thumb ACOS targets. Laurence ingests Amazon Advertising and Seller Central data, prices every keyword auction, and exposes the resulting data to customers through Ask Laurence and a hosted, OAuth-protected Model Context Protocol server that brings Amazon Ads data into Claude Code, Cursor, and Codex. The company raised a $5.8M seed round led by Susa Ventures and Box Group with participation from Y Combinator.
image: https://www.laurence.com/icon.png
layout: provider
mcp_servers:
- description: 'Laurence operates an official hosted, remote MCP server that brings a customer''s Amazon Advertising and Amazon Marketing Stream (AMS) data into Claude Code, Cursor, and Codex. The server is available '
  name: Laurence MCP Server
  slug: laurence-mcp-server
modified: '2026-08-13'
name: Laurence
nav: Providers
network: true
overview: 'Laurence publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Amazon, E-Commerce, and Marketing.


  Laurence''s developer surface includes authentication, documentation, engineering blog, signup flow, support, and 22 more developer resources.'
plans:
- name: Laurence Plans Pricing
  plan_count: 0
  slug: laurence-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Laurence Rate Limits
  slug: laurence-rate-limits
scopes:
- name: Laurence Scopes
  scope_count: 0
  slug: laurence-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/laurence/refs/heads/main/screenshots/laurence-2026-07-25T224624.png
security:
- kind: authentication
  name: Laurence Authentication
  slug: laurence-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Laurence Domain Security
  slug: laurence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: laurence
tags:
- Company
- Advertising
- Amazon
- E-Commerce
- Marketing
- Machine-Learning
- Retail Media
- MCP
website: https://www.laurence.com
---
