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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API providing programmatic access to Secureframe controls, frameworks, tests, evidence, personnel, vendors, and audit data. Authenticated with API access tokens.
  name: Secureframe Public API
  slug: public-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/secureframe-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/secureframe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secureframe-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/secureframe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/secureframe
- group: company
  title: ''
  type: Website
  url: https://secureframe.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.secureframe.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/secureframe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/secureframe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/secureframe-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://secureframe.com/blog
created: '2026-05-08'
description: Secureframe automates security and privacy compliance for SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, NIST, and more. The Secureframe Public API exposes controls, frameworks, evidence, tests, personnel, and vendor data.
finops:
- name: Secureframe Finops
  service_category: GRC
  slug: secureframe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/secureframe.png
layout: provider
modified: '2026-05-08'
name: Secureframe
nav: Providers
network: true
overview: 'Secureframe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GRC, Compliance, SOC 2, ISO 27001, and Risk.


  Secureframe''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Secureframe Plans Pricing
  plan_count: 1
  slug: secureframe-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Secureframe Rate Limits
  slug: secureframe-rate-limits
score:
  band: emerging
  composite: 12.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/secureframe/refs/heads/main/screenshots/secureframe-2026-06-20T193625.png
security:
- kind: domain-security
  name: Secureframe Domain Security
  slug: secureframe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Secureframe Vulnerability Disclosure
  slug: secureframe-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Secureframe Trust Center
  slug: secureframe-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: secureframe
tags:
- GRC
- Compliance
- SOC 2
- ISO 27001
- Risk
website: https://secureframe.com/
---
