---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.7
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The HipChat REST API v2 was the primary developer surface for the team chat platform, exposing rooms, users, messages, notifications, emoticons, OAuth sessions, add-on capabilities, and webhook manage
  name: HipChat REST API v2
  slug: hipchat-rest-api-v2
- description: 'Event-driven webhook delivery from HipChat rooms. Webhooks could be registered via the REST API or declared in an add-on descriptor. Each delivery included a JWT-signed signed_request query parameter '
  name: HipChat Webhooks API
  slug: hipchat-webhooks-api
artifact_total: 22
asyncapis:
- description: Event-driven webhook deliveries from Atlassian's discontinued HipChat platform. Every webhook POST included a `signed_request` query parameter containing a JWT that the receiver was expected to verify
  name: HipChat Webhooks API
  slug: hipchat-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/hipchat-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hipchat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hipchat-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/server/hipchat/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.atlassian.com/server/hipchat/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hipchat
- group: company
  title: Atlassian-Slack partnership announcement (July 26, 2018)
  type: Blog
  url: https://www.atlassian.com/blog/announcements/new-atlassian-slack-partnership
- group: other
  title: HipChat → Slack migration (sunset February 15, 2019)
  type: Sunset
  url: https://www.atlassian.com/migration/move-from-hipchat-to-slack
- group: commercial
  title: Historical pricing (no longer in market)
  type: Pricing
  url: plans/hipchat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hipchat-rate-limits.yml
- group: commercial
  title: Historical FinOps record (no longer billable)
  type: FinOps
  url: finops/hipchat-finops.yml
created: 2024-01-01 00:00:00+00:00
deprecated: true
deprecated_note: HipChat has been discontinued. Retained for historical reference.
description: HipChat was Atlassian's team chat platform, providing persistent group chat, video, file sharing, and an extensive integration ecosystem. Atlassian discontinued HipChat Cloud, Stride, HipChat Server, and HipChat Data Center on February 15, 2019 after selling the IP to Slack in July 2018 and committing to a joint migration path for customers. This profile preserves the historical API surface (REST API v2, Webhooks, Connect add-on framework) for archival and migration-pattern research; no live endpoints remain.
examples:
- key_count: 13
  name: Hipchat Room Example
  slug: hipchat-room-example
- key_count: 4
  name: Hipchat Room Message Webhook Example
  slug: hipchat-room-message-webhook-example
- key_count: 2
  name: Hipchat Send Notification Example
  slug: hipchat-send-notification-example
- key_count: 15
  name: Hipchat User Example
  slug: hipchat-user-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hipchat.png
json_schemas:
- name: HipChat Message
  property_count: 10
  slug: hipchat-message
- name: HipChat Room
  property_count: 13
  slug: hipchat-room
- name: HipChat User
  property_count: 15
  slug: hipchat-user
- name: HipChat Webhook
  property_count: 7
  slug: hipchat-webhook
json_structures:
- name: Hipchat Message Structure
  property_count: 8
  slug: hipchat-message-structure
- name: Hipchat Room Structure
  property_count: 11
  slug: hipchat-room-structure
jsonld:
- class_count: 27
  name: Hipchat Context
  property_count: 12
  slug: hipchat-context
layout: provider
modified: '2026-05-23'
name: HipChat
nav: Providers
network: true
overview: 'HipChat publishes 2 APIs on the [APIs.io](https://apis.io/) network: REST API v2 and Webhooks API. Tagged areas include Chat, Messaging, Collaboration, Team Communication, and Sunset.


  The HipChat catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  HipChat''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Hipchat Plans Pricing
  plan_count: 4
  slug: hipchat-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Hipchat Rate Limits
  slug: hipchat-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: HipChat API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: hipchat-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: HipChat API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hipchat-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: HipChat API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 4
  slug: hipchat-rest-api-rules
score:
  band: developing
  composite: 43.3
  delta: -5.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 11.4
    contract_quality: 74.4
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 11.4
    operational_transparency: 23.7
  previous_composite: 48.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/hipchat/refs/heads/main/screenshots/hipchat-2026-06-20T182747.png
security:
- kind: domain-security
  name: Hipchat Domain Security
  slug: hipchat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hipchat Vulnerability Disclosure
  slug: hipchat-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Hipchat Trust Center
  slug: hipchat-trust-center
  summary_line: FedRAMP
slug: hipchat
tags:
- Chat
- Messaging
- Collaboration
- Team Communication
- Sunset
- Historical
- Atlassian
- Webhooks
website: https://developer.atlassian.com/server/hipchat/
---
