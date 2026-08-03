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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: Bloomberg's primary secure messaging service for financial professionals, providing real-time message delivery, group chats, broadcast lists, and file sharing within the Bloomberg Terminal and Bloombe
  name: Bloomberg IB (Instant Bloomberg)
  slug: bloomberg-ib-service
- description: Gateway service enabling Bloomberg IB messages to be sent and received via email for communication with counterparties not on the Bloomberg network.
  name: Bloomberg Email Gateway
  slug: bloomberg-email-gateway
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-message-domain-security.yml
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
description: Bloomberg Message is the core messaging service within the Bloomberg Terminal ecosystem, enabling financial professionals to communicate securely through the Bloomberg IB (Instant Bloomberg) messaging system. It provides a compliant, archived communication channel for trading desks, asset managers, and financial institutions to exchange information, research, and trade-related messages.
features:
- description: Encrypted and authenticated messaging for financial professionals.
  name: Secure Messaging
- description: Send messages to curated broadcast lists of contacts and clients.
  name: Broadcast Lists
- description: Multi-participant discussions for teams and trading desks.
  name: Group Chats
- description: Automatic archiving of all messages for compliance and eDiscovery.
  name: Message Archiving
- description: Share documents and files securely through the messaging platform.
  name: File Transfer
- description: Access Bloomberg Message from mobile and non-Terminal devices.
  name: Bloomberg Anywhere Integration
finops:
- name: Bloomberg Message Finops
  service_category: API
  slug: bloomberg-message-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-message.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Message
nav: Providers
network: true
overview: 'Bloomberg Message publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, Financial Communication, Bloomberg IB, Compliance, and Trading Communication.


  Bloomberg Message''s developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Message Plans Pricing
  plan_count: 3
  slug: bloomberg-message-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Bloomberg Message Rate Limits
  slug: bloomberg-message-rate-limits
score:
  band: emerging
  composite: 25.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 25.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-message/refs/heads/main/screenshots/bloomberg-message-2026-06-20T173507.png
security:
- kind: domain-security
  name: Bloomberg Message Domain Security
  slug: bloomberg-message-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-message
tags:
- Messaging
- Financial Communication
- Bloomberg IB
- Compliance
- Trading Communication
- Bloomberg
use_cases:
- description: Distribute research and trade ideas from sell-side to buy-side clients.
  name: Sell-Side Distribution
- description: Communicate trade intentions and confirmations between counterparties.
  name: Trade Communication
- description: Maintain compliant records of financial communications for regulators.
  name: Compliance Records
- description: Share market commentary and analysis with clients through broadcast messages.
  name: Market Commentary
website: https://www.bloomberg.com/professional/
---
