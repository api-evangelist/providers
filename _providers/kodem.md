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
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The Kodem platform API. The service is reachable at https://api.kodemsecurity.com and is fully authenticated — every path returns HTTP 401 with a JSON {"detail":"Unauthorized"} envelope until a creden
  name: Kodem API
  slug: kodem-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.kodemsecurity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.kodemsecurity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kodemsecurity.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.kodemsecurity.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kodemsecurity.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kodemsecurity.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.kodemsecurity.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.kodemsecurity.com/book-a-demo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kodem/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kodemsecurity.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/kodem-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kodem-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kodem-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kodem-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kodem-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kodem-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kodem-domain-security.yml
created: '2026-07-17'
description: Kodem Security is an AI-native application security platform built on runtime intelligence, founded in 2021 by Aviv Mussinger, Idan Bartura, and Pavel Furman. Kodem connects code analysis, runtime evidence, AI reasoning, and runtime protection into a single system so security teams prioritize and fix what is actually exploitable in production rather than triaging every theoretical finding. The platform spans runtime-powered software composition analysis (SCA) across transitive and OS-level dependencies, native SAST powered by Opengrep with 1,000+ rules plus secrets detection, and Application Detection & Response (ADR) that detects exploit attempts at the application layer without signatures. Its AI layer, Kai, is grounded in function-level runtime evidence to accelerate triage, prioritization, and repository-grounded remediation. Kodem is SOC 2 Type II and deploys across cloud and on-premise environments in about five minutes.
image: https://cdn.prod.website-files.com/63da9726cdbeda469366f7f2/69446ff571232a027ec80a33_kodem-global-opengraph.png
layout: provider
modified: '2026-07-19'
name: Kodem
nav: Providers
network: true
overview: 'Kodem publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Application Security, Runtime Security, and Software Composition Analysis.


  Kodem''s developer surface includes documentation, signup flow, pricing, engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.4
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kodem/refs/heads/main/screenshots/kodem-2026-07-25T224243.png
security:
- kind: authentication
  name: Kodem Authentication
  slug: kodem-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Kodem Domain Security
  slug: kodem-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kodem
tags:
- Company
- Cybersecurity
- Application Security
- Runtime Security
- Software Composition Analysis
- Static Analysis
- Vulnerability Management
- DevSecOps
- SBOM
- AI Security
website: https://www.kodemsecurity.com/
---
