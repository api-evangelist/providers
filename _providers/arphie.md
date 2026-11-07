---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
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
  score: 29.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Arphie's remote Model Context Protocol server. It exposes Arphie projects, workload and project-volume metrics, and the company's agentic chat engine to MCP clients such as Claude, ChatGPT, Cursor, an
  name: Arphie MCP
  slug: arphie-mcp
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/arphie/security/arphie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arphie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arphie.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.arphie.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.arphie.ai/
- group: start
  title: ''
  type: Login
  url: https://app.arphie.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.arphie.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.arphie.ai/contact
- group: auth
  title: ''
  type: Compliance
  url: https://www.arphie.ai/security
- group: auth
  title: ''
  type: Security
  url: https://www.arphie.ai/responsible-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/arphie/security/arphie-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arphie-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arphie.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arphie.ai/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arphie.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arphie.ai/docs/intro
- group: agent
  href: https://artifacts.apis.io/arphie/mcp/arphie-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arphie-mcp.yml
- group: agent
  href: https://artifacts.apis.io/arphie/llms/arphie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arphie-llms.txt
- group: agent
  href: https://artifacts.apis.io/arphie/well-known/arphie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arphie-well-known.yml
- group: auth
  href: https://artifacts.apis.io/arphie/authentication/arphie-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arphie-authentication.yml
- group: auth
  href: https://artifacts.apis.io/arphie/scopes/arphie-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/arphie-scopes.yml
- group: design
  href: https://artifacts.apis.io/arphie/conformance/arphie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arphie-conformance.yml
- group: design
  href: https://artifacts.apis.io/arphie/conventions/arphie-conventions.yml
  title: ''
  type: Conventions
  url: conventions/arphie-conventions.yml
- group: design
  href: https://artifacts.apis.io/arphie/lifecycle/arphie-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/arphie-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/arphie/rate-limits/arphie-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arphie-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/arphie/plans/arphie-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arphie-plans-pricing.yml
created: '2026-07-17'
description: Arphie is an AI-powered knowledge activation platform that helps go-to-market teams automate RFP (Request for Proposal) responses, security questionnaires, and due-diligence questionnaires. Its AI agents draft answers from a company's knowledge base, cite sources with confidence scores, and integrate with knowledge sources such as Google Drive, SharePoint, Confluence, Notion, Seismic, and Highspot. Arphie is used by high-growth and publicly traded companies to win more deals faster while keeping proposal content accurate, current, and auditable. The company is SOC 2 Type 2 compliant, operates zero data retention with model providers, supports SAML 2.0 SSO and role-based access controls, and is backed by General Catalyst. Arphie publishes no REST API and no OpenAPI, but it does operate a live, remote Model Context Protocol server at https://app.arphie.ai/api/mcp — OAuth-protected, with RFC 9728 protected-resource discovery — that brings Arphie projects, workload metrics, and
  agentic chat into Claude, ChatGPT, Cursor, an IDE, or the terminal. Arphie also serves an llms.txt for AI agents. This profile was surfaced as a portfolio lead and enriched by the API Evangelist pipeline.
image: https://cdn.prod.website-files.com/672fc2345132970736914ada/67313797c7d6407f3b2c8a39_Arphie%20Social.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at app.arphie.ai over HTTP requiring OAuth.
  name: Arphie MCP
  slug: arphie-mcp
modified: '2026-08-13'
name: Arphie
nav: Providers
network: true
overview: 'Arphie is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Artificial Intelligence, Sales Enablement, and RFP Automation.


  Arphie''s developer surface includes signup flow, engineering blog, support, documentation, getting-started guide, authentication, and 18 more developer resources.'
plans:
- name: Arphie Plans Pricing
  plan_count: 0
  slug: arphie-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Arphie Rate Limits
  slug: arphie-rate-limits
scopes:
- name: Arphie Scopes
  scope_count: 1
  slug: arphie-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 33.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/arphie/arphie-2026-07-25T201242.png
security:
- kind: authentication
  name: Arphie Authentication
  slug: arphie-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Arphie Domain Security
  slug: arphie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arphie Vulnerability Disclosure
  slug: arphie-vulnerability-disclosure
  summary_line: disclosure policy published
slug: arphie
tags:
- Company
- Enterprise
- Artificial Intelligence
- Sales Enablement
- RFP Automation
- Security Questionnaires
- Knowledge Management
- Go-To-Market
- MCP
- Agents
website: https://www.arphie.ai/
---
