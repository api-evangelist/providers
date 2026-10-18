---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Roote Agentic Access
  operation_count: 20
  slug: roote-agentic-access
  summary_line: 20 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Capabilities API from ROOTE — 1 operation(s) for capabilities.
  name: ROOTE Capabilities API
  slug: roote-capabilities-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Changelog.json API from ROOTE — 1 operation(s) for changelog.json.
  name: ROOTE Changelog.json API
  slug: roote-changelog-json-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Charging API from ROOTE — 1 operation(s) for charging.
  name: ROOTE Charging API
  slug: roote-charging-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Geocode API from ROOTE — 1 operation(s) for geocode.
  name: ROOTE Geocode API
  slug: roote-geocode-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Health API from ROOTE — 1 operation(s) for health.
  name: ROOTE Health API
  slug: roote-health-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Mobility API from ROOTE — 1 operation(s) for mobility.
  name: ROOTE Mobility API
  slug: roote-mobility-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Nearby API from ROOTE — 1 operation(s) for nearby.
  name: ROOTE Nearby API
  slug: roote-nearby-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Openapi.json API from ROOTE — 1 operation(s) for openapi.json.
  name: ROOTE Openapi.json API
  slug: roote-openapi-json-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Parking API from ROOTE — 1 operation(s) for parking.
  name: ROOTE Parking API
  slug: roote-parking-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Place Search API from ROOTE — 1 operation(s) for place search.
  name: ROOTE Place Search API
  slug: roote-place-search-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Reverse Geocode API from ROOTE — 1 operation(s) for reverse geocode.
  name: ROOTE Reverse Geocode API
  slug: roote-reverse-geocode-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Ride Hailing API from ROOTE — 1 operation(s) for ride hailing.
  name: ROOTE Ride Hailing API
  slug: roote-ride-hailing-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Services API from ROOTE — 1 operation(s) for services.
  name: ROOTE Services API
  slug: roote-services-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Transit API from ROOTE — 5 operation(s) for transit.
  name: ROOTE Transit API
  slug: roote-transit-api
- baseURL: https://api.roote.ai
  baseurl_source: declared
  description: The Usage API from ROOTE — 1 operation(s) for usage.
  name: ROOTE Usage API
  slug: roote-usage-api
artifact_total: 20
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/agentic-access/roote-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/roote-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/rules/roote-rules.yml
  title: ''
  type: Spectral
  url: rules/roote-rules.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/changelog/roote-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/roote-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/authentication/roote-authentication.yml
  title: ''
  type: Authentication
  url: authentication/roote-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/errors/roote-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/roote-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/conformance/roote-conformance.yml
  title: ''
  type: Conformance
  url: conformance/roote-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/llms/roote-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/roote-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/mcp/roote-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/roote-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/hosts/roote-hosts.yml
  title: ''
  type: Hosts
  url: hosts/roote-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/vendors/roote-vendors.yml
  title: ''
  type: Vendors
  url: vendors/roote-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.roote.ai\\\
- group: docs
  title: ''
  type: APIReference
  url: https://doc.roote.ai/resources/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/roote/refs/heads/main/security/roote-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/roote-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://roote.ai
- group: docs
  title: ''
  type: Documentation
  url: https://doc.roote.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.roote.ai/getting-started
created: '2026-10-05'
description: ROOTE provides a French-language mobility platform that offers live mobility data, geocoding, nearby transport options, and urban services via a REST API. The service targets developers building AI agents, mobile apps, and location‑based products, delivering real‑time information on transport options, routes, and availability across multiple cities.
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.roote.ai.
  name: ROOTE MCP Server
  slug: roote-mcp-yml
modified: '2026-10-05'
name: ROOTE
nav: Providers
network: true
overview: 'ROOTE publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Capabilities API, Changelog.json API, Charging API, and 12 more. Tagged areas include Mobility, French, Artificial Intelligence, and Transportation.


  The ROOTE catalog on APIs.io includes 1 Spectral governance ruleset.


  ROOTE''s developer surface includes changelog, authentication, API reference, documentation, getting-started guide, and 12 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: ROOTE API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 4
    warn: 1
  slug: roote-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 47.5
    developer_ergonomics: 51.8
    discoverability: 63.3
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Roote Authentication
  slug: roote-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Roote Domain Security
  slug: roote-domain-security
  summary_line: TLSv1.3 · HSTS
slug: roote
tags:
- Mobility
- French
- Artificial Intelligence
- Transportation
website: https://roote.ai
---
