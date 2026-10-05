---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bee Maps Agentic Access
  operation_count: 9
  slug: bee-maps-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: https://beemaps.com/api/developer
  baseurl_source: spec
  description: Account balance and usage
  name: Bee Maps Account API
  slug: bee-maps-account-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: spec
  description: AI-detected driving events with video
  name: Bee Maps AI Events API
  slug: bee-maps-ai-events-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: spec
  description: On-demand mapping requests
  name: Bee Maps Bursts API
  slug: bee-maps-bursts-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: spec
  description: Camera calibration data
  name: Bee Maps Devices API
  slug: bee-maps-devices-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: spec
  description: Street-level dashcam imagery
  name: Bee Maps Imagery API
  slug: bee-maps-imagery-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: spec
  description: ML-detected road objects
  name: Bee Maps Map Features API
  slug: bee-maps-map-features-api
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/agentic-access/bee-maps-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bee-maps-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/rules/bee-maps-rules.yml
  title: ''
  type: Spectral
  url: rules/bee-maps-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/json-ld/bee-maps-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bee-maps-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/vocabulary/bee-maps-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bee-maps-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/data-model/bee-maps-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bee-maps-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/errors/bee-maps-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bee-maps-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/conformance/bee-maps-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bee-maps-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/hosts/bee-maps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bee-maps-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/vendors/bee-maps-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bee-maps-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/security/bee-maps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bee-maps-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bee-maps/refs/heads/main/authentication/bee-maps-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bee-maps-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-09-27'
  detail: No API documentation or machine‑readable contract was found on the company's site or any discovered hosts.
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/company/bee-maps/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bee Maps is currently a stub entry in the API Evangelist catalog with no publicly available website or detailed information. The company appears in secondary-market harvest data but lacks an identifiable domain, API documentation, or official online presence. Consequently, the entry serves as a placeholder for future enrichment when verifiable resources become available.
jsonld:
- class_count: 8
  name: Bee Maps Context
  property_count: 37
  slug: bee-maps-context
layout: provider
modified: '2026-09-27'
name: Bee Maps
nav: Providers
network: true
overview: 'Bee Maps publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, AI Events API, Bursts API, and 3 more. Tagged areas include Company, Mapping, GIS, Location, and Data.


  The Bee Maps catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bee Maps'' developer surface includes authentication and 11 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Bee Maps API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: bee-maps-rules
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.8
    catalog_earned_first_party: 0.0
    catalog_gap: 73.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 56.3
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bee Maps Authentication
  slug: bee-maps-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Bee Maps Domain Security
  slug: bee-maps-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bee-maps
tags:
- Company
- Mapping
- GIS
- Location
- Data
website: https://www.nasdaqprivatemarket.com/
---
