---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Licenseplatedata Agentic Access
  operation_count: 3
  slug: licenseplatedata-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://api.licenseplatedata.com/v1
  baseurl_source: declared
  description: Vehicle imagery
  name: LicensePlateData Images API
  slug: licenseplatedata-images-api
- baseURL: https://api.licenseplatedata.com/v1
  baseurl_source: declared
  description: Convert license plates to VINs
  name: LicensePlateData Plate API
  slug: licenseplatedata-plate-api
- baseURL: https://api.licenseplatedata.com/v1
  baseurl_source: declared
  description: Decode VINs into vehicle attributes
  name: LicensePlateData VIN API
  slug: licenseplatedata-vin-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LicensePlateData Images API
  slug: open-licenseplatedata-images-api
- collection_type: open
  name: LicensePlateData Images Plate API
  slug: open-licenseplatedata-plate-api
- collection_type: open
  name: LicensePlateData Images VIN API
  slug: open-licenseplatedata-vin-api
- collection_type: open
  name: LicensePlateData API
  slug: open-licenseplatedata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/licenseplatedata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/licenseplatedata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/licenseplatedata-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://licenseplatedata.com/blog
created: '2025-02-24'
description: Developer-first tools that give access to a library of vehicle information, including license plate to VIN lookup, VIN decoding, and OEM-style vehicle imagery for passenger cars, ATVs, and light and heavy trucks and trailers from 1980 to current model years.
finops:
- name: Licenseplatedata Finops
  service_category: API
  slug: licenseplatedata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/licenseplatedata.png
layout: provider
modified: '2026-05-19'
name: LicensePlateData
nav: Providers
network: true
overview: 'LicensePlateData publishes 3 APIs on the [APIs.io](https://apis.io/) network: Images API, Plate API, and VIN API. Tagged areas include Vehicles, License Plates, VIN, Automotive, and Plate Lookup.


  LicensePlateData''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Licenseplatedata Plans Pricing
  plan_count: 3
  slug: licenseplatedata-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Licenseplatedata Rate Limits
  slug: licenseplatedata-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/licenseplatedata/refs/heads/main/screenshots/licenseplatedata-2026-06-20T184505.png
security:
- kind: authentication
  name: Licenseplatedata Authentication
  slug: licenseplatedata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Licenseplatedata Domain Security
  slug: licenseplatedata-domain-security
  summary_line: TLSv1.3 · DMARC
slug: licenseplatedata
tags:
- Vehicles
- License Plates
- VIN
- Automotive
- Plate Lookup
- VIN Decoding
---
