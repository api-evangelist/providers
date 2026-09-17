---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - sandbox
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://api.impala.travel/v1
  baseurl_source: declared
  description: Making and managing bookings.
  name: Impala Bookings API
  slug: impala-bookings-api
- baseURL: https://api.impala.travel/v1
  baseurl_source: declared
  description: Accessing hotel content, available rooms and rates.
  name: Impala Hotels API
  slug: impala-hotels-api
- baseURL: https://api.impala.travel/v1
  baseurl_source: declared
  description: Getting rates for future dates.
  name: Impala Rate Calendar API
  slug: impala-rate-calendar-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Impala Hotel Booking Bookings API
  slug: open-impala-bookings-api
- collection_type: open
  name: Impala Hotel Booking Bookings Hotels API
  slug: open-impala-hotels-api
- collection_type: open
  name: Impala Hotel Booking Bookings Rate Calendar API
  slug: open-impala-rate-calendar-api
common:
- group: company
  title: ''
  type: Website
  url: https://impala.travel
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/capabilities/impala-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/impala-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/overlays/impala-hotels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/impala-hotels-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/authentication/impala-authentication.yml
  title: ''
  type: Authentication
  url: authentication/impala-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/packages/impala-packages.yml
  title: ''
  type: Packages
  url: packages/impala-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/packages/impala-packages.yml
  title: ''
  type: SDKs
  url: packages/impala-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/mcp/impala-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/impala-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/llms/impala-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/impala-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/conventions/impala-conventions.yml
  title: ''
  type: Conventions
  url: conventions/impala-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/errors/impala-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/impala-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/lifecycle/impala-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/impala-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/conformance/impala-conformance.yml
  title: ''
  type: Conformance
  url: conformance/impala-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/data-model/impala-data-model.yml
  title: ''
  type: DataModel
  url: data-model/impala-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/sandbox/impala-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/impala-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetImpala
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/getimpala/impala-hotel-booking-api/documentation/fdkbiih/impala-hotel-booking-api
created: '2026-07-17'
description: 'Impala built a single, standardized REST API for the hotel industry — one integration to search availability, read rate plans, and create, amend, and cancel bookings across many property management systems (PMS), so any app could sell hotel rooms and earn commission per booking. Founded in London in 2016 and backed by Speedinvest, Lakestar, and Kima Ventures, Impala shipped a sandbox (with a demo hotel, "The Charleston"), a Postman collection, and PHP/JavaScript wrappers. The company is now defunct: getimpala.com / impala.travel and the API and docs hosts no longer resolve, and the primary domain is held by an unrelated party. This profile preserves the historical OpenAPI (apis.guru impala.travel:hotels 1.003) and pipeline-derived artifacts for the record.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/impala.png
layout: provider
modified: '2026-09-16'
name: Impala
nav: Providers
network: true
overview: 'Impala publishes 3 APIs on the [APIs.io](https://apis.io/) network: Bookings API, Hotels API, and Rate Calendar API. Tagged areas include Company, Hotels, Travel, Booking, and Hospitality.


  Impala''s developer surface includes authentication, sandbox, and 15 more developer resources.'
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/impala/refs/heads/main/screenshots/impala-2026-07-25T222147.png
security:
- kind: authentication
  name: Impala Authentication
  slug: impala-authentication
  summary_line: apiKey/http · 2 schemes
slug: impala
tags:
- Company
- Hotels
- Travel
- Booking
- Hospitality
- Payments
- Defunct
website: https://impala.travel
---
