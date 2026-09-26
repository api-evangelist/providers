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
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Beanstalk API provides endpoints for repository management, deployments, and collaboration features as described in the developer guides.
  name: Beanstalk API
  slug: beanstalk-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beanstalk-app/refs/heads/main/well-known/beanstalk-app-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beanstalk-app-status-security.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/beanstalk-app/refs/heads/main/plans/beanstalk-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beanstalk-app-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beanstalk-app/refs/heads/main/well-known/beanstalk-app-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beanstalk-app-blog-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beanstalk-app/refs/heads/main/well-known/beanstalk-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beanstalk-app-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beanstalk-app/refs/heads/main/vendors/beanstalk-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beanstalk-app-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/beanstalk-app/refs/heads/main/packages/beanstalk-app-packages.yml
  title: ''
  type: SDKs
  url: packages/beanstalk-app-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/beanstalk-app/refs/heads/main/packages/beanstalk-app-packages.yml
  title: ''
  type: Packages
  url: packages/beanstalk-app-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.beanstalkapp.com
- group: auth
  title: ''
  type: Security
  url: https://beanstalkapp.com/Security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beanstalk-app/refs/heads/main/security/beanstalk-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beanstalk-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beanstalkapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://guides.beanstalkapp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.beanstalkapp.com/
- group: operate
  title: ''
  type: Support
  url: https://support.beanstalkapp.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.beanstalkapp.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://beanstalkapp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://signup.beanstalkapp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beanstalkapp.com/terms-of-service
coverage:
  checked: 2026-09-22
  detail: API reference at https://api.beanstalkapp.com/ returns 404 for common OpenAPI paths, and no machine‑readable spec is published.
  evidence:
  - status: 404
    url: https://api.beanstalkapp.com/openapi.json
  - status: 404
    url: https://api.beanstalkapp.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-22'
description: Beanstalk provides a complete workflow platform for writing, reviewing, and deploying code, supporting both Git and SVN repositories. It offers features like branch management, code reviews, permissions, notifications, and integrations, serving over 70,000 companies worldwide. The service includes pricing plans, support resources, and a status page for operational transparency.
image: https://beanstalkapp.com/images/apple-touch-icon-144x144-precomposed.png
layout: provider
modified: '2026-09-22'
name: Beanstalk
nav: Providers
network: true
overview: 'Beanstalk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Code Hosting, CI/CD, and Collaboration.


  Beanstalk''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Beanstalk App Plans Pricing
  plan_count: 6
  slug: beanstalk-app-plans-pricing
random_paper: 17
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 26.3
  previous_composite: 28.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beanstalk App Domain Security
  slug: beanstalk-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beanstalk-app
tags:
- Company
- DevOps
- Code Hosting
- CI/CD
- Collaboration
website: https://beanstalkapp.com/
---
