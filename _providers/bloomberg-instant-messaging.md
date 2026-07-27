---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: 'Programmatic access to Bloomberg''s secure IB messaging network for sending and receiving messages within the Bloomberg Terminal ecosystem. Supports integration with trading and compliance systems for '
  name: Bloomberg IB Messaging API
  slug: bloomberg-ib-api
- description: Bloomberg's enterprise communication platform extending the Bloomberg messaging network to broader enterprise connectivity, enabling compliant communication with financial counterparties outside the B
  name: Bloomberg B-Chat
  slug: bloomberg-bchat
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-instant-messaging-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bloomberg.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg Instant Messaging (IB) is a secure, compliant messaging platform embedded in the Bloomberg Terminal and accessible via Bloomberg Anywhere. It enables real-time communication between financial professionals globally, with message archiving, compliance monitoring, and integration capabilities. Bloomberg also provides B-Chat for broader enterprise messaging connectivity.
features:
- description: End-to-end secure messaging between financial professionals on the Bloomberg network.
  name: Secure Messaging
- description: Automatic message archiving for compliance and regulatory requirements.
  name: Message Archiving
- description: Supervision tools for monitoring and reviewing communications.
  name: Compliance Controls
- description: Multi-participant group chats and chat rooms for financial discussions.
  name: Group Chats
- description: Secure file and document sharing within the messaging platform.
  name: File Sharing
- description: Access Bloomberg messaging from mobile and remote devices via Bloomberg Anywhere.
  name: Bloomberg Anywhere Access
finops:
- name: Bloomberg Instant Messaging Finops
  service_category: API
  slug: bloomberg-instant-messaging-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-instant-messaging.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Instant Messaging
nav: Providers
network: true
overview: 'Bloomberg Instant Messaging publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, Instant Messaging, Compliance, Financial Communication, and Bloomberg IB.


  Bloomberg Instant Messaging''s developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Instant Messaging Plans Pricing
  plan_count: 3
  slug: bloomberg-instant-messaging-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Bloomberg Instant Messaging Rate Limits
  slug: bloomberg-instant-messaging-rate-limits
score:
  band: emerging
  composite: 28.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 28.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-instant-messaging/refs/heads/main/screenshots/bloomberg-instant-messaging-2026-06-20T173443.png
security:
- kind: domain-security
  name: Bloomberg Instant Messaging Domain Security
  slug: bloomberg-instant-messaging-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-instant-messaging
tags:
- Messaging
- Instant Messaging
- Compliance
- Financial Communication
- Bloomberg IB
- Bloomberg
use_cases:
- description: Negotiate trades and discuss pricing in real time with counterparties.
  name: Trade Negotiation
- description: Share research reports and market insights with clients and colleagues.
  name: Research Distribution
- description: Archive and monitor communications for regulatory compliance.
  name: Compliance Surveillance
- description: Maintain compliant communication records with institutional clients.
  name: Client Communication
website: https://www.bloomberg.com/professional/
---
