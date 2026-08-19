---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pangaea Agentic Access
  operation_count: 6
  slug: pangaea-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 9
apis:
- description: REST service for retrieving tabular dataset data filtered by dataset DOI and parameter values. Supports column selection, value filtering with range queries, and multiple filter criteria with AND/OR l
  name: PANGAEA Data Download Service - Filter by DOI
  slug: pangaea-data-download-service-filter-by-doi
- description: REST service for retrieving geoscientific measurements filtered by geographic bounding box, temporal range, depth constraints, and PANGAEA parameter IDs. Ideal for extracting cross-dataset measurement
  name: PANGAEA Data Download Service - Filter by Geo Parameters
  slug: pangaea-data-download-service-filter-by-geo-parameters
- description: OGC-compliant Web Map Service providing bathymetric (ocean depth) map layers for integration into GIS software. Hosted by AWI and based on PANGAEA bathymetry data collected from scientific expeditions
  name: PANGAEA Bathymetry WMS
  slug: pangaea-bathymetry-wms
- description: Elasticsearch-backed REST API for querying PANGAEA's controlled vocabulary and term dictionary used for classifying datasets by topic, parameter, and method.
  name: PANGAEA Term Dictionary API
  slug: pangaea-term-dictionary-api
- description: Filter dataset data by DOI and parameter values
  name: PANGAEA DOI Filter API
  slug: pangaea-doi-filter-api
- description: Filter cross-dataset data by geographic and temporal constraints
  name: PANGAEA Geo Filter API
  slug: pangaea-geo-filter-api
- description: Open Archives Initiative Protocol for Metadata Harvesting 2.0
  name: PANGAEA OAI-PMH API
  slug: pangaea-oai-pmh-api
- description: Full-text and faceted dataset search
  name: PANGAEA Search API
  slug: pangaea-search-api
- description: Controlled vocabulary and term dictionary
  name: PANGAEA Terms API
  slug: pangaea-terms-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PANGAEA Data Download Services DOI Filter API
  slug: open-pangaea-doi-filter-api
- collection_type: open
  name: PANGAEA Data Download Services DOI Filter Geo Filter API
  slug: open-pangaea-geo-filter-api
- collection_type: open
  name: PANGAEA Data Download Services DOI Filter OAI-PMH API
  slug: open-pangaea-oai-pmh-api
- collection_type: open
  name: PANGAEA Data Download Services DOI Filter Search API
  slug: open-pangaea-search-api
- collection_type: open
  name: PANGAEA Data Download Services DOI Filter Terms API
  slug: open-pangaea-terms-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pangaea-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pangaea-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pangaea-domain-security.yml
description: PANGAEA is a data publisher and library for earth and environmental science, providing open access to geoscientific datasets including ocean data, climate records, sediment cores, and environmental measurements from scientific expeditions worldwide.
examples:
- key_count: 7
  name: Download Data By Doi
  slug: download-data-by-doi
- key_count: 4
  name: Oai Pmh Harvest
  slug: oai-pmh-harvest
- key_count: 7
  name: Search By Bounding Box
  slug: search-by-bounding-box
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.pangaea.de/assets/img/pangaea-logo.png
layout: provider
modified: 2026-06-13
name: PANGAEA
nav: Providers
network: true
overview: PANGAEA publishes 5 APIs on the [APIs.io](https://apis.io/) network, including DOI Filter API, Geo Filter API, OAI-PMH API, and 2 more. Tagged areas include Earth Science, Ocean Data, Climate Records, Environmental Science, and Geoscience.
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 121
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 30.0
  delta: 0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.4
    developer_ergonomics: 0.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pangaea/refs/heads/main/screenshots/pangaea-2026-06-20T191337.png
security:
- kind: domain-security
  name: Pangaea Domain Security
  slug: pangaea-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pangaea Vulnerability Disclosure
  slug: pangaea-vulnerability-disclosure
  summary_line: disclosure policy published
slug: pangaea
tags:
- Earth Science
- Ocean Data
- Climate Records
- Environmental Science
- Geoscience
- Open Data
- Scientific Data
website: https://www.pangaea.de/
---
