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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The MIT Roles API provides programmatic access to institutional role and authorization data, enabling MIT applications and authorized integrators to query, manage, and synchronize roles assigned to pe
  name: MIT Roles API
  slug: roles
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mit.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.mit.edu/
- group: auth
  title: ''
  type: Authentication
  url: https://ist.mit.edu/touchstone
created: '2025-02-08'
description: The Massachusetts Institute of Technology (MIT) operates an internal developer portal that exposes APIs for the institution's information systems. The MIT developer environment publishes APIs such as the Roles API for managing institutional roles and authorizations. Access to the developer portal and most APIs requires MIT authentication via Shibboleth / Touchstone single sign-on, making the catalog primarily available to community members, partners, and authorized integrators rather than to the general public.
finops:
- name: Mit Finops
  service_category: API
  slug: mit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mit.png
layout: provider
modified: '2026-04-28'
name: MIT
nav: Providers
network: true
overview: 'MIT publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, Identity, Research, and Roles.


  MIT''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Mit Plans Pricing
  plan_count: 3
  slug: mit-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Mit Rate Limits
  slug: mit-rate-limits
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mit/refs/heads/main/screenshots/mit-2026-06-20T185615.png
security:
- kind: domain-security
  name: Mit Domain Security
  slug: mit-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: mit
tags:
- Education
- Higher Education
- Identity
- Research
- Roles
- University
website: https://www.mit.edu/
---
