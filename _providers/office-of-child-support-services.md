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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: U.S. Department of Health & Human Services; Administration for Children & Families; Select an ACF Office. Administration for Native Americans (ANA) Administration on Children, Youth, and Families (ACY
  name: Office of Child Support Services
  slug: office-of-child-support-services
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/office-of-child-support-services-domain-security.yml
created: '2024-12-03'
description: The Office of Child Support Services is a government agency that works to ensure that children receive the financial support they need from their non-custodial parent. This office helps establish legal paternity, locate absent parents, and establish and enforce child support orders. They work with both custodial and non-custodial parents to facilitate the collection and distribution of child support payments, ensuring that children have the resources they need to thrive.
finops:
- name: Office Of Child Support Services Finops
  service_category: API
  slug: office-of-child-support-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/office-of-child-support-services.png
layout: provider
modified: '2026-04-28'
name: Office of Child Support Services
nav: Providers
network: true
overview: Office of Child Support Services publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government.
plans:
- name: Office Of Child Support Services Plans Pricing
  plan_count: 3
  slug: office-of-child-support-services-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Office Of Child Support Services Rate Limits
  slug: office-of-child-support-services-rate-limits
score:
  band: minimal
  composite: 9.5
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
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/office-of-child-support-services/refs/heads/main/screenshots/office-of-child-support-services-2026-06-20T190631.png
security:
- kind: domain-security
  name: Office Of Child Support Services Domain Security
  slug: office-of-child-support-services-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: office-of-child-support-services
tags:
- Federal-Government
---
