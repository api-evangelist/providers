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
    event_surface_described: unknown
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Hooksbase API as documented publicly: 92 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Hooksbase API
  slug: hooksbase-api
artifact_total: 6
common:
- group: start
  title: ''
  type: Login
  url: https://app.hooksbase.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hooksbase.com/docs/quickstart
- group: operate
  href: https://artifacts.apis.io/hooksbase/rate-limits/hooksbase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hooksbase-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hooksbase/plans/hooksbase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hooksbase-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hooksbase/rules/hooksbase-rules.yml
  title: ''
  type: Spectral
  url: rules/hooksbase-rules.yml
- group: design
  href: https://artifacts.apis.io/hooksbase/vocabulary/hooksbase-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hooksbase-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/hooksbase/cli/hooksbase-cli.yml
  title: ''
  type: CLI
  url: cli/hooksbase-cli.yml
- group: design
  href: https://artifacts.apis.io/hooksbase/conventions/hooksbase-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hooksbase-conventions.yml
- group: design
  href: https://artifacts.apis.io/hooksbase/conventions/hooksbase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hooksbase-conventions.yml
- group: auth
  href: https://artifacts.apis.io/hooksbase/authentication/hooksbase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hooksbase-authentication.yml
- group: design
  href: https://artifacts.apis.io/hooksbase/conformance/hooksbase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hooksbase-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hooksbase/llms/hooksbase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hooksbase-llms.txt
- group: other
  href: https://artifacts.apis.io/hooksbase/hosts/hooksbase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hooksbase-hosts.yml
- group: other
  href: https://artifacts.apis.io/hooksbase/vendors/hooksbase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hooksbase-vendors.yml
- group: build
  href: https://artifacts.apis.io/hooksbase/packages/hooksbase-packages.yml
  title: ''
  type: SDKs
  url: packages/hooksbase-packages.yml
- group: build
  href: https://artifacts.apis.io/hooksbase/packages/hooksbase-packages.yml
  title: ''
  type: Packages
  url: packages/hooksbase-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.hooksbase.com/glossary/webhook
- group: auth
  href: https://artifacts.apis.io/hooksbase/security/hooksbase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hooksbase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hooksbase.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hooksbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hooksbase.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.hooksbase.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.hooksbase.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hooksbase
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hooksbase.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hooksbase.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hooksbase.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/hooksbase/workspace
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract found on any discovered host.
  evidence:
  - status: 404
    url: https://api.hooksbase.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: Hooksbase provides event infrastructure for AI agents, enabling reliable ingestion, routing, transformation, and delivery of events from HTTP, email, forms, and schedules. It offers automation workflows, versioned automations, and replay capabilities without building custom webhook plumbing, supporting integrations with major platforms and cloud destinations.
image: https://www.hooksbase.com/opengraph-image
layout: provider
modified: '2026-10-17'
name: Hooksbase
nav: Providers
network: true
overview: 'Hooksbase is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Event Infrastructure, Artificial Intelligence, Webhook, and Automation.


  The Hooksbase catalog on APIs.io includes 1 Spectral governance ruleset.


  Hooksbase''s developer surface includes getting-started guide, CLI, authentication, documentation, API reference, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Hooksbase Plans Pricing
  plan_count: 5
  slug: hooksbase-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Hooksbase Rate Limits
  slug: hooksbase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Hooksbase API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: hooksbase-rules
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.8
    catalog_earned_first_party: 24.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 8.1
    developer_ergonomics: 71.4
    discoverability: 57.1
    operational_transparency: 44.7
  previous_composite: 46.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hooksbase Authentication
  slug: hooksbase-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Hooksbase Domain Security
  slug: hooksbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hooksbase
tags:
- Company
- Event Infrastructure
- Artificial Intelligence
- Webhook
- Automation
- Integration
website: https://hooksbase.com/
---
