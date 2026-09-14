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
  name: Keeptrack Agentic Access
  operation_count: 5
  slug: keeptrack-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Keep Track is the free, open source tool that makes space exploration accessible to all - professionals and amateurs alike. With its user-friendly interface, you can simulate satellite launches, visua
  name: KeepTrack
  slug: keeptrack
- baseURL: https://www.keeptrack.space/api
  baseurl_source: declared
  description: Bulk catalog and listings.
  name: KeepTrack Catalog API
  slug: keeptrack-catalog-api
- baseURL: https://www.keeptrack.space/api
  baseurl_source: declared
  description: Retrieve orbital elements (TLE, OMM).
  name: KeepTrack Orbits API
  slug: keeptrack-orbits-api
- baseURL: https://www.keeptrack.space/api
  baseurl_source: declared
  description: Compute real-time positions and ephemerides.
  name: KeepTrack Positions API
  slug: keeptrack-positions-api
- baseURL: https://www.keeptrack.space/api
  baseurl_source: declared
  description: Search and retrieve catalog data about tracked space objects.
  name: KeepTrack Satellites API
  slug: keeptrack-satellites-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KeepTrack Space Catalog API
  slug: open-keeptrack-catalog-api
- collection_type: open
  name: KeepTrack Space Catalog Orbits API
  slug: open-keeptrack-orbits-api
- collection_type: open
  name: KeepTrack Space Catalog Positions API
  slug: open-keeptrack-positions-api
- collection_type: open
  name: KeepTrack Space Catalog Satellites API
  slug: open-keeptrack-satellites-api
- collection_type: open
  name: KeepTrack Space API
  slug: open-keeptrack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keeptrack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keeptrack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keeptrack-authentication.yml
created: '2024-11-07T00:00:00.000Z'
description: Keep Track is the free, open source tool that makes space exploration accessible to all - professionals and amateurs alike. With its user-friendly interface, you can simulate satellite launches, visualize debris patterns, and explore a catalog of 30,000+ real satellites and debris. Zoom through geosynchronous orbits, run collision scenarios, and track debris fragmentation over time.
finops:
- name: Keeptrack Finops
  service_category: API
  slug: keeptrack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keeptrack.png
layout: provider
modified: '2026-04-28'
name: KeepTrack
nav: Providers
network: true
overview: 'KeepTrack publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Orbits API, Positions API, and 1 more. Tagged areas include Satellites and Space.


  KeepTrack''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: Keeptrack Plans Pricing
  plan_count: 3
  slug: keeptrack-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Keeptrack Rate Limits
  slug: keeptrack-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/keeptrack/refs/heads/main/screenshots/keeptrack-2026-06-20T183941.png
security:
- kind: authentication
  name: Keeptrack Authentication
  slug: keeptrack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Keeptrack Domain Security
  slug: keeptrack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: keeptrack
tags:
- Satellites
- Space
---
