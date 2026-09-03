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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Fenergo SaaS Platform API surface covers Entity Data, Journey, ETL, Data Migration, External Data, Policy, Legal Entity Screening, Risk, Event Notification & Ingress, Portal, Review Journey Schedu
  name: Fenergo SaaS Platform API
  slug: fenergo
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fenergo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fenergo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fenergo
- group: company
  title: ''
  type: Website
  url: https://www.fenergo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fenergox.com/api-docs/fenergo-saas-api-specifications/introduction
- group: company
  title: ''
  type: Blog
  url: https://resources.fenergo.com/
created: '2025-05-02'
description: Fenergo is a financial services SaaS platform for Client Lifecycle Management (CLM), Know Your Customer (KYC), client onboarding, transaction monitoring, and regulatory compliance. The Fenergo SaaS Platform exposes API specifications across Entity Data, Journey, ETL, Data Migration, External Data, Policy, Legal Entity Screening, Risk, Event Notification & Ingress, Portal, Review Journey Scheduling, and Transaction Monitoring domains.
finops:
- name: Fenergo Finops
  service_category: API
  slug: fenergo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fenergo.png
layout: provider
modified: '2026-04-28'
name: Fenergo
nav: Providers
network: true
overview: 'Fenergo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, Financial, KYC, and Onboarding.


  Fenergo''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Fenergo Plans Pricing
  plan_count: 3
  slug: fenergo-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Fenergo Rate Limits
  slug: fenergo-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fenergo/refs/heads/main/screenshots/fenergo-2026-06-20T181135.png
security:
- kind: domain-security
  name: Fenergo Domain Security
  slug: fenergo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fenergo
tags:
- Compliance
- Financial
- KYC
- Onboarding
website: https://www.fenergo.com/
---
