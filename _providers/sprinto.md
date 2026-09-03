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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST API for building custom compliance, evidence, and risk workflows on Sprinto. Detailed reference is gated; access is provisioned through Sprinto support.
  name: Sprinto Platform API
  slug: platform-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sprinto-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sprinto-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://sprinto.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goSprinto
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sprinto-com
- group: company
  title: ''
  type: Website
  url: https://sprinto.com/
- group: other
  title: ''
  type: Developer
  url: https://www.sprinto.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/sprinto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sprinto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sprinto-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sprinto.com/llms.txt
created: '2026-05-08'
description: Sprinto is a security and compliance automation platform supporting SOC 2, ISO 27001, HIPAA, GDPR, PCI DSS, and more. Sprinto offers an API for building custom compliance and risk workflows; specific public reference docs are limited and require a customer login.
finops:
- name: Sprinto Finops
  service_category: Compliance & Governance
  slug: sprinto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sprinto.png
layout: provider
modified: '2026-05-08'
name: Sprinto
nav: Providers
network: true
overview: 'Sprinto publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GRC, Compliance, SOC 2, ISO 27001, and Security.


  Sprinto''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Sprinto Plans Pricing
  plan_count: 1
  slug: sprinto-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Sprinto Rate Limits
  slug: sprinto-rate-limits
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sprinto/refs/heads/main/screenshots/sprinto-2026-06-20T194423.png
security:
- kind: domain-security
  name: Sprinto Domain Security
  slug: sprinto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sprinto Trust Center
  slug: sprinto-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: sprinto
tags:
- GRC
- Compliance
- SOC 2
- ISO 27001
- Security
website: https://sprinto.com/
---
