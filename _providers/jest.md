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
api_count: 3
apis:
- description: Core testing framework API for writing and running tests, including globals, expect assertions, mock functions, and configuration options.
  name: Jest Core API
  slug: jest-core-api
- description: Command-line interface for running Jest tests with various options.
  name: Jest CLI
  slug: jest-cli
- description: Programmatic configuration options for customizing Jest behavior.
  name: Jest Configuration API
  slug: jest-configuration
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jestjs.io
- group: docs
  title: ''
  type: Documentation
  url: https://jestjs.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://jestjs.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jestjs
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/j6FKKQQrW9
created: '2024-01-01'
description: Jest is a delightful JavaScript testing framework with a focus on simplicity. It works with projects using Babel, TypeScript, Node, React, Angular, Vue and more. Jest provides snapshot testing, parallel execution, built-in mocking, and code coverage out of the box.
finops:
- name: Jest Finops
  service_category: API
  slug: jest-finops
image: https://jestjs.io/img/jest.png
layout: provider
modified: '2026-03-16'
name: Jest
nav: Providers
network: true
overview: 'Jest publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include JavaScript, Mocking, Snapshot Testing, Testing, and Unit Testing.


  Jest''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Jest Plans Pricing
  plan_count: 3
  slug: jest-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Jest Rate Limits
  slug: jest-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jest/refs/heads/main/screenshots/jest-2026-06-20T183722.png
security:
- kind: domain-security
  name: Jest Domain Security
  slug: jest-domain-security
  summary_line: TLSv1.3 · HSTS
slug: jest
tags:
- JavaScript
- Mocking
- Snapshot Testing
- Testing
- Unit Testing
website: https://jestjs.io
---
