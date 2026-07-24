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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 32.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'Form-encoded REST API for phone verification and OTP: issue a session token, normalize a phone number, send a pincode over SMS or voice, and verify the user-entered code. Responses carry status plus p'
  name: RingCaptcha Verification API
  slug: ringcaptcha-verification-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://ringcaptcha.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.ringcaptcha.com/docs/web
- group: docs
  title: ''
  type: Documentation
  url: https://my.ringcaptcha.com/docs/web
- group: docs
  title: ''
  type: APIReference
  url: https://ringcaptcha.notion.site/Dev-Docs-e2af75c9765349848ad53c8601a8217f
- group: company
  title: ''
  type: Blog
  url: https://blog.ringcaptcha.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ringcaptcha
- group: commercial
  title: ''
  type: Pricing
  url: https://ringcaptcha.com/plans
- group: start
  title: ''
  type: SignUp
  url: https://my.ringcaptcha.com/login
- group: operate
  title: ''
  type: Support
  url: mailto:hello@ringcaptcha.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ringcaptcha.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ringcaptcha.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/thrivecom-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thrivecom-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thrivecom-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/thrivecom-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/thrivecom-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thrivecom-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thrivecom-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thrivecom-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thrivecom-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thrivecom-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thrivecom-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ringcaptcha.com/privacy-policy
created: '2026-07-17'
description: RingCaptcha, operated by ThriveCom, is a phone-verification and two-factor authentication (2FA) platform that helps businesses confirm real users and block fraud. It delivers one-time passcodes over SMS, voice, WhatsApp and missed-call (Blink) verification, normalizes and validates phone numbers to E.164, and returns fraud, carrier and device metadata to filter fake signups, bots and spam leads. Developers integrate through a simple form-encoded REST API at api.ringcaptcha.com, authenticated with per-application api_key, secret_key and app_key credentials, plus official client SDKs for Node.js, Python, PHP, Ruby, C#, Android, iOS and WordPress. RingCaptcha was surfaced as a 500 Global portfolio company and profiled through the API Evangelist enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thrivecom.png
layout: provider
mcp_servers:
- description: ''
  name: thrivecom-mcp.yml
  slug: thrivecom-mcpyml
modified: '2026-07-21'
name: RingCaptcha (ThriveCom)
nav: Providers
network: true
overview: 'RingCaptcha (ThriveCom) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Two-Factor Authentication, Phone Verification, One-Time Passcode, and SMS.


  RingCaptcha (ThriveCom)''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, support, authentication, and 16 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 31.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Thrivecom Authentication
  slug: thrivecom-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Thrivecom Domain Security
  slug: thrivecom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thrivecom
tags:
- Company
- Two-Factor Authentication
- Phone Verification
- One-Time Passcode
- SMS
- Voice
- Fraud Prevention
- Identity Verification
- Authentication
website: https://ringcaptcha.com
---
