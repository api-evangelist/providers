---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Domainium provides API access to its domain name generation and branding tools.
  name: Domainium API
  slug: domainium-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/domainium-io/mcp/domainium-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/domainium-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/domainium-io/hosts/domainium-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domainium-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/domainium-io/vendors/domainium-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domainium-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/domainium-io/security/domainium-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domainium-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domainium.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://domainium.io/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://domainium.io/signup
- group: start
  title: ''
  type: Login
  url: https://domainium.io/login
- group: commercial
  title: ''
  type: Pricing
  url: https://domainium.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domainium.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://domainium.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domainium.io/terms
coverage:
  checked: '2026-10-30'
  detail: The provider offers a developer portal but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://domainium.io/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Domainium.io offers a suite of domain name generation and branding tools, including bulk domain checks, price comparisons, and creative name generators for businesses, startups, podcasts, and more. The platform provides a developer portal, API access, and various utilities to help users discover and secure domain names efficiently.
image: https://domainium.io/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at domainium.io requiring an API key.
  name: domainium-io MCP Server
  slug: domainium-io-mcp-yml
modified: '2026-10-30'
name: domainium-io
nav: Providers
network: true
overview: 'domainium-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Domain, Branding, and Tools.


  domainium-io''s developer surface includes getting-started guide, pricing, signup flow, and 9 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 51.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/domainium-io/domainium-io-2026-11-03T130921.png
security:
- kind: domain-security
  name: Domainium Io Domain Security
  slug: domainium-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: domainium-io
tags:
- Company
- Domain
- Branding
- Tools
website: https://domainium.io/
---
