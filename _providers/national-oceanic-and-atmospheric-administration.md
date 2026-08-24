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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Oceanic And Atmospheric Administration Agentic Access
  operation_count: 1
  slug: national-oceanic-and-atmospheric-administration-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Retrieve observations and predictions from CO-OPS stations.
  name: National Oceanic and Atmospheric Administration Observations API
  slug: national-oceanic-and-atmospheric-administration-observations-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NOAA CO-OPS Data Observations API
  slug: open-national-oceanic-and-atmospheric-administration-observations-api
- collection_type: open
  name: NOAA CO-OPS Data API
  slug: open-national-oceanic-and-atmospheric-administration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-oceanic-and-atmospheric-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-oceanic-and-atmospheric-administration-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NOAAGov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/noaa
- group: company
  title: ''
  type: Website
  url: https://www.noaa.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.ncdc.noaa.gov/cdo-web/webservices/v2
- group: company
  title: ''
  type: Blog
  url: https://www.noaa.gov/rss.xml
created: '2024-12-03'
description: The National Oceanic and Atmospheric Administration (NOAA) is a federal agency within the U.S. Department of Commerce that focuses on monitoring and predicting changes in the Earth's environment, including climate, weather, oceans, and coasts.
finops:
- name: National Oceanic And Atmospheric Administration Finops
  service_category: API
  slug: national-oceanic-and-atmospheric-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-oceanic-and-atmospheric-administration.png
layout: provider
modified: '2026-05-19'
name: National Oceanic and Atmospheric Administration
nav: Providers
network: true
overview: 'National Oceanic and Atmospheric Administration publishes 1 API on the [APIs.io](https://apis.io/) network: Observations API. Tagged areas include Atmosphere, Federal-Government, Oceans, and Weather.


  National Oceanic and Atmospheric Administration''s developer surface includes developer portal, engineering blog, and 5 more developer resources.'
plans:
- name: National Oceanic And Atmospheric Administration Plans Pricing
  plan_count: 3
  slug: national-oceanic-and-atmospheric-administration-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: National Oceanic And Atmospheric Administration Rate Limits
  slug: national-oceanic-and-atmospheric-administration-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 21.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-oceanic-and-atmospheric-administration/refs/heads/main/screenshots/national-oceanic-and-atmospheric-administration-2026-06-20T190034.png
security:
- kind: domain-security
  name: National Oceanic And Atmospheric Administration Domain Security
  slug: national-oceanic-and-atmospheric-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-oceanic-and-atmospheric-administration
tags:
- Atmosphere
- Federal-Government
- Oceans
- Weather
website: https://www.noaa.gov/
---
