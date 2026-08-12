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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST API for managing HPE 3PAR StoreServ / Primera / Alletra storage arrays — virtual volumes, CPGs, hosts, ports, VLUNs, snapshots, and remote copy. Served by the WSAPI server that runs on each array
  name: HPE 3PAR Web Services API (WSAPI)
  slug: hpe-3par-web-services-api-wsapi
artifact_total: 1
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hpe.com/platform/hpe-3par-and-primera/home/
- group: docs
  title: ''
  type: Documentation
  url: https://support.hpe.com/hpesc/public/docDisplay?docId=c03606339
- group: docs
  title: ''
  type: APIReference
  url: https://support.hpe.com/hpesc/public/docDisplay?docId=c03606339
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hpe-storage
- group: operate
  title: ''
  type: Support
  url: https://developer.hpe.com/slack-signup/
- group: build
  title: ''
  type: Packages
  url: packages/3par-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/3par-packages.yml
created: '2026-07-17'
description: 3PAR is an enterprise storage platform, now part of Hewlett Packard Enterprise (HPE acquired 3PAR in 2010), that powers mission-critical applications with HPE 3PAR StoreServ and Primera arrays. For developers and automation engineers, 3PAR exposes the HPE 3PAR Web Services API (WSAPI) — a REST interface that manages storage provisioning, virtual volumes, hosts, ports, CPGs, snapshots, and remote copy on 3PAR/Primera/Alletra arrays, offering a more flexible and programmable alternative to the 3PAR Command Line Interface. HPE publishes first-party client libraries (Python, Ruby, PowerShell) plus Ansible, Puppet, Chef, OpenStack Cinder, and Docker volume integrations against WSAPI. This profile was surfaced as a venture-portfolio lead (Mayfield, Menlo Ventures backed the original 3PAR before its IPO and HP acquisition) and enriched from HPE's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/3par.png
layout: provider
modified: '2026-07-17'
name: 3PAR (HPE 3PAR StoreServ)
nav: Providers
network: true
overview: '3PAR (HPE 3PAR StoreServ) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, Enterprise Storage, Infrastructure, and Data Management.


  3PAR (HPE 3PAR StoreServ)''s developer surface includes documentation, API reference, support, and 4 more developer resources.'
random_paper: 26
score:
  band: emerging
  composite: 14.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/3par/refs/heads/main/screenshots/3par-2026-07-25T181153.png
slug: 3par
tags:
- Company
- Storage
- Enterprise Storage
- Infrastructure
- Data Management
- REST API
- WSAPI
- HPE
website: https://developer.hpe.com/platform/hpe-3par-and-primera/home/
---
