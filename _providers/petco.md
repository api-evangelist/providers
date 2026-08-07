---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Petco Animal Supplies API provides access to platform services and data for enterprise integration and automation.
  name: Petco Animal Supplies API
  slug: petco-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/petco-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/petco-animal-supplies-inc-
- group: company
  title: ''
  type: Website
  url: https://www.petco.com
created: '2026-04-19'
description: Petco Animal Supplies is a major US corporation and Fortune 1000 company. The Petco Animal Supplies API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Petco Finops
  service_category: B2B Integration
  slug: petco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/petco.png
layout: provider
modified: '2026-04-19'
name: Petco Animal Supplies
nav: Providers
network: true
overview: Petco Animal Supplies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pet Care, Retail, and Veterinary.
plans:
- name: Petco Plans Pricing
  plan_count: 1
  slug: petco-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 1
  name: Petco Rate Limits
  slug: petco-rate-limits
score:
  band: emerging
  composite: 14.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 14.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Petco Domain Security
  slug: petco-domain-security
  summary_line: TLSv1.3 · DMARC
slug: petco
tags:
- Pet Care
- Retail
- Veterinary
website: https://www.petco.com
---
