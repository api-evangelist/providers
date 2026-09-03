---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Carter's API provides access to platform services and data for enterprise integration and automation.
  name: Carter's API
  slug: carter-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carters.com
created: '2026-04-19'
description: Carter's is a major US corporation and Fortune 1000 company. The Carter's API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Carter Finops
  service_category: Retail
  slug: carter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carter.png
layout: provider
modified: '2026-04-19'
name: Carter's
nav: Providers
network: true
overview: Carter's publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Children, Apparel, and Fortune 1000.
plans:
- name: Carter Plans Pricing
  plan_count: 1
  slug: carter-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Carter Rate Limits
  slug: carter-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carter/refs/heads/main/screenshots/carter-2026-06-20T174021.png
security:
- kind: domain-security
  name: Carter Domain Security
  slug: carter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carter
tags:
- Retail
- Children
- Apparel
- Fortune 1000
website: https://www.carters.com
---
