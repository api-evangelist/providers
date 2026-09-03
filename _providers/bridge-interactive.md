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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
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
  name: Bridge Interactive RESO Web API API
  slug: bridge-interactive-reso-web-api-api
artifact_total: 18
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bridge-interactive-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bridge-interactive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bridge-interactive-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/bridge-interactive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bridge-interactive-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bridge-interactive-finops.yml
created: '2026-06-21'
description: Bridge Interactive (a Zillow Group company) is a real-estate data-access platform that normalizes MLS listing data to RESO standards and serves it through the Bridge API. The Bridge Data Output platform exposes a proprietary RESTful Bridge Web API and a RESO-compliant RESO Web API (OData) for properties, members, offices, open houses, and media, all secured with a Bearer server token.
finops:
- name: Bridge Interactive Finops
  service_category: Analytics and Data
  slug: bridge-interactive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bridge-interactive.png
layout: provider
modified: '2026-06-21'
name: Bridge Interactive
nav: Providers
network: true
overview: 'Bridge Interactive publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Listings API, Offices API, and 2 more. Tagged areas include Real-Estate, MLS, RESO, Listings, and Property Data.


  Bridge Interactive''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Bridge Interactive Plans Pricing
  plan_count: 3
  slug: bridge-interactive-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Bridge Interactive Rate Limits
  slug: bridge-interactive-rate-limits
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- Real-Estate
- MLS
- RESO
- Listings
- Property Data
website: https://www.bridgeinteractive.com
---
