---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Photon Health Agentic Access
  operation_count: 1
  slug: photon-health-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The GraphQL API from Photon Health — 1 operation(s) for graphql.
  name: Photon Health GraphQL API
  slug: photon-health-graphql-api
artifact_total: 9
collections:
- collection_type: open
  name: Photon Health Clinical API
  slug: open-photon-health
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/photon-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/photon-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/photon-health-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Photon-Health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/photon-health
- group: company
  title: ''
  type: Website
  url: https://www.photon.health
- group: docs
  title: ''
  type: Documentation
  url: https://docs.photon.health
- group: commercial
  title: ''
  type: Plans
  url: plans/photon-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/photon-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/photon-health-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://photonhealth.com/blog
created: '2026-06-21'
description: Photon Health is a modern e-prescribing (eRx) platform that lets digital-health organizations create patients, write prescriptions, route orders to pharmacies, and manage fulfillment through a single GraphQL Clinical API. The platform pairs the API with embeddable Elements UI components, webhooks, and a transparent prescription marketplace for pharmacy price and fulfillment comparison.
finops:
- name: Photon Health Finops
  service_category: Healthcare and Life Sciences
  slug: photon-health-finops
graphqls:
- description: GraphQL schema for the [Photon Health](https://www.photon.health) Clinical API — a modern
  name: Photon Health GraphQL API
  slug: photon-health-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/photon-health.png
layout: provider
modified: '2026-06-21'
name: Photon Health
nav: Providers
network: true
overview: 'Photon Health publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Health, e-Prescribing, eRx, Prescriptions, and Pharmacy.


  Photon Health''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Photon Health Plans Pricing
  plan_count: 2
  slug: photon-health-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Photon Health Rate Limits
  slug: photon-health-rate-limits
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Photon Health Authentication
  slug: photon-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Photon Health Domain Security
  slug: photon-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: photon-health
tags:
- Health
- e-Prescribing
- eRx
- Prescriptions
- Pharmacy
- GraphQL
website: https://www.photon.health
---
