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
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/ahmtransfer-com/llms/ahmtransfer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ahmtransfer-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ahmtransfer-com/mcp/ahmtransfer-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ahmtransfer-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/ahmtransfer-com/hosts/ahmtransfer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ahmtransfer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ahmtransfer-com/vendors/ahmtransfer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ahmtransfer-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ahmtransfer.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://ahmtransfer.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ahmtransfer.com/privacy/
- group: auth
  href: https://artifacts.apis.io/ahmtransfer-com/security/ahmtransfer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ahmtransfer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ahmtransfer.com/
coverage:
  checked: '2026-11-01'
  detail: The provider's website offers no machine‑readable API specification despite having a public site.
  evidence:
  - status: 200
    url: https://ahmtransfer.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AHM Transfer provides VIP airport transfer services in Alanya, Antalya, and Gazipaşa, offering fixed per‑vehicle pricing for routes such as Gazipaşa Airport to Alanya Center (€45) and Antalya Airport to Side (€45). Customers can quickly reserve via WhatsApp, with 24/7 service and a fleet of comfortable vehicles. The company emphasizes reliable, door‑to‑door transportation for travelers seeking convenient, premium transfers between major Turkish airports and resort destinations.
image: https://ahmtransfer.com/fleet-1.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at ahmtransfer.com.
  name: AHM Transfer MCP Server
  slug: ahmtransfer-com-mcp-yml
modified: '2026-11-01'
name: AHM Transfer
nav: Providers
network: true
overview: 'AHM Transfer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation, VIP Transfer, Airport Shuttle, Turkey, and Travel.


  AHM Transfer''s developer surface includes support and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 9.8
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ahmtransfer Com Domain Security
  slug: ahmtransfer-com-domain-security
  summary_line: TLSv1.3
slug: ahmtransfer-com
tags:
- Transportation
- VIP Transfer
- Airport Shuttle
- Turkey
- Travel
website: https://ahmtransfer.com/
---
