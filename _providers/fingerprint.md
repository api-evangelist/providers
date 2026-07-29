---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Fingerprint Agentic Access
  operation_count: 6
  slug: fingerprint-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- description: Search identification events with filters.
  name: Fingerprint Event Search API
  slug: fingerprint-event-search-api
- description: Get and update individual identification events.
  name: Fingerprint Events API
  slug: fingerprint-events-api
- description: Find visitorIds likely belonging to the same person.
  name: Fingerprint Related Visitors API
  slug: fingerprint-related-visitors-api
- description: Get visit history and delete visitor data.
  name: Fingerprint Visitors API
  slug: fingerprint-visitors-api
artifact_total: 12
collections:
- collection_type: open
  name: Fingerprint Server API
  slug: open-fingerprint
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fingerprint-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fingerprint-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fingerprint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fingerprint-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fingerprintjs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fingerprintjs
- group: company
  title: ''
  type: Website
  url: https://fingerprint.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fingerprint.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/fingerprint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fingerprint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fingerprint-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fingerprint.com/rss.xml
created: '2026-06-25'
description: Fingerprint (formerly FingerprintJS) is a device-identification and fraud-prevention platform. Its browser and mobile agents generate a stable visitorId, and the Server API returns detailed identification events enriched with Smart Signals (bot, VPN, proxy, tampering, emulator, and more) for account takeover, payment fraud, and bot-mitigation use cases.
finops:
- name: Fingerprint Finops
  service_category: Identity and Fraud Prevention
  slug: fingerprint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fingerprint.png
layout: provider
modified: '2026-06-25'
name: Fingerprint
nav: Providers
network: true
overview: 'Fingerprint publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Event Search API, Events API, Related Visitors API, and 1 more. Tagged areas include Device Identification, Fraud Prevention, Bot Detection, Smart Signals, and Identity.


  Fingerprint''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Fingerprint Plans Pricing
  plan_count: 3
  slug: fingerprint-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 2
  name: Fingerprint Rate Limits
  slug: fingerprint-rate-limits
score:
  band: thin
  composite: 39.7
  delta: -2.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fingerprint/refs/heads/main/screenshots/fingerprint-2026-07-25T214519.png
security:
- kind: authentication
  name: Fingerprint Authentication
  slug: fingerprint-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Fingerprint Domain Security
  slug: fingerprint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fingerprint Trust Center
  slug: fingerprint-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: fingerprint
tags:
- Device Identification
- Fraud Prevention
- Bot Detection
- Smart Signals
- Identity
website: https://fingerprint.com
---
