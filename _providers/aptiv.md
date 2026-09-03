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
- description: The Aptiv API provides access to platform services and data for enterprise integration and automation.
  name: Aptiv API
  slug: aptiv-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aptiv-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aptiv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aptiv
- group: company
  title: ''
  type: Website
  url: https://www.aptiv.com
created: '2026-04-19'
description: Aptiv is a major US corporation and Fortune 1000 company. The Aptiv API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Aptiv Finops
  service_category: Industrial / Automotive
  slug: aptiv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aptiv.png
layout: provider
modified: '2026-04-19'
name: Aptiv
nav: Providers
network: true
overview: Aptiv publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Electrical Systems, and Technology.
plans:
- name: Aptiv Plans Pricing
  plan_count: 1
  slug: aptiv-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Aptiv Rate Limits
  slug: aptiv-rate-limits
score:
  band: minimal
  composite: 10.6
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
    operational_transparency: 7.9
  previous_composite: 10.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aptiv/refs/heads/main/screenshots/aptiv-2026-06-20T172341.png
security:
- kind: domain-security
  name: Aptiv Domain Security
  slug: aptiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aptiv
tags:
- Automotive
- Electrical Systems
- Technology
website: https://www.aptiv.com
---
