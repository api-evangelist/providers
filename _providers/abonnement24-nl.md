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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://abonnement24.nl/api
  baseurl_source: declared
  description: API providing telecom deal search functions for phones, sim‑only plans, internet & TV bundles.
  name: Abonnement24 API
  slug: abonnement24-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/abonnement24-nl/overlays/abonnement24-nl-mcp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/abonnement24-nl-mcp-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/abonnement24-nl/llms/abonnement24-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abonnement24-nl-llms.txt
- group: agent
  href: https://artifacts.apis.io/abonnement24-nl/mcp/abonnement24-nl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/abonnement24-nl-mcp.yml
- group: other
  href: https://artifacts.apis.io/abonnement24-nl/hosts/abonnement24-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abonnement24-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/abonnement24-nl/vendors/abonnement24-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abonnement24-nl-vendors.yml
- group: auth
  href: https://artifacts.apis.io/abonnement24-nl/security/abonnement24-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abonnement24-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abonnement24.nl/
- group: company
  title: ''
  type: Blog
  url: https://abonnement24.nl/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abonnement24.nl/privacy
- group: operate
  title: ''
  type: Support
  url: https://abonnement24.nl/contact
- group: other
  title: ''
  type: Image
  url: https://abonnement24.nl/opengraph-image?e04d3901158234e3
created: '2026-10-31'
description: Abonnement24 is a Dutch comparison platform that helps consumers compare mobile phone contracts, sim‑only plans, internet and TV bundles. It aggregates live prices from major providers such as Odido, Vodafone, KPN, Youfone and others, presenting the total cost over the full contract term, including action prices, regular prices and cashback. The service aims to show transparent, real‑world pricing without hidden fees, enabling users to find the most affordable options.
image: https://abonnement24.nl/opengraph-image?e04d3901158234e3
layout: provider
mcp_servers:
- description: Remote MCP server at abonnement24.nl.
  name: Abonnement24 MCP Server
  slug: abonnement24-nl-mcp-yml
modified: '2026-10-31'
name: Abonnement24
nav: Providers
network: true
overview: 'Abonnement24 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Comparison, Netherlands, Mobile, and Internet.


  Abonnement24''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 3.6
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 14.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 6.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abonnement24 Nl Domain Security
  slug: abonnement24-nl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: abonnement24-nl
tags:
- Telecommunications
- Comparison
- Netherlands
- Mobile
- Internet
website: https://abonnement24.nl/
---
