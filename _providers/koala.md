---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Koala Agentic Access
  operation_count: 2
  slug: koala-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 4
apis:
- description: Client-side JavaScript SDK and pixel for tracking website visitor behavior, identifying companies, and capturing product usage events. The snippet is installed on the customer's website and sends even
  name: Koala JavaScript SDK & Pixel API
  slug: koala-sdk-api
- description: Edge compute API for deploying Koala tracking logic in Cloudflare Workers, Vercel Edge Functions, and similar edge runtimes. Enables low-latency visitor identification and signal capture at the networ
  name: Koala Edge API
  slug: koala-edge-api
- description: Endpoints for sending events and traits tied to company accounts.
  name: Koala Account Ingestion API
  slug: koala-account-ingestion-api
- description: Endpoints for sending events and traits tied to individual visitors (profiles).
  name: Koala Profile Ingestion API
  slug: koala-profile-ingestion-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/koala-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/koala-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getkoala.com/
- group: docs
  title: ''
  type: Documentation
  url: https://getkoala.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getkoala
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getkoala
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
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/koala/refs/heads/main/plans/koala-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/koala/refs/heads/main/rate-limits/koala-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/koala/refs/heads/main/finops/koala-finops.yml
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
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/koala/refs/heads/main/json-schema/koala-account-batch-request-schema.json
created: '2026-06-12'
description: Koala is a B2B intent data and buyer signal platform that helps sales and marketing teams identify high-intent website visitors and prioritize accounts showing purchasing signals. The platform unifies first-party product usage data with third-party intent signals to score accounts and surface the most relevant leads. Koala provides a JavaScript SDK for client-side visitor tracking, a server-side batch API for event ingestion, and an Edge API for use in edge compute environments. Teams use Koala to automate lead routing, trigger sales plays, and enrich CRM records based on real-time behavioral signals from their website and product.
examples:
- key_count: 3
  name: Koala Account Batch Event Example
  slug: koala-account-batch-event-example
- key_count: 3
  name: Koala Account Batch Traits Example
  slug: koala-account-batch-traits-example
- key_count: 3
  name: Koala Profile Batch Identify Example
  slug: koala-profile-batch-identify-example
- key_count: 3
  name: Koala Profile Batch Track Example
  slug: koala-profile-batch-track-example
finops:
- name: Koala Finops
  service_category: ''
  slug: koala-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/koala.png
json_schemas:
- name: KoalaAccountBatchRequest
  property_count: 4
  slug: koala-account-batch-request
- name: KoalaProfileBatchRequest
  property_count: 5
  slug: koala-profile-batch-request
jsonld:
- class_count: 0
  name: Koala Context
  property_count: 23
  slug: koala-context
layout: provider
modified: '2026-06-12'
name: Koala
nav: Providers
network: true
overview: 'Koala publishes 2 APIs on the [APIs.io](https://apis.io/) network: Account Ingestion API and Profile Ingestion API. Tagged areas include B2B, Intent Data, Buyer Signals, Lead Routing, and Sales Intelligence.


  The Koala catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Koala''s developer surface includes documentation, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Koala Plans Pricing
  plan_count: 4
  slug: koala-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 4
  name: Koala Rate Limits
  slug: koala-rate-limits
rules:
- name: Koala API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: koala-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.6
  delta: -4.4
  facets:
    commercial_clarity: 57.9
    contract_quality: 64.4
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/koala/refs/heads/main/screenshots/koala-2026-06-20T184118.png
security:
- kind: domain-security
  name: Koala Domain Security
  slug: koala-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Koala Trust Center
  slug: koala-trust-center
  summary_line: SOC 2, GDPR
slug: koala
tags:
- B2B
- Intent Data
- Buyer Signals
- Lead Routing
- Sales Intelligence
- Visitor Identification
- Product-Led Growth
- Account Scoring
website: https://getkoala.com/
---
