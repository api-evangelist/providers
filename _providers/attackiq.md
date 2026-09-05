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
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'REST/JSON API for the AttackIQ Security Optimization Platform. Manage assessments, tests, scenarios, and assets and retrieve execution results. Authenticated with a per-user API token (Authorization: '
  name: AttackIQ Platform API
  slug: attackiq-platform-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.attackiq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.attackiq.com/hc/en-us/categories/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.attackiq.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://help.attackiq.com/hc/en-us/categories/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.attackiq.com/academy/
- group: operate
  title: ''
  type: Support
  url: https://help.attackiq.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.attackiq.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AttackIQ
- group: start
  title: ''
  type: SignUp
  url: https://login.attackiq.com/
- group: start
  title: ''
  type: Login
  url: https://login.attackiq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.attackiq.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.attackiq.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.attackiq.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.attackiq.com/
- group: build
  title: ''
  type: Packages
  url: packages/attackiq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/attackiq-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/attackiq-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/attackiq-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/attackiq-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/attackiq-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/attackiq-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/attackiq-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/attackiq-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/attackiq-domain-security.yml
created: '2026-07-17'
description: AttackIQ is a cybersecurity company that pioneered Breach and Attack Simulation (BAS) and now delivers a Continuous Threat Exposure Management (CTEM) platform. Its Security Optimization Platform continuously and safely emulates real adversary tactics, techniques, and procedures aligned to the MITRE ATT&CK framework, validating that security controls detect and prevent attacks and measuring control effectiveness over time. The platform exposes a REST/JSON Platform API (firedrill.attackiq.com/v1) for managing assessments, assets, scenarios, tests, and results, authenticated with per-user API tokens, plus an official Python SDK and `aiq` command-line interface. AttackIQ is a portfolio company of Index Ventures.
image: https://www.attackiq.com/wp-content/uploads/2026/05/attackiq-ctem-3.webp
layout: provider
modified: '2026-07-18'
name: AttackIQ
nav: Providers
network: true
overview: 'AttackIQ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Breach and Attack Simulation, and Continuous Threat Exposure Management.


  AttackIQ''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 17 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 22.8
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/attackiq/refs/heads/main/screenshots/attackiq-2026-07-25T201626.png
security:
- kind: authentication
  name: Attackiq Authentication
  slug: attackiq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Attackiq Domain Security
  slug: attackiq-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Attackiq Trust Center
  slug: attackiq-trust-center
  summary_line: trust center published
slug: attackiq
tags:
- Company
- Security
- Cybersecurity
- Breach and Attack Simulation
- Continuous Threat Exposure Management
- Security Validation
- MITRE ATT&CK
- Threat Exposure Management
website: https://www.attackiq.com
---
