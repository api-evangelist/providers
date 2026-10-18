---
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
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: gRPC services exposed by SeaweedFS cluster components (Seaweed master, VolumeServer, SeaweedFiler, SeaweedS3, SeaweedIdentityAccessManagement, SeaweedMessaging broker and agent, mount, worker and plug
  name: SeaweedFS gRPC API
  slug: seaweedfs-grpc
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seaweedfs/refs/heads/main/hosts/seaweedfs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seaweedfs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seaweedfs/refs/heads/main/vendors/seaweedfs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seaweedfs-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seaweedfs/refs/heads/main/packages/seaweedfs-packages.yml
  title: ''
  type: SDKs
  url: packages/seaweedfs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seaweedfs/refs/heads/main/packages/seaweedfs-packages.yml
  title: ''
  type: Packages
  url: packages/seaweedfs-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seaweedfs/refs/heads/main/security/seaweedfs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seaweedfs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seaweedfs.com
- group: docs
  title: ''
  type: Documentation
  url: https://seaweedfs.com/docs/deploy/
- group: start
  title: ''
  type: GettingStarted
  url: https://seaweedfs.com/docs/deploy/
- group: docs
  title: ''
  type: APIReference
  url: https://seaweedfs.com/docs/reference/ec_repair/
- group: company
  title: ''
  type: Blog
  url: https://seaweedfs.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seaweedfs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/seaweedfs/seaweedfs
- group: commercial
  title: ''
  type: Pricing
  url: https://seaweedfs.com/docs/pricing/
- group: operate
  title: ''
  type: Support
  url: https://seaweedfs.com/docs/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seaweedfs.com/docs/terms/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/seaweedfs/seaweedfs/releases
created: '2026-10-13'
description: SeaweedFS is a distributed file system and S3-compatible object store, open source at github.com/seaweedfs/seaweedfs with an Enterprise edition sold at seaweedfs.com (data recovery, self-healing storage, erasure coding automation, point-in-time recovery, support plans). Its components - master, volume, filer, S3 gateway, IAM and message-queue broker - talk over published gRPC services (179 RPCs across 14 .proto files) alongside HTTP and S3 interfaces documented in the project wiki.
layout: provider
modified: '2026-10-13'
name: SeaweedFS
nav: Providers
network: true
overview: 'SeaweedFS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Object Storage, Distributed File System, S3 Compatible, and gRPC.


  SeaweedFS''s developer surface includes documentation, getting-started guide, API reference, engineering blog, pricing, support, changelog, and 9 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 42.9
    discoverability: 62.5
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Seaweedfs Domain Security
  slug: seaweedfs-domain-security
  summary_line: TLSv1.3
slug: seaweedfs
tags:
- Company
- Object Storage
- Distributed File System
- S3 Compatible
- gRPC
- Open Source
- Storage
website: https://seaweedfs.com
---
