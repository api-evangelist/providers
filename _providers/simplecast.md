---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Simplecast Agentic Access
  operation_count: 62
  slug: simplecast-agentic-access
  summary_line: 62 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.simplecast.com
  baseurl_source: declared
  description: Audience analytics for podcasts and episodes.
  name: Simplecast Analytics API
  slug: simplecast-analytics-api
- baseURL: https://api.simplecast.com
  baseurl_source: declared
  description: Distribution channels a podcast is syndicated to.
  name: Simplecast Distribution API
  slug: simplecast-distribution-api
- baseURL: https://api.simplecast.com
  baseurl_source: declared
  description: Episodes and their authors, keywords, markers, and audio.
  name: Simplecast Episodes API
  slug: simplecast-episodes-api
- baseURL: https://api.simplecast.com
  baseurl_source: declared
  description: Account, categories, keywords, authors, and helper resources.
  name: Simplecast Metadata API
  slug: simplecast-metadata-api
- baseURL: https://api.simplecast.com
  baseurl_source: declared
  description: Podcasts (shows) and their related metadata.
  name: Simplecast Podcasts API
  slug: simplecast-podcasts-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Simplecast Analytics API
  slug: open-simplecast-analytics-api
- collection_type: open
  name: Simplecast Analytics Distribution API
  slug: open-simplecast-distribution-api
- collection_type: open
  name: Simplecast Analytics Episodes API
  slug: open-simplecast-episodes-api
- collection_type: open
  name: Simplecast Analytics Metadata API
  slug: open-simplecast-metadata-api
- collection_type: open
  name: Simplecast Analytics Podcasts API
  slug: open-simplecast-podcasts-api
- collection_type: open
  name: Simplecast API
  slug: open-simplecast
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sirius-xm/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/simplecast-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simplecast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simplecast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simplecast-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simplecast
- group: company
  title: ''
  type: Website
  url: https://www.simplecast.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.simplecast.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/simplecast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simplecast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/simplecast-finops.yml
created: '2026-07-05'
description: Simplecast is a podcast hosting, distribution, and analytics platform for creators, networks, and brands, owned by SiriusXM Media (acquired by SiriusXM in 2020). It provides podcast and episode management, distribution to Apple Podcasts, Spotify, and other channels, embeddable players, and IAB-certified audience analytics. Simplecast exposes a documented REST API at https://api.simplecast.com covering podcasts, episodes, analytics, and distribution channels, authenticated with a bearer token generated from the Private Apps page in the Simplecast dashboard. The API is read-oriented and self-describing - each response returns the actions available to the authenticated user - with a small number of write operations such as uploading episode audio. Access requires a Simplecast account; broader API integration is positioned as part of the higher-tier (Professional / Enterprise) plans.
finops:
- name: Simplecast Finops
  service_category: Media and Podcasting
  slug: simplecast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplecast.png
layout: provider
modified: '2026-07-05'
name: Simplecast
nav: Providers
network: true
overview: 'Simplecast publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Distribution API, Episodes API, and 2 more. Tagged areas include Podcasting, Podcast Hosting, Podcast Distribution, Podcast Analytics, and Audio.


  Simplecast''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Simplecast Plans Pricing
  plan_count: 5
  slug: simplecast-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Simplecast Rate Limits
  slug: simplecast-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/simplecast/refs/heads/main/screenshots/simplecast-2026-09-02T155534.png
security:
- kind: authentication
  name: Simplecast Authentication
  slug: simplecast-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Simplecast Domain Security
  slug: simplecast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simplecast
tags:
- Podcasting
- Podcast Hosting
- Podcast Distribution
- Podcast Analytics
- Audio
- Media
- SiriusXM Media
website: https://www.simplecast.com
---
