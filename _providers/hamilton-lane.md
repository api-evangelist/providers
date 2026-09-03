---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Hamilton Lane API provides access to platform services and data for enterprise integration and automation.
  name: Hamilton Lane API
  slug: hamilton-lane-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hamilton-lane-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hamiltonlane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hamilton-lane
- group: company
  title: ''
  type: Website
  url: https://www.hamiltonlane.com
created: '2026-04-19'
description: Hamilton Lane is a major US corporation and Fortune 1000 company. The Hamilton Lane API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Hamilton Lane Finops
  service_category: Private Markets Data / Analytics Subscription
  slug: hamilton-lane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hamilton-lane.png
layout: provider
modified: '2026-04-19'
name: Hamilton Lane
nav: Providers
network: true
overview: Hamilton Lane publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Private Markets, Asset Management, and Investment.
plans:
- name: Hamilton Lane Plans Pricing
  plan_count: 1
  slug: hamilton-lane-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Hamilton Lane Rate Limits
  slug: hamilton-lane-rate-limits
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hamilton-lane/refs/heads/main/screenshots/hamilton-lane-2026-06-20T182459.png
security:
- kind: domain-security
  name: Hamilton Lane Domain Security
  slug: hamilton-lane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hamilton-lane
tags:
- Private Markets
- Asset Management
- Investment
website: https://www.hamiltonlane.com
---
