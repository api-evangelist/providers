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
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Bird Com Agentic Access
  operation_count: 21
  slug: bird-com-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 6
apis:
- description: Manage workspace channels and channel media.
  name: Bird Channels API
  slug: bird-com-channels-api
- description: Manage workspace contacts and lists.
  name: Bird Contacts API
  slug: bird-com-contacts-api
- description: Manage threaded omnichannel conversations.
  name: Bird Conversations API
  slug: bird-com-conversations-api
- description: Predecessor MessageBird REST API (rest.messagebird.com).
  name: Bird Legacy MessageBird API
  slug: bird-com-legacy-messagebird-api
- description: Send and receive messages across channels.
  name: Bird Messaging API
  slug: bird-com-messaging-api
- description: Discover, purchase, and manage phone numbers.
  name: Bird Numbers API
  slug: bird-com-numbers-api
artifact_total: 15
collections:
- collection_type: open
  name: Bird API
  slug: open-bird-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bird-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bird-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bird-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bird-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bird-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/messagebird
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bird
- group: company
  title: ''
  type: Website
  url: https://bird.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bird.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/bird-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bird-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bird-com-finops.yml
created: '2026-06-20'
description: Bird (formerly MessageBird) is an omnichannel CRM for marketing, service, and payments. Its REST APIs at https://api.bird.com let businesses send and receive messages across SMS, WhatsApp, email, and voice through a unified Channels and Conversations interface, manage contacts and phone numbers, and migrate from the legacy MessageBird REST API at https://rest.messagebird.com.
finops:
- name: Bird Com Finops
  service_category: Communications and Messaging
  slug: bird-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bird-com.png
layout: provider
modified: '2026-06-20'
name: Bird
nav: Providers
network: true
overview: 'Bird publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Contacts API, Conversations API, and 3 more. Tagged areas include CRM, Messaging, SMS, WhatsApp, and Email.


  Bird''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Bird Com Plans Pricing
  plan_count: 4
  slug: bird-com-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 6
  name: Bird Com Rate Limits
  slug: bird-com-rate-limits
score:
  band: thin
  composite: 40.6
  delta: 3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 49.6
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bird-com/refs/heads/main/screenshots/bird-com-2026-06-20T173301.png
security:
- kind: authentication
  name: Bird Com Authentication
  slug: bird-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bird Com Domain Security
  slug: bird-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bird Com Vulnerability Disclosure
  slug: bird-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Bird Com Trust Center
  slug: bird-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: bird-com
tags:
- CRM
- Messaging
- SMS
- WhatsApp
- Email
- Voice
- Omnichannel
- CPaaS
website: https://bird.com/
---
