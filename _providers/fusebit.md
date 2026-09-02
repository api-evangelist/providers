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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Fusebit provides a code-first integration platform that enables developers to build, deploy, and manage integrations within their SaaS products. The platform is no longer actively maintained following
  name: Fusebit API
  slug: apis
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fusebit-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fusebit
- group: company
  title: ''
  type: Website
  url: https://fusebit.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fusebit.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fusebit
created: '2026-03-27'
description: Fusebit is a developer-first embedded integration platform for adding third-party integrations to SaaS products. The company was acquired and the Fusebit platform and developer documentation are no longer actively maintained, but the historical API surface and SDK assets remain available via the Fusebit GitHub organization for reference.
finops:
- name: Fusebit Finops
  service_category: API
  slug: fusebit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fusebit.png
layout: provider
modified: '2026-04-28'
name: Fusebit
nav: Providers
network: true
overview: 'Fusebit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Embedded iPaaS, Integration, and Acquired.


  Fusebit''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Fusebit Plans Pricing
  plan_count: 3
  slug: fusebit-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Fusebit Rate Limits
  slug: fusebit-rate-limits
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Fusebit Domain Security
  slug: fusebit-domain-security
  summary_line: no transport/DNS hardening detected
slug: fusebit
tags:
- Developer Tools
- Embedded iPaaS
- Integration
- Acquired
website: https://fusebit.io
---
