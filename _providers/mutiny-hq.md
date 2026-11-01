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
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Mutiny's hosted Model Context Protocol server and its only public programmatic entry point. It exposes the workspace's asset creation, template, content library and publishing capabilities to any MCP-
  name: Mutiny MCP Server
  slug: mutiny-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.mutinyhq.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.mutinyhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.mutinyhq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mutinyhq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mutinyhq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.mutinyhq.com/register
- group: start
  title: ''
  type: Login
  url: https://app.mutinyhq.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mutinyhq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mutinyhq.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MutinyHQ
- group: agent
  href: https://artifacts.apis.io/mutiny-hq/mcp/mutiny-hq-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mutiny-hq-mcp.yml
- group: auth
  href: https://artifacts.apis.io/mutiny-hq/authentication/mutiny-hq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mutiny-hq-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mutiny-hq/scopes/mutiny-hq-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mutiny-hq-scopes.yml
- group: agent
  href: https://artifacts.apis.io/mutiny-hq/well-known/mutiny-hq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mutiny-hq-well-known.yml
- group: design
  href: https://artifacts.apis.io/mutiny-hq/conformance/mutiny-hq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mutiny-hq-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://help.mutinyhq.com/articles/4986991401-mutiny-compliance-overview
- group: auth
  href: https://artifacts.apis.io/mutiny-hq/security/mutiny-hq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mutiny-hq-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/mutiny-hq/llms/mutiny-hq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mutiny-hq-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://help.mutinyhq.com/articles/7238243181-mutiny-mcp-tools-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.mutinyhq.com/articles/8733886310-getting-started-with-mutiny-in-your-ai-assistant
- group: build
  href: https://artifacts.apis.io/mutiny-hq/packages/mutiny-hq-packages.yml
  title: ''
  type: Packages
  url: packages/mutiny-hq-packages.yml
- group: build
  href: https://artifacts.apis.io/mutiny-hq/packages/mutiny-hq-packages.yml
  title: ''
  type: SDKs
  url: packages/mutiny-hq-packages.yml
- group: design
  href: https://artifacts.apis.io/mutiny-hq/conventions/mutiny-hq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mutiny-hq-conventions.yml
- group: design
  href: https://artifacts.apis.io/mutiny-hq/conventions/mutiny-hq-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mutiny-hq-conventions.yml
- group: design
  href: https://artifacts.apis.io/mutiny-hq/errors/mutiny-hq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mutiny-hq-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mutiny-hq/data-model/mutiny-hq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mutiny-hq-data-model.yml
- group: design
  href: https://artifacts.apis.io/mutiny-hq/lifecycle/mutiny-hq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mutiny-hq-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/mutiny-hq/plans/mutiny-hq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mutiny-hq-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mutiny-hq/rate-limits/mutiny-hq-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mutiny-hq-rate-limits.yml
created: '2026-07-17'
description: Mutiny is a GTM (go-to-market) assistant built for customer-facing work — a vertical AI platform for B2B revenue teams (used by Snowflake, Uber, Rippling, GitLab, and Figma). It generates on-brand customer-facing assets such as deal rooms, pitch decks, business cases, ABM campaigns, comparison pages, and meeting recaps, and automates repetitive sales and marketing workflows through an agent, skill, and routine framework. Mutiny integrates with common CRM and GTM systems (Salesforce, HubSpot, Marketo, 6sense, Segment) and exposes a hosted Model Context Protocol (MCP) server so agents like Claude and ChatGPT can create, browse, and publish assets in conversation. Mutiny is backed by Insight Partners. It does not publish a general-purpose REST API; its programmatic entry point is the OAuth-protected MCP server.
finops:
- has_sources: true
  method: derived
  name: Mutiny Hq Finops
  primary_unit: subscription
  service_category: ''
  slug: mutiny-hq-finops
  template: false
image: https://framerusercontent.com/assets/Ec1hAhKLtluxlMfLydNP0NTrIA.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.mutinyhq.com over HTTP; 12 tools listed.
  name: Mutiny HQ MCP Server
  slug: mutiny
modified: '2026-08-13'
name: Mutiny HQ
nav: Providers
network: true
overview: 'Mutiny HQ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Go-To-Market, Sales Enablement, Marketing, and Website Personalization.


  Mutiny HQ''s developer surface includes documentation, engineering blog, pricing, signup flow, authentication, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: Mutiny Hq Plans Pricing
  plan_count: 3
  slug: mutiny-hq-plans-pricing
- name: Mutiny Hq Price Estimates
  plan_count: 0
  slug: mutiny-hq-price-estimates
random_paper: 4
rate_limits:
- limit_count: 0
  name: Mutiny Hq Rate Limits
  slug: mutiny-hq-rate-limits
scopes:
- name: Mutiny Hq Scopes
  scope_count: 5
  slug: mutiny-hq-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 40.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa-cpra
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mutiny-hq/mutiny-hq-2026-08-07T184453.png
security:
- kind: authentication
  name: Mutiny Hq Authentication
  slug: mutiny-hq-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Mutiny Hq Domain Security
  slug: mutiny-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mutiny-hq
tags:
- Company
- Go-To-Market
- Sales Enablement
- Marketing
- Website Personalization
- Artificial Intelligence
- Agents
- MCP
- Account Based Marketing
- Content Generation
website: https://www.mutinyhq.com/
---
