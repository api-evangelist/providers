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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'DapperDox is an open-source API documentation generator that renders beautiful, customizable reference docs from OpenAPI specifications with support for themes, overlays, and cross-referencing across '
  name: DapperDox
  slug: dapperdox
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/DapperDox/dapperdox/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/DapperDox/dapperdox/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/DapperDox/dapperdox/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dapperdox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dapperdox.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dapperdox.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DapperDox
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/DapperDox/dapperdox
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dapperdox-vocabulary.yml
created: '2026-03-27'
description: DapperDox is an open-source API documentation generator that creates beautiful, customizable reference documentation from OpenAPI specifications. It supports theming, overlays, and cross-referencing across multiple API specifications, making it suitable for teams managing complex API ecosystems. DapperDox is a developer tool rather than a hosted service, so it does not expose its own public web API.
finops:
- name: Dapperdox Finops
  service_category: API
  slug: dapperdox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dapperdox.png
layout: provider
modified: '2026-04-28'
name: DapperDox
nav: Providers
network: true
overview: 'DapperDox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Reference, Documentation, Developer Tools, Open-Source, and OpenAPI.


  DapperDox''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Dapperdox Plans Pricing
  plan_count: 3
  slug: dapperdox-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Dapperdox Rate Limits
  slug: dapperdox-rate-limits
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 15.2
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 59.3
    governance: 15.2
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 17.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dapperdox/refs/heads/main/screenshots/dapperdox-2026-06-20T175450.png
security:
- kind: domain-security
  name: Dapperdox Domain Security
  slug: dapperdox-domain-security
  summary_line: no transport/DNS hardening detected
slug: dapperdox
tags:
- API Reference
- Documentation
- Developer Tools
- Open-Source
- OpenAPI
- Static Site
website: https://dapperdox.io/
---
