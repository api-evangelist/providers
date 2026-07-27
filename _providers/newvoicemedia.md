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
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Subscribe to VCC event notifications delivered over HTTPS and signed with a Vonage-Signature header.
  name: Vonage Contact Center Webhooks API
  slug: vonage-contact-center-webhooks-api
artifact_total: 5
asyncapis:
- description: ''
  name: Newvoicemedia Webhooks
  slug: newvoicemedia-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.newvoicemedia.com/en-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs-vcc.atlassian.net/wiki/spaces/VCCA
- group: docs
  title: ''
  type: Documentation
  url: https://docs-vcc.atlassian.net/wiki/spaces/VCCA/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs-vcc.atlassian.net/wiki/spaces/VCCA/pages/3599630337/Trying+out+Vonage+Contact+Center+APIs
- group: auth
  title: ''
  type: Authentication
  url: authentication/newvoicemedia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/newvoicemedia-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/newvoicemedia-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/newvoicemedia-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newvoicemedia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newvoicemedia-llms.txt
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/vonage/vonage-contact-centre-apis
- group: operate
  title: ''
  type: Contact
  url: https://docs-vcc.atlassian.net/wiki/spaces/VCCA/pages/3568074802
created: '2026-07-17'
description: NewVoiceMedia is a cloud contact-center (CCaaS) platform founded in the UK and acquired by Vonage in 2018, now delivered as Vonage Contact Center (VCC). Its developer program, still published under the newvoicemedia.com domain and the VCC documentation, exposes a suite of REST APIs for managing customer interactions, agent presence and availability, conversation analytics, call and interaction content (recordings and transcripts), insights and reporting stats, PCI-compliant payments, media channels, user administration, and event webhooks. All APIs authenticate with OAuth 2.0 client-credentials, returning a short-lived Bearer token, and are served from regional API gateways at https://{region}.api.cc.vonage.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newvoicemedia.png
layout: provider
modified: '2026-07-25'
name: NewVoiceMedia
nav: Providers
network: true
overview: 'NewVoiceMedia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Contact Center, CCaaS, and Communications.


  The NewVoiceMedia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NewVoiceMedia''s developer surface includes documentation, getting-started guide, authentication, and 9 more developer resources.'
random_paper: 16
scopes:
- name: Newvoicemedia Scopes
  scope_count: 10
  slug: newvoicemedia-scopes
  summary_line: 10 scopes · clientCredentials
score:
  band: emerging
  composite: 24.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 22.6
    developer_ergonomics: 43.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 24.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Newvoicemedia Authentication
  slug: newvoicemedia-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Newvoicemedia Domain Security
  slug: newvoicemedia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: newvoicemedia
tags:
- Company
- Cloud
- Contact Center
- CCaaS
- Communications
- Customer Experience
- Telephony
- Analytics
website: https://www.newvoicemedia.com/en-us
---
