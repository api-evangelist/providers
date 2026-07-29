---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: AsyncAPI 2.6 description of Talkdesk's publicly documented outbound webhook surface, covering the Events API (partner-app lifecycle), the Webhook Trigger API (Talkdesk Connections triggers for call/ag
  name: Talkdesk Webhook Surface
  slug: webhooks
artifact_total: 5
asyncapis:
- description: AsyncAPI 2.6 description of Talkdesk's publicly documented outbound webhook surface. Talkdesk does not publish a single unified "Subscriptions Service" catalog of events such as call_started / call_en
  name: Talkdesk Webhook Surface
  slug: talkdesk-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/talkdesk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talkdesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.talkdesk.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.talkdesk.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.talkdesk.com
- group: operate
  title: ''
  type: Support
  url: https://support.talkdesk.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.talkdesk.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.talkdesk.com/terms-of-service/privacy-notice/
- group: company
  title: ''
  type: Blog
  url: https://www.talkdesk.com/blog/
created: '2026-05-30'
description: 'Talkdesk is a cloud contact center platform with Customer Experience Automation (CXA) capabilities including omnichannel engagement, workforce engagement management, quality management, analytics, and a marketplace of partner integrations. The Talkdesk developer surface exposes REST APIs and webhook delivery across three documented webhook services: the Events API (partner-app lifecycle events signed with ECDSA), the Webhook Trigger API (Talkdesk Connections triggers for call, agent, contact, and note events), and the Automated Notifications bridge for Digital Connect (DCE). This index currently models the webhook surface as an AsyncAPI 2.6 document.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talkdesk.png
layout: provider
modified: '2026-05-30'
name: Talkdesk
nav: Providers
network: true
overview: 'Talkdesk publishes 1 API on the [APIs.io](https://apis.io/) network: Webhook Surface. Tagged areas include Contact Center, CCaaS, Voice, Webhooks, and Events.


  The Talkdesk catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Talkdesk''s developer surface includes documentation, support, engineering blog, and 6 more developer resources.'
random_paper: 41
rules:
- name: Talkdesk API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: talkdesk-asyncapi-spectral-rules
score:
  band: thin
  composite: 33.3
  delta: 0.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 54.3
    developer_ergonomics: 23.9
    discoverability: 59.3
    governance: 47.9
    operational_transparency: 0.0
  previous_composite: 32.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/talkdesk/refs/heads/main/screenshots/talkdesk-2026-06-20T194911.png
security:
- kind: domain-security
  name: Talkdesk Domain Security
  slug: talkdesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Talkdesk Vulnerability Disclosure
  slug: talkdesk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: talkdesk
tags:
- Contact Center
- CCaaS
- Voice
- Webhooks
- Events
- Telephony
- Customer Experience
- Digital Connect
- AppConnect
website: https://www.talkdesk.com
---
