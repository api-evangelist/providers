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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/toit-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://toit.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.toit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.toit.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.toit.io/getstarted
- group: operate
  title: ''
  type: Support
  url: https://help.toit.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.toit.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://toit.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://toit.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toit.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/toitlang
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/toitware
- group: other
  title: ''
  type: Protobuf
  url: grpc/toit-api-index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toit-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/toit-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/toit-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/toit-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/toit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/toit-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toit-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/toit-llms.txt
created: '2026-07-17'
description: Toit builds an open-source, high-level programming language and runtime for microcontrollers, targeting the ESP32 family, together with fleet-management tooling for deploying, monitoring and hot-reloading software across large fleets of connected IoT devices. The Toit language, virtual machine, package registry and the Jaguar (`jag`) live-reload developer CLI are open source and free; Toit also offers a self-hostable fleet broker and paid engineering support. The company previously operated a managed cloud platform exposing a gRPC API (device, pub/sub data, program compilation and organization management) before pivoting to the open-source language stack; those Protobuf definitions were archived in 2023. Toit is backed by Creandum.
image: https://github.com/toitlang.png
layout: provider
modified: '2026-07-21'
name: Toit
nav: Providers
network: true
overview: 'Toit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, IoT, Embedded, and ESP32.


  Toit''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, authentication, CLI, and 14 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 64.3
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 32.5
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/toit/refs/heads/main/screenshots/toit-2026-09-02T163842.png
security:
- kind: authentication
  name: Toit Authentication
  slug: toit-authentication
  summary_line: bearer/apiKey · 2 schemes
- kind: domain-security
  name: Toit Domain Security
  slug: toit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: toit
tags:
- Company
- Software-as-a-Service
- IoT
- Embedded
- ESP32
- Microcontrollers
- Programming Language
- Fleet Management
- Firmware
- Developer Tools
- gRPC
website: https://toit.io/
---
