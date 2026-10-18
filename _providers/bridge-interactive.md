---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bridge Interactive Agentic Access
  operation_count: 14
  slug: bridge-interactive-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- baseURL: https://api.bridgedataoutput.com/api/v2
  baseurl_source: declared
  description: The Agents API from Bridge Interactive — 2 operation(s) for agents.
  name: Bridge Interactive Agents API
  slug: bridge-interactive-agents-api
- baseURL: https://api.bridgedataoutput.com/api/v2
  baseurl_source: declared
  description: The Listings API from Bridge Interactive — 2 operation(s) for listings.
  name: Bridge Interactive Listings API
  slug: bridge-interactive-listings-api
- baseURL: https://api.bridgedataoutput.com/api/v2
  baseurl_source: declared
  description: The Offices API from Bridge Interactive — 2 operation(s) for offices.
  name: Bridge Interactive Offices API
  slug: bridge-interactive-offices-api
- baseURL: https://api.bridgedataoutput.com/api/v2
  baseurl_source: declared
  description: The Open Houses API from Bridge Interactive — 1 operation(s) for open houses.
  name: Bridge Interactive Open Houses API
  slug: bridge-interactive-open-houses-api
- baseURL: https://api.bridgedataoutput.com/api/v2
  baseurl_source: declared
  description: The RESO Web API API from Bridge Interactive — 7 operation(s) for reso web api.
  name: Bridge Interactive RESO Web API
  slug: bridge-interactive-reso-web-api-api
- baseURL: https://api.bridgedataoutput.com/api/v2/OData
  baseurl_source: declared
  description: The Webhooks API from Bridge — 3 operation(s) for webhooks.
  name: Bridge Interactive Webhooks API
  slug: bridge-interactive-webhooks-api
- baseURL: https://api.bridgedataoutput.com/api/v2/OData
  baseurl_source: declared
  description: RESO Property resource (listings)
  name: Bridge Interactive Property API
  slug: bridge-interactive-property-api
- baseURL: https://api.bridgedataoutput.com/api/v2/OData
  baseurl_source: declared
  description: RESO Member resource (agents)
  name: Bridge Interactive Member API
  slug: bridge-interactive-member-api
- baseURL: https://api.bridgedataoutput.com/api/v2/OData
  baseurl_source: declared
  description: RESO Office resource (brokerages)
  name: Bridge Interactive Office API
  slug: bridge-interactive-office-api
- description: Zillow Group Data feeds delivered through Bridge — parcels, assessments, transactions, and Zillow Group Econ Data (ZHVI, ZORI, market metrics) — accessible via the same OData/RESO Web API surface as M
  name: Zillow Group Data (ZG Data) API
  slug: bridge-interactive-zillow-group-data-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bridge API (Bridge Data Output) Agents API
  slug: open-bridge-interactive-agents-api
- collection_type: open
  name: Bridge API (Bridge Data Output) Agents Listings API
  slug: open-bridge-interactive-listings-api
- collection_type: open
  name: Bridge API (Bridge Data Output) Agents Offices API
  slug: open-bridge-interactive-offices-api
- collection_type: open
  name: Bridge API (Bridge Data Output) Agents Open Houses API
  slug: open-bridge-interactive-open-houses-api
- collection_type: open
  name: Bridge API (Bridge Data Output) Agents RESO Web API API
  slug: open-bridge-interactive-reso-web-api-api
- collection_type: open
  name: Bridge API (Bridge Data Output)
  slug: open-bridge-interactive
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/rules/bridge-interactive-rules.yml
  title: ''
  type: Spectral
  url: rules/bridge-interactive-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/vocabulary/bridge-interactive-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bridge-interactive-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/data-model/bridge-interactive-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bridge-interactive-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/errors/bridge-interactive-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bridge-interactive-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/conformance/bridge-interactive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bridge-interactive-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/integrations/bridge-interactive-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/bridge-interactive-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/capabilities/bridge-interactive-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bridge-interactive-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/agentic-access/bridge-interactive-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bridge-interactive-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/security/bridge-interactive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridge-interactive-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/authentication/bridge-interactive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bridge-interactive-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bridge-interactive
- group: company
  title: ''
  type: Website
  url: https://www.bridgeinteractive.com
- group: docs
  title: ''
  type: Documentation
  url: https://bridgedataoutput.com/docs/platform/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/plans/bridge-interactive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bridge-interactive-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/rate-limits/bridge-interactive-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bridge-interactive-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/finops/bridge-interactive-finops.yml
  title: ''
  type: FinOps
  url: finops/bridge-interactive-finops.yml
created: '2026-06-21'
description: Bridge Interactive (a Zillow Group company) is a real-estate data-access platform that normalizes MLS listing data to RESO standards and serves it through the Bridge API. The Bridge Data Output platform exposes a proprietary RESTful Bridge Web API and a RESO-compliant RESO Web API (OData) for properties, members, offices, open houses, and media, all secured with a Bearer server token.
finops:
- has_sources: true
  method: generated
  name: Bridge Interactive Finops
  primary_unit: ''
  service_category: Analytics and Data
  slug: bridge-interactive-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bridge-interactive.png
json_schemas:
- name: Bundle
  property_count: 4
  slug: bridge-interactive-bundle
- name: ODataCollection
  property_count: 3
  slug: bridge-interactive-odata-collection
- name: SingleResource
  property_count: 3
  slug: bridge-interactive-single-resource
- name: Bridge RESO Member
  property_count: 23
  slug: bridge-member
- name: Bridge RESO Property
  property_count: 51
  slug: bridge-property
jsonld:
- class_count: 31
  name: Bridge Interactive Context
  property_count: 1
  slug: bridge-interactive-context
layout: provider
modified: '2026-09-16'
name: Bridge Interactive
nav: Providers
network: true
overview: 'Bridge Interactive publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Listings API, Offices API, and 7 more. Tagged areas include Real Estate, MLS, RESO, Listings, and Property Data.


  The Bridge Interactive catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bridge Interactive''s developer surface includes authentication, documentation, and 14 more developer resources.'
plans:
- name: Bridge Interactive Plans Pricing
  plan_count: 3
  slug: bridge-interactive-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Bridge Interactive Rate Limits
  slug: bridge-interactive-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bridge Interactive API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: bridge-interactive-rules
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 7.9
    contract_governance: 19.7
    contract_quality: 59.9
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/bridge-interactive/refs/heads/main/screenshots/bridge-interactive-2026-07-25T203811.png
security:
- kind: authentication
  name: Bridge Interactive Authentication
  slug: bridge-interactive-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bridge Interactive Domain Security
  slug: bridge-interactive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bridge-interactive
tags:
- Real Estate
- MLS
- RESO
- Listings
- Property Data
website: https://www.bridgeinteractive.com
---
