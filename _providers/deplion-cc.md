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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Remote streamable-HTTP MCP server (registry name cc.deplion/deplion, v0.5.0) that lets an AI assistant create and publish static websites, configure forms and read leads in a Deplion account. Deplion '
  name: Deplion MCP Server
  slug: deplion-mcp
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/deplion-cc/plans/deplion-cc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deplion-cc-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deplion-cc/conventions/deplion-cc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deplion-cc-conventions.yml
- group: auth
  href: https://artifacts.apis.io/deplion-cc/authentication/deplion-cc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deplion-cc-authentication.yml
- group: auth
  href: https://artifacts.apis.io/deplion-cc/scopes/deplion-cc-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/deplion-cc-scopes.yml
- group: design
  href: https://artifacts.apis.io/deplion-cc/lifecycle/deplion-cc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/deplion-cc-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/deplion-cc/well-known/deplion-cc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deplion-cc-well-known.yml
- group: other
  href: https://artifacts.apis.io/deplion-cc/hosts/deplion-cc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deplion-cc-hosts.yml
- group: other
  href: https://artifacts.apis.io/deplion-cc/vendors/deplion-cc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deplion-cc-vendors.yml
- group: auth
  href: https://artifacts.apis.io/deplion-cc/security/deplion-cc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deplion-cc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deplion.cc/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deplion.cc/s/documentations
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.deplion.cc/s/documentations/doc/connect-your-ai-assistant-7Pwj7bazqW
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.deplion.cc/s/help-center
- group: company
  title: ''
  type: Blog
  url: https://deplion.cc/resources/blog
- group: company
  title: ''
  type: Newsroom
  url: https://deplion.cc/resources/news
- group: learn
  title: ''
  type: Tutorials
  url: https://deplion.cc/resources/tutorials
- group: commercial
  title: ''
  type: Pricing
  url: https://deplion.cc/pricing
- group: start
  title: ''
  type: SignUp
  url: https://deplion.cc/register
- group: start
  title: ''
  type: Login
  url: https://deplion.cc/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deplion.cc/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deplion.cc/legal/privacy-policy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://deplion.cc/legal/acceptable-use-policy
created: '2026-11-05'
description: Deplion (deplion.cc, operated by Bytech LLP) is a publishing workspace for AI-built websites. Users connect Deplion to the AI assistant they already use (Claude, ChatGPT, Cursor, Codex, VS Code or any MCP client) over a remote streamable-HTTP MCP server, and the assistant can create projects, write files, open previews, publish releases, roll back versions and manage live sites on a subdomain or a custom domain, with forms, submissions, webhooks and CRM features on paid Start and Pro plans.
image: https://deplion.cc/apple-touch-icon.png
layout: provider
mcp_servers:
- description: Create and publish static websites, configure forms, and read leads through Deplion.
  name: Deplion MCP Server
  slug: deplion-mcp-server
modified: '2026-11-05'
name: Deplion
nav: Providers
network: true
overview: 'Deplion is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MCP, Website Publishing, and Web Hosting.


  Deplion''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Deplion Cc Plans Pricing
  plan_count: 3
  slug: deplion-cc-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Deplion Cc Rate Limits
  slug: deplion-cc-rate-limits
scopes:
- name: Deplion Cc Scopes
  scope_count: 1
  slug: deplion-cc-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deplion Cc Authentication
  slug: deplion-cc-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Deplion Cc Domain Security
  slug: deplion-cc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: deplion-cc
tags:
- Company
- Artificial Intelligence
- MCP
- Website Publishing
- Web Hosting
- Deployment
- No-Code
- AI Agents
website: https://deplion.cc/
---
