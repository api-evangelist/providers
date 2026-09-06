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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: A Model Context Protocol server exposed by the WordPress MCP Adapter running on the sequans.com corporate site. Two MCP endpoints are registered and enumerable anonymously through the WordPress REST r
  name: Sequans Website MCP Server
  slug: sequans-site-mcp
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://sequans.com/
- group: company
  title: ''
  type: Blog
  url: https://sequans.com/sequans-blog/
- group: operate
  title: ''
  type: Support
  url: https://sequans.com/my-sequans/
- group: operate
  title: ''
  type: HelpCenter
  url: https://forum.sequans.com/
- group: start
  title: ''
  type: SignUp
  url: https://signup.sequans.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sequans.com/sequans-privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sequans
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sequans-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sequans-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sequans-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sequans-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sequans-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sequans-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sequans-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/sequans-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sequans-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sequans-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sequans-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/sequans-packages.yml
created: '2026-08-17'
description: 'Sequans Communications S.A. (NYSE: SQNS) is a fabless semiconductor company founded in 2003 and headquartered in Paris, France, designing and supplying 5G and 4G cellular IoT chips and modules. Its massive-IoT portfolio is built on the Monarch LTE-M/NB-IoT and Calliope Cat 1bis platforms, and its broadband-IoT portfolio on the Cassiopeia Cat 4/Cat 6 and Taurus 5G platforms, alongside the Iris software-defined RF transceiver and licensable silicon and software IP. Sequans sells chips, modules and IP to device makers rather than a developer-facing web API: its technical documentation, firmware, SDKs and AT-command references are distributed through the my.sequans.com support zone and the download.sequans.com customer portal, both of which require an account. The only anonymously reachable machine-readable surfaces on sequans.com are the WordPress REST API behind the corporate site and a WordPress MCP Adapter server advertised through RFC 8414 / RFC 9728 OAuth discovery documents.'
image: https://sequans.com/wp-content/uploads/2025/07/cropped-sequans-logo.png.png
layout: provider
mcp_servers:
- description: ''
  name: Sequans MCP Server
  slug: sequans-mcp-server
modified: '2026-08-17'
name: Sequans
nav: Providers
network: true
overview: 'Sequans publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Cellular IoT, 5G, and LTE-M.


  Sequans'' developer surface includes engineering blog, support, signup flow, authentication, and 15 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 19.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 52.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/screenshots/sequans-2026-09-02T154933.png
security:
- kind: domain-security
  name: Sequans Domain Security
  slug: sequans-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sequans
tags:
- Company
- Semiconductors
- Cellular IoT
- 5G
- LTE-M
- NB-IoT
- IoT Modules
- Hardware
- Telecommunications
- France
website: https://sequans.com/
---
