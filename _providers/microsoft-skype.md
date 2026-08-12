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
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: Skype URIs provide a mechanism for launching Skype actions from web pages and applications. Developers can create links that initiate calls, video calls, and chat conversations with specified Skype us
  name: Skype URIs API
  slug: skype-uris
- description: Azure Communication Services (successor to Skype developer APIs) provides cloud-based communication APIs for voice calling, video calling, SMS messaging, email, and chat. It powers Microsoft Teams int
  name: Azure Communication Services
  slug: communication-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-skype-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skype
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://www.skype.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/communication-services/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/communication-services/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=skype_for_business_blog
created: '2024-01-01'
description: Microsoft Skype provides communication APIs for voice, video, and messaging. For new development, Azure Communication Services is the recommended successor, providing cloud-based communication capabilities including calling, SMS, chat, and email.
finops:
- name: Microsoft Skype Finops
  service_category: API
  slug: microsoft-skype-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-skype.png
layout: provider
modified: '2026-04-28'
name: Microsoft Skype
nav: Providers
network: true
overview: 'Microsoft Skype publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Communication, Messaging, Microsoft, Video, and Voice.


  Microsoft Skype''s developer surface includes developer portal, documentation, pricing, support, engineering blog, and 5 more developer resources.'
plans:
- name: Microsoft Skype Plans Pricing
  plan_count: 3
  slug: microsoft-skype-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 5
  name: Microsoft Skype Rate Limits
  slug: microsoft-skype-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: -6.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-skype/refs/heads/main/screenshots/microsoft-skype-2026-06-20T185532.png
security:
- kind: domain-security
  name: Microsoft Skype Domain Security
  slug: microsoft-skype-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-skype
tags:
- Communication
- Messaging
- Microsoft
- Video
- Voice
website: https://www.skype.com/
---
