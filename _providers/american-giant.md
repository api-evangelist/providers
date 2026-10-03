---
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
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.2
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/american-giant/refs/heads/main/mcp/american-giant-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/american-giant-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/american-giant/refs/heads/main/hosts/american-giant-hosts.yml
  title: ''
  type: Hosts
  url: hosts/american-giant-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/american-giant/refs/heads/main/vendors/american-giant-vendors.yml
  title: ''
  type: Vendors
  url: vendors/american-giant-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/american-giant/refs/heads/main/security/american-giant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/american-giant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: 2026-09-24
  detail: American Giant's website provides only e‑commerce retail pages and no developer or API documentation.
  evidence:
  - status: 200
    url: https://www.american-giant.com
  reason: no-developer-program
  state: none
created: '2026-09-24'
description: American Giant is an American-made clothing and activewear brand offering a range of apparel including sweatshirts, hoodies, tees, and outerwear. The company emphasizes quality, domestic manufacturing, and sustainable practices, providing free shipping on orders over $150 and a focus on classic, durable designs.
layout: provider
mcp_servers:
- description: ''
  name: American Giant MCP Server
  slug: american-giant-mcp-server
modified: '2026-09-24'
name: American Giant
nav: Providers
network: true
overview: American Giant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Clothing, Activewear, AmericanMade, and E-Commerce.
random_paper: 0
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  previous_composite: 3.0
  provenance:
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: American Giant Domain Security
  slug: american-giant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: american-giant
tags:
- Company
- Clothing
- Activewear
- AmericanMade
- E-Commerce
website: https://www.nasdaqprivatemarket.com/
---
