---
api_count: 2
apis:
- baseURL: https://tiles.aereo.io
  baseurl_source: declared
  description: 'A microservice for serving the map tiles behind Aereo Cloud. Publishes a FastAPI-generated OpenAPI 3.1.0 description with twelve read operations delivering Mapbox vector tiles (.pbf), Cloud Optimized '
  name: Aereo Cloud Tile Server
  slug: aaravunmannedsystems-tile-server
- baseURL: https://ac-rti-server-prod.aereo.io
  baseurl_source: declared
  description: 'WebSocket-based real-time SAM2 (Segment Anything 2) inference service used by Aereo Cloud for interactive segmentation of drone imagery. Its HTTP contract exposes only a liveness probe; the inference '
  name: Aereo Cloud Real-Time Inference Server
  slug: aereo7a4d-real-time-inference-server
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://aereo.io/
- group: start
  title: ''
  type: Portal
  url: https://cloud.aereo.io/
- group: start
  title: ''
  type: Login
  url: https://cloud.aereo.io/
- group: operate
  title: ''
  type: Support
  url: https://aereo.io/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aereo.io/wp-content/uploads/2023/11/Aereo-Privacy-Policy-1.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aereo.io/wp-content/uploads/2023/11/Aereo-Data-security-policy-Terms-Conditions-1.pdf
- group: auth
  title: ''
  type: Authentication
  url: authentication/aaravunmannedsystems-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aaravunmannedsystems-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aaravunmannedsystems-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aaravunmannedsystems-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aaravunmannedsystems-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aaravunmannedsystems-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aaravunmannedsystems-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aaravunmannedsystems-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/aaravunmannedsystems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aaravunmannedsystems-rate-limits.yml
created: '2026-09-05'
description: 'Aarav Unmanned Systems (AUS), which rebranded as Aereo in 2023, is an Indian end-to-end enterprise drone company founded in 2013 out of the research labs of IIT Kanpur and headquartered in Bengaluru. It designs and manufactures survey-grade UAVs and operates Aereo Cloud, a geospatial data platform that turns drone-captured imagery into orthomosaics, digital terrain models, 3D tilesets and AI-driven analytics for mining volumetrics, infrastructure and construction monitoring, urban and rural land records, agriculture and forest conservation. The company reports mapping over 45,000 villages and surveying more than 15 million acres. Its public machine-readable API surface is narrow: the Aereo Cloud web application is authenticated and JS-rendered, but its Tile Server microservice publishes a real OpenAPI 3.1.0 description at https://tiles.aereo.io/openapi.json covering vector, raster, Cesium terrain and 3D Tiles delivery.'
image: https://aereo.io/wp-content/uploads/2023/06/logo.svg
layout: provider
modified: '2026-09-05'
name: Aarav Unmanned Systems (Aereo)
nav: Providers
network: true
overview: 'Aarav Unmanned Systems (Aereo) publishes 2 APIs on the [APIs.io](https://apis.io/) network: Aereo Cloud Tile Server and Aereo Cloud Real-Time Inference Server. Tagged areas include Drones, UAV, Geospatial, Mapping, and Remote Sensing.


  Aarav Unmanned Systems (Aereo)''s developer surface includes developer portal, support, authentication, and 14 more developer resources.'
plans:
- name: Aaravunmannedsystems Plans Pricing
  plan_count: 0
  slug: aaravunmannedsystems-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Aaravunmannedsystems Rate Limits
  slug: aaravunmannedsystems-rate-limits
security:
- kind: authentication
  name: Aaravunmannedsystems Authentication
  slug: aaravunmannedsystems-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aaravunmannedsystems Domain Security
  slug: aaravunmannedsystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aaravunmannedsystems
tags:
- Drones
- UAV
- Geospatial
- Mapping
- Remote Sensing
- Surveying
- Mining
- Agriculture
- Satellite Imagery
- Analytics
- India
website: https://aereo.io/
---
