---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.7
  scored_at: '2026-08-17'
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
random_paper: 75
score:
  band: emerging
  composite: 16.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 16.9
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
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
