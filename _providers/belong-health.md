---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API reference for Belong Health platform
  name: Belong Health API
  slug: belong-health-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belong-health/refs/heads/main/hosts/belong-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/belong-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belong-health/refs/heads/main/vendors/belong-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/belong-health-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/belong-health/refs/heads/main/security/belong-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belong-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://belong-health.com/
- group: docs
  title: ''
  type: Documentation
  url: https://belong-health.com/what-we-do/
- group: docs
  title: ''
  type: APIReference
  url: https://belong-health.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://belong-health.com/what-we-do/
- group: operate
  title: ''
  type: Support
  url: https://belong-health.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://belong-health.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://belong-health.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://belong-health.com/privacy-policy/
coverage:
  checked: '2026-09-27'
  detail: The API reference page https://belong-health.com/what-we-do/ redirects (301) and serves a JavaScript‑rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 301
    url: https://belong-health.com/what-we-do/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Belong Health provides a full‑stack health plan platform that helps insurers and health systems launch and grow Medicare Advantage and Special Needs Plans. Through coverage and care, they serve complex, high‑need communities, offering services such as MSSP, MA & SNP, and integrated care management. The company partners with health plans to streamline product development, risk sharing, and patient outcomes, aiming to make supportive healthcare available to everyone.
image: https://images.prismic.io/belong-health/e960e9ba-795d-4856-bee4-1275d9837c43_GettyImages-1190822834_%402x.jpg?auto=compress,format&rect=0,162,2958,1553&w=1200&h=630
layout: provider
modified: '2026-09-27'
name: Belong Health
nav: Providers
network: true
overview: 'Belong Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Insurance, Medicare, Healthcare, and Platform.


  Belong Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 6 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Belong Health Domain Security
  slug: belong-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: belong-health
tags:
- Health
- Insurance
- Medicare
- Healthcare
- Platform
- Company
website: https://belong-health.com/
---
