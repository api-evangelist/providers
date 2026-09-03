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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Fastify is a fast and low-overhead web framework for Node.js, designed for building high-performance APIs and microservices. It features a powerful plugin architecture, JSON Schema-based request and r
  name: Fastify
  slug: fastify
artifact_total: 8
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/fastify/fastify/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/fastify/fastify/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/fastify/fastify/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/fastify/fastify/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/fastify/fastify/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/fastify/fastify/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fastify-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fastify-dev
- group: company
  title: ''
  type: Website
  url: https://fastify.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://fastify.dev/docs/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://fastify.dev/docs/latest/Guides/Getting-Started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fastify
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/fastify/fastify
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@fastifyjs
- group: build
  title: ''
  type: Plugins
  url: https://fastify.dev/ecosystem/
- group: other
  title: ''
  type: Benchmarks
  url: https://fastify.dev/benchmarks/
- group: agent
  title: ''
  type: LlmsText
  url: https://fastify.dev/llms.txt
created: '2026-03-26'
description: Fastify is a fast and low-overhead web framework for Node.js, designed for building high-performance APIs and microservices. It features a powerful plugin architecture, JSON Schema-based request and response validation, automatic serialization, comprehensive logging with Pino, and TypeScript support out of the box.
finops:
- name: Fastify Finops
  service_category: API
  slug: fastify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fastify.png
json_schemas:
- name: Fastify Plugin and Server Configuration
  property_count: 18
  slug: fastify-plugin-config
- name: Fastify Route Schema Definition
  property_count: 10
  slug: fastify-route
layout: provider
modified: '2026-04-28'
name: Fastify
nav: Providers
network: true
overview: 'Fastify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Frameworks, High Performance, JavaScript, JSON-Schema, and Node.js.


  The Fastify catalog on APIs.io includes 1 Spectral governance ruleset.


  Fastify''s developer surface includes documentation, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Fastify Plans Pricing
  plan_count: 3
  slug: fastify-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Fastify Rate Limits
  slug: fastify-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Fastify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fastify-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 60.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 13.3
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fastify/refs/heads/main/screenshots/fastify-2026-06-20T181051.png
security:
- kind: domain-security
  name: Fastify Domain Security
  slug: fastify-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fastify
tags:
- Frameworks
- High Performance
- JavaScript
- JSON-Schema
- Node.js
- TypeScript
website: https://fastify.dev/
---
