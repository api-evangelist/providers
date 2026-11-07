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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/harvey-norman/mcp/harvey-norman-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/harvey-norman-mcp.yml
- group: agent
  href: https://artifacts.apis.io/harvey-norman/well-known/harvey-norman-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/harvey-norman-well-known.yml
- group: other
  href: https://artifacts.apis.io/harvey-norman/hosts/harvey-norman-hosts.yml
  title: ''
  type: Hosts
  url: hosts/harvey-norman-hosts.yml
- group: other
  href: https://artifacts.apis.io/harvey-norman/vendors/harvey-norman-vendors.yml
  title: ''
  type: Vendors
  url: vendors/harvey-norman-vendors.yml
- group: auth
  href: https://artifacts.apis.io/harvey-norman/security/harvey-norman-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/harvey-norman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://harveynorman.com.au/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.harveynormanholdings.com.au/
- group: other
  title: ''
  type: CompanyOverview
  url: https://www.harveynormanholdings.com.au/pages/company-overview
- group: other
  title: ''
  type: Governance
  url: https://www.harveynormanholdings.com.au/pages/governance
- group: operate
  title: ''
  type: Support
  url: https://www.harveynormanholdings.com.au/pages/contact
- group: company
  title: ''
  type: Careers
  url: https://www.harveynormansupportcareers.com.au/hnso/en/listing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harveynormanholdings.com.au/pages/privacy-policy
created: '2026-10-21'
description: 'Harvey Norman is an Australian retail brand for electrical, computers, furniture, bedding and homewares, operated through a franchise system owned by Harvey Norman Holdings Limited (HNHL, ASX: HVN). According to the group''s own company overview, HNHL is a public company listed on the Australian Securities Exchange that operates an integrated retail, franchise, property and digital system across eight countries, and owns the Harvey Norman, Domayne and Joyce Mayne trademarks, licensing them to independent franchisees in Australia. The consumer site harveynorman.com.au is fronted by an anti-bot challenge; no public developer portal, API documentation or API contract has been found.'
image: https://www.harveynormanholdings.com.au/cdn/shop/t/12/assets/apple-touch-icon-hnholdings-1024x1024.png?v=119165569640335848231731463395
layout: provider
mcp_servers:
- description: Universal Commerce Protocol (UCP) MCP server for the Harvey Norman Holdings online store at www.harveynormanholdings.com.au. The store is built on Shopify and its server identifies itself as "universa
  name: Harvey Norman Holdings UCP MCP Server
  slug: harvey-norman-holdings-ucp-mcp-server
modified: '2026-10-21'
name: Harvey Norman
nav: Providers
network: true
overview: 'Harvey Norman is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Consumer Electronics, Furniture, and Franchising.


  Harvey Norman''s developer surface includes support and 11 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.7
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
  previous_composite: 7.4
  provenance:
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/harvey-norman/harvey-norman-2026-11-03T133223.png
security:
- kind: domain-security
  name: Harvey Norman Domain Security
  slug: harvey-norman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harvey-norman
tags:
- Company
- Retail
- Consumer Electronics
- Furniture
- Franchising
- Australia
- E-Commerce
website: https://harveynorman.com.au/
---
