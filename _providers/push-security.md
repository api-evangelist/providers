---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
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
random_paper: 16
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 44.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/push-security/refs/heads/main/screenshots/push-security-2026-08-17T081406.png
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
