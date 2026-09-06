---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Cloudflare Queues Agentic Access
  operation_count: 20
  slug: cloudflare-queues-agentic-access
  summary_line: 20 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: declared
  description: Operations for managing queue consumers (Worker push or HTTP pull)
  name: Cloudflare Queues Consumer API
  slug: cloudflare-queues-consumer-api
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: declared
  description: Operations for sending, receiving, and acknowledging messages
  name: Cloudflare Queues Messages API
  slug: cloudflare-queues-messages-api
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: declared
  description: Operations for retrieving queue metrics
  name: Cloudflare Queues Metrics API
  slug: cloudflare-queues-metrics-api
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: declared
  description: Operations for managing Cloudflare Queues and their configuration
  name: Cloudflare Queues Queue API
  slug: cloudflare-queues-queue-api
artifact_total: 29
collections:
- collection_type: postman
  name: Cloudflare Queues Consumer API
  slug: postman-cloudflare-queues-consumer-api
- collection_type: postman
  name: Cloudflare Queues Consumer Messages API
  slug: postman-cloudflare-queues-messages-api
- collection_type: postman
  name: Cloudflare Queues Consumer Metrics API
  slug: postman-cloudflare-queues-metrics-api
- collection_type: postman
  name: Cloudflare Queues Consumer Queue API
  slug: postman-cloudflare-queues-queue-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloudflare Queues Consumer API
  slug: open-cloudflare-queues-consumer-api
- collection_type: open
  name: Cloudflare Queues Consumer Messages API
  slug: open-cloudflare-queues-messages-api
- collection_type: open
  name: Cloudflare Queues Consumer Metrics API
  slug: open-cloudflare-queues-metrics-api
- collection_type: open
  name: Cloudflare Queues Consumer Queue API
  slug: open-cloudflare-queues-queue-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cloudflare/workers-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cloudflare/workers-sdk/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/cloudflare/workers-sdk/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cloudflare/workers-sdk/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cloudflare/workers-sdk/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/cloudflare/workers-sdk/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cloudflare-queues/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudflare-queues-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudflare-queues-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudflare-queues-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudflare-queues-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudflare.com/developer-platform/queues/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/queues/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cloudflare.com/queues/get-started/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cloudflare.com/api/resources/queues/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cloudflare
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/cloudflare/workers-sdk
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/cloudflare/api-schemas/main/openapi.yaml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudflare
- group: company
  title: ''
  type: Blog
  url: https://blog.cloudflare.com/tag/cloudflare-queues/
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.cloudflare.com/queues/platform/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cloudflarestatus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/Cloudflare
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.cloudflare.com/changelog/product/queues/
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudflare-queues-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudflare-queues-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloudflare-queues-finops.yml
created: '2026-06-13'
description: Cloudflare Queues is a flexible, scalable message queue service built into the Cloudflare Workers ecosystem. It provides guaranteed message delivery with a REST API for creating and managing queues, sending individual or batched messages, configuring push-based Worker consumers and HTTP pull consumers, managing dead letter queues, and monitoring queue metrics. Queues supports delivery delays, message retention up to 14 days, throughput up to 5,000 messages per second per queue, and event subscriptions for reactive workflows.
examples:
- key_count: 3
  name: Cloudflare Queues Create Consumer
  slug: cloudflare-queues-create-consumer
- key_count: 4
  name: Cloudflare Queues Create Queue
  slug: cloudflare-queues-create-queue
- key_count: 4
  name: Cloudflare Queues Pull Messages
  slug: cloudflare-queues-pull-messages
- key_count: 4
  name: Cloudflare Queues Push Message
  slug: cloudflare-queues-push-message
finops:
- name: Cloudflare Queues Finops
  service_category: ''
  slug: cloudflare-queues-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudflare-queues.png
json_schemas:
- name: Cloudflare Queue Consumer
  property_count: 0
  slug: cloudflare-queues-consumer
- name: Cloudflare Queue Message
  property_count: 0
  slug: cloudflare-queues-message
- name: Cloudflare Queue
  property_count: 9
  slug: cloudflare-queues-queue
jsonld:
- class_count: 4
  name: Cloudflare Queues Context
  property_count: 50
  slug: cloudflare-queues-context
layout: provider
modified: '2026-06-13'
name: Cloudflare Queues
nav: Providers
network: true
overview: 'Cloudflare Queues publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Consumer API, Messages API, Metrics API, and 1 more. Tagged areas include Messaging, Message Queue, Serverless, Workers, and Cloudflare.


  The Cloudflare Queues catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudflare Queues'' developer surface includes authentication, documentation, getting-started guide, API reference, engineering blog, pricing, changelog, and 20 more developer resources.'
plans:
- name: Cloudflare Queues Plans Pricing
  plan_count: 2
  slug: cloudflare-queues-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 20
  name: Cloudflare Queues Rate Limits
  slug: cloudflare-queues-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cloudflare Queues API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cloudflare-queues-jsonschema-spectral-rules
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 71.3
    catalog_earned_first_party: 0.0
    catalog_gap: 43.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 63.7
    developer_ergonomics: 44.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 78.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudflare-queues/refs/heads/main/screenshots/cloudflare-queues-2026-06-20T174559.png
security:
- kind: authentication
  name: Cloudflare Queues Authentication
  slug: cloudflare-queues-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Cloudflare Queues Domain Security
  slug: cloudflare-queues-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudflare Queues Vulnerability Disclosure
  slug: cloudflare-queues-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cloudflare-queues
tags:
- Messaging
- Message Queue
- Serverless
- Workers
- Cloudflare
- Async
- Dead Letter Queue
- Event-Driven
website: https://www.cloudflare.com/developer-platform/queues/
---
