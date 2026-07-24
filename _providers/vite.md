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
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Vite Agentic Access
  operation_count: 6
  slug: vite-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 2
apis:
- description: Create and manage the Vite development server
  name: Vite Dev Server API
  slug: vite-dev-server-api
- description: HMR-related plugin capabilities
  name: Vite Hot Module Replacement API
  slug: vite-hot-module-replacement-api
artifact_total: 16
collections:
- collection_type: open
  name: Vite JavaScript API
  slug: open-vite-javascript-api
- collection_type: open
  name: Vite Plugin API
  slug: open-vite-plugin-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vite-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vitejs.dev
- group: docs
  title: ''
  type: Documentation
  url: https://vite.dev/guide/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vitejs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/vitejs/vite
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/vite_js
- group: operate
  title: ''
  type: Discord
  url: https://chat.vitejs.dev
- group: build
  title: ''
  type: npm Package
  url: https://www.npmjs.com/package/vite
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/vitejs/vite/blob/main/LICENSE
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vitejs/vite-plugin-vue
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vitejs/vite-plugin-react
- group: agent
  title: ''
  type: LlmsText
  url: https://vite.dev/llms.txt
created: '2025-01-08'
description: Vite is a next-generation frontend build tool that dramatically improves the frontend development experience. It provides a lightning-fast dev server using native ES modules, an optimized production build via Rolldown/Rollup, a rich plugin API, and a fully-typed JavaScript API for programmatic usage.
examples:
- key_count: 5
  name: Vite Javascript Api Build Example
  slug: vite-javascript-api-build-example
- key_count: 5
  name: Vite Javascript Api Create Server Example
  slug: vite-javascript-api-create-server-example
finops:
- name: Vite Finops
  service_category: API
  slug: vite-finops
image: https://vitejs.dev/logo.svg
json_schemas:
- name: Vite InlineConfig
  property_count: 13
  slug: vite-inline-config
json_structures:
- name: Vite Inline Config Structure
  property_count: 0
  slug: vite-inline-config-structure
jsonld:
- class_count: 8
  name: Vite Context
  property_count: 36
  slug: vite-context
layout: provider
modified: '2026-05-19'
name: Vite
nav: Providers
network: true
overview: 'Vite publishes 2 APIs on the [APIs.io](https://apis.io/) network: Dev Server API and Hot Module Replacement API. Tagged areas include Build Tools, Bundler, Development Server, ESM, and Frontend.


  The Vite catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vite''s developer surface includes documentation, changelog, and 12 more developer resources.'
plans:
- name: Vite Plans Pricing
  plan_count: 3
  slug: vite-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Vite Rate Limits
  slug: vite-rate-limits
rules:
- name: Vite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vite-jsonschema-spectral-rules
- name: Vite API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: vite-rules
score:
  band: developing
  composite: 47.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.3
    developer_ergonomics: 15.2
    discoverability: 60.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 47.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vite/refs/heads/main/screenshots/vite-2026-06-20T201105.png
security:
- kind: domain-security
  name: Vite Domain Security
  slug: vite-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: vite
tags:
- Build Tools
- Bundler
- Development Server
- ESM
- Frontend
- Hot Module Replacement
- JavaScript
- Plugin API
- TypeScript
- Vite
website: https://vitejs.dev
---
