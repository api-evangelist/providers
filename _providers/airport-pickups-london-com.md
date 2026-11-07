---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Airport Pickups London Com Agentic Access
  operation_count: 14
  slug: airport-pickups-london-com-agentic-access
  summary_line: 14 operations · 12 acting
api_count: 1
apis:
- baseURL: https://mcp.airport-pickups-london.com
  baseurl_source: declared
  description: The Amend Booking API from Airport Pickups London — 1 operation(s) for amend booking.
  name: Airport Pickups London Amend Booking API
  slug: airport-pickups-london-com-amend-booking-api
- baseURL: https://mcp.airport-pickups-london.com
  baseurl_source: declared
  description: The Book API from Airport Pickups London — 1 operation(s) for book.
  name: Airport Pickups London Book API
  slug: airport-pickups-london-com-book-api
- baseURL: https://mcp.airport-pickups-london.com
  baseurl_source: declared
  description: The Cancel Booking API from Airport Pickups London — 1 operation(s) for cancel booking.
  name: Airport Pickups London Cancel Booking API
  slug: airport-pickups-london-com-cancel-booking-api
- baseURL: https://mcp.airport-pickups-london.com
  baseurl_source: declared
  description: The Lookup Booking API from Airport Pickups London — 1 operation(s) for lookup booking.
  name: Airport Pickups London Lookup Booking API
  slug: airport-pickups-london-com-lookup-booking-api
- baseURL: https://mcp.airport-pickups-london.com
  baseurl_source: declared
  description: The Quote API from Airport Pickups London — 1 operation(s) for quote.
  name: Airport Pickups London Quote API
  slug: airport-pickups-london-com-quote-api
- baseURL: https://mcp.airport-pickups-london.com
  baseurl_source: declared
  description: The Track API from Airport Pickups London — 1 operation(s) for track.
  name: Airport Pickups London Track API
  slug: airport-pickups-london-com-track-api
- baseURL: https://mcp.airport-pickups-london.com
  baseurl_source: declared
  description: The Validate Flight API from Airport Pickups London — 1 operation(s) for validate flight.
  name: Airport Pickups London Validate Flight API
  slug: airport-pickups-london-com-validate-flight-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/airport-pickups-london-com/agentic-access/airport-pickups-london-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/airport-pickups-london-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/airport-pickups-london-com/rules/airport-pickups-london-com-rules.yml
  title: ''
  type: Spectral
  url: rules/airport-pickups-london-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/airport-pickups-london-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/airport-pickups-london-com/errors/airport-pickups-london-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/airport-pickups-london-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/airport-pickups-london-com/conformance/airport-pickups-london-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airport-pickups-london-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/airport-pickups-london-com/llms/airport-pickups-london-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airport-pickups-london-com-llms.txt
- group: other
  href: https://artifacts.apis.io/airport-pickups-london-com/a2a/airport-pickups-london-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/airport-pickups-london-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/airport-pickups-london-com/mcp/airport-pickups-london-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/airport-pickups-london-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/airport-pickups-london-com/well-known/airport-pickups-london-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/airport-pickups-london-com-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/airport-pickups-london-com/well-known/airport-pickups-london-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airport-pickups-london-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/airport-pickups-london-com/hosts/airport-pickups-london-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airport-pickups-london-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/airport-pickups-london-com/vendors/airport-pickups-london-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/airport-pickups-london-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/airport-pickups-london-com/authentication/airport-pickups-london-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airport-pickups-london-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/airport-pickups-london-com/security/airport-pickups-london-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airport-pickups-london-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airport-pickups-london.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.airport-pickups-london.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://mcp.airport-pickups-london.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.airport-pickups-london.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.airport-pickups-london.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.airport-pickups-london.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airport-pickups-london.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airport-pickups-london.com/privacy-policy
created: '2026-11-01'
description: Airport Pickups London provides reliable airport transfer services across London, including Heathrow, Gatwick, Stansted, Luton and City Airport. Customers can book taxis, minibuses and shuttles online for stress‑free travel. The company emphasizes professional, punctual service and offers 24/7 support for travelers needing airport pickups or drop‑offs.
image: https://www.airport-pickups-london.com/images/homeScreenImage.webp
layout: provider
mcp_servers:
- description: Remote MCP server at gemini.airport-pickups-london.com.
  name: Airport Pickups London MCP Server
  slug: airport-pickups-london-com-mcp-yml
modified: '2026-11-01'
name: Airport Pickups London
nav: Providers
network: true
overview: 'Airport Pickups London publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Amend Booking API, Book API, Cancel Booking API, and 4 more. Tagged areas include Company, Airport, Transport, Taxi, and London.


  The Airport Pickups London catalog on APIs.io includes 1 Spectral governance ruleset.


  Airport Pickups London''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 17 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Airport Pickups London API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: airport-pickups-london-com-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 53.5
    developer_ergonomics: 35.1
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Airport Pickups London Com Authentication
  slug: airport-pickups-london-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Airport Pickups London Com Domain Security
  slug: airport-pickups-london-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: airport-pickups-london-com-book-transfer
  slug: airport-pickups-london-com-book-transfer
slug: airport-pickups-london-com
tags:
- Company
- Airport
- Transport
- Taxi
- London
website: https://airport-pickups-london.com/
---
