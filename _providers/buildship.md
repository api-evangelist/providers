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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: BuildShip offers an AI-powered workflow builder with integrations and automation capabilities.
  name: BuildShip API
  slug: buildship-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/buildship/plans/buildship-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildship-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/buildship/changelog/buildship-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/buildship-changelog.yml
- group: other
  href: https://artifacts.apis.io/buildship/hosts/buildship-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildship-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildship/vendors/buildship-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildship-vendors.yml
- group: auth
  href: https://artifacts.apis.io/buildship/security/buildship-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildship-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildship.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.buildship.com/
- group: docs
  title: ''
  type: APIReference
  url: https://buildship.com/assistant-api
- group: start
  title: ''
  type: GettingStarted
  url: https://buildship.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://buildship.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://buildship.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.buildship.com/support-messages
coverage:
  checked: '2026-10-19'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found after probing common spec locations.
  evidence:
  - status: 200
    url: https://api.buildship.com/openapi.json
  - status: 404
    url: https://api.buildship.com/openapi.yaml
  - status: 404
    url: https://api.buildship.com/swagger.json
  - status: 404
    url: https://api.buildship.com/v1/openapi.json
  - status: 200
    url: https://app.buildship.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: BuildShip provides an AI-powered workflow builder that enables businesses to create, automate, and ship AI-driven processes without writing code. Users can connect data sources, tools, and agents through a visual interface, customize with full-code access, and deploy solutions across HR, finance, marketing, and more. The platform offers ready-made nodes, integrations with popular services, and enterprise features for scaling AI automation.
image: https://framerusercontent.com/images/1TWZPPULHUdlm9Sj2cHsAYi62k.png
layout: provider
modified: '2026-10-19'
name: BuildShip
nav: Providers
network: true
overview: 'BuildShip is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Workflows, Automation, No-Code, and Integration.


  BuildShip''s developer surface includes changelog, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 5 more developer resources.'
plans:
- name: Buildship Plans Pricing
  plan_count: 4
  slug: buildship-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buildship Domain Security
  slug: buildship-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buildship
tags:
- Artificial Intelligence
- Workflows
- Automation
- No-Code
- Integration
- Company
website: https://buildship.com/
---
