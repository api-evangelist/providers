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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dilutionlens Com Agentic Access
  operation_count: 10
  slug: dilutionlens-com-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- description: Remote MCP server advertised by DilutionLens (llms.txt and apis.yml description) exposing ASX dilution data tools to AI agents.
  name: DilutionLens MCP Server
  slug: dilutionlens-mcp
- baseURL: https://dilutionlens.com
  baseurl_source: declared
  description: The Company API from DilutionLens — 9 operation(s) for company.
  name: DilutionLens Company API
  slug: dilutionlens-com-company-api
- baseURL: https://dilutionlens.com
  baseurl_source: declared
  description: The Screen API from DilutionLens — 1 operation(s) for screen.
  name: DilutionLens Screen API
  slug: dilutionlens-com-screen-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/dilutionlens-com/agentic-access/dilutionlens-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dilutionlens-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/dilutionlens-com/rate-limits/dilutionlens-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dilutionlens-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dilutionlens-com/plans/dilutionlens-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dilutionlens-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dilutionlens-com/rules/dilutionlens-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dilutionlens-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/dilutionlens-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dilutionlens-com/conventions/dilutionlens-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dilutionlens-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/dilutionlens-com/errors/dilutionlens-com-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/dilutionlens-com-error-codes.yml
- group: design
  href: https://artifacts.apis.io/dilutionlens-com/errors/dilutionlens-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dilutionlens-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dilutionlens-com/conformance/dilutionlens-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dilutionlens-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dilutionlens-com/overlays/dilutionlens-com-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dilutionlens-com-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dilutionlens-com/llms/dilutionlens-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dilutionlens-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dilutionlens-com/mcp/dilutionlens-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dilutionlens-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dilutionlens-com/mcp/dilutionlens-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dilutionlens-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dilutionlens-com/hosts/dilutionlens-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dilutionlens-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dilutionlens-com/vendors/dilutionlens-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dilutionlens-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dilutionlens-com/authentication/dilutionlens-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dilutionlens-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dilutionlens-com/security/dilutionlens-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dilutionlens-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dilutionlens.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dilutionlens.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://dilutionlens.com/methodology/
- group: start
  title: ''
  type: GettingStarted
  url: https://dilutionlens.com/how-it-works/
- group: company
  title: ''
  type: Blog
  url: https://dilutionlens.com/watch/
- group: commercial
  title: ''
  type: Pricing
  url: https://dilutionlens.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://dilutionlens.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dilutionlens.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dilutionlens.com/privacy/
- group: other
  title: ''
  type: X
  url: https://x.com/DilutionLensApp
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@DilutionLens
created: '2026-11-05'
description: DilutionLens is an ASX dilution-intelligence service operated by Assemblance Technologies LLC (Delaware, USA). It reads public ASX filings (Appendix 2A/3B/3G/3H, quarterly 4C/5B cash reports, Appendix 3Y dealing notices, raise announcements) and tracks share counts, capital raises, option and rights overhang, cash runway and a methodology-published dilution risk level for every ASX-listed company, rebuilt every trading day. Data is available on free company pages, through a per-ticker REST API (openapi.json) and a remote MCP server at https://dilutionlens.com/mcp, with paid depth on monthly or annual plans.
image: https://dilutionlens.com/opengraph-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at dilutionlens.com requiring an API key; 6 tools listed.
  name: DilutionLens MCP Server
  slug: dilutionlens-mcp-server
modified: '2026-11-05'
name: DilutionLens
nav: Providers
network: true
overview: 'DilutionLens publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Company API, Screen API, and 1 more. Tagged areas include Company, Financial Data, Capital Markets, ASX, and Equity Dilution.


  The DilutionLens catalog on APIs.io includes 1 Spectral governance ruleset.


  DilutionLens'' developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, YouTube channel, and 22 more developer resources.'
plans:
- name: Dilutionlens Com Plans Pricing
  plan_count: 4
  slug: dilutionlens-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Dilutionlens Com Rate Limits
  slug: dilutionlens-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: DilutionLens API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: dilutionlens-com-rules
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 47.0
    discoverability: 65.0
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dilutionlens Com Authentication
  slug: dilutionlens-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dilutionlens Com Domain Security
  slug: dilutionlens-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: dilutionlens-assess-dilution-risk
  slug: dilutionlens-com-assess-dilution-risk
- name: dilutionlens-screen-and-drill-down
  slug: dilutionlens-com-screen-and-drill-down
slug: dilutionlens-com
tags:
- Company
- Financial Data
- Capital Markets
- ASX
- Equity Dilution
- Market Data
- MCP
- Investing
website: https://dilutionlens.com/
---
