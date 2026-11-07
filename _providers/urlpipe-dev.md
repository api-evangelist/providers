---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Turn any URL into clean data: Markdown, HTML, screenshots, PDFs, metadata, summaries, keywords, structured extraction, Lighthouse, console output and the technologies it is built with.'
  name: URLpipe API
  slug: urlpipe-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/urlpipe-dev/rate-limits/urlpipe-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/urlpipe-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/urlpipe-dev/plans/urlpipe-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/urlpipe-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/urlpipe-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/urlpipe-dev/cli/urlpipe-dev-cli.yml
  title: ''
  type: CLI
  url: cli/urlpipe-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/urlpipe-dev/conventions/urlpipe-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/urlpipe-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/urlpipe-dev/authentication/urlpipe-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/urlpipe-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/urlpipe-dev/errors/urlpipe-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/urlpipe-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/urlpipe-dev/conformance/urlpipe-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/urlpipe-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/urlpipe-dev/llms/urlpipe-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/urlpipe-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/urlpipe-dev/mcp/urlpipe-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/urlpipe-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/urlpipe-dev/well-known/urlpipe-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/urlpipe-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/urlpipe-dev/hosts/urlpipe-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/urlpipe-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/urlpipe-dev/vendors/urlpipe-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/urlpipe-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/urlpipe-dev/packages/urlpipe-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/urlpipe-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/urlpipe-dev/packages/urlpipe-dev-packages.yml
  title: ''
  type: Packages
  url: packages/urlpipe-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://urlpipe.dev/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://urlpipe.dev/status
- group: start
  title: ''
  type: SignUp
  url: https://urlpipe.dev/auth/sign-up/new
- group: auth
  title: ''
  type: Security
  url: https://urlpipe.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://urlpipe.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/URLpipe
- group: operate
  title: ''
  type: ChangeLog
  url: https://urlpipe.dev/changelog
- group: auth
  href: https://artifacts.apis.io/urlpipe-dev/security/urlpipe-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/urlpipe-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://urlpipe.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://urlpipe.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://urlpipe.dev/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://urlpipe.dev/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://urlpipe.dev/web-scraping-api
created: '2026-10-31'
description: URLpipe provides a web data API that transforms any URL into structured data. It offers endpoints for converting pages to Markdown, capturing screenshots, extracting metadata, generating AI summaries, performing Lighthouse audits, and more. The service runs on real Chrome, supports both HTTP and MCP protocols, and offers a free tier with no credit card required. Designed for developers, AI agents, and automation workflows, URLpipe delivers clean, consumable data from the web.
image: https://urlpipe.dev/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at urlpipe.dev requiring an API key.
  name: urlpipe-dev MCP Server
  slug: urlpipe-dev-mcp-yml
modified: '2026-10-31'
name: urlpipe-dev
nav: Providers
network: true
overview: 'urlpipe-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web Data, Web Scraping, Markdown, and Screenshots.


  urlpipe-dev''s developer surface includes CLI, authentication, signup flow, changelog, documentation, getting-started guide, pricing, and 21 more developer resources.'
plans:
- name: Urlpipe Dev Plans Pricing
  plan_count: 7
  slug: urlpipe-dev-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Urlpipe Dev Rate Limits
  slug: urlpipe-dev-rate-limits
scopes:
- name: Urlpipe Dev Scopes
  scope_count: 0
  slug: urlpipe-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 46.9
    discoverability: 65.0
    operational_transparency: 44.7
  previous_composite: 45.9
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Urlpipe Dev Authentication
  slug: urlpipe-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Urlpipe Dev Domain Security
  slug: urlpipe-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: urlpipe-dev
tags:
- Company
- Web Data
- Web Scraping
- Markdown
- Screenshots
- Artificial Intelligence
website: https://urlpipe.dev/
---
