---
api_count: 1
apis:
- description: 'Live REST/JSON API behind Agerpoint Cloud and the Agerpoint Capture apps, served from cloudapi.agerpoint.com on ASP.NET Core (Kestrel). Resource families observed on the public first-party web client '
  name: Agerpoint Cloud API
  slug: agerpoint-cloud-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.agerpoint.com
- group: start
  title: ''
  type: Login
  url: https://cloud.agerpoint.com
- group: operate
  title: ''
  type: Support
  url: https://www.agerpoint.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.agerpoint.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.agerpoint.com/blog?format=rss
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agerpoint
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agerpoint.com/privacy-statements
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agerpoint.com/contracts
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agerpoint-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agerpoint-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agerpoint-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agerpoint-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agerpoint-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agerpoint-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/agerpoint-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agerpoint-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/agerpoint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agerpoint-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agerpoint-lifecycle.yml
coverage:
  checked: '2026-09-12'
  detail: 'Agerpoint''s only API is the console backend at cloudapi.agerpoint.com, where every path — including the OGC WMS endpoint at /api/maps/wms — answers HTTP 401 "WWW-Authenticate: Bearer" and requires an Auth0 token issued to a paying tenant, while www.agerpoint.com serves no /developers, /docs or /api page at all (404) and the tile service returns "RBAC: access denied".'
  evidence:
  - status: 401
    url: https://cloudapi.agerpoint.com/api/Capture/00000000-0000-0000-0000-000000000000
  - status: 401
    url: https://cloudapi.agerpoint.com/api/maps/wms?service=WMS&request=GetCapabilities
  - status: 404
    url: https://www.agerpoint.com/developers
  - status: 404
    url: https://cloudapi.agerpoint.com/swagger/v1/swagger.json
  - status: 403
    url: https://tiles.agerpoint.com/conformance
  reason: customer-only-docs
  state: gated
created: '2026-09-12'
description: 'Agerpoint is a spatial-intelligence company in Research Triangle Park, North Carolina that turns real-world field data into AI-derived crop, tree and land measurements. Its Capture mobile app builds full-resolution 3D digital twins of plants from a smartphone or tablet video, and Agerpoint Cloud — a spatial data management and analytics platform — fuses those captures with LiDAR, drone imagery, satellite data, sensors and equipment telemetry to derive plant metrics through a machine-learning pipeline for yield estimation, disease detection, carbon sequestration and biodiversity assessment. The platform is backed by a live REST API at cloudapi.agerpoint.com covering captures, projects, layers, geometry collections, image mosaics, Gaussian-splat models, analytic requests and pipeline jobs, secured by OAuth 2.0 / OIDC bearer tokens from an Auth0 tenant. That API is currently a customer-only surface: it powers the first-party console and mobile apps, and Agerpoint publishes no
  public developer portal, reference, or machine-readable contract for it. The company also sells API-integration and custom software development as professional services.'
image: https://static1.squarespace.com/static/606493cd17d20236b6ecab96/t/6a43fbdcb741a94a56e4ea61/1782840284360/ap-social-sharing-image.png?format=1500w
layout: provider
modified: '2026-09-12'
name: Agerpoint
nav: Providers
network: true
overview: 'Agerpoint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Geospatial, Remote Sensing, Digital Twin, and LiDAR.


  Agerpoint''s developer surface includes support, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Agerpoint Plans Pricing
  plan_count: 0
  slug: agerpoint-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Agerpoint Rate Limits
  slug: agerpoint-rate-limits
scopes:
- name: Agerpoint Scopes
  scope_count: 0
  slug: agerpoint-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Agerpoint Authentication
  slug: agerpoint-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agerpoint Domain Security
  slug: agerpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agerpoint
tags:
- Agriculture
- Geospatial
- Remote Sensing
- Digital Twin
- LiDAR
- Point Cloud
- Carbon Measurement
- Forestry
- Machine Learning
- Spatial Analytics
- Company
website: https://www.agerpoint.com
---
