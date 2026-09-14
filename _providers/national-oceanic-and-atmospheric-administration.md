---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Oceanic And Atmospheric Administration Agentic Access
  operation_count: 1
  slug: national-oceanic-and-atmospheric-administration-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.tidesandcurrents.noaa.gov/api/prod
  baseurl_source: declared
  description: Retrieve observations and predictions from CO-OPS stations.
  name: National Oceanic and Atmospheric Administration Observations API
  slug: national-oceanic-and-atmospheric-administration-observations-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NOAA CO-OPS Data Observations API
  slug: open-national-oceanic-and-atmospheric-administration-observations-api
- collection_type: open
  name: NOAA CO-OPS Data API
  slug: open-national-oceanic-and-atmospheric-administration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-oceanic-and-atmospheric-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-oceanic-and-atmospheric-administration-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NOAAGov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/noaa
- group: company
  title: ''
  type: Website
  url: https://www.noaa.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.ncdc.noaa.gov/cdo-web/webservices/v2
- group: company
  title: ''
  type: Blog
  url: https://www.noaa.gov/rss.xml
created: '2024-12-03'
description: The National Oceanic and Atmospheric Administration (NOAA) is a federal agency within the U.S. Department of Commerce that focuses on monitoring and predicting changes in the Earth's environment, including climate, weather, oceans, and coasts.
finops:
- name: National Oceanic And Atmospheric Administration Finops
  service_category: API
  slug: national-oceanic-and-atmospheric-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-oceanic-and-atmospheric-administration.png
layout: provider
modified: '2026-05-19'
name: National Oceanic and Atmospheric Administration
nav: Providers
network: true
overview: 'National Oceanic and Atmospheric Administration publishes 1 API on the [APIs.io](https://apis.io/) network: Observations API. Tagged areas include Atmosphere, Federal-Government, Oceans, and Weather.


  National Oceanic and Atmospheric Administration''s developer surface includes developer portal, engineering blog, and 5 more developer resources.'
plans:
- name: National Oceanic And Atmospheric Administration Plans Pricing
  plan_count: 3
  slug: national-oceanic-and-atmospheric-administration-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: National Oceanic And Atmospheric Administration Rate Limits
  slug: national-oceanic-and-atmospheric-administration-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/national-oceanic-and-atmospheric-administration/refs/heads/main/screenshots/national-oceanic-and-atmospheric-administration-2026-06-20T190034.png
security:
- kind: domain-security
  name: National Oceanic And Atmospheric Administration Domain Security
  slug: national-oceanic-and-atmospheric-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-oceanic-and-atmospheric-administration
tags:
- Atmosphere
- Federal-Government
- Oceans
- Weather
website: https://www.noaa.gov/
---
