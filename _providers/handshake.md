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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Read-only, institution-scoped EDU API for career-services data: applications, appointments, career fairs, jobs, postings, qualifications, and meetings. Authenticates via x-api-key header; supports pag'
  name: Handshake EDU API
  slug: handshake-edu-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.joinhandshake.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://edu-api.joinhandshake.com:444/
- group: docs
  title: ''
  type: Documentation
  url: https://support.joinhandshake.com/hc/en-us/sections/31055822163351-API
- group: docs
  title: ''
  type: APIReference
  url: https://support.joinhandshake.com/hc/en-us/articles/35762729693719-EDU-API-Endpoint-Definitions
- group: start
  title: ''
  type: GettingStarted
  url: https://support.joinhandshake.com/hc/en-us/articles/31061076506391-Getting-Started-with-EDU-API
- group: operate
  title: ''
  type: Support
  url: https://support.joinhandshake.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://joinhandshake.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.joinhandshake.com/access?user_type=employer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinhandshake.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joinhandshake.com/legal/tos/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joinhandshake.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/handshake-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/handshake-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/handshake-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/handshake-conventions.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/handshake-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.joinhandshake.com/
- group: auth
  title: ''
  type: Security
  url: https://joinhandshake.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/handshake-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/handshake-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/handshake-llms.txt
created: '2026-07-17'
description: 'Handshake (joinhandshake.com) is the early-career talent network that connects students and recent graduates with employers, alongside the higher-education Career Services teams that support them. For developers and institutional integrators, Handshake exposes the EDU API: a read-only, institution-scoped, versioned API for career-services data management and automation, covering applications, appointments, career fairs, jobs, postings, qualifications, and meetings. The EDU API is currently in beta and gated to Career Services partners, authenticates with an x-api-key header issued from the Developer Portal, and supports pagination, sorting, and delta fetching. Handshake was originally added to the API Evangelist network as a VC portfolio lead and has since been enriched from its public developer documentation, trust center, and status surfaces.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/handshake.png
layout: provider
modified: '2026-07-19'
name: Handshake
nav: Providers
network: true
overview: 'Handshake publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hr Tech, Careers, Recruiting, and Higher Education.


  Handshake''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 14 more developer resources.'
random_paper: 41
score:
  band: thin
  composite: 39.0
  delta: 5.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 33.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/handshake/refs/heads/main/screenshots/handshake-2026-07-25T220619.png
security:
- kind: authentication
  name: Handshake Authentication
  slug: handshake-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Handshake Domain Security
  slug: handshake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Handshake Vulnerability Disclosure
  slug: handshake-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Handshake Trust Center
  slug: handshake-trust-center
  summary_line: SOC 2 Type II, PCI DSS, TX-RAMP, UK Cyber Essentials, GDPR, CCPA, EU-U.S. Data Privacy Framework
slug: handshake
tags:
- Company
- Hr Tech
- Careers
- Recruiting
- Higher Education
- Talent
- Students
- Jobs
website: https://www.joinhandshake.com/
---
