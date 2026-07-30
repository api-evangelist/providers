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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Updox Agentic Access
  operation_count: 10
  slug: updox-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 12
apis:
- description: Send and receive HISP Direct secure messages between providers, with Direct Messaging webhooks for delivery/receipt events. Endpoints modeled from Updox's documented Direct Messaging functional area a
  name: Updox Direct Messaging API
  slug: updox-direct-messaging-api
- description: Manage secure two-way patient conversations (secure text/SMS threads), with Secure Conversation Management webhooks for new-message events. Endpoints modeled from Updox's documented functional area an
  name: Updox Secure Conversation API
  slug: updox-secure-conversation-api
- description: Create, retrieve, and route documents within the Updox inbox, with Document Management webhooks for document lifecycle events. Endpoints modeled from Updox's documented functional area and webhook cat
  name: Updox Document Management API
  slug: updox-document-management-api
- description: Create and update patient records and demographics that anchor reminders, forms, portal access, and conversations, with Patient Management webhooks. Endpoints modeled from Updox's documented functiona
  name: Updox Patient Management API
  slug: updox-patient-management-api
- description: Provision and manage patient portal access and portal messaging, with Patient Portal webhooks for portal activity. Endpoints modeled from Updox's documented functional area and webhook catalog.
  name: Updox Patient Portal API
  slug: updox-patient-portal-api
- description: Schedule and manage appointment reminders and broadcast messages across text, voice, and email, with Reminders webhooks for confirmation/response events. Endpoints modeled from Updox's documented func
  name: Updox Reminders API
  slug: updox-reminders-api
- description: Send electronic intake and consent forms to patients and receive completed submissions, with Forms webhooks for completion events. Endpoints modeled from Updox's documented functional area and webhook
  name: Updox Forms API
  slug: updox-forms-api
- description: Administer accounts, users, and application connectivity, including the tiered Ping health-check actions (Ping, PingWithApplicationAuth, PingWithAccountAuth, PingWithAuth) and Account Management webho
  name: Updox Account Management API
  slug: updox-account-management-api
- description: Practice-level contact/address-book actions.
  name: Updox Address Book API
  slug: updox-address-book-api
- description: Inbound electronic fax retrieval.
  name: Updox Faxing API
  slug: updox-faxing-api
- description: Connectivity and authentication health checks.
  name: Updox Ping API
  slug: updox-ping-api
- description: Telehealth video call actions.
  name: Updox Video Chat API
  slug: updox-video-chat-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/updox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/updox-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/updox
- group: company
  title: ''
  type: Website
  url: https://www.updox.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.updox.com/help/public-api
- group: docs
  title: ''
  type: APIReference
  url: https://updoxqa.com/api/newio
- group: operate
  title: ''
  type: Support
  url: https://www.updox.com/support/
- group: commercial
  title: ''
  type: Plans
  url: plans/updox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/updox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/updox-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.updox.com
created: '2026-07-04'
description: Updox is a healthcare communication and patient engagement platform for in-person and virtual care, offering a single inbox for secure/direct messaging, electronic fax, document management, patient reminders, forms, and telehealth video chat, integrated with 100+ EHR and pharmacy management systems. Updox has been a part of EverCommerce (NASDAQ - EVCM) since its December 2020 acquisition. Updox exposes a documented public/partner API (an IO Docs explorer plus a knowledge-base API reference) used mainly by EHR, pharmacy, and integration partners; API access is granted via application credentials rather than open self-serve signup, and much of the endpoint surface below is modeled from Updox's documented functional areas and webhook catalog.
finops:
- name: Updox Finops
  service_category: Healthcare Communication and Patient Engagement
  slug: updox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/updox.png
layout: provider
modified: '2026-07-04'
name: Updox
nav: Providers
network: true
overview: 'Updox publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Address Book API, Faxing API, Ping API, and 1 more. Tagged areas include Healthcare, Patient Engagement, Secure Messaging, Electronic Fax, and Telehealth.


  Updox''s developer surface includes documentation, API reference, support, engineering blog, and 7 more developer resources.'
plans:
- name: Updox Plans Pricing
  plan_count: 4
  slug: updox-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 3
  name: Updox Rate Limits
  slug: updox-rate-limits
score:
  band: thin
  composite: 31.9
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Updox Domain Security
  slug: updox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: updox
tags:
- Healthcare
- Patient Engagement
- Secure Messaging
- Electronic Fax
- Telehealth
- Document Management
- HIPAA
- EverCommerce
website: https://www.updox.com
---
