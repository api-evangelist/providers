---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Vincario Agentic Access
  operation_count: 16
  slug: vincario-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- baseURL: https://api.vincario.com/3.2
  baseurl_source: declared
  description: Decode a VIN into a vehicle specification (VIN Decode) and list which fields can be decoded for a VIN (VIN Decode Info).
  name: Vincario VIN Decoder API
  slug: vincario-vin-decoder-api
- baseURL: https://api.vincario.com/3.2
  baseurl_source: declared
  description: Look up manufacturer (OEM) data for a VIN.
  name: Vincario OEM VIN Lookup API
  slug: vincario-oem-vin-lookup-api
- baseURL: https://api.vincario.com/3.2
  baseurl_source: declared
  description: Retrieve manufacturer (OEM) service history for a VIN.
  name: Vincario OEM Service History API
  slug: vincario-oem-service-history-api
- baseURL: https://api.vincario.com/3.2
  baseurl_source: declared
  description: Estimate the market value of a vehicle by VIN.
  name: Vincario Vehicle Market Value API
  slug: vincario-vehicle-market-value-api
- baseURL: https://api.vincario.com/3.2
  baseurl_source: declared
  description: Check whether a VIN appears in supported stolen-vehicle databases.
  name: Vincario Stolen Check API
  slug: vincario-stolen-check-api
- baseURL: https://api.vincario.com/3.2
  baseurl_source: declared
  description: Return the remaining credit balance of the account.
  name: Vincario Credit Balance API
  slug: vincario-get-balance-api
- baseURL: https://api.vincario.com/3.2
  baseurl_source: declared
  description: Value lists for vehicle makes, models, make and model combinations, body, color, drive, fuel, product type and transmission.
  name: Vincario Enums API
  slug: vincario-enums-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vincario/refs/heads/main/agentic-access/vincario-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vincario-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vincario/refs/heads/main/security/vincario-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vincario-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vincario/refs/heads/main/security/vincario-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vincario-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vincario/refs/heads/main/authentication/vincario-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vincario-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vincario
- group: company
  title: ''
  type: Website
  url: https://vincario.com
- group: docs
  title: ''
  type: Documentation
  url: https://vincario.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://vincario.com/api-docs/3.2/
- group: docs
  title: ''
  type: OpenAPI
  url: https://vincario.com/api-docs/openapi/3.2
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vincario/refs/heads/main/mcp/vincario-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vincario-mcp.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Vincario/MCP-vincario
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vincario/refs/heads/main/plans/vincario-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vincario-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vincario/refs/heads/main/rate-limits/vincario-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vincario-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vincario/refs/heads/main/finops/vincario-finops.yml
  title: ''
  type: FinOps
  url: finops/vincario-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://vincario.com/blog/feed/
created: '2026-06-21'
description: Vincario (vincario.com, formerly vindecoder.eu) provides a REST API, currently version 3.2, that decodes a Vehicle Identification Number (VIN) into a vehicle specification and provides OEM VIN lookup, OEM service history, vehicle market value, stolen-vehicle checks, value lists (enums) for makes, models and other attributes, and the account credit balance. Requests are authenticated with an API key plus a control sum in the URL path. Vincario also runs a public MCP server (com.vincario/vehicle-data) and offers VIN OCR scanning and UK license plate lookup services, whose APIs are not yet publicly documented.
finops:
- has_sources: true
  method: generated
  name: Vincario Finops
  primary_unit: ''
  service_category: Data and Analytics
  slug: vincario-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vincario.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.vincario.com over streamable HTTP; 4 tools listed.
  name: Vincario MCP server (com.vincario/vehicle-data, https://mcp.vincario.com/mcp)
  slug: com-vincario-vehicle-data
modified: '2026-10-06'
name: Vincario
nav: Providers
network: true
overview: 'Vincario publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including VIN Decoder API, OEM VIN Lookup API, OEM Service History API, and 4 more. Tagged areas include VIN, Vehicle Data, Automotive, VIN Decoder, and Market Value.


  Vincario''s developer surface includes authentication, documentation, API reference, engineering blog, and 11 more developer resources.'
plans:
- name: Vincario Plans Pricing
  plan_count: 5
  slug: vincario-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Vincario Rate Limits
  slug: vincario-rate-limits
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 48.4
    developer_ergonomics: 31.0
    discoverability: 68.3
    operational_transparency: 10.5
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/vincario/refs/heads/main/screenshots/vincario-2026-09-02T165927.png
security:
- kind: authentication
  name: Vincario Authentication
  slug: vincario-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vincario Domain Security
  slug: vincario-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Vincario Vulnerability Disclosure
  slug: vincario-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vincario
tags:
- VIN
- Vehicle Data
- Automotive
- VIN Decoder
- Market Value
website: https://vincario.com
---
