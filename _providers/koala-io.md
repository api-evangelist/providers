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
    error_semantics: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Koala Io Agentic Access
  operation_count: 5
  slug: koala-io-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 5
apis:
- description: The client-side pixel loaded from cdn.getkoala.com/v1/{key}/sdk.js. Exposes ko.identify(), ko.track(), ko.qualify(), ko.reset() and autotracks pageviews, form fills, and session time. This is a browse
  name: Koala Web Pixel (JavaScript SDK)
  slug: koala-io-web-pixel-sdk
- description: Account-level (company) trait and event ingestion.
  name: Koala Accounts API
  slug: koala-io-accounts-api
- description: Server-side ingestion of visitor identifies, events, and traits.
  name: Koala Collection API
  slug: koala-io-collection-api
- description: GDPR right-to-erasure requests and status.
  name: Koala Deletion API
  slug: koala-io-deletion-api
- description: Bootstrap configuration used by the client-side pixel.
  name: Koala SDK API
  slug: koala-io-sdk-api
artifact_total: 13
collections:
- collection_type: open
  name: Koala API
  slug: open-koala-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/koala-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/koala-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koala-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/koala-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getkoala
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getkoala
- group: company
  title: ''
  type: Website
  url: https://getkoala.com
- group: docs
  title: ''
  type: Documentation
  url: https://getkoala.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/koala-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/koala-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/koala-io-finops.yml
created: '2026-07-01'
description: Koala is a B2B buyer-intent and go-to-market platform that de-anonymizes website and product traffic, identifies the visitors and companies behind it, enriches them with firmographic and contact data (via Clearbit Reveal/Enrich and ZoomInfo), and scores first-party intent so sales teams can act on the accounts showing the strongest signals. Its developer surface is a client-side JavaScript pixel plus an HTTP collection API for server-side identify, event, and account ingestion, with a separate secret-key admin API for GDPR deletion.
finops:
- name: Koala Io Finops
  service_category: Analytics and Sales Intelligence
  slug: koala-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/koala-io.png
layout: provider
modified: '2026-07-01'
name: Koala
nav: Providers
network: true
overview: 'Koala publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Collection API, Deletion API, and 1 more. Tagged areas include Buyer Intent, Visitor Identification, De-anonymization, Enrichment, and Go-to-Market.


  Koala''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Koala Io Plans Pricing
  plan_count: 3
  slug: koala-io-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 7
  name: Koala Io Rate Limits
  slug: koala-io-rate-limits
score:
  band: thin
  composite: 40.7
  delta: -2.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/koala-io/refs/heads/main/screenshots/koala-io-2026-07-25T224023.png
security:
- kind: authentication
  name: Koala Io Authentication
  slug: koala-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Koala Io Domain Security
  slug: koala-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Koala Io Trust Center
  slug: koala-io-trust-center
  summary_line: SOC 2, GDPR
slug: koala-io
tags:
- Buyer Intent
- Visitor Identification
- De-anonymization
- Enrichment
- Go-to-Market
- Sales Intelligence
- B2B
website: https://getkoala.com
---
