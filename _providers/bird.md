---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 6
  human_in_the_loop: 0
  name: Bird Agentic Access
  operation_count: 16
  slug: bird-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 10
apis:
- description: Sync customer data from multiple sources in real time to build a 360-degree customer view. Manage contacts, lists, segmentation, and profile enrichment programmatically.
  name: Bird Customer Data API
  slug: bird-customer-data-api
- description: Search, purchase, and manage phone numbers inventory programmatically. Supports number search by country and capability, number porting, and inventory management at scale.
  name: Bird Phone Numbers API
  slug: bird-phone-numbers-api
- description: Verify the identity of your customers programmatically to enable additional services such as two-factor authentication and fraud prevention across SMS and voice channels.
  name: Bird Identity Verification API
  slug: bird-identity-verification-api
- description: Create and manage dynamic customer interactions across multiple channels. Build customer journeys, flows, and automated sequences that adapt to customer actions.
  name: Bird Touchpoints API
  slug: bird-touchpoints-api
- description: Programmatically manage your Bird organization, workspaces, users, roles, and access keys. Configure SSO and manage multi-workspace enterprise deployments.
  name: Bird Accounts API
  slug: bird-accounts-api
- description: FAQ dataset management and answer prediction operations.
  name: Bird FAQ API
  slug: bird-faq-api
- description: Intent recognition and dataset management operations.
  name: Bird Intent API
  slug: bird-intent-api
- description: Language detection operations.
  name: Bird LanguageDetection API
  slug: bird-languagedetection-api
- description: Named entity recognition operations.
  name: Bird NamedEntityRecognition API
  slug: bird-namedentityrecognition-api
- description: MessageBird’s SMS API allows you to send and receive SMS messages to and from any country in the world through a REST API. Each message is identified by a unique random ID so that users can always che
  name: Bird SMS Messaging API
  slug: bird-sms-messaging-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bird-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bird-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bird-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bird-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bird-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://bird.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bird.com/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/messagebird
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/birdhq/
- group: company
  title: ''
  type: Blog
  url: https://bird.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bird.com/en-us/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bird.com
- group: other
  title: ''
  type: X
  url: https://x.com/messagebird
- group: commercial
  title: ''
  type: Plans
  url: plans/bird-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bird-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bird-finops.yml
created: '2026-06-13'
description: Bird (formerly MessageBird) is an omnichannel customer communications platform offering REST APIs for email, SMS, WhatsApp, RCS, push notifications, voice, and data management. Trusted by more than 450,000 developers, Bird provides enterprise-grade connectivity through a global carrier network alongside a full customer engagement and marketing automation suite.
examples:
- key_count: 4
  name: Bird Detect Language Example
  slug: bird-detect-language-example
- key_count: 4
  name: Bird Predict Intent Example
  slug: bird-predict-intent-example
- key_count: 4
  name: Bird Send Sms Example
  slug: bird-send-sms-example
finops:
- name: Bird Finops
  service_category: ''
  slug: bird-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bird.png
json_schemas:
- name: BirdContact
  property_count: 6
  slug: bird-contact
- name: BirdMessage
  property_count: 15
  slug: bird-message
jsonld:
- class_count: 53
  name: Bird Context
  property_count: 7
  slug: bird-context
layout: provider
modified: '2026-06-13'
name: Bird
nav: Providers
network: true
overview: 'Bird publishes 5 APIs on the [APIs.io](https://apis.io/) network, including FAQ API, Intent API, LanguageDetection API, and 2 more. Tagged areas include Communications, SMS, Email, WhatsApp, and Voice.


  The Bird catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bird''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Bird Plans Pricing
  plan_count: 3
  slug: bird-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Bird Rate Limits
  slug: bird-rate-limits
rules:
- name: Bird API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bird-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.8
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 69.0
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 54.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bird/refs/heads/main/screenshots/bird-2026-06-20T173301.png
security:
- kind: authentication
  name: Bird Authentication
  slug: bird-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bird Domain Security
  slug: bird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bird Vulnerability Disclosure
  slug: bird-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Bird Trust Center
  slug: bird-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: bird
tags:
- Communications
- SMS
- Email
- WhatsApp
- Voice
- Messaging
- Omnichannel
- Customer Engagement
website: https://bird.com
---
