---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Bitly Agentic Access
  operation_count: 42
  slug: bitly-agentic-access
  summary_line: 42 operations · 14 acting
api_count: 10
apis:
- description: The Bitlinks API from Bitly — 4 operation(s) for bitlinks.
  name: Bitly Bitlinks API
  slug: bitly-bitlinks-api
- description: The BSDs API from Bitly — 1 operation(s) for bsds.
  name: Bitly BSDs API
  slug: bitly-bsds-api
- description: The Campaigns API from Bitly — 2 operation(s) for campaigns.
  name: Bitly Campaigns API
  slug: bitly-campaigns-api
- description: The Channels API from Bitly — 2 operation(s) for channels.
  name: Bitly Channels API
  slug: bitly-channels-api
- description: The Custom Bitlinks API from Bitly — 2 operation(s) for custom bitlinks.
  name: Bitly Custom Bitlinks API
  slug: bitly-custom-bitlinks-api
- description: The Group Metrics API from Bitly — 7 operation(s) for group metrics.
  name: Bitly Group Metrics API
  slug: bitly-group-metrics-api
- description: The Groups API from Bitly — 5 operation(s) for groups.
  name: Bitly Groups API
  slug: bitly-groups-api
- description: The Metrics API from Bitly — 8 operation(s) for metrics.
  name: Bitly Metrics API
  slug: bitly-metrics-api
- description: The Organizations API from Bitly — 4 operation(s) for organizations.
  name: Bitly Organizations API
  slug: bitly-organizations-api
- description: The QR Codes API from Bitly — 1 operation(s) for qr codes.
  name: Bitly QR Codes API
  slug: bitly-qr-codes-api
artifact_total: 16
collections:
- collection_type: open
  name: Bitly API v4
  slug: open-bitly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitly-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bitly-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitly-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bitly
- group: company
  title: ''
  type: Website
  url: https://bitly.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bitly.com
- group: docs
  title: ''
  type: APIReference
  url: https://dev.bitly.com/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://bitly.com/pages/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.bitly.com/sign_up
- group: start
  title: ''
  type: Login
  url: https://app.bitly.com/sign_in
- group: auth
  title: ''
  type: Authentication
  url: https://dev.bitly.com/docs/getting-started/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://dev.bitly.com/docs/getting-started/rate-limits
- group: operate
  title: ''
  type: Support
  url: https://support.bitly.com
- group: operate
  title: ''
  type: StatusPage
  url: https://bitly.statuspage.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitly
- group: company
  title: ''
  type: Blog
  url: https://bitly.com/blog/
created: '2026-05-11'
description: Bitly is a URL shortening and link management platform that enables developers and marketers to create branded short links, generate QR codes, track engagement analytics, and manage link campaigns at scale. The Bitly v4 REST API provides programmatic access to link creation, custom domains, groups, campaigns, click metrics, and QR codes using Bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitly.png
layout: provider
modified: '2026-05-11'
name: Bitly
nav: Providers
network: true
overview: 'Bitly publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Bitlinks API, BSDs API, Campaigns API, and 7 more. Tagged areas include Links, URL Shortener, QR Codes, Analytics, and Marketing.


  Bitly''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 11 more developer resources.'
random_paper: 84
score:
  band: thin
  composite: 36.8
  delta: -0.5
  facets:
    commercial_clarity: 31.6
    contract_quality: 55.2
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitly/refs/heads/main/screenshots/bitly-2026-06-20T173312.png
security:
- kind: authentication
  name: Bitly Authentication
  slug: bitly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bitly Domain Security
  slug: bitly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bitly Vulnerability Disclosure
  slug: bitly-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bitly Trust Center
  slug: bitly-trust-center
  summary_line: SOC 2, GDPR
slug: bitly
tags:
- Links
- URL Shortener
- QR Codes
- Analytics
- Marketing
website: https://bitly.com
---
