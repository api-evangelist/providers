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
api_count: 1
apis:
- description: Read-only API for querying OpenStreetMap data. Supports retrieval of nodes, ways, relations, and areas using the Overpass Query Language (QL) or XML syntax, with output in JSON, XML, CSV, or custom fo
  name: Overpass API
  slug: overpass-api
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/drolbr/Overpass-API/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/drolbr/Overpass-API/releases
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overpass-api-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.overpass-api.de/overpass-doc/en/
- group: docs
  title: ''
  type: LanguageReference
  url: https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/drolbr/Overpass-API
- group: commercial
  title: ''
  type: License
  url: https://github.com/drolbr/Overpass-API/blob/master/LICENSE
- group: build
  title: ''
  type: InteractiveTool
  url: https://overpass-turbo.eu/
- group: operate
  title: ''
  type: StatusPage
  url: https://overpass-api.de/api/status
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/overpass-api/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/overpass-api/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/overpass-api/refs/heads/main/finops/finops.yml
description: Overpass API is a read-only OpenStreetMap data API that enables querying geographic features including nodes, ways, relations, and tags using the Overpass Query Language (QL). It supports complex spatial queries with filters for bounding boxes, tags, proximity, area containment, and element relationships, making it the primary tool for extracting custom subsets of OSM data programmatically.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://overpass-api.de/img/osm_logo.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: Overpass API
nav: Providers
network: true
overview: 'Overpass API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include OpenStreetMap, Geographic, Spatial, GIS, and Maps.


  The Overpass API catalog on APIs.io includes 1 JSON-LD context.


  Overpass API''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 3
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/overpass-api/refs/heads/main/screenshots/overpass-api-2026-06-20T191236.png
security:
- kind: domain-security
  name: Overpass Api Domain Security
  slug: overpass-api-domain-security
  summary_line: TLSv1.3
slug: overpass-api
tags:
- OpenStreetMap
- Geographic
- Spatial
- GIS
- Maps
- Open Data
- Query Language
---
