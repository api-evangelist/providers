---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fema Agentic Access
  operation_count: 9
  slug: fema-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://www.fema.gov/api/open/v2
  baseurl_source: declared
  description: Self-describing metadata - dataset list and data dictionaries.
  name: OpenFEMA Catalog API
  slug: fema-catalog-api
- baseURL: https://www.fema.gov/api/open/v2
  baseurl_source: declared
  description: Federally declared disasters.
  name: OpenFEMA Disaster Declarations API
  slug: fema-disaster-declarations-api
- baseURL: https://www.fema.gov/api/open/v2
  baseurl_source: declared
  description: Hazard Mitigation Assistance (HMA) grant program data.
  name: OpenFEMA Hazard Mitigation API
  slug: fema-hazard-mitigation-api
- baseURL: https://www.fema.gov/api/open/v2
  baseurl_source: declared
  description: Integrated Public Alert and Warning System archived alerts.
  name: OpenFEMA IPAWS API
  slug: fema-ipaws-api
- baseURL: https://www.fema.gov/api/open/v2
  baseurl_source: declared
  description: National Flood Insurance Program redacted policy and claims data.
  name: OpenFEMA NFIP API
  slug: fema-nfip-api
- baseURL: https://www.fema.gov/api/open/v2
  baseurl_source: declared
  description: FEMA Public Assistance (PA) grant program data.
  name: OpenFEMA Public Assistance API
  slug: fema-public-assistance-api
- baseURL: https://www.fema.gov/api/open/v2
  baseurl_source: declared
  description: Per-disaster financial summary totals from NEMIS.
  name: OpenFEMA Web Disaster Summaries API
  slug: fema-web-disaster-summaries-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenFEMA Catalog API
  slug: open-fema-catalog-api
- collection_type: open
  name: OpenFEMA Catalog Disaster Declarations API
  slug: open-fema-disaster-declarations-api
- collection_type: open
  name: OpenFEMA Catalog Hazard Mitigation API
  slug: open-fema-hazard-mitigation-api
- collection_type: open
  name: OpenFEMA Catalog IPAWS API
  slug: open-fema-ipaws-api
- collection_type: open
  name: OpenFEMA Catalog NFIP API
  slug: open-fema-nfip-api
- collection_type: open
  name: OpenFEMA Catalog Public Assistance API
  slug: open-fema-public-assistance-api
- collection_type: open
  name: OpenFEMA Catalog Web Disaster Summaries API
  slug: open-fema-web-disaster-summaries-api
- collection_type: open
  name: OpenFEMA API
  slug: open-fema
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fema-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fema-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fema-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fema.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fema.gov/about/openfema/api
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fema-rate-limits.yml
created: '2026-07-03'
description: OpenFEMA is FEMA's open data platform, publishing free, public, machine-readable datasets on disaster declarations, public assistance grants, hazard mitigation projects, the National Flood Insurance Program (NFIP), and emergency alerting through a read-only RESTful API. The API uses OData-style query string parameters ($filter, $select, $top, $skip, $orderby) over individually versioned dataset endpoints, requires no API key or subscription, and returns JSON, CSV, or Parquet.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fema.png
layout: provider
modified: '2026-07-03'
name: OpenFEMA
nav: Providers
network: true
overview: 'OpenFEMA publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Disaster Declarations API, Hazard Mitigation API, and 4 more. Tagged areas include Government, Open Data, Emergency Management, Disaster, and FEMA.


  OpenFEMA''s developer surface includes documentation and 5 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 5
  name: Fema Rate Limits
  slug: fema-rate-limits
security:
- kind: domain-security
  name: Fema Domain Security
  slug: fema-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: fema
tags:
- Government
- Open Data
- Emergency Management
- Disaster
- FEMA
- Public Safety
website: https://www.fema.gov/
---
