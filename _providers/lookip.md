---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.lookip.io
  baseurl_source: declared
  description: Public ASN directory. No key, no credit.
  name: Lookip ASN API
  slug: lookip-asn-api
- baseURL: https://api.lookip.io
  baseurl_source: declared
  description: Up to 100 addresses per call.
  name: Lookip Batch API
  slug: lookip-batch-api
- baseURL: https://api.lookip.io
  baseurl_source: declared
  description: Single-address lookups.
  name: Lookip Lookup API
  slug: lookip-lookup-api
- baseURL: https://api.lookip.io
  baseurl_source: declared
  description: Service index, liveness and this document.
  name: Lookip Service API
  slug: lookip-service-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/lookip/well-known/lookip-provider-apis.json
  title: ''
  type: APIsJSON
  url: well-known/lookip-provider-apis.json
- group: agent
  href: https://artifacts.apis.io/lookip/llms/lookip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lookip-llms.txt
- group: company
  title: ''
  type: Website
  url: https://lookip.io
- group: commercial
  title: ''
  type: Plans
  url: https://lookip.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://lookip.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lookip.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lookip.io/legal/privacy
created: '2026-08-26'
description: Lookip is an IP and domain intelligence API — geolocation, network and ASN, hosting and proxy detection, and related lookups over a single authenticated surface. The contract is an OpenAPI 3.1.1 document of 18 paths and 24 schemas served from api.lookip.io with bearer authentication.
layout: provider
mcp_servers:
- description: Remote MCP server at api.lookip.io over HTTP; 5 tools listed.
  name: Lookip MCP Server
  slug: lookip
modified: '2026-08-26'
name: Lookip
nav: Providers
network: true
overview: 'Lookip publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including ASN API, Batch API, Lookup API, and 1 more. Tagged areas include IP Lookup, Geolocation, ASN, and Proxy Detection.


  The Lookip catalog on APIs.io includes 1 Spectral governance ruleset.


  Lookip''s developer surface includes signup flow and 6 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Lookip API Rules
  rule_count: 69
  severity_counts:
    error: 66
    hint: 0
    info: 2
    warn: 1
  slug: lookip-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 57.5
    developer_ergonomics: 40.5
    discoverability: 63.3
    operational_transparency: 0.0
  previous_composite: 34.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lookip/lookip-2026-09-02T150318.png
slug: lookip
tags:
- IP Lookup
- Geolocation
- ASN
- Proxy Detection
website: https://lookip.io
---
