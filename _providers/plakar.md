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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 12.9
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: http://plakar.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://plakar.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://plakar.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://plakar.io/docs/community/v1.1.0/quickstart/first-backup
- group: company
  title: ''
  type: Blog
  url: https://plakar.io/posts
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PlakarKorp
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/uuegtnF2Q5
- group: operate
  title: ''
  type: StatusPage
  url: https://status.plakar.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plakar.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plakar.io/legal-notice/
- group: auth
  title: ''
  type: TrustCenter
  url: security/plakar-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.plakar.io
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plakar-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/plakar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/plakar-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/plakar-cli.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/plakar-connectors.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/plakar-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plakar-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plakar-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plakar-llms.txt
created: '2026-07-17'
description: Plakar is an open-source, end-to-end encrypted, deduplicated backup and restore platform powered by Kloset, an immutable data store engine. It encrypts and deduplicates data at the source before it leaves your system (encryption keys stay in your own secret manager), stores it in a non-proprietary format on S3-compatible, cloud, or local backends, and supports immutable object-lock backups for zero-trust data protection. Plakar ships a CLI and built-in web UI, an official Go SDK (go-kloset-sdk), and a proto3 gRPC connector protocol for building custom importers, exporters, and storage backends. Sources include PostgreSQL, MySQL/MariaDB, Kubernetes, Proxmox, VMware vSphere, S3, SFTP, and many cloud drives. The commercial self-hosted Plakar Control Plane adds organization-wide scheduling, SLA management, and centralized administration. Backed by Seedcamp.
image: https://plakar.io/branding/
layout: provider
modified: '2026-07-20'
name: Plakar
nav: Providers
network: true
overview: 'Plakar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Backup, Data Protection, Disaster Recovery, and Open-Source.


  Plakar''s developer surface includes documentation, getting-started guide, engineering blog, support, CLI, changelog, and 15 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 52.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 34.8
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Plakar Domain Security
  slug: plakar-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Plakar Trust Center
  slug: plakar-trust-center
  summary_line: SOC 2, ISO 27001
slug: plakar
tags:
- Company
- Backup
- Data Protection
- Disaster Recovery
- Open-Source
- Encryption
- Deduplication
- Storage
- CLI
- gRPC
- Go SDK
- Kubernetes
website: http://plakar.io
---
