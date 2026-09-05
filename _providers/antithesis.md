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
    agent_skills: true
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Programmatic access to the Antithesis autonomous testing platform via tenant-scoped webhook endpoints. POST /basic_test launches a test run; POST /debugging starts a multiverse debugging session. Auth
  name: Antithesis Platform API (Webhooks)
  slug: antithesis-platform-api-webhooks
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://antithesis.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://antithesis.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://antithesis.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://antithesis.com/docs/reference/rest_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://antithesis.com/docs/getting_started/setup_guide/
- group: company
  title: ''
  type: Blog
  url: https://antithesis.com/learn/?category=Blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/antithesishq
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/antithesis
- group: start
  title: ''
  type: Login
  url: https://antithesis.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antithesis.com/legal/terms_of_use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antithesis.com/legal/privacy_policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.antithesis.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/antithesis-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/antithesis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/antithesis-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/antithesis-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/antithesis-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/antithesis-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/antithesis-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/antithesis-domain-security.yml
created: '2026-07-17'
description: Antithesis is an autonomous software testing platform that finds deep bugs in mission-critical systems using deterministic simulation and continuous fuzzing. It runs your entire system inside a deterministic hypervisor, injects faults and network partitions, explores reachable states, and reproduces any bug perfectly for time-travel "multiverse" debugging and automated root-cause analysis. Teams integrate through language SDKs (Go, Java, C/C++, Python, JavaScript, Rust, .NET) that define always/sometimes properties and assertions, package their software with Docker Compose or Kubernetes, then launch tests through a webhook/REST API or the snouty CLI. It is used to harden databases, distributed systems, blockchains, and financial trading infrastructure.
image: https://github.com/antithesishq.png
layout: provider
modified: '2026-07-17'
name: Antithesis
nav: Providers
network: true
overview: 'Antithesis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Testing, Software Testing, and Deterministic Simulation.


  Antithesis'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, CLI, and 14 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 32.3
  provenance:
    conformance: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/antithesis/refs/heads/main/screenshots/antithesis-2026-07-25T200432.png
security:
- kind: authentication
  name: Antithesis Authentication
  slug: antithesis-authentication
  summary_line: http/openIdConnect · 4 schemes
- kind: domain-security
  name: Antithesis Domain Security
  slug: antithesis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: antithesis
tags:
- Company
- Developer Tools
- Testing
- Software Testing
- Deterministic Simulation
- Fuzzing
- Reliability
- Distributed Systems
- SDK
website: https://antithesis.com
---
