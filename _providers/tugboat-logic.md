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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Tugboat Logic is now OneTrust Certification Automation. Programmatic access, where available, is provided through the OneTrust developer platform. Legacy Tugboat Logic APIs are not separately document
  name: Tugboat Logic via OneTrust Developer Platform
  slug: onetrust-platform
artifact_total: 6
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/onetrust/
- group: auth
  title: ''
  type: TrustCenter
  url: security/tugboat-logic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tugboat-logic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tugboat-logic-inc
- group: company
  title: ''
  type: Website
  url: https://www.onetrust.com/products/certification-automation/
- group: other
  title: ''
  type: Developer
  url: https://developer.onetrust.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/tugboat-logic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tugboat-logic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tugboat-logic-finops.yml
created: '2026-05-08'
description: Tugboat Logic is a security assurance and compliance automation platform acquired by OneTrust in 2021. It supports SOC 2, ISO 27001, HIPAA, GDPR, and NIST. As of 2024, the product has been rebranded under OneTrust's Certification Automation offering; legacy Tugboat Logic APIs are not publicly documented and integrations now flow through OneTrust's developer platform.
finops:
- name: Tugboat Logic Finops
  service_category: Compliance & Governance
  slug: tugboat-logic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tugboat-logic.png
layout: provider
modified: '2026-05-08'
name: Tugboat Logic
nav: Providers
network: true
overview: Tugboat Logic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GRC, Compliance, SOC 2, ISO 27001, and Security.
plans:
- name: Tugboat Logic Plans Pricing
  plan_count: 1
  slug: tugboat-logic-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Tugboat Logic Rate Limits
  slug: tugboat-logic-rate-limits
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tugboat-logic/refs/heads/main/screenshots/tugboat-logic-2026-06-20T195824.png
security:
- kind: domain-security
  name: Tugboat Logic Domain Security
  slug: tugboat-logic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Tugboat Logic Trust Center
  slug: tugboat-logic-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tugboat-logic
tags:
- GRC
- Compliance
- SOC 2
- ISO 27001
- Security
website: https://www.onetrust.com/products/certification-automation/
---
