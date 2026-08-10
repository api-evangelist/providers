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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Ceph Agentic Access
  operation_count: 18
  slug: ceph-agentic-access
  summary_line: 18 operations · 12 acting
api_count: 6
apis:
- description: The Auth API from Ceph — 3 operation(s) for auth.
  name: Ceph Auth API
  slug: ceph-auth-api
- description: The Cluster API from Ceph — 1 operation(s) for cluster.
  name: Ceph Cluster API
  slug: ceph-cluster-api
- description: The Configuration API from Ceph — 3 operation(s) for configuration.
  name: Ceph Configuration API
  slug: ceph-configuration-api
- description: The CRUSH API from Ceph — 2 operation(s) for crush.
  name: Ceph CRUSH API
  slug: ceph-crush-api
- description: The Daemon API from Ceph — 2 operation(s) for daemon.
  name: Ceph Daemon API
  slug: ceph-daemon-api
- description: The User API from Ceph — 2 operation(s) for user.
  name: Ceph User API
  slug: ceph-user-api
artifact_total: 11
collections:
- collection_type: open
  name: Ceph Manager REST API
  slug: open-ceph
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ceph-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ceph-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ceph-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ceph-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ceph
- group: company
  title: ''
  type: Website
  url: https://ceph.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ceph.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ceph
- group: other
  title: ''
  type: Mailing Lists
  url: https://ceph.io/en/community/connect/
- group: other
  title: ''
  type: Foundation
  url: https://ceph.io/en/foundation/
- group: company
  title: ''
  type: Blog
  url: https://ceph.io/en/news/blog/feed.xml
created: '2026-05-11'
description: Ceph is an open source, distributed storage platform that provides unified object, block, and file storage on commodity hardware with no single point of failure. The Ceph Manager (ceph-mgr) ships with a RESTful API that exposes the same operations available in the Ceph Dashboard for managing pools, OSDs, hosts, monitors, RGW, RBD, CephFS, and cluster configuration. The API is OpenAPI 3.0 compliant and authenticates via JWT bearer tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ceph.png
layout: provider
modified: '2026-05-11'
name: Ceph
nav: Providers
network: true
overview: 'Ceph publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Cluster API, Configuration API, and 3 more. Tagged areas include Storage, Distributed Storage, Object Storage, Block Storage, and File Storage.


  Ceph''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
random_paper: 68
score:
  band: emerging
  composite: 26.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 56.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ceph/refs/heads/main/screenshots/ceph-2026-06-20T174133.png
security:
- kind: authentication
  name: Ceph Authentication
  slug: ceph-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ceph Domain Security
  slug: ceph-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ceph Vulnerability Disclosure
  slug: ceph-vulnerability-disclosure
  summary_line: disclosure policy published
slug: ceph
tags:
- Storage
- Distributed Storage
- Object Storage
- Block Storage
- File Storage
- Open Source
- Software-Defined Storage
website: https://ceph.io
---
