---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Spacex Api Agentic Access
  operation_count: 26
  slug: spacex-api-agentic-access
  summary_line: 26 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX Dragon capsule data
  name: SpaceX API Capsules API
  slug: spacex-api-capsules-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX first stage booster core data
  name: SpaceX API Cores API
  slug: spacex-api-cores-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX astronaut crew data
  name: SpaceX API Crew API
  slug: spacex-api-crew-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX landing pad data
  name: SpaceX API Landing Pads API
  slug: spacex-api-landing-pads-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX mission launch data
  name: SpaceX API Launches API
  slug: spacex-api-launches-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX launch site data
  name: SpaceX API Launchpads API
  slug: spacex-api-launchpads-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX payload data
  name: SpaceX API Payloads API
  slug: spacex-api-payloads-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX Roadster tracking data
  name: SpaceX API Roadster API
  slug: spacex-api-roadster-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX rocket vehicle data
  name: SpaceX API Rockets API
  slug: spacex-api-rockets-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX fleet ship data
  name: SpaceX API Ships API
  slug: spacex-api-ships-api
- baseURL: https://api.spacexdata.com/v5
  baseurl_source: declared
  description: SpaceX Starlink satellite data
  name: SpaceX API Starlink API
  slug: spacex-api-starlink-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SpaceX Capsules API
  slug: open-spacex-api-capsules-api
- collection_type: open
  name: SpaceX Capsules Cores API
  slug: open-spacex-api-cores-api
- collection_type: open
  name: SpaceX Capsules Crew API
  slug: open-spacex-api-crew-api
- collection_type: open
  name: SpaceX Capsules Landing Pads API
  slug: open-spacex-api-landing-pads-api
- collection_type: open
  name: SpaceX Capsules Launches API
  slug: open-spacex-api-launches-api
- collection_type: open
  name: SpaceX Capsules Launchpads API
  slug: open-spacex-api-launchpads-api
- collection_type: open
  name: SpaceX Capsules Payloads API
  slug: open-spacex-api-payloads-api
- collection_type: open
  name: SpaceX Capsules Roadster API
  slug: open-spacex-api-roadster-api
- collection_type: open
  name: SpaceX Capsules Rockets API
  slug: open-spacex-api-rockets-api
- collection_type: open
  name: SpaceX Capsules Ships API
  slug: open-spacex-api-ships-api
- collection_type: open
  name: SpaceX Capsules Starlink API
  slug: open-spacex-api-starlink-api
- collection_type: open
  name: SpaceX API
  slug: open-spacex-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/r-spacex/SpaceX-API/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/r-spacex/SpaceX-API/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/r-spacex/SpaceX-API/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spacex-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spacex-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spacex-api-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spacex
- group: company
  title: ''
  type: Website
  url: https://www.spacex.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/r-spacex/SpaceX-API
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/r-spacex/SpaceX-API/blob/master/docs/v5/README.md
created: '2024-11-07'
description: The SpaceX API is an open-source REST API providing comprehensive data about SpaceX missions, rockets, capsules, cores, crew, launchpads, landing pads, payloads, and the Starlink satellite constellation. It offers endpoints for all past and upcoming launches, real-time mission data, and vehicle telemetry. No authentication is required.
examples:
- key_count: 4
  name: Spacex Api List Launches Example
  slug: spacex-api-list-launches-example
finops:
- name: Spacex Api Finops
  service_category: API
  slug: spacex-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spacex-api.png
json_schemas:
- name: SpaceX Launch
  property_count: 23
  slug: spacex-api-launch
json_structures:
- name: Spacex Api Launch Structure
  property_count: 0
  slug: spacex-api-launch-structure
jsonld:
- class_count: 17
  name: Spacex Api Context
  property_count: 15
  slug: spacex-api-context
layout: provider
modified: '2026-05-19'
name: SpaceX API
nav: Providers
network: true
overview: 'SpaceX API publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Capsules API, Cores API, Crew API, and 8 more. Tagged areas include Space, Aerospace, Launches, and SpaceX.


  The SpaceX API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SpaceX API''s developer surface includes GitHub presence, documentation, and 8 more developer resources.'
plans:
- name: Spacex Api Plans Pricing
  plan_count: 3
  slug: spacex-api-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Spacex Api Rate Limits
  slug: spacex-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SpaceX API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spacex-api-jsonschema-spectral-rules
- effective_rule_count: 8
  extends: []
  name: SpaceX API API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 4
  slug: spacex-api-rules
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 60.3
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spacex-api/refs/heads/main/screenshots/spacex-api-2026-06-20T194252.png
security:
- kind: domain-security
  name: Spacex Api Domain Security
  slug: spacex-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spacex Api Vulnerability Disclosure
  slug: spacex-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spacex-api
tags:
- Space
- Aerospace
- Launches
- SpaceX
website: https://www.spacex.com
---
