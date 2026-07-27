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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 70
  human_in_the_loop: 4
  name: Suprsend Agentic Access
  operation_count: 122
  slug: suprsend-agentic-access
  summary_line: 122 operations · 70 acting · 4 human-in-the-loop
api_count: 21
apis:
- description: The SuprSend Management API provides programmatic control over workspace assets including workflows, templates, and other SuprSend configuration resources. It uses service tokens for authentication ra
  name: SuprSend Management API
  slug: management-api
- description: The Broadcast API from SuprSend — 1 operation(s) for broadcast.
  name: SuprSend Broadcast API
  slug: suprsend-broadcast-api
- description: The Broadcast Run API from SuprSend — 1 operation(s) for broadcast run.
  name: SuprSend Broadcast Run API
  slug: suprsend-broadcast-run-api
- description: The Bulk API from SuprSend — 3 operation(s) for bulk.
  name: SuprSend Bulk API
  slug: suprsend-bulk-api
- description: The Event API from SuprSend — 5 operation(s) for event.
  name: SuprSend Event API
  slug: suprsend-event-api
- description: The Message API from SuprSend — 1 operation(s) for message.
  name: SuprSend Message API
  slug: suprsend-message-api
- description: The Object API from SuprSend — 8 operation(s) for object.
  name: SuprSend Object API
  slug: suprsend-object-api
- description: The Preference Category API from SuprSend — 4 operation(s) for preference category.
  name: SuprSend Preference Category API
  slug: suprsend-preference-category-api
- description: The Schema API from SuprSend — 3 operation(s) for schema.
  name: SuprSend Schema API
  slug: suprsend-schema-api
- description: The Subscriber List API from SuprSend — 11 operation(s) for subscriber list.
  name: SuprSend Subscriber List API
  slug: suprsend-subscriber-list-api
- description: The Template API from SuprSend — 12 operation(s) for template.
  name: SuprSend Template API
  slug: suprsend-template-api
- description: The Tenant API from SuprSend — 7 operation(s) for tenant.
  name: SuprSend Tenant API
  slug: suprsend-tenant-api
- description: The Translation API from SuprSend — 5 operation(s) for translation.
  name: SuprSend Translation API
  slug: suprsend-translation-api
- description: The Trigger API from SuprSend — 2 operation(s) for trigger.
  name: SuprSend Trigger API
  slug: suprsend-trigger-api
- description: The User API from SuprSend — 9 operation(s) for user.
  name: SuprSend User API
  slug: suprsend-user-api
- description: The Workflow API from SuprSend — 4 operation(s) for workflow.
  name: SuprSend Workflow API
  slug: suprsend-workflow-api
- description: The Workflow Run API from SuprSend — 1 operation(s) for workflow run.
  name: SuprSend Workflow Run API
  slug: suprsend-workflow-run-api
- description: The Workspace API from SuprSend — 1 operation(s) for workspace.
  name: SuprSend Workspace API
  slug: suprsend-workspace-api
- description: The Ws Api Key API from SuprSend — 2 operation(s) for ws api key.
  name: SuprSend Ws Api Key API
  slug: suprsend-ws-api-key-api
- description: The Ws Public Key API from SuprSend — 3 operation(s) for ws public key.
  name: SuprSend Ws Public Key API
  slug: suprsend-ws-public-key-api
- description: The Ws Signing Key API from SuprSend — 3 operation(s) for ws signing key.
  name: SuprSend Ws Signing Key API
  slug: suprsend-ws-signing-key-api
artifact_total: 31
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/suprsend-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/suprsend-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suprsend-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/suprsend-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.suprsend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.suprsend.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/suprsend
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/suprsend/
- group: other
  title: ''
  type: X
  url: https://x.com/suprsend
- group: company
  title: ''
  type: Blog
  url: https://www.suprsend.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.suprsend.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.suprsend.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.suprsend.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/suprsend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/suprsend-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/suprsend-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/suprsend-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/suprsend-examples.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/suprsend-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/suprsend-context.jsonld
created: '2026-06-12'
description: SuprSend is a notification infrastructure platform that enables engineering teams to build, manage, and scale multi-channel notifications through a single unified API. It supports delivery across email, SMS, push notifications, in-app inbox, WhatsApp, Slack, and Microsoft Teams without requiring separate integrations for each channel. The platform provides workflow orchestration, template management, user preference management, smart channel routing with vendor fallback, and real-time delivery logs. SuprSend also offers a Management API for programmatic control of workflows and templates, a CLI for asset synchronization, and an MCP server enabling AI agents to interact with notification infrastructure through tool calling.
finops:
- name: Suprsend Finops
  service_category: ''
  slug: suprsend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suprsend.png
json_schemas:
- name: SuprSend API Schemas
  property_count: 0
  slug: suprsend
jsonld:
- class_count: 27
  name: Suprsend Context
  property_count: 29
  slug: suprsend-context
layout: provider
modified: '2026-06-12'
name: SuprSend
nav: Providers
network: true
overview: 'SuprSend publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Broadcast API, Broadcast Run API, Bulk API, and 17 more. Tagged areas include Notifications, Multi-Channel, Email, SMS, and Push Notifications.


  The SuprSend catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SuprSend''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, code examples, and 14 more developer resources.'
plans:
- name: Suprsend Plans Pricing
  plan_count: 4
  slug: suprsend-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Suprsend Rate Limits
  slug: suprsend-rate-limits
rules:
- name: SuprSend API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: suprsend-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.2
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 67.9
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 68.4
  previous_composite: 62.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/suprsend/refs/heads/main/screenshots/suprsend-2026-06-20T194803.png
security:
- kind: authentication
  name: Suprsend Authentication
  slug: suprsend-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Suprsend Domain Security
  slug: suprsend-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Suprsend Trust Center
  slug: suprsend-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: suprsend
tags:
- Notifications
- Multi-Channel
- Email
- SMS
- Push Notifications
- In-App Inbox
- WhatsApp
- Slack
- Notification Infrastructure
- Workflow Automation
- Template Management
website: https://www.suprsend.com/
---
