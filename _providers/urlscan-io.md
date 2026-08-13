---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
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
  score: 0.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Scan and Analyse URLs
  name: URLScan.io
  slug: urlscanio
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/urlscan-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urlscan-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://urlscan.io/about-api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://urlscan.io/blog/feed.xml
created: '2026-05-28'
description: Scan and Analyse URLs
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/urlscan-io.png
layout: provider
modified: '2026-05-28'
name: URLScan.io
nav: Providers
network: true
overview: 'URLScan.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anti Malware and Public APIs.


  URLScan.io''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 61
score:
  band: minimal
  composite: 6.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/urlscan-io/refs/heads/main/screenshots/urlscan-io-2026-06-20T200529.png
security:
- kind: domain-security
  name: Urlscan Io Domain Security
  slug: urlscan-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Urlscan Io Vulnerability Disclosure
  slug: urlscan-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: urlscan-io
tags:
- Anti Malware
- Public APIs
website: https://urlscan.io/about-api/
---
