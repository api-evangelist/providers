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
- description: 'The REST API served by every Qumulo cluster for managing files, snapshots, quotas, replication, multi-protocol shares (NFS/SMB/S3/FTP), networking, cluster lifecycle, monitoring/analytics, and access '
  name: Qumulo Core REST API
  slug: qumulo-core-rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qumulo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qumulo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qumulo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qumulo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qumulo.com/rest-api-guide/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qumulo.com/administrator-guide/
- group: operate
  title: ''
  type: Support
  url: https://care.qumulo.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.qumulo.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qumulo
- group: start
  title: ''
  type: SignUp
  url: https://www.qumulo.com/try-qumulo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qumulo.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qumulo.com/terms-hub
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qumulo.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.qumulo.com/
- group: build
  title: ''
  type: CLI
  url: cli/qumulo-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/qumulo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qumulo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qumulo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qumulo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qumulo-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/qumulo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qumulo-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qumulo-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qumulo-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qumulo-llms.txt
created: '2026-07-17'
description: Qumulo is an enterprise data platform company that delivers a single, unified file and object storage system spanning on-premises data centers, the edge, and the public cloud (AWS, Azure, GCP) at exabyte scale. Every Qumulo cluster exposes a comprehensive versioned REST API (v1/v2/v3+) and the companion `qq` command-line tool for programmatic administration of files, snapshots, quotas, replication, multi-protocol access (NFS, SMB, S3, FTP), networking, cluster operations, monitoring/analytics, and access control. The platform targets data-intensive workloads such as AI/ML, high-performance computing, media and entertainment, genomics, and enterprise backup, giving organizations a global namespace and real-time analytics across their unstructured data.
image: https://www.datocms-assets.com/195389/1770871886-share-qumulo.jpg
layout: provider
modified: '2026-07-20'
name: Qumulo
nav: Providers
network: true
overview: 'Qumulo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, File Storage, Data Platform, and Cloud Storage.


  Qumulo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 18 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 39.1
  delta: 1.6
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 37.5
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Qumulo Authentication
  slug: qumulo-authentication
  summary_line: http-bearer/session/saml/oauth2-support-portal · 3 schemes
- kind: domain-security
  name: Qumulo Domain Security
  slug: qumulo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qumulo
tags:
- Company
- Storage
- File Storage
- Data Platform
- Cloud Storage
- Unstructured Data
- Enterprise
- Infrastructure
- REST API
- CLI
website: https://qumulo.com/
---
