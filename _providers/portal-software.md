---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.portal.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.oracle.com/content-management/webcenter-portal/ — a different registrable domain (portal.com -> oracle.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/portal-software/refs/heads/main/security/portal-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/portal-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.portal.com
created: '2026-07-17'
description: Portal Software was an Accel-backed billing and revenue-management software company whose portal.com domain now permanently redirects (HTTP 301) to Oracle WebCenter Portal, indicating the business and its assets have been absorbed into Oracle. It was surfaced as an Accel portfolio company and added to the API Evangelist network as a stub, but the enrichment pass finds no independent developer portal, OpenAPI specification, SDKs, MCP server, or published security program under portal.com — the domain serves only an Oracle marketing redirect, so there is no standalone API surface to enrich beyond the domain-level TLS/DNS security probe.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portal-software.png
layout: provider
modified: '2026-09-15'
name: Portal Software
nav: Providers
network: true
overview: Portal Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Billing, Revenue Management, Defunct, and Acquired.
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/portal-software/refs/heads/main/screenshots/portal-software-2026-09-02T151800.png
security:
- kind: domain-security
  name: Portal Software Domain Security
  slug: portal-software-domain-security
  summary_line: TLSv1.3 · HSTS
slug: portal-software
tags:
- Company
- Billing
- Revenue Management
- Defunct
- Acquired
- Oracle
website: http://www.portal.com
---
