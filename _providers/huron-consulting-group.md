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
- description: The Huron Consulting Group API provides access to platform services and data for enterprise integration and automation.
  name: Huron Consulting Group API
  slug: huron-consulting-group-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huron-consulting-group-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/huronconsulting
- group: company
  title: ''
  type: Website
  url: https://www.huronconsultinggroup.com
created: '2026-04-19'
description: Huron Consulting Group is a major US corporation and Fortune 1000 company. The Huron Consulting Group API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Huron Consulting Group Finops
  service_category: Management Consulting
  slug: huron-consulting-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/huron-consulting-group.png
layout: provider
modified: '2026-04-19'
name: Huron Consulting Group
nav: Providers
network: true
overview: Huron Consulting Group publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Consulting, Healthcare, and Education.
plans:
- name: Huron Consulting Group Plans Pricing
  plan_count: 1
  slug: huron-consulting-group-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Huron Consulting Group Rate Limits
  slug: huron-consulting-group-rate-limits
score:
  band: minimal
  composite: 9.5
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
    operational_transparency: 5.3
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/huron-consulting-group/refs/heads/main/screenshots/huron-consulting-group-2026-06-20T182955.png
security:
- kind: domain-security
  name: Huron Consulting Group Domain Security
  slug: huron-consulting-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: huron-consulting-group
tags:
- Consulting
- Healthcare
- Education
website: https://www.huronconsultinggroup.com
---
