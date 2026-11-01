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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/realscout/plans/realscout-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/realscout-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.realscout.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://learn.realscout.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.realscout.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.realscout.com/
- group: start
  title: ''
  type: Login
  url: https://www.realscout.com/agents/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.realscout.com/terms-and-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.realscout.com/terms-and-policies
- group: agent
  href: https://artifacts.apis.io/realscout/mcp/realscout-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/realscout-mcp.yml
- group: auth
  href: https://artifacts.apis.io/realscout/authentication/realscout-authentication.yml
  title: ''
  type: Authentication
  url: authentication/realscout-authentication.yml
- group: auth
  href: https://artifacts.apis.io/realscout/scopes/realscout-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/realscout-scopes.yml
- group: agent
  href: https://artifacts.apis.io/realscout/well-known/realscout-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/realscout-well-known.yml
- group: auth
  href: https://artifacts.apis.io/realscout/security/realscout-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/realscout-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/realscout/llms/realscout-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/realscout-llms.txt
created: '2026-07-17'
description: RealScout is a lead-nurture and collaborative home-search platform for real estate professionals — agents, teams, and brokerages — that turns an agent's existing database and local MLS inventory into a recurring source of transactions. It is CRM-agnostic and plugs into existing stacks (Follow Up Boss, Sierra, Salesforce, HubSpot) via native integrations, Zapier/Make, and direct API access on Enterprise plans. Core products include AI Search (natural-language-to-MLS-criteria), Scout Score (0–100 contact engagement scoring), Contact Enrichment, Search Links, and Auto-Nurture alerts. RealScout publishes an OAuth 2.1-protected, standards-compliant MCP server (api://realscout-admin-mcp) for agent/AI access. Backed by DCM Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realscout.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.realscout.com over HTTP.
  name: RealScout MCP Server
  slug: realscout-admin-mcp
modified: '2026-07-20'
name: RealScout
nav: Providers
network: true
overview: 'RealScout is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Real Estate, PropTech, and Lead Nurture.


  RealScout''s developer surface includes pricing, support, engineering blog, authentication, and 10 more developer resources.'
plans:
- name: Realscout Plans Pricing
  plan_count: 5
  slug: realscout-plans-pricing
random_paper: 18
scopes:
- name: Realscout Scopes
  scope_count: 1
  slug: realscout-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 25.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/realscout/realscout-2026-09-02T153004.png
security:
- kind: authentication
  name: Realscout Authentication
  slug: realscout-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Realscout Domain Security
  slug: realscout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: realscout
tags:
- Company
- Enterprise
- Real Estate
- PropTech
- Lead Nurture
- Home Search
- MLS
- MCP
- Artificial Intelligence
website: https://www.realscout.com/
---
