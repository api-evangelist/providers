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
api_count: 1
apis:
- description: The Fiix CMMS API provides programmatic access to maintenance management data including assets, work orders, purchase orders, parts inventory, users, and maintenance schedules. Supports CRUD operation
  name: Fiix CMMS API
  slug: fiix-cmms-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fiix-software-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fiix-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fiixsoftware.com
- group: docs
  title: ''
  type: Documentation
  url: https://fiixlabs.github.io/api-documentation/
- group: company
  title: ''
  type: Blog
  url: https://fiixsoftware.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fiixlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fiix-software
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@FiixSoftware
- group: commercial
  title: ''
  type: Pricing
  url: https://fiixsoftware.com/pricing/
- group: company
  title: ''
  type: About
  url: https://fiixsoftware.com/about/
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.fiixsoftware.com/
created: '2026-06-05'
description: Fiix (by Rockwell Automation) is a cloud-based CMMS (Computerized Maintenance Management System) platform for maintenance and reliability teams in manufacturing, facilities, and utilities. The Fiix API provides programmatic access to assets, work orders, purchase orders, parts, users, and maintenance data through custom client libraries, with integration support for ERP and industrial automation systems including FactoryTalk Optix.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fiix-software.png
jsonld:
- class_count: 0
  name: Fiix Software Context
  property_count: 9
  slug: fiix-software-context
layout: provider
modified: '2026-06-05'
name: Fiix Software
nav: Providers
network: true
overview: 'Fiix Software publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CMMS, Maintenance Management, Asset Management, Manufacturing, and Reliability.


  The Fiix Software catalog on APIs.io includes 1 JSON-LD context.


  Fiix Software''s developer surface includes documentation, engineering blog, YouTube channel, pricing, support, and 6 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fiix-software/refs/heads/main/screenshots/fiix-software-2026-06-20T181200.png
security:
- kind: domain-security
  name: Fiix Software Domain Security
  slug: fiix-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fiix Software Trust Center
  slug: fiix-software-trust-center
  summary_line: SOC 2, ISO 27001
slug: fiix-software
tags:
- CMMS
- Maintenance Management
- Asset Management
- Manufacturing
- Reliability
- Work Orders
website: https://fiixsoftware.com
---
