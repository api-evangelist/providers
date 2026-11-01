---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Manage Mockfly mock projects, endpoints and responses programmatically.
  name: Mockfly Public API
  slug: mockfly-public-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/mockfly/plans/mockfly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mockfly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mockfly/vocabulary/mockfly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mockfly-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/mockfly/cli/mockfly-cli.yml
  title: ''
  type: CLI
  url: cli/mockfly-cli.yml
- group: auth
  href: https://artifacts.apis.io/mockfly/authentication/mockfly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mockfly-authentication.yml
- group: design
  href: https://artifacts.apis.io/mockfly/conformance/mockfly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mockfly-conformance.yml
- group: other
  href: https://artifacts.apis.io/mockfly/overlays/mockfly-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mockfly-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/mockfly/llms/mockfly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mockfly-llms.txt
- group: other
  href: https://artifacts.apis.io/mockfly/hosts/mockfly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mockfly-hosts.yml
- group: other
  href: https://artifacts.apis.io/mockfly/vendors/mockfly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mockfly-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mockfly/security/mockfly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mockfly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mockfly.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mockfly.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://mockfly.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://mockfly.dev/articles/getting-started-with-mockfly/
- group: commercial
  title: ''
  type: Pricing
  url: https://mockfly.dev/pricing/
- group: company
  title: ''
  type: Blog
  url: https://mockfly.dev/articles/
- group: operate
  title: ''
  type: Support
  url: https://mockfly.dev/faq/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/organization/mockfly-workspace
created: '2026-10-20'
description: Mockfly provides a lightweight, developer‑friendly API platform that enables rapid creation, testing, and deployment of mock APIs for developers and QA teams. The service offers customizable endpoints, dynamic response generation, and seamless integration with CI/CD pipelines, helping teams accelerate development cycles and improve testing reliability. Mockfly’s intuitive dashboard and extensive documentation empower users to simulate complex API behaviors without building full backends, reducing overhead and speeding time‑to‑market. It supports import of OpenAPI, Postman collections, and HAR files, offers AI‑generated mock data, conditional response rules, custom domains, and real‑time analytics, making it a comprehensive solution for modern API development and testing workflows.
image: https://mockfly.dev/assets/logo.png
layout: provider
modified: '2026-10-20'
name: Mockfly
nav: Providers
network: true
overview: 'Mockfly is listed with 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include API Platform, Mock APIs, Developer Tools, Testing, and CI/CD Integration.


  Mockfly''s developer surface includes CLI, authentication, documentation, getting-started guide, pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Mockfly Plans Pricing
  plan_count: 4
  slug: mockfly-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 50.3
    catalog_earned_first_party: 12.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 8.3
    contract_quality: 37.6
    developer_ergonomics: 61.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mockfly Authentication
  slug: mockfly-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mockfly Domain Security
  slug: mockfly-domain-security
  summary_line: TLSv1.3
slug: mockfly
tags:
- API Platform
- Mock APIs
- Developer Tools
- Testing
- CI/CD Integration
website: https://mockfly.dev/
---
