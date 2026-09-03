---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 0
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-defense-finance-accounting-service
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defense-finance-accounting-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dfas
- group: company
  title: ''
  type: Website
  url: https://www.dfas.mil
- group: company
  title: ''
  type: About
  url: https://www.dfas.mil/About-DFAS/
- group: other
  title: ''
  type: myPay
  url: https://mypay.dfas.mil
- group: operate
  title: ''
  type: Contact
  url: https://www.dfas.mil/Customer-Service/
created: '2024-12-03'
description: The Defense Finance and Accounting Service (DFAS) is the agency within the Department of Defense responsible for paying members of the U.S. military, DoD civilian employees, contractors, and annuitants, as well as providing finance and accounting services to DoD components and other federal agencies. DFAS exposes member-facing self-service portals such as myPay but does not currently publish a public developer API.
finops:
- name: Defense Finance Accounting Service Finops
  service_category: API
  slug: defense-finance-accounting-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defense-finance-accounting-service.png
layout: provider
modified: '2026-04-28'
name: Defense Finance and Accounting Service
nav: Providers
network: true
overview: Defense Finance and Accounting Service is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Defense, Department of Defense, Finance, and Accounting.
plans:
- name: Defense Finance Accounting Service Plans Pricing
  plan_count: 1
  slug: defense-finance-accounting-service-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Defense Finance Accounting Service Rate Limits
  slug: defense-finance-accounting-service-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defense-finance-accounting-service/refs/heads/main/screenshots/defense-finance-accounting-service-2026-06-20T175832.png
security:
- kind: domain-security
  name: Defense Finance Accounting Service Domain Security
  slug: defense-finance-accounting-service-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: defense-finance-accounting-service
tags:
- Federal-Government
- Defense
- Department of Defense
- Finance
- Accounting
- Military Pay
- Civilian Pay
- Retirement
- Annuitants
website: https://www.dfas.mil
---
