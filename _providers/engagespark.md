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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Engagespark Agentic Access
  operation_count: 23
  slug: engagespark-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 7
apis:
- description: The Balance API from engageSPARK — 1 operation(s) for balance.
  name: engageSPARK Balance API
  slug: engagespark-balance-api
- description: The Campaigns API from engageSPARK — 2 operation(s) for campaigns.
  name: engageSPARK Campaigns API
  slug: engagespark-campaigns-api
- description: The Contacts API from engageSPARK — 2 operation(s) for contacts.
  name: engageSPARK Contacts API
  slug: engagespark-contacts-api
- description: The Files API from engageSPARK — 2 operation(s) for files.
  name: engageSPARK Files API
  slug: engagespark-files-api
- description: The SMS API from engageSPARK — 4 operation(s) for sms.
  name: engageSPARK SMS API
  slug: engagespark-sms-api
- description: The Top-Up API from engageSPARK — 3 operation(s) for top-up.
  name: engageSPARK Top-Up API
  slug: engagespark-top-up-api
- description: The WhatsApp API from engageSPARK — 3 operation(s) for whatsapp.
  name: engageSPARK WhatsApp API
  slug: engagespark-whatsapp-api
artifact_total: 11
asyncapis:
- description: ''
  name: Engagespark Webhooks
  slug: engagespark-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/engagespark-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/engagespark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://engagespark.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.engagespark.com/support/how-can-i-use-your-api/
- group: docs
  title: ''
  type: Documentation
  url: https://openapi.engagespark.com/
- group: docs
  title: ''
  type: APIReference
  url: https://openapi.engagespark.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.engagespark.com/support/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.engagespark.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.engagespark.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.engagespark.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.engagespark.com/register
- group: start
  title: ''
  type: Login
  url: https://app.engagespark.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.engagespark.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.engagespark.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/engagespark
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/engagespark-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: engageSPARK is a mobile messaging and engagement platform for reaching hard-to-reach populations in low- and middle-income countries at scale. It lets NGOs, researchers, microfinance institutions, and businesses run SMS, automated voice (IVR), WhatsApp, and pre-paid airtime top-up campaigns across 180+ countries without writing code, or programmatically through its HTTP API. The engageSPARK API (api.engagespark.com, v1) exposes token-authenticated endpoints for sending SMS, WhatsApp, and airtime top-ups, managing contacts and organizations, subscribing and unsubscribing contacts to voice and SMS campaigns, reading message and top-up history, checking organization balance, and managing files. Incoming-SMS and campaign-action webhooks let the platform push survey responses and inbound messages into external systems such as Salesforce or Qualtrics.
image: https://www.engagespark.com/wp-content/uploads/2017/03/engagespark_logo_small.png
layout: provider
modified: '2026-07-19'
name: engageSPARK
nav: Providers
network: true
overview: 'engageSPARK publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Campaigns API, Contacts API, and 4 more. Tagged areas include Company, Messaging, SMS, Voice, and WhatsApp.


  The engageSPARK catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  engageSPARK''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 10 more developer resources.'
random_paper: 54
score:
  band: thin
  composite: 41.6
  delta: -5.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 70.9
    developer_ergonomics: 42.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/engagespark/refs/heads/main/screenshots/engagespark-2026-07-25T213341.png
security:
- kind: authentication
  name: Engagespark Authentication
  slug: engagespark-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Engagespark Domain Security
  slug: engagespark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: engagespark
tags:
- Company
- Messaging
- SMS
- Voice
- WhatsApp
- Airtime
- Communications
- CPaaS
- Surveys
- International Development
website: https://engagespark.com
---
