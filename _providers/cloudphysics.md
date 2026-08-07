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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudphysics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudphysics.com/
created: '2026-07-17'
description: CloudPhysics is a SaaS-based big-data analytics platform for virtualized IT infrastructure, founded in 2011 and acquired by Hewlett Packard Enterprise in 2021. Deployed as the CloudPhysics Observer virtual appliance against VMware vSphere / vCenter, it collects IT metadata and delivers data-driven insights for capacity planning, cost optimization, migration assessment, and infrastructure health. It is now part of HPE; cloudphysics.com redirects to HPE storage. CloudPhysics exposes no public developer API of its own — the product consumes the VMware vCenter API to gather metadata rather than publishing a developer-facing API, so this profile carries identity and domain-security signal only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudphysics.png
layout: provider
modified: '2026-07-18'
name: CloudPhysics
nav: Providers
network: true
overview: CloudPhysics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Analytics, Virtualization, and VMware.
random_paper: 63
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudphysics/refs/heads/main/screenshots/cloudphysics-2026-07-25T205706.png
security:
- kind: domain-security
  name: Cloudphysics Domain Security
  slug: cloudphysics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudphysics
tags:
- Company
- Enterprise
- Analytics
- Virtualization
- VMware
- Cloud Migration
- Infrastructure
- SaaS
website: https://www.cloudphysics.com/
---
