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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Common security vulnerabilities in REST APIs include Cross-Site Request Forgery (CSRF), Injection attacks, and insecure direct object references. Pynt helps identify and fix these issues through autom
  name: Pynt
  slug: pynt
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pynt-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pynt-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pynt
- group: agent
  title: ''
  type: LlmsText
  url: https://www.pynt.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.pynt.io/blog
created: '2025-01-08'
description: Pynt is an API security testing platform that helps developers identify and remediate security vulnerabilities in REST APIs including CSRF, Injection attacks, and insecure direct object references.
finops:
- name: Pynt Finops
  service_category: API
  slug: pynt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pynt.png
layout: provider
modified: '2026-03-16'
name: Pynt
nav: Providers
network: true
overview: 'Pynt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, Platform, and Security.


  Pynt''s developer surface includes engineering blog and 4 more developer resources.'
plans:
- name: Pynt Plans Pricing
  plan_count: 3
  slug: pynt-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Pynt Rate Limits
  slug: pynt-rate-limits
score:
  band: emerging
  composite: 11.0
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 9.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pynt/refs/heads/main/screenshots/pynt-2026-06-20T192329.png
security:
- kind: domain-security
  name: Pynt Domain Security
  slug: pynt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pynt
tags:
- API Testing
- Platform
- Security
---
