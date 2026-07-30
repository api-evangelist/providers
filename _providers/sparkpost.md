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
- acting_count: 34
  human_in_the_loop: 0
  name: Sparkpost Agentic Access
  operation_count: 79
  slug: sparkpost-agentic-access
  summary_line: 79 operations · 34 acting
api_count: 12
apis:
- description: The DKIM Keys API from SparkPost — 3 operation(s) for dkim keys.
  name: SparkPost DKIM Keys API
  slug: sparkpost-dkim-keys-api
- description: The Events API from SparkPost — 4 operation(s) for events.
  name: SparkPost Events API
  slug: sparkpost-events-api
- description: The Inbound Domains API from SparkPost — 2 operation(s) for inbound domains.
  name: SparkPost Inbound Domains API
  slug: sparkpost-inbound-domains-api
- description: The Metrics API from SparkPost — 17 operation(s) for metrics.
  name: SparkPost Metrics API
  slug: sparkpost-metrics-api
- description: The Recipient Lists API from SparkPost — 2 operation(s) for recipient lists.
  name: SparkPost Recipient Lists API
  slug: sparkpost-recipient-lists-api
- description: The Relay Webhooks API from SparkPost — 3 operation(s) for relay webhooks.
  name: SparkPost Relay Webhooks API
  slug: sparkpost-relay-webhooks-api
- description: The Sending Domains API from SparkPost — 3 operation(s) for sending domains.
  name: SparkPost Sending Domains API
  slug: sparkpost-sending-domains-api
- description: The Subaccounts API from SparkPost — 3 operation(s) for subaccounts.
  name: SparkPost Subaccounts API
  slug: sparkpost-subaccounts-api
- description: The Suppression List API from SparkPost — 3 operation(s) for suppression list.
  name: SparkPost Suppression List API
  slug: sparkpost-suppression-list-api
- description: The Templates API from SparkPost — 4 operation(s) for templates.
  name: SparkPost Templates API
  slug: sparkpost-templates-api
- description: The Transmissions API from SparkPost — 2 operation(s) for transmissions.
  name: SparkPost Transmissions API
  slug: sparkpost-transmissions-api
- description: The Webhooks API from SparkPost — 6 operation(s) for webhooks.
  name: SparkPost Webhooks API
  slug: sparkpost-webhooks-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sparkpost-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sparkpost-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sparkpost-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sparkpost-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.sparkpost.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.sparkpost.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.sparkpost.com/docs/getting-started/getting-started-sparkpost
- group: docs
  title: ''
  type: SupportDocumentation
  url: https://support.sparkpost.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SparkPost
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sparkpost
- group: other
  title: ''
  type: X
  url: https://x.com/sparkpost
- group: company
  title: ''
  type: Blog
  url: https://www.sparkpost.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sparkpost.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sparkpost.com/
- group: build
  title: ''
  type: SDKNodejs
  url: https://github.com/SparkPost/node-sparkpost
- group: build
  title: ''
  type: SDKPython
  url: https://github.com/SparkPost/python-sparkpost
- group: build
  title: ''
  type: SDKPHP
  url: https://github.com/SparkPost/php-sparkpost
- group: build
  title: ''
  type: SDKJava
  url: https://github.com/SparkPost/java-sparkpost
- group: build
  title: ''
  type: SDKGo
  url: https://github.com/SparkPost/gosparkpost
- group: build
  title: ''
  type: SDKElixir
  url: https://github.com/SparkPost/elixir-sparkpost
- group: build
  title: ''
  type: PostmanCollection
  url: https://github.com/SparkPost/postman-collection
- group: commercial
  title: ''
  type: Plans
  url: plans/sparkpost-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sparkpost-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sparkpost-finops.yml
created: 2026-06-13
description: SparkPost (now part of Bird) is the world's leading email delivery platform, providing a REST API for sending transactional and marketing emails, managing templates, tracking analytics, handling suppressions, and processing inbound email. Trusted by enterprises such as The New York Times, Adobe, and Zillow, SparkPost delivers billions of emails daily with advanced analytics, A/B testing, and real-time event streams via webhooks.
examples:
- key_count: 3
  name: Sparkpost Create Webhook Example
  slug: sparkpost-create-webhook-example
- key_count: 3
  name: Sparkpost Send Email Example
  slug: sparkpost-send-email-example
- key_count: 3
  name: Sparkpost Suppression Bulk Example
  slug: sparkpost-suppression-bulk-example
finops:
- name: Sparkpost Finops
  service_category: ''
  slug: sparkpost-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sparkpost.png
json_schemas:
- name: SparkPost Suppression Entry
  property_count: 7
  slug: sparkpost-suppression-entry
- name: SparkPost Transmission
  property_count: 8
  slug: sparkpost-transmission
- name: SparkPost Webhook
  property_count: 12
  slug: sparkpost-webhook
jsonld:
- class_count: 16
  name: Sparkpost Context
  property_count: 40
  slug: sparkpost-context
layout: provider
modified: 2026-06-13
name: SparkPost
nav: Providers
network: true
overview: 'SparkPost publishes 12 APIs on the [APIs.io](https://apis.io/) network, including DKIM Keys API, Events API, Inbound Domains API, and 9 more. Tagged areas include Email, Transactional Email, Marketing Email, Email Delivery, and SMTP.


  The SparkPost catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SparkPost''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Sparkpost Plans Pricing
  plan_count: 3
  slug: sparkpost-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Sparkpost Rate Limits
  slug: sparkpost-rate-limits
rules:
- name: SparkPost API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sparkpost-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.6
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.1
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sparkpost/refs/heads/main/screenshots/sparkpost-2026-06-20T194256.png
security:
- kind: authentication
  name: Sparkpost Authentication
  slug: sparkpost-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sparkpost Domain Security
  slug: sparkpost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sparkpost Vulnerability Disclosure
  slug: sparkpost-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: sparkpost
tags:
- Email
- Transactional Email
- Marketing Email
- Email Delivery
- SMTP
- Webhooks
- Analytics
- Templates
- Suppression List
website: https://www.sparkpost.com/
---
