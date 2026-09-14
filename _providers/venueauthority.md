---
api_count: 2
apis:
- baseURL: https://venueauthority.com
  baseurl_source: declared
  description: Create and download workspace-scoped evidence exports.
  name: Venue Authority Audit Exports API
  slug: venueauthority-audit-exports-api
- baseURL: https://venueauthority.com
  baseurl_source: declared
  description: Read supported sources, record counts, availability, and freshness.
  name: Venue Authority Coverage API
  slug: venueauthority-coverage-api
- baseURL: https://venueauthority.com
  baseurl_source: declared
  description: Resolve a merchant and retrieve its canonical regulator record and retained evidence.
  name: Venue Authority Resolution & Evidence API
  slug: venueauthority-resolution-evidence-api
- baseURL: https://venueauthority.com
  baseurl_source: declared
  description: Manage workspace-owned facility watchlists and stable change history.
  name: Venue Authority Watchlists API
  slug: venueauthority-watchlists-api
- baseURL: https://venueauthority.com
  baseurl_source: declared
  description: Register endpoints and inspect delivery attempts.
  name: Venue Authority Webhooks API
  slug: venueauthority-webhooks-api
artifact_total: 6
common:
- group: other
  title: ''
  type: APIsJSON
  url: https://venueauthority.com/apis.json
- group: agent
  title: ''
  type: LLMsTxt
  url: https://venueauthority.com/llms.txt
- group: company
  title: ''
  type: Website
  url: https://venueauthority.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://venueauthority.com/developers
- group: commercial
  title: ''
  type: Plans
  url: https://venueauthority.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://venueauthority.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://venueauthority.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://venueauthority.com/privacy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://venueauthority.com/trust/api-key-and-tenant-security
- group: operate
  title: ''
  type: Support
  url: https://venueauthority.com/support
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kingymon1/venue-authority-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kingymon1/venue-authority-api/tree/main/packages/node-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kingymon1/venue-authority-api/tree/main/packages/python-sdk
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/kingymon1/venue-authority-api/tree/main/packages/mcp-server
- group: build
  title: ''
  type: GitHubRelease
  url: https://github.com/kingymon1/venue-authority-api/releases/tag/clients-v0.1.0
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kingymon11-8337942/venue-authority/overview
- group: docs
  title: ''
  type: PostmanDocumentation
  url: https://documenter.getpostman.com/view/57620096/2sBYArVYPE
created: '2026-08-21'
description: Venue Authority is a self-serve facility verification and monitoring API for payment facilitators, marketplaces, KYB providers and restaurant platforms working with food-service businesses. It matches a business name and street address to a supported regulator facility record, returns source-linked evidence for that match, and supports ongoing portfolio monitoring so a change at the regulator surfaces after onboarding rather than at the next manual review. The public contract is an OpenAPI 3.1 document of 12 paths and 15 operations, authenticated with a bearer API key, and the provider tags every operation into five groups — resolution and evidence, coverage, watchlists, webhooks and audit exports — which is how it is carried here as five per-resource documents. Coverage is enumerated by the API itself rather than described in prose, and the provider publishes an APIs.json, llms.txt, llms-full.txt, a Postman collection and a machine-readable error catalogue alongside the contract,
  plus MIT-licensed Node.js, Python and MCP client packages released on GitHub with checksummed build artifacts.
image: https://venueauthority.com/venue-authority-mark.svg
layout: provider
mcp_servers:
- description: ''
  name: Venue Authority MCP Server
  slug: venue-authority-mcp-server
modified: '2026-08-21'
name: Venue Authority
nav: Providers
network: true
overview: 'Venue Authority publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Audit Exports API, Coverage API, Resolution & Evidence API, and 2 more. Tagged areas include Food Service, facility verification, Merchant Onboarding, regulator records, and Monitoring.


  Venue Authority''s developer surface includes support and 16 more developer resources.'
random_paper: 15
screenshot: https://raw.githubusercontent.com/api-evangelist/venueauthority/refs/heads/main/screenshots/venueauthority-2026-09-02T165648.png
slug: venueauthority
tags:
- Food Service
- facility verification
- Merchant Onboarding
- regulator records
- Monitoring
- KYB
- Payment Facilitators
- Marketplaces
- restaurant platforms
website: https://venueauthority.com
---
