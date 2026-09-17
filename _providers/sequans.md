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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: A Model Context Protocol server exposed by the WordPress MCP Adapter running on the sequans.com corporate site. Two MCP endpoints are registered and enumerable anonymously through the WordPress REST r
  name: Sequans Website MCP Server
  slug: sequans-site-mcp
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/security/sequans-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sequans-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/security/sequans-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sequans-vulnerability-disclosure.yml
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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/well-known/sequans-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sequans-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/mcp/sequans-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sequans-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/authentication/sequans-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sequans-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/scopes/sequans-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sequans-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/conventions/sequans-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sequans-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/security/sequans-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sequans-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/llms/sequans-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sequans-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/plans/sequans-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sequans-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/rate-limits/sequans-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sequans-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/conformance/sequans-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sequans-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/conformance/sequans-conformance.yml
  title: ''
  type: Compliance
  url: conformance/sequans-conformance.yml
- group: operate
  title: ''
  type: Contact
  url: https://sequans.com/contact/
created: '2026-08-17'
description: 'Sequans Communications S.A. (NYSE: SQNS) is a fabless semiconductor company founded in 2003 and headquartered in Paris, France, designing and supplying 5G and 4G cellular IoT chips and modules. Its massive-IoT portfolio is built on the Monarch LTE-M/NB-IoT and Calliope Cat 1bis platforms, and its broadband-IoT portfolio on the Cassiopeia Cat 4/Cat 6 and Taurus 5G platforms, alongside the Iris software-defined RF transceiver and licensable silicon and software IP. Sequans sells chips, modules and IP to device makers rather than a developer-facing web API: its technical documentation, firmware, SDKs and AT-command references are distributed through the my.sequans.com support zone and the download.sequans.com customer portal, both of which require an account. The only anonymously reachable machine-readable surfaces on sequans.com are the WordPress REST API behind the corporate site and a WordPress MCP Adapter server advertised through RFC 8414 / RFC 9728 OAuth discovery documents.'
image: https://sequans.com/wp-content/uploads/2025/07/cropped-sequans-logo.png.png
layout: provider
mcp_servers:
- description: Sequans' corporate website (sequans.com, WordPress) runs the WordPress MCP Adapter, which exposes a remote Model Context Protocol server. Sequans does not document or announce it anywhere; it was foun
  name: Sequans MCP Server
  slug: sequans-mcp-server
modified: '2026-09-16'
name: Sequans
nav: Providers
network: true
overview: 'Sequans publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Cellular IoT, 5G, and LTE-M.


  Sequans'' developer surface includes engineering blog, support, signup flow, authentication, and 16 more developer resources.'
plans:
- name: Sequans Plans Pricing
  plan_count: 0
  slug: sequans-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Sequans Rate Limits
  slug: sequans-rate-limits
scopes:
- name: Sequans Scopes
  scope_count: 1
  slug: sequans-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.5
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 19.2
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 68.1
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/sequans/refs/heads/main/screenshots/sequans-2026-09-02T154933.png
security:
- kind: authentication
  name: Sequans Authentication
  slug: sequans-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Sequans Domain Security
  slug: sequans-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sequans Vulnerability Disclosure
  slug: sequans-vulnerability-disclosure
  summary_line: Hackerone
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
