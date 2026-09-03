---
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-09-02'
api_count: 2
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
artifact_total: 4
common:
- group: other
  title: ''
  type: APIsJSON
  url: well-known/lookip-provider-apis.json
- group: agent
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
modified: '2026-08-26'
name: Lookip
nav: Providers
network: true
overview: 'Lookip publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ASN API, Batch API, Lookup API, and 1 more. Tagged areas include IP Lookup, Geolocation, ASN, and Proxy Detection.


  Lookip''s developer surface includes signup flow and 6 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 85.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 60.2
    developer_ergonomics: 40.5
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 36.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lookip/refs/heads/main/screenshots/lookip-2026-09-02T150318.png
slug: lookip
tags:
- IP Lookup
- Geolocation
- ASN
- Proxy Detection
website: https://lookip.io
---
