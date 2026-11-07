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
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/arb-corporation/llms/arb-corporation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arb-corporation-llms.txt
- group: agent
  href: https://artifacts.apis.io/arb-corporation/mcp/arb-corporation-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arb-corporation-mcp.yml
- group: agent
  href: https://artifacts.apis.io/arb-corporation/well-known/arb-corporation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arb-corporation-well-known.yml
- group: other
  href: https://artifacts.apis.io/arb-corporation/hosts/arb-corporation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arb-corporation-hosts.yml
- group: other
  href: https://artifacts.apis.io/arb-corporation/vendors/arb-corporation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arb-corporation-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.arb.com.au/Vehicles/Nissan/patrol/Y63/register
- group: auth
  href: https://artifacts.apis.io/arb-corporation/security/arb-corporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arb-corporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arb.com.au/
- group: operate
  title: ''
  type: Support
  url: https://www.arb.com.au/Contact-Us
- group: company
  title: ''
  type: Investors
  url: https://www.arb.com.au/investors
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arb.com.au/investors/Policies/arb-website-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arb.com.au/investors/Policies/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/arb-corporation-pty-ltd
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ARB4x4Accessories
created: '2026-10-21'
description: ARB Corporation (ARB 4x4 Accessories) is an Australian designer, manufacturer and retailer of off-road 4x4 vehicle accessories, operating at arb.com.au. Its range covers 4x4 protection (bull bars, side steps, rear bars, under-vehicle protection), Old Man Emu suspension kits and GVM upgrades, ute canopies, trays and lids, and roof racks, sold through ARB stores and dealers, with an investors section on its site. No public developer API documentation was found on its own site during this pass.
image: https://www.arb.com.au/content/dam/arb/permanent-site-assets/arb/logos/ARB%20Logo.svg
layout: provider
mcp_servers:
- description: Universal Commerce Protocol (UCP) MCP server for ARB Corporation's ARB 4x4 OUTLET online store (4x4outlet.arb.com.au), a Shopify storefront. It is the Shopify platform's standard storefront UCP server
  name: ARB 4x4 Outlet UCP MCP server
  slug: universal-commerce
modified: '2026-10-21'
name: ARB Corporation
nav: Providers
network: true
overview: 'ARB Corporation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, 4x4 Accessories, Off-Road, and Manufacturing.


  ARB Corporation''s developer surface includes signup flow, support, YouTube channel, and 11 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.3
  provenance:
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/arb-corporation/arb-corporation-2026-11-03T121053.png
security:
- kind: domain-security
  name: Arb Corporation Domain Security
  slug: arb-corporation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arb-corporation
tags:
- Company
- Automotive
- 4x4 Accessories
- Off-Road
- Manufacturing
- Retail
- Australia
website: https://www.arb.com.au/
---
