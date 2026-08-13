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
    agent_skills: derived
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
  score: 10.1
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'Pixie''s gRPC API for programmatically running PxL scripts against live Kubernetes clusters and managing Pixie Cloud resources. Two services: Pixie Cloud (cluster discovery, API/deploy keys, artifacts,'
  name: Pixie API
  slug: pixie-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://px.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.px.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.px.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.px.dev/reference/api/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.px.dev/using-pixie/api-quick-start/
- group: operate
  title: ''
  type: Support
  url: https://px.dev/community/
- group: company
  title: ''
  type: Blog
  url: https://blog.px.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixie-io
- group: build
  title: ''
  type: Packages
  url: packages/pixie-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pixie-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/pixie-labs-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pixie-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pixie-labs-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pixie-labs-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pixie-labs-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixie-labs-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pixie-labs-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pixie-labs-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Pixie Labs built Pixie, an open-source, Kubernetes-native application observability and debugging platform that uses dynamic eBPF probes to auto-instrument workloads and capture metrics, events, full-body traces, and logs in seconds without code changes. Data is collected and queried in-cluster via PxL scripts, avoiding costly telemetry export. Pixie Labs was acquired by New Relic in December 2020; the project was contributed to the Cloud Native Computing Foundation (CNCF) as a sandbox project and is developed in the open at px.dev under the pixie-io GitHub organization. Pixie exposes a gRPC API (Pixie Cloud for cluster discovery/management and Pixie Vizier for PxL script execution) with first-party Go and Python client libraries and the px CLI.
image: https://raw.githubusercontent.com/pixie-io/pixie/main/.readme_assets/pixie_banner.png
layout: provider
modified: '2026-07-20'
name: Pixie Labs
nav: Providers
network: true
overview: 'Pixie Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Observability, Kubernetes, and eBPF.


  Pixie Labs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 12 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 66.8
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 24.1
  provenance:
    conformance: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Pixie Labs Authentication
  slug: pixie-labs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Pixie Labs Domain Security
  slug: pixie-labs-domain-security
  summary_line: TLSv1.3 · HSTS
slug: pixie-labs
tags:
- Company
- Ai
- Observability
- Kubernetes
- eBPF
- Monitoring
- Tracing
- Open Source
- CNCF
- gRPC
- Developer Tools
website: https://px.dev
---
