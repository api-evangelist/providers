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
- description: Read/Link MCP for maps.ikeytz.com. Public read-only.
  name: ikeytz Maps MCP
  slug: ikeytz-maps-mcp
artifact_total: 4
common:
- group: auth
  title: ''
  type: Security
  url: https://www.ikeytz.com/datenschutz
- group: agent
  href: https://artifacts.apis.io/ikeytz-com/llms/ikeytz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ikeytz-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ikeytz-com/mcp/ikeytz-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ikeytz-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ikeytz-com/well-known/ikeytz-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ikeytz-com-security.txt
- group: auth
  href: https://artifacts.apis.io/ikeytz-com/well-known/ikeytz-com-schluesseldienst-landkreis-ludwigsburg-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ikeytz-com-schluesseldienst-landkreis-ludwigsburg-security.txt
- group: auth
  href: https://artifacts.apis.io/ikeytz-com/well-known/ikeytz-com-maps-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ikeytz-com-maps-security.txt
- group: auth
  href: https://artifacts.apis.io/ikeytz-com/well-known/ikeytz-com-ikeytz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ikeytz-com-ikeytz-security.txt
- group: agent
  href: https://artifacts.apis.io/ikeytz-com/well-known/ikeytz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ikeytz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ikeytz-com/hosts/ikeytz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ikeytz-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ikeytz-com/security/ikeytz-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ikeytz-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ikeytz-com/security/ikeytz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ikeytz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ikeytz.com/
- group: operate
  title: ''
  type: Support
  url: https://www.ikeytz.com/kontakt
- group: company
  title: ''
  type: About
  url: https://ikeytz.com/
created: '2026-10-30'
description: ikeytz is a locksmith service based in Ludwigsburg, Germany, offering 24‑hour emergency door opening, key replacement, lock changes, and security technology for residential and commercial customers across the Ludwigsburg district and surrounding areas. The company provides transparent fixed‑price quotes, on‑site assessments, and professional technicians, emphasizing rapid response, non‑destructive entry methods, and compliance with local safety regulations.
image: https://www.ikeytz.com/logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at maps.ikeytz.com.
  name: ikeytz-com MCP Server
  slug: ikeytz-com-mcp-yml
modified: '2026-10-30'
name: ikeytz-com
nav: Providers
network: true
overview: 'ikeytz-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Locksmith, Security, EmergencyService, and Germany.


  ikeytz-com''s developer surface includes support and 13 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ikeytz-com/ikeytz-com-2026-11-03T133650.png
security:
- kind: domain-security
  name: Ikeytz Com Domain Security
  slug: ikeytz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ikeytz Com Vulnerability Disclosure
  slug: ikeytz-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ikeytz-com
tags:
- Company
- Locksmith
- Security
- EmergencyService
- Germany
- Ludwigsburg
website: https://ikeytz.com/
---
