---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Natural Resources Conservation Service Agentic Access
  operation_count: 4
  slug: natural-resources-conservation-service-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: Soil Data Access (SDA) is a USDA-NRCS web service that supports ad hoc query and real-time delivery of official soil survey data (SSURGO and STATSGO2) for any user-defined geographic area. The service
  name: NRCS Soil Data Access
  slug: soil-data-access-api
- baseURL: https://sdmdataaccess.nrcs.usda.gov
  baseurl_source: declared
  description: The Query API from Natural Resources Conservation Service — 1 operation(s) for query.
  name: Natural Resources Conservation Service Query API
  slug: natural-resources-conservation-service-query-api
- baseURL: https://sdmdataaccess.nrcs.usda.gov
  baseurl_source: declared
  description: The SOAP API from Natural Resources Conservation Service — 1 operation(s) for soap.
  name: Natural Resources Conservation Service SOAP API
  slug: natural-resources-conservation-service-soap-api
- baseURL: https://sdmdataaccess.nrcs.usda.gov
  baseurl_source: declared
  description: The Spatial API from Natural Resources Conservation Service — 2 operation(s) for spatial.
  name: Natural Resources Conservation Service Spatial API
  slug: natural-resources-conservation-service-spatial-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USDA NRCS Soil Data Access Query API
  slug: open-natural-resources-conservation-service-query-api
- collection_type: open
  name: USDA NRCS Soil Data Access Query SOAP API
  slug: open-natural-resources-conservation-service-soap-api
- collection_type: open
  name: USDA NRCS Soil Data Access Query Spatial API
  slug: open-natural-resources-conservation-service-spatial-api
- collection_type: open
  name: USDA NRCS Soil Data Access
  slug: open-natural-resources-conservation-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/natural-resources-conservation-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/natural-resources-conservation-service-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USDA-NRCS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/natural-resources-conservation-service
- group: company
  title: ''
  type: Website
  url: https://www.nrcs.usda.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.nrcs.usda.gov/resources/data-and-reports
- group: other
  title: ''
  type: Data
  url: https://sdmdataaccess.nrcs.usda.gov
created: '2024-12-03'
description: The Natural Resources Conservation Service (NRCS) is a federal agency under the United States Department of Agriculture that works to help farmers, ranchers, and landowners conserve and protect natural resources. They provide technical assistance, financial assistance, and conservation planning to help individuals and communities implement conservation practices that improve soil health, water quality, and wildlife habitat.
finops:
- name: Natural Resources Conservation Service Finops
  service_category: API
  slug: natural-resources-conservation-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/natural-resources-conservation-service.png
layout: provider
modified: '2026-05-02'
name: Natural Resources Conservation Service
nav: Providers
network: true
overview: 'Natural Resources Conservation Service publishes 3 APIs on the [APIs.io](https://apis.io/) network: Query API, SOAP API, and Spatial API. Tagged areas include Federal-Government, Agriculture, Conservation, Soil, and Natural Resources.


  Natural Resources Conservation Service''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Natural Resources Conservation Service Plans Pricing
  plan_count: 3
  slug: natural-resources-conservation-service-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Natural Resources Conservation Service Rate Limits
  slug: natural-resources-conservation-service-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.6
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/natural-resources-conservation-service/refs/heads/main/screenshots/natural-resources-conservation-service-2026-06-20T190054.png
security:
- kind: domain-security
  name: Natural Resources Conservation Service Domain Security
  slug: natural-resources-conservation-service-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: natural-resources-conservation-service
tags:
- Federal-Government
- Agriculture
- Conservation
- Soil
- Natural Resources
website: https://www.nrcs.usda.gov
---
