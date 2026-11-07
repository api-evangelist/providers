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
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://mcp.airtreks.com
  baseurl_source: declared
  description: Multi-stop flight API for planning and pricing complex itineraries.
  name: AirTreks Routing API
  slug: airtreks-routing-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/airtreks-com/conformance/airtreks-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airtreks-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/airtreks-com/llms/airtreks-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airtreks-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/airtreks-com/mcp/airtreks-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/airtreks-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/airtreks-com/hosts/airtreks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airtreks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/airtreks-com/vendors/airtreks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/airtreks-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airtreks.com/about/privacy
- group: other
  title: ''
  type: Leadership
  url: https://airtreks.com/about/team/marin-voth
- group: company
  title: ''
  type: Blog
  url: https://airtreks.com/blog
- group: auth
  href: https://artifacts.apis.io/airtreks-com/security/airtreks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airtreks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airtreks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://airtreks.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.airtreks.com/openapi.json
created: '2026-11-01'
description: AirTreks, founded in 1987, specializes in designing and booking round‑the‑world and multi‑stop airline tickets that many major search engines cannot price. Leveraging a proprietary TripPlanner, they combine routes across airline alliances to create cost‑effective itineraries for travelers covering up to 35 stops across all continents. With over 100,000 travelers booked and 38+ years in business, AirTreks offers personalized service, handling complex itineraries, payment options, and travel support.
image: https://airtreks.com/og-default.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.airtreks.com.
  name: AirTreks MCP Server
  slug: airtreks-com-mcp-yml
modified: '2026-11-01'
name: AirTreks
nav: Providers
network: true
overview: 'AirTreks is listed with 1 API on the [APIs.io](https://apis.io/) network: Routing API. Tagged areas include Travel, Aviation, Booking, Multi-Stop, and Round-the-World.


  AirTreks'' developer surface includes engineering blog, API reference, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 5.3
    contract_governance: 4.5
    contract_quality: 37.6
    developer_ergonomics: 9.5
    discoverability: 65.8
    operational_transparency: 0.0
  previous_composite: 22.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airtreks Com Domain Security
  slug: airtreks-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airtreks-com
tags:
- Travel
- Aviation
- Booking
- Multi-Stop
- Round-the-World
website: https://airtreks.com/
---
