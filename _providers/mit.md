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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-05'
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
random_paper: 15
rate_limits:
- limit_count: 5
  name: Mit Rate Limits
  slug: mit-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
