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
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Airportloungelist Com Agentic Access
  operation_count: 12
  slug: airportloungelist-com-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://airportloungelist.com/api/v1
  baseurl_source: declared
  description: The Access API from Airport Lounge List — 2 operation(s) for access.
  name: Airport Lounge List Access API
  slug: airportloungelist-com-access-api
- baseURL: https://airportloungelist.com/api/v1
  baseurl_source: declared
  description: The Airports API from Airport Lounge List — 4 operation(s) for airports.
  name: Airport Lounge List Airports API
  slug: airportloungelist-com-airports-api
- baseURL: https://airportloungelist.com/api/v1
  baseurl_source: declared
  description: The Lounges API from Airport Lounge List — 4 operation(s) for lounges.
  name: Airport Lounge List Lounges API
  slug: airportloungelist-com-lounges-api
- baseURL: https://airportloungelist.com/api/v1
  baseurl_source: declared
  description: The Networks API from Airport Lounge List — 2 operation(s) for networks.
  name: Airport Lounge List Networks API
  slug: airportloungelist-com-networks-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/airportloungelist-com/agentic-access/airportloungelist-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/airportloungelist-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/airportloungelist-com/rules/airportloungelist-com-rules.yml
  title: ''
  type: Spectral
  url: rules/airportloungelist-com-rules.yml
- group: auth
  href: https://artifacts.apis.io/airportloungelist-com/authentication/airportloungelist-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airportloungelist-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/airportloungelist-com/errors/airportloungelist-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/airportloungelist-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/airportloungelist-com/conformance/airportloungelist-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airportloungelist-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/airportloungelist-com/llms/airportloungelist-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airportloungelist-com-llms.txt
- group: other
  href: https://artifacts.apis.io/airportloungelist-com/a2a/airportloungelist-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/airportloungelist-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/airportloungelist-com/well-known/airportloungelist-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airportloungelist-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/airportloungelist-com/hosts/airportloungelist-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airportloungelist-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/airportloungelist-com/vendors/airportloungelist-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/airportloungelist-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airportloungelist.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://airportloungelist.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airportloungelist.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://airportloungelist.com/guides/united-club
- group: company
  title: ''
  type: Blog
  url: https://airportloungelist.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://airportloungelist.com/setup
- group: auth
  href: https://artifacts.apis.io/airportloungelist-com/security/airportloungelist-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airportloungelist-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airportloungelist.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://airportloungelist.com/openapi.json
  - status: 401
    url: https://airportloungelist.com/mcp
  - status: 200
    url: https://airportloungelist.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Airport Lounge List provides a comprehensive platform to search and compare over 2,600 airport lounges across more than 870 airports worldwide. Users can explore lounge amenities, access options through Priority Pass, LoungeKey, credit cards, day passes, and membership programs. The service includes detailed reviews, photos, and up‑to‑date information to help travelers choose the best lounge experience for their needs.
image: https://og-image-api.merchantai.workers.dev/?subtitle=Find+Airport+Lounges+Worldwide&template=aviation&title=Airport+Lounge+List&type=og
layout: provider
modified: '2026-11-01'
name: Airport Lounge List
nav: Providers
network: true
overview: 'Airport Lounge List publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, Airports API, Lounges API, and 1 more. Tagged areas include Airport, Travel, Lounge, Aviation, and Comparison.


  The Airport Lounge List catalog on APIs.io includes 1 Spectral governance ruleset.


  Airport Lounge List''s developer surface includes authentication, support, documentation, engineering blog, getting-started guide, and 13 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Airport Lounge List API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: airportloungelist-com-rules
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
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
  name: Airportloungelist Com Authentication
  slug: airportloungelist-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Airportloungelist Com Domain Security
  slug: airportloungelist-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: airportloungelist-com
tags:
- Airport
- Travel
- Lounge
- Aviation
- Comparison
- Company
website: https://airportloungelist.com/
---
