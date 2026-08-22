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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'The Brokkr REST API provisions, terminates, and manages Hydra Host GPU fleets programmatically across every data center and OEM hardware stack, and exposes real-time GPU inventory. Observed live: uri-'
  name: Brokkr API
  slug: brokkr-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hydrahost-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hydrahost-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hydrahost-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hydrahost.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hydrahost-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hydrahost-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hydrahost-llms.txt
- group: company
  title: ''
  type: Website
  url: https://hydrahost.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hydrahost.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hydrahost.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hydrahost.com/docs/brokkr-api-overview
- group: company
  title: ''
  type: Blog
  url: https://hydrahost.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://hydrahost.com/calculator/
- group: start
  title: ''
  type: SignUp
  url: https://brokkr.hydrahost.com/login
- group: start
  title: ''
  type: Login
  url: https://brokkr.hydrahost.com/login
- group: operate
  title: ''
  type: Support
  url: https://hydrahost.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hydrahost.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hydrahost.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hydra-host
created: '2026-07-17'
description: Hydra Host is a bare-metal GPU cloud provider that rents and sells dedicated NVIDIA GPU servers (B200, H200, RTX 4090 and more) with full root access across 40+ global data centers for AI training, inference, developer platforms, and neocloud infrastructure. Its Brokkr platform — marketed as the "AI Factory Operating System" — exposes a single REST API (base https://brokkr.hydrahost.com/api/v1) to provision, terminate, and manage GPU fleets programmatically across every data center and OEM hardware stack (Quanta, Lenovo, HPE, NVIDIA), with real-time inventory, interruptible/on-demand/reserved contract terms, and single-tenant, encrypted "Confidential Metal" compute.
image: https://hydrahost.com/images/large-og.jpg
layout: provider
modified: '2026-07-19'
name: Hydrahost
nav: Providers
network: true
overview: 'Hydrahost publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GPU Cloud, Bare Metal, Artificial Intelligence, and Machine Learning.


  Hydrahost''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, support, and 13 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 17.2
  delta: -9.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 26.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/hydrahost/refs/heads/main/screenshots/hydrahost-2026-07-25T221820.png
security:
- kind: domain-security
  name: Hydrahost Domain Security
  slug: hydrahost-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Hydrahost Trust Center
  slug: hydrahost-trust-center
  summary_line: trust center published
slug: hydrahost
tags:
- Company
- GPU Cloud
- Bare Metal
- Artificial Intelligence
- Machine Learning
- Cloud Infrastructure
- Compute
- Neocloud
website: https://hydrahost.com/
---
