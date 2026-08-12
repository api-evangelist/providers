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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-08-11'
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
artifact_total: 21
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
- group: other
  title: ''
  type: X
  url: https://x.com/getkoala_com
- group: company
  title: ''
  type: Blog
  url: https://getkoala.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://getkoala.com/pricing
- group: build
  title: ''
  type: SDKs
  url: https://github.com/getkoala/react
- group: build
  title: ''
  type: NPM
  url: https://www.npmjs.com/package/@getkoala/edge-api-client
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/koala/refs/heads/main/vocabulary/koala-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/koala/refs/heads/main/json-ld/koala-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/koala/refs/heads/main/json-schema/koala-profile-batch-request-schema.json
created: '2026-07-01'
description: Koala is a B2B buyer-intent and go-to-market platform that de-anonymizes website and product traffic, identifies the visitors and companies behind it, enriches them with firmographic and contact data (via Clearbit Reveal/Enrich and ZoomInfo), and scores first-party intent so sales teams can act on the accounts showing the strongest signals. Its developer surface is a client-side JavaScript pixel plus an HTTP collection API for server-side identify, event, and account ingestion, with a separate secret-key admin API for GDPR deletion.
examples:
- key_count: 3
  name: Koala Io Account Batch Event Example
  slug: koala-io-account-batch-event-example
- key_count: 3
  name: Koala Io Account Batch Traits Example
  slug: koala-io-account-batch-traits-example
- key_count: 3
  name: Koala Io Profile Batch Identify Example
  slug: koala-io-profile-batch-identify-example
- key_count: 3
  name: Koala Io Profile Batch Track Example
  slug: koala-io-profile-batch-track-example
finops:
- name: Koala Io Finops
  service_category: Analytics and Sales Intelligence
  slug: koala-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/koala-io.png
json_schemas:
- name: KoalaAccountBatchRequest
  property_count: 4
  slug: koala-io-account-batch-request
- name: KoalaProfileBatchRequest
  property_count: 5
  slug: koala-io-profile-batch-request
jsonld:
- class_count: 0
  name: Koala Io Context
  property_count: 23
  slug: koala-io-context
layout: provider
modified: '2026-08-08'
name: Koala
nav: Providers
network: true
overview: 'Koala publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Collection API, Deletion API, and 1 more. Tagged areas include Buyer Intent, Visitor Identification, De-anonymization, Enrichment, and Go-to-Market.


  The Koala catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Koala''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Koala Io Plans Pricing
  plan_count: 3
  slug: koala-io-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 7
  name: Koala Io Rate Limits
  slug: koala-io-rate-limits
rules:
- name: Koala API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: koala-io-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.5
  delta: -0.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 67.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
