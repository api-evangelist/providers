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
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 22.1
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: REST/JSON API to programmatically administer the Push platform (accounts, apps, findings, integrations) plus webhooks for real-time platform events.
  name: Push Security REST API v1
  slug: push-security-rest-api-v1
artifact_total: 6
asyncapis:
- description: ''
  name: Push Security Webhooks
  slug: push-security-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://pushsecurity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pushsecurity.com/help/audience/engineering/rest-v1
- group: docs
  title: ''
  type: Documentation
  url: https://pushsecurity.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://pushsecurity.com/help/audience/engineering/rest-v1
- group: start
  title: ''
  type: GettingStarted
  url: https://pushsecurity.com/help/audience/administrators/docs/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://pushsecurity.com/help
- group: operate
  title: ''
  type: Support
  url: https://pushsecurity.com/contact
- group: company
  title: ''
  type: Blog
  url: https://pushsecurity.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pushsecurity.com/pricing
- group: start
  title: ''
  type: Login
  url: https://pushsecurity.com/login
- group: start
  title: ''
  type: SignUp
  url: https://pushsecurity.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pushsecurity.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pushsecurity.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pushsecurity
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pushsecurity.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/push-security-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.pushsecurity.com/
- group: auth
  title: ''
  type: Security
  url: https://pushsecurity.com/.well-known/security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/push-security-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/push-security-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/push-security-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/push-security-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/push-security-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/push-security-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/push-security-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/push-security-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/push-security-vulnerability-disclosure.yml
created: '2026-07-17'
description: Push Security is an AI-native browser security platform that deploys as a lightweight enterprise browser extension to every employee, giving security teams real-time telemetry, autonomous threat-hunting agents, and deep browser visibility across the full identity and browser attack surface. From the browser, Push tracks logins, AI-tool usage, and identity events to stop advanced identity attacks (account takeover, zero-day phishing, ClickFix, malicious OAuth integrations, session hijacking), discover shadow AI and shadow SaaS, harden unmanaged identities, and accelerate incident response. Push exposes a REST API (v1) and webhooks to programmatically administer the platform and forward events to SIEM/SOAR and ticketing systems. Backed by GV and Redpoint Ventures.
image: https://pushsecurity.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Push Security
nav: Providers
network: true
overview: 'Push Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Security, Identity, and Browser Security.


  The Push Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Push Security''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 21
score:
  band: thin
  composite: 42.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 22.6
    developer_ergonomics: 52.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 42.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Push Security Authentication
  slug: push-security-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Push Security Domain Security
  slug: push-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Push Security Vulnerability Disclosure
  slug: push-security-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Push Security Trust Center
  slug: push-security-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27701, GDPR, Cyber Essentials
slug: push-security
tags:
- Company
- Enterprise
- Security
- Identity
- Browser Security
- SaaS Security
- Cybersecurity
- Threat Detection
- SIEM
website: https://pushsecurity.com
---
