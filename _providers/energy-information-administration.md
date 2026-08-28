---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Energy Information Administration Agentic Access
  operation_count: 13
  slug: energy-information-administration-agentic-access
  summary_line: 13 operations
api_count: 10
apis:
- description: CO2 emissions aggregates by state and sector.
  name: Energy Information Administration CO2 Emissions API
  slug: energy-information-administration-co2-emissions-api
- description: Coal production, shipments, consumption, and trade data.
  name: Energy Information Administration Coal API
  slug: energy-information-administration-coal-api
- description: Browse the API tree to discover available routes, facets, and metadata.
  name: Energy Information Administration Discovery API
  slug: energy-information-administration-discovery-api
- description: Electricity generation, retail sales, and balancing authority data.
  name: Energy Information Administration Electricity API
  slug: energy-information-administration-electricity-api
- description: International energy statistics and projections.
  name: Energy Information Administration International API
  slug: energy-information-administration-international-api
- description: Natural gas production, prices, storage, and trade data.
  name: Energy Information Administration Natural Gas API
  slug: energy-information-administration-natural-gas-api
- description: Nuclear plant generator outage data.
  name: Energy Information Administration Nuclear API
  slug: energy-information-administration-nuclear-api
- description: Crude oil reserves, refining, consumption, and stocks data.
  name: Energy Information Administration Petroleum API
  slug: energy-information-administration-petroleum-api
- description: State Energy Data System.
  name: Energy Information Administration SEDS API
  slug: energy-information-administration-seds-api
- description: Comprehensive energy summaries across all sources.
  name: Energy Information Administration Total Energy API
  slug: energy-information-administration-total-energy-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions API
  slug: open-energy-information-administration-co2-emissions-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions Coal API
  slug: open-energy-information-administration-coal-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions Discovery API
  slug: open-energy-information-administration-discovery-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions Electricity API
  slug: open-energy-information-administration-electricity-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions International API
  slug: open-energy-information-administration-international-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions Natural Gas API
  slug: open-energy-information-administration-natural-gas-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions Nuclear API
  slug: open-energy-information-administration-nuclear-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data API
  slug: open-energy-information-administration-open-data-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions Petroleum API
  slug: open-energy-information-administration-petroleum-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions SEDS API
  slug: open-energy-information-administration-seds-api
- collection_type: open
  name: U.S. Energy Information Administration Open Data CO2 Emissions Total Energy API
  slug: open-energy-information-administration-total-energy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/energy-information-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energy-information-administration-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/energy-information-administration-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eiagov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-energy-information-administration
- group: company
  title: ''
  type: Website
  url: https://www.eia.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.eia.gov/opendata/
- group: other
  title: ''
  type: API Browser
  url: https://www.eia.gov/opendata/browser/
- group: start
  title: ''
  type: Signup
  url: https://www.eia.gov/opendata/register.php
- group: other
  title: ''
  type: Bulk Downloads
  url: https://www.eia.gov/opendata/bulkfiles.php
- group: other
  title: ''
  type: Excel Add-in
  url: https://www.eia.gov/opendata/excel/
- group: company
  title: ''
  type: Blog
  url: https://www.eia.gov/rss/todayinenergy.xml
created: '2024-12-03'
description: The U.S. Energy Information Administration (EIA) is committed to its free and open data by making it available through an Application Programming Interface (API) and its open data tools. The EIA Open Data API v2 is multi-faceted and contains time-series datasets organized by the main energy categories, including electricity, natural gas, petroleum, coal, nuclear, renewables, total energy, international energy statistics, the State Energy Data System (SEDS), and CO2 emissions aggregates.
finops:
- name: Energy Information Administration Finops
  service_category: API
  slug: energy-information-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energy-information-administration.png
layout: provider
modified: '2026-05-19'
name: Energy Information Administration
nav: Providers
network: true
overview: 'Energy Information Administration publishes 10 APIs on the [APIs.io](https://apis.io/) network, including CO2 Emissions API, Coal API, Discovery API, and 7 more. Tagged areas include Energy, Federal-Government, and Open Data.


  Energy Information Administration''s developer surface includes authentication, documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Energy Information Administration Plans Pricing
  plan_count: 3
  slug: energy-information-administration-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Energy Information Administration Rate Limits
  slug: energy-information-administration-rate-limits
score:
  band: thin
  composite: 31.6
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/energy-information-administration/refs/heads/main/screenshots/energy-information-administration-2026-06-20T180702.png
security:
- kind: authentication
  name: Energy Information Administration Authentication
  slug: energy-information-administration-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Energy Information Administration Domain Security
  slug: energy-information-administration-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: energy-information-administration
tags:
- Energy
- Federal-Government
- Open Data
website: https://www.eia.gov
---
