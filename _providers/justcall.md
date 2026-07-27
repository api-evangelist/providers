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
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Justcall Agentic Access
  operation_count: 3
  slug: justcall-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 4
apis:
- description: REST API for placing calls, sending SMS and MMS messages, managing contacts, phone numbers, users, and call dispositions in JustCall. Authentication uses an API key and API secret passed in the Author
  name: JustCall REST API
  slug: rest-api
- description: Manage and query voice calls handled through JustCall.
  name: JustCall Calls API
  slug: justcall-calls-api
- description: Create and manage contacts in the JustCall directory.
  name: JustCall Contacts API
  slug: justcall-contacts-api
- description: Send and manage SMS/MMS messages.
  name: JustCall SMS API
  slug: justcall-sms-api
artifact_total: 9
collections:
- collection_type: open
  name: JustCall REST API
  slug: open-justcall
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/justcall-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/justcall-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/justcall-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/justcall-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/justcall-io
- group: company
  title: ''
  type: Website
  url: https://justcall.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.justcall.io/docs/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://justcall.io/developer-docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://justcall.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://justcall.io/signup
- group: operate
  title: ''
  type: Support
  url: https://help.justcall.io
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.justcall.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://justcall.io/blog/
created: '2026-05-11'
description: JustCall is a cloud-based phone system and contact center platform that provides voice calling, SMS/MMS messaging, IVR, call analytics, and contact management for small and mid-sized businesses. The platform integrates with CRMs, helpdesks, and automation tools. JustCall exposes REST APIs and webhooks for programmatically managing calls, SMS, contacts, phone numbers, and call dispositions, authenticated via API key plus API secret in headers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/justcall.png
layout: provider
modified: '2026-05-11'
name: JustCall
nav: Providers
network: true
overview: 'JustCall publishes 3 APIs on the [APIs.io](https://apis.io/) network: Calls API, Contacts API, and SMS API. Tagged areas include Voice, SMS, Cloud Phone, Contact Center, and Telephony.


  JustCall''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 50
score:
  band: thin
  composite: 34.8
  delta: 3.3
  facets:
    commercial_clarity: 18.4
    contract_quality: 56.6
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/justcall/refs/heads/main/screenshots/justcall-2026-06-20T183845.png
security:
- kind: authentication
  name: Justcall Authentication
  slug: justcall-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Justcall Domain Security
  slug: justcall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Justcall Trust Center
  slug: justcall-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, CSA STAR
slug: justcall
tags:
- Voice
- SMS
- Cloud Phone
- Contact Center
- Telephony
- Communications
website: https://justcall.io
---
