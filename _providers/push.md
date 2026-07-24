---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 15.4
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'Token-authenticated REST API to interact with the Cendyn CRM / PUSHTech platform: query and manage account data, apps, campaigns, deliveries, contacts, and activities, and receive HMAC-signed webhook '
  name: Cendyn CRM (PUSHTech) REST API
  slug: cendyn-crm-pushtech-rest-api
artifact_total: 4
asyncapis:
- description: ''
  name: Push Webhooks
  slug: push-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://pushtech.com
- group: start
  title: ''
  type: DeveloperPortal
  url: http://developers.pushtech.com
- group: docs
  title: ''
  type: Documentation
  url: http://developers.pushtech.com/api
- group: docs
  title: ''
  type: APIReference
  url: http://developers.pushtech.com/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: http://developers.pushtech.com/api/authentication
- group: operate
  title: ''
  type: Support
  url: http://help.pushtech.com
- group: company
  title: ''
  type: Blog
  url: http://blog.pushtech.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pushtech.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pushtech.com/privacy_policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/push-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/push-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/push-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/push-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/push-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/push-domain-security.yml
created: '2026-07-17'
description: Push (PUSHTech, now part of Cendyn) is a CRM, marketing automation, sales, and support platform focused on the hospitality, retail, ecommerce, and marketplace sectors, with deep specialization in hotel guest-journey automation used by more than 1,500 hotels. The platform unifies customer databases and orchestrates pre-stay, during-stay, and post-stay guest communications across email, SMS, and in-app / web push notification channels. Push exposes a token-authenticated REST API (Cendyn CRM API at api.eu.cendyncrm.com) for account, apps, campaign, delivery, contact, and activity data, an HMAC-signed webhooks surface for activity, delivery, and contact events, and a first-party JavaScript Web SDK for browser tracking and web push. Originally added to the API Evangelist network as a 500 Global portfolio lead, this profile has been enriched from the public developer portal.
image: https://pushtech.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Push
nav: Providers
network: true
overview: 'Push publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Marketing Automation, Hospitality, and Hotels.


  The Push catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Push''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 40
score:
  band: thin
  composite: 31.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 22.6
    developer_ergonomics: 58.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Push Authentication
  slug: push-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Push Domain Security
  slug: push-domain-security
  summary_line: TLSv1.3 · DMARC
slug: push
tags:
- Company
- CRM
- Marketing Automation
- Hospitality
- Hotels
- Guest Experience
- Email
- SMS
- Push Notifications
- Webhooks
website: https://pushtech.com
---
