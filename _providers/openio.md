---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
- description: Amazon S3-compatible object storage gateway exposed by OpenIO SDS, with an OpenStack Swift-compatible gateway alongside. Self-hosted software, so the API base URL is deployment-specific.
  name: OpenIO SDS S3-Compatible Object Storage API
  slug: openio-sds-s3-compatible-object-storage-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.openio.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openio.io/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.openio.io/latest/source/arch-design/s3_compliancy.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openio.io/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/open-io
- group: auth
  title: ''
  type: Authentication
  url: authentication/openio-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openio-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/openio-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/openio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/openio-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openio-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openio-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openio-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openio-domain-security.yml
created: '2026-07-17'
description: OpenIO SDS is an open-source, software-defined object storage platform for building hyper-scalable, high-performance storage infrastructures. It stores data across commodity hardware and exposes it through an Amazon S3-compatible gateway and an OpenStack Swift-compatible gateway, backed by native RAWX, Conscience, Directory, Container, Content and Account services. Developers integrate via first-party Python, C and Java client libraries and the `openio` command-line interface, or with any standard AWS S3 / Swift SDK and CLI. The S3 gateway supports Signature v2/v4, versioning, lifecycle, CORS, tagging, ACLs and multipart uploads, plus a documented subset of AWS IAM (paid plans). OpenIO was founded as a French storage company backed by Partech and acquired by OVHcloud in 2020; the SDS project remains publicly documented open source.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openio.png
layout: provider
modified: '2026-07-20'
name: OpenIO
nav: Providers
network: true
overview: 'OpenIO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure Saas, Object Storage, S3, and Cloud Storage.


  OpenIO''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, and 9 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 17.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 17.3
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Openio Authentication
  slug: openio-authentication
  summary_line: awsSignature/swiftAuth · 2 schemes
- kind: domain-security
  name: Openio Domain Security
  slug: openio-domain-security
  summary_line: no transport/DNS hardening detected
slug: openio
tags:
- Company
- Infrastructure Saas
- Object Storage
- S3
- Cloud Storage
- Open-Source
- OpenStack Swift
- Storage
website: https://www.openio.io/
---
