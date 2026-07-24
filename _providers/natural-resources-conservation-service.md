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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Natural Resources Conservation Service Agentic Access
  operation_count: 4
  slug: natural-resources-conservation-service-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 4
apis:
- description: Soil Data Access (SDA) is a USDA-NRCS web service that supports ad hoc query and real-time delivery of official soil survey data (SSURGO and STATSGO2) for any user-defined geographic area. The service
  name: NRCS Soil Data Access
  slug: soil-data-access-api
- description: The Query API from Natural Resources Conservation Service — 1 operation(s) for query.
  name: Natural Resources Conservation Service Query API
  slug: natural-resources-conservation-service-query-api
- description: The SOAP API from Natural Resources Conservation Service — 1 operation(s) for soap.
  name: Natural Resources Conservation Service SOAP API
  slug: natural-resources-conservation-service-soap-api
- description: The Spatial API from Natural Resources Conservation Service — 2 operation(s) for spatial.
  name: Natural Resources Conservation Service Spatial API
  slug: natural-resources-conservation-service-spatial-api
artifact_total: 10
collections:
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
overview: 'Natural Resources Conservation Service publishes 3 APIs on the [APIs.io](https://apis.io/) network: Query API, SOAP API, and Spatial API. Tagged areas include Federal Government, Agriculture, Conservation, Soil, and Natural Resources.


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
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.6
    developer_ergonomics: 8.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/natural-resources-conservation-service/refs/heads/main/screenshots/natural-resources-conservation-service-2026-06-20T190054.png
security:
- kind: domain-security
  name: Natural Resources Conservation Service Domain Security
  slug: natural-resources-conservation-service-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: natural-resources-conservation-service
tags:
- Federal Government
- Agriculture
- Conservation
- Soil
- Natural Resources
website: https://www.nrcs.usda.gov
---
