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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ocean-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocean-io-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oceanio
- group: company
  title: ''
  type: Website
  url: https://ocean.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ocean.io/help/api
- group: commercial
  title: ''
  type: Plans
  url: plans/ocean-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ocean-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ocean-io-finops.yml
created: '2026-05-08'
description: Ocean.io is a B2B account-based prospecting and enrichment platform focused on lookalike search and ICP refinement. It offers a REST API for company enrichment and lookalike account discovery. API access is gated to paying customers and configured per contract.
finops:
- name: Ocean Io Finops
  service_category: Sales Intelligence
  slug: ocean-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ocean-io.png
layout: provider
modified: '2026-07-25'
name: Ocean.io
nav: Providers
network: true
overview: Ocean.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Intelligence, B2B, Enrichment, Lookalike, and ABM.
plans:
- name: Ocean Io Plans Pricing
  plan_count: 1
  slug: ocean-io-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Ocean Io Rate Limits
  slug: ocean-io-rate-limits
score:
  band: emerging
  composite: 17.5
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 17.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ocean-io/refs/heads/main/screenshots/ocean-io-2026-06-20T190601.png
security:
- kind: domain-security
  name: Ocean Io Domain Security
  slug: ocean-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ocean Io Trust Center
  slug: ocean-io-trust-center
  summary_line: SOC 2
slug: ocean-io
tags:
- Sales Intelligence
- B2B
- Enrichment
- Lookalike
- ABM
- Prospecting
website: https://ocean.io/
---
