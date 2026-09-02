---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Netreo REST API provides programmatic access to the Netreo monitoring platform, including endpoints for devices, dashboards, alerts, incidents, business services, and reporting. The API list catal
  name: Netreo API
  slug: netreo-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netreo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netreo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netreo
- group: company
  title: ''
  type: Website
  url: https://www.helixops.ai/products/netreo.html
- group: docs
  title: ''
  type: Documentation
  url: https://solutions.netreo.com/docs
- group: operate
  title: ''
  type: Support
  url: https://solutions.netreo.com/support
created: '2025-02-12'
description: Netreo is an IT infrastructure monitoring platform (now part of BMC as BMC Helix Operations Management with Netreo) that provides full-stack observability across networks, servers, applications, cloud services and databases. The platform exposes a documented REST API for programmatic access to monitoring data, configuration, and automation workflows.
finops:
- name: Netreo Finops
  service_category: API
  slug: netreo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netreo.png
layout: provider
modified: '2026-04-28'
name: Netreo
nav: Providers
network: true
overview: 'Netreo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Monitoring, IT Operations, Infrastructure Monitoring, Network Monitoring, and Observability.


  Netreo''s developer surface includes documentation, support, and 4 more developer resources.'
plans:
- name: Netreo Plans Pricing
  plan_count: 3
  slug: netreo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Netreo Rate Limits
  slug: netreo-rate-limits
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netreo/refs/heads/main/screenshots/netreo-2026-06-20T190203.png
security:
- kind: domain-security
  name: Netreo Domain Security
  slug: netreo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: netreo
tags:
- Cloud Monitoring
- IT Operations
- Infrastructure Monitoring
- Network Monitoring
- Observability
website: https://www.helixops.ai/products/netreo.html
---
