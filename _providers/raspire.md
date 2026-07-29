---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/raspire-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://raspire.com/trust
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/raspire-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://raspire.com/vulnerability-disclosure
- group: company
  title: ''
  type: Website
  url: https://raspire.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raspire-domain-security.yml
created: '2026-07-17'
description: Raspire (RASPIRE) provides runtime security for mobile applications, positioning itself as the first line of defense for Android and iOS apps against AI-powered fraud attacks, API abuse, and runtime threats. Developers upload compiled apps (APK/IPA) and Raspire automatically hardens them with anti-fraud protection, app integrity verification, reverse-engineering prevention, and API protection, without requiring changes to application source code. The platform gives security teams real-time visibility into threats and blocks attacks in real time, and can integrate with existing SIEM systems and application monitoring platforms as part of a CI/CD pipeline. Raspire is a Y Combinator company. As surfaced to the API Evangelist network it does not publish a public developer API, OpenAPI specification, or SDKs; this profile captures its identity and probed domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raspire.png
layout: provider
modified: '2026-07-20'
name: Raspire
nav: Providers
network: true
overview: Raspire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Mobile, Application Security, and Runtime Application Self-Protection.
random_paper: 65
score:
  band: minimal
  composite: 9.5
  delta: -1.8
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Raspire Domain Security
  slug: raspire-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Raspire Vulnerability Disclosure
  slug: raspire-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Raspire Trust Center
  slug: raspire-trust-center
  summary_line: SOC 2, HIPAA
slug: raspire
tags:
- Company
- Security
- Mobile
- Application Security
- Runtime Application Self-Protection
- RASP
- Fraud Prevention
- API Security
website: https://raspire.com/
---
