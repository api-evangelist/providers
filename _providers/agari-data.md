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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: RESTful JSON API for the Agari platform (Fortra Email Security). Cloud Email Protection endpoints (/v1/ep) expose monitored messages and policy events; Brand Protection / DMARC endpoints (/v1/cp) expo
  name: Agari Platform API
  slug: agari-platform-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/agari-data-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.fortra.com/platform/email-security
- group: design
  title: ''
  type: Conformance
  url: conformance/agari-data-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agari-data-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agari-data-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agari-data-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.agari.com/agari-platform
- group: docs
  title: ''
  type: Documentation
  url: https://developers.agari.com/agari-platform/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.agari.com/agari-platform/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.agari.com/agari-platform/docs/quick-start
- group: auth
  title: ''
  type: Authentication
  url: authentication/agari-data-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.agari.com/
- group: company
  title: ''
  type: Blog
  url: https://emailsecurity.fortra.com/blog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agari-data-llms.txt
created: '2026-07-17'
description: Agari Data (now part of Fortra Email Security) is an enterprise email security company that uses AI-driven identity intelligence and DMARC email authentication to stop advanced email attacks such as phishing, business email compromise (BEC), and brand impersonation. The Agari Platform API gives developers and security teams programmatic, OAuth 2.0 secured access to Cloud Email Protection and Brand Protection (DMARC) data — including monitored messages, policy events, and threat telemetry — so events can be ingested into SIEM/SOAR tools like Splunk and Microsoft Sentinel. The RESTful API returns JSON, is versioned under a URI path (v1), and is split by product (Cloud Email Protection under /ep, Brand Protection under /cp) with US and EU regional endpoints. Originally founded as Agari Data and later acquired into HelpSystems/Fortra, it was surfaced as a portfolio company of Battery Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agari-data.png
layout: provider
modified: '2026-07-17'
name: Agari Data
nav: Providers
network: true
overview: 'Agari Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Security, Phishing Protection, DMARC, and Business Email Compromise.


  Agari Data''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, and 9 more developer resources.'
random_paper: 43
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 21.8
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agari-data/refs/heads/main/screenshots/agari-data-2026-07-25T181800.png
security:
- kind: authentication
  name: Agari Data Authentication
  slug: agari-data-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Agari Data Domain Security
  slug: agari-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Agari Data Trust Center
  slug: agari-data-trust-center
  summary_line: PCI DSS, HIPAA, GDPR
slug: agari-data
tags:
- Company
- Email Security
- Phishing Protection
- DMARC
- Business Email Compromise
- Threat Intelligence
- Cybersecurity
website: https://www.agari.com/
---
