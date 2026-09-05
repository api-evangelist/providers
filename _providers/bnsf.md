---
access_model:
  confidence: high
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bnsf Agentic Access
  operation_count: 2
  slug: bnsf-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: The BNSF Tracing API provides real-time shipment tracking from origin to destination for automotive VINs, carload railcars, intermodal units, and trains. Supports bulk queries of up to 300 vehicles or
  name: BNSF Tracing API
  slug: bnsf-tracing-api
- description: The BNSF Hub Operations API provides access to intermodal facility data including container and trailer delivery details, storage locations, driver pickup and delivery information, dray bookings, gate
  name: BNSF Hub Operations API
  slug: bnsf-hub-operations-api
- description: The BNSF Pricing & Rates API provides access to freight shipping prices and rates for both carload and intermodal shipments, enabling customers to obtain BNSF shipping costs programmatically.
  name: BNSF Pricing & Rates API
  slug: bnsf-pricing-rates-api
- description: The BNSF Schedules API provides intermodal transit schedules enabling customers to view planned departure and arrival times to help schedule freight shipments across the BNSF rail network.
  name: BNSF Schedules API
  slug: bnsf-schedules-api
- description: The BNSF Waybill Management API enables customers to submit bills of lading with transit details and retrieve submissions for carload shipments. Supports electronic submission and retrieval of waybill
  name: BNSF Waybill Management API
  slug: bnsf-waybill-management-api
- baseURL: https://api.bnsf.com:6443
  baseurl_source: spec
  description: The BNSF Reference Files API provides access to reference data including city names, commodity descriptions (STCC codes), station data, event codes, and hazardous materials information used in freight
  name: BNSF Reference Files API
  slug: bnsf-reference-files-api
- baseURL: https://api.bnsf.com:6443
  baseurl_source: spec
  description: The Diagnostics API from BNSF — 1 operation(s) for diagnostics.
  name: BNSF Diagnostics API
  slug: bnsf-diagnostics-api
- baseURL: https://api.bnsf.com:6443
  baseurl_source: spec
  description: The Reference Files API from BNSF — 1 operation(s) for reference files.
  name: BNSF Reference Files API
  slug: bnsf-reference-files-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BNSF Customer Diagnostics API
  slug: open-bnsf-diagnostics-api
- collection_type: open
  name: BNSF Customer Diagnostics Reference Files API
  slug: open-bnsf-reference-files-api
- collection_type: open
  name: BNSF Customer API
  slug: open-bnsf
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bnsf-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bnsf-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bnsf-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bnsf-railway
- group: company
  title: ''
  type: Website
  url: https://www.bnsf.com
- group: start
  title: ''
  type: Portal
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
- group: start
  title: ''
  type: Console
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/developers-console/
- group: operate
  title: ''
  type: Support
  url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/support/
created: '2025-02-06'
description: BNSF Railway, a subsidiary of Berkshire Hathaway Inc., is one of the largest freight railroad networks in North America. The company operates an extensive network of over 32,000 route miles in 28 states and three Canadian provinces, serving major markets in the United States and connecting with Mexico through rail lines in Texas.
finops:
- name: Bnsf Finops
  service_category: API
  slug: bnsf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bnsf.png
layout: provider
modified: '2026-04-21'
name: BNSF
nav: Providers
network: true
overview: 'BNSF publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Reference Files API, Diagnostics API, and 1 more. Tagged areas include Freight, Railroad, Shipping, Trains, and Intermodal.


  BNSF''s developer surface includes authentication, developer portal, documentation, developer console, support, and 4 more developer resources.'
plans:
- name: Bnsf Plans Pricing
  plan_count: 3
  slug: bnsf-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Bnsf Rate Limits
  slug: bnsf-rate-limits
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bnsf/refs/heads/main/screenshots/bnsf-2026-06-20T173544.png
security:
- kind: authentication
  name: Bnsf Authentication
  slug: bnsf-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Bnsf Domain Security
  slug: bnsf-domain-security
  summary_line: TLSv1.2 · DMARC
slug: bnsf
tags:
- Freight
- Railroad
- Shipping
- Trains
- Intermodal
- Logistics
website: https://www.bnsf.com
---
