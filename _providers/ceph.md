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
    agentic_access: derived
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
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Ceph Agentic Access
  operation_count: 18
  slug: ceph-agentic-access
  summary_line: 18 operations · 12 acting
api_count: 1
apis:
- baseURL: https://{manager_host}:{dashboard_port}/api
  baseurl_source: declared
  description: The Auth API from Ceph — 3 operation(s) for auth.
  name: Ceph Auth API
  slug: ceph-auth-api
- baseURL: https://{manager_host}:{dashboard_port}/api
  baseurl_source: declared
  description: The Cluster API from Ceph — 1 operation(s) for cluster.
  name: Ceph Cluster API
  slug: ceph-cluster-api
- baseURL: https://{manager_host}:{dashboard_port}/api
  baseurl_source: declared
  description: The Configuration API from Ceph — 3 operation(s) for configuration.
  name: Ceph Configuration API
  slug: ceph-configuration-api
- baseURL: https://{manager_host}:{dashboard_port}/api
  baseurl_source: declared
  description: The CRUSH API from Ceph — 2 operation(s) for crush.
  name: Ceph CRUSH API
  slug: ceph-crush-api
- baseURL: https://{manager_host}:{dashboard_port}/api
  baseurl_source: declared
  description: The Daemon API from Ceph — 2 operation(s) for daemon.
  name: Ceph Daemon API
  slug: ceph-daemon-api
- baseURL: https://{manager_host}:{dashboard_port}/api
  baseurl_source: declared
  description: The User API from Ceph — 2 operation(s) for user.
  name: Ceph User API
  slug: ceph-user-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ceph Manager REST Auth API
  slug: open-ceph-auth-api
- collection_type: open
  name: Ceph Manager REST Auth Cluster API
  slug: open-ceph-cluster-api
- collection_type: open
  name: Ceph Manager REST Auth Configuration API
  slug: open-ceph-configuration-api
- collection_type: open
  name: Ceph Manager REST Auth CRUSH API
  slug: open-ceph-crush-api
- collection_type: open
  name: Ceph Manager REST Auth Daemon API
  slug: open-ceph-daemon-api
- collection_type: open
  name: Ceph Manager REST Auth User API
  slug: open-ceph-user-api
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
random_paper: 17
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 51.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 24.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
- Software-Defined Storage
website: https://ceph.io
---
