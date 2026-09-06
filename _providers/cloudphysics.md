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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/hewlett-packard-enterprise/
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
random_paper: 4
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Software-as-a-Service
website: https://www.cloudphysics.com/
---
