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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'REST API for global employment operations including hiring, payroll, benefits, time off, expenses, invoicing, offboarding, and webhooks. Supports both customer-direct and reseller/partner integration '
  name: Oyster HR API
  slug: oyster-hr-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/oyster-hr-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oyster-hr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oysterhr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oysterhr.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/oysterhr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oysterhr
- group: company
  title: ''
  type: Blog
  url: https://www.oysterhr.com/library
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oysterhr.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.oysterhr.com/
- group: other
  title: ''
  type: X
  url: https://x.com/oyster_hr
- group: commercial
  title: ''
  type: Plans
  url: plans/oyster-hr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oyster-hr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/oyster-hr-finops.yml
created: '2026-06-13'
description: Global employment platform with a REST API for hiring international employees, managing contracts, processing global payroll, and ensuring local compliance in 180+ countries. The API enables integration with HRIS and payroll systems, time-off management, expense management, invoicing, benefits, offboarding, and provides embeddable web components for partners and resellers.
finops:
- name: Oyster Hr Finops
  service_category: ''
  slug: oyster-hr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oyster-hr.png
layout: provider
modified: '2026-06-13'
name: Oyster HR
nav: Providers
network: true
overview: 'Oyster HR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include HR, Global Employment, Payroll, Employer of Record, and EOR.


  Oyster HR''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Oyster Hr Plans Pricing
  plan_count: 5
  slug: oyster-hr-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Oyster Hr Rate Limits
  slug: oyster-hr-rate-limits
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 32.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oyster-hr/refs/heads/main/screenshots/oyster-hr-2026-06-20T191300.png
security:
- kind: domain-security
  name: Oyster Hr Domain Security
  slug: oyster-hr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Oyster Hr Trust Center
  slug: oyster-hr-trust-center
  summary_line: SOC 2
slug: oyster-hr
tags:
- HR
- Global Employment
- Payroll
- Employer of Record
- EOR
- Contractors
- Compliance
- Remote Work
website: https://www.oysterhr.com/
---
