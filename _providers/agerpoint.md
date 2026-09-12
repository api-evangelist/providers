---
api_count: 1
artifact_total: 0
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
random_paper: 3
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
---
