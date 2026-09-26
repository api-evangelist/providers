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
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: REST API for planning and launching guaranteed and auction out-of-home (OOH) campaigns, placing insertion orders, submitting and scheduling creatives, and gathering in-flight delivery reporting. Authe
  name: AdQuick Partner API
  slug: adquick-partner-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.adquick.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.adquick.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adquick.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adquick.com/campaigns
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adquick.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.adquick.com/
- group: operate
  title: ''
  type: Support
  url: https://help.adquick.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adquick
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adquick.com/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/mcp/adquick-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adquick-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/authentication/adquick-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adquick-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/scopes/adquick-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adquick-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/errors/adquick-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adquick-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/conventions/adquick-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adquick-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/conformance/adquick-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adquick-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/well-known/adquick-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adquick-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/security/adquick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adquick-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/llms/adquick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adquick-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/mcp/adquick-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adquick-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/packages/adquick-packages.yml
  title: ''
  type: Packages
  url: packages/adquick-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/data-model/adquick-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adquick-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/rate-limits/adquick-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adquick-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/plans/adquick-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adquick-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/lifecycle/adquick-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adquick-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/security/adquick-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/adquick-trust-center.yml
created: '2026-07-17'
description: AdQuick is an intelligence and marketplace platform for out-of-home (OOH) advertising that lets advertisers plan, buy, execute, and measure billboard, transit, street-furniture, and programmatic digital-out-of-home (DOOH) campaigns across a network of 1,500+ media owners covering close to 100% of US OOH supply. AdQuick exposes a partner REST API (X-PARTNER-TOKEN authentication) at api.adquick.com for planning guaranteed and auction OOH campaigns, placing insertion orders, submitting and scheduling creatives, and pulling in-flight delivery reporting, plus a hosted Model Context Protocol (MCP) server (OAuth 2.0 + PKCE) at www.adquick.com/mcp that gives AI agents natural-language access to inventory discovery, campaign management, market analytics, exports, and programmatic DSP tooling. Backed by Initialized Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adquick.png
layout: provider
mcp_servers:
- description: Search OOH inventory, manage campaigns, analyze markets, and generate reports across US out-of-home advertising through natural language. Distributed in the Claude Connectors Directory.
  name: AdQuick MCP Server
  slug: adquick-mcp-server
modified: '2026-08-13'
name: AdQuick
nav: Providers
network: true
overview: 'AdQuick publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, Advertising, Out-of-Home Advertising, and Digital Out Of Home.


  AdQuick''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 20 more developer resources.'
plans:
- name: Adquick Plans Pricing
  plan_count: 0
  slug: adquick-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Adquick Rate Limits
  slug: adquick-rate-limits
scopes:
- name: Adquick Scopes
  scope_count: 6
  slug: adquick-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.8
  facets:
    access_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 2.6
  previous_composite: 25.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/adquick/refs/heads/main/screenshots/adquick-2026-07-25T181659.png
security:
- kind: authentication
  name: Adquick Authentication
  slug: adquick-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Adquick Domain Security
  slug: adquick-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Adquick Trust Center
  slug: adquick-trust-center
  summary_line: trust center published
slug: adquick
tags:
- Company
- Enterprise Saas
- Advertising
- Out-of-Home Advertising
- Digital Out Of Home
- Programmatic Advertising
- Media Buying
- Marketing
- MCP
website: https://www.adquick.com
---
