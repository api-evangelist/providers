---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Portcast Agentic Access
  operation_count: 13
  slug: portcast-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 5
apis:
- description: Manage custom augmentation data on a bookmark.
  name: Portcast Augmentation API
  slug: portcast-augmentation-api
- description: Container route, risks, and terminal data sub-APIs.
  name: Portcast Container Detail API
  slug: portcast-container-detail-api
- description: Supported carrier SCAC reference data.
  name: Portcast Reference API
  slug: portcast-reference-api
- description: Retrieve tracking results, predicted ETA/ETD, and milestones.
  name: Portcast Tracking Data API
  slug: portcast-tracking-data-api
- description: Start tracking an ocean shipment.
  name: Portcast Tracking Upload API
  slug: portcast-tracking-upload-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Portcast Container Tracking Augmentation API
  slug: open-portcast-augmentation-api
- collection_type: open
  name: Portcast Container Tracking Augmentation Container Detail API
  slug: open-portcast-container-detail-api
- collection_type: open
  name: Portcast Container Tracking Augmentation Reference API
  slug: open-portcast-reference-api
- collection_type: open
  name: Portcast Container Tracking Augmentation Tracking Data API
  slug: open-portcast-tracking-data-api
- collection_type: open
  name: Portcast Container Tracking Augmentation Tracking Upload API
  slug: open-portcast-tracking-upload-api
- collection_type: open
  name: Portcast Container Tracking API
  slug: open-portcast
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/portcast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portcast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/portcast-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/portcast
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/portcast
- group: company
  title: ''
  type: Website
  url: https://www.portcast.io/
- group: docs
  title: ''
  type: Documentation
  url: https://portcast.stoplight.io/docs/portcast-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/portcast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/portcast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/portcast-finops.yml
created: '2026-06-21'
description: Portcast is a predictive supply-chain visibility platform whose Container Tracking API delivers the full journey of an ocean container - milestones, vessel schedules, port codes, and machine-learning predicted ETAs and ETDs - in a single JSON response, tracked by container number, bill of lading, or booking number plus carrier SCAC, with push (webhook) callbacks on every update.
finops:
- name: Portcast Finops
  service_category: Supply Chain and Logistics
  slug: portcast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portcast.png
layout: provider
modified: '2026-06-21'
name: Portcast
nav: Providers
network: true
overview: 'Portcast publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Augmentation API, Container Detail API, Reference API, and 2 more. Tagged areas include Supply Chain, Container Tracking, Logistics, Predictive ETA, and Ocean Freight.


  Portcast''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Portcast Plans Pricing
  plan_count: 2
  slug: portcast-plans-pricing
random_paper: 135
rate_limits:
- limit_count: 2
  name: Portcast Rate Limits
  slug: portcast-rate-limits
score:
  band: thin
  composite: 35.0
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Portcast Authentication
  slug: portcast-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Portcast Domain Security
  slug: portcast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: portcast
tags:
- Supply Chain
- Container Tracking
- Logistics
- Predictive ETA
- Ocean Freight
website: https://www.portcast.io/
---
