---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'Autofleet''s public REST API and webhook surface for its fleet and mobility optimization platform — vehicles, drivers, tasks, rides, bookings, routes and dispatch — marketed on the integration page as '
  name: Autofleet Platform API
  slug: platform
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://autofleet.io
- group: company
  title: ''
  type: Blog
  url: https://autofleet.io/resources
- group: operate
  title: ''
  type: Support
  url: https://autofleet.io/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autofleet.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autofleet.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Autofleet
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autofleet-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/autofleet-packages.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/autofleet-robots.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/autofleet-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/autofleet-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autofleet-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: Autofleet's entire ReadMe developer hub at docs.autofleet.io is password-protected — every path, including /openapi.json, /llms.txt and /sitemap.xml, 302s to /password?redirect=<path> — so although the API gateway at api.autofleet.io is live and the company markets a "public API and webhooks", no endpoint, spec, auth or error reference can be read without a customer password.
  evidence:
  - status: 302
    url: https://docs.autofleet.io/
  - status: 302
    url: https://docs.autofleet.io/openapi.json
  - status: 200
    url: https://docs.autofleet.io/password?redirect=/
  - status: 200
    url: https://api.autofleet.io/
  - status: 404
    url: https://api.autofleet.io/openapi.json
  - status: 200
    url: https://autofleet.io/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: 'Autofleet is a fleet and mobility optimization platform founded in 2018 in Tel Aviv by Kobi Eisenberg and Dor Shay, and since 2024 an independently operated, wholly owned subsidiary of Element Fleet Management Corp. (TSX: EFN). Its AI-driven software plans, dispatches, routes and simulates vehicle-based operations across postal and parcel delivery, last-mile logistics, rental and car sharing, corporate motor pools, microtransit, NEMT and school transport, taxi and rideshare, field service, and autonomous mobility, in more than 20 countries. The platform is sold as an integration hub — Autofleet markets a public API and webhooks for connecting telematics, GPS, keyless access, maintenance, booking, dispatch, CRM and ERP systems — and adds Nova, a fleet-specific generative AI layer for natural-language operational questions. The API gateway is live at api.autofleet.io, but the developer reference at docs.autofleet.io is a password-protected ReadMe hub, so no machine-readable contract
  is publicly retrievable.'
image: https://cdn.prod.website-files.com/62efd8600e99ef30950239a5/630cd578c9f8724a3a154de4_Social_Share_Image%20(1).png
layout: provider
modified: '2026-08-06'
name: Autofleet
nav: Providers
network: true
overview: 'Autofleet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fleet Management, Mobility, Transportation, Logistics, and Route Optimization.


  Autofleet''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/autofleet/refs/heads/main/screenshots/autofleet-2026-08-07T161953.png
security:
- kind: domain-security
  name: Autofleet Domain Security
  slug: autofleet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autofleet
tags:
- Fleet Management
- Mobility
- Transportation
- Logistics
- Route Optimization
- Dispatch
- Last Mile Delivery
- Car Sharing
- Telematics
- Artificial Intelligence
website: https://autofleet.io
---
