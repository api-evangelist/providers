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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Zudoku Agentic Access
  operation_count: 6
  slug: zudoku-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- baseURL: https://zudoku.dev
  baseurl_source: spec
  description: Zudoku is an open-source, developer-first API documentation framework built by Zuplo. It uses a file-based configuration model (zudoku.config.ts) to generate interactive API documentation from OpenAPI
  name: Zudoku Configuration API
  slug: configuration-api
- baseURL: https://zudoku.dev
  baseurl_source: spec
  description: OpenAPI document references for generating API documentation.
  name: Zudoku API References API
  slug: zudoku-api-references-api
- baseURL: https://zudoku.dev
  baseurl_source: spec
  description: Authentication provider configuration.
  name: Zudoku Authentication API
  slug: zudoku-authentication-api
- baseURL: https://zudoku.dev
  baseurl_source: spec
  description: Site navigation and sidebar configuration.
  name: Zudoku Navigation API
  slug: zudoku-navigation-api
- baseURL: https://zudoku.dev
  baseurl_source: spec
  description: Plugin registration and configuration.
  name: Zudoku Plugins API
  slug: zudoku-plugins-api
- baseURL: https://zudoku.dev
  baseurl_source: spec
  description: Theme, branding, and visual customization.
  name: Zudoku Theming API
  slug: zudoku-theming-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zudoku Configuration API References API
  slug: open-zudoku-api-references-api
- collection_type: open
  name: Zudoku Configuration API References Authentication API
  slug: open-zudoku-authentication-api
- collection_type: open
  name: Zudoku API References Configuration API
  slug: open-zudoku-configuration-api
- collection_type: open
  name: Zudoku Configuration API References Navigation API
  slug: open-zudoku-navigation-api
- collection_type: open
  name: Zudoku Configuration API References Plugins API
  slug: open-zudoku-plugins-api
- collection_type: open
  name: Zudoku Configuration API References Theming API
  slug: open-zudoku-theming-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zudoku-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zudoku-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://zudoku.dev/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://zudoku.dev/docs/configuration/authentication
- group: docs
  title: ''
  type: Guide
  url: https://zudoku.dev/docs/guides/static-files
- group: docs
  title: ''
  type: APIReference
  url: https://zudoku.dev/docs/configuration/api-reference
- group: other
  title: ''
  type: APICatalog
  url: https://zudoku.dev/docs/configuration/api-catalog
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/zuplo/zudoku
- group: agent
  title: ''
  type: LlmsText
  url: https://zudoku.dev/llms.txt
created: '2026-01-05'
description: Zudoku is an open-source, developer-first platform for creating clean, consistent API documentation built on a modern stack including React, TypeScript, and Vite. The tool enables developers to auto-generate documentation from OpenAPI v2/v3 schemas (supporting both single and multi-API setups) and provides built-in authentication and authorization support for OAuth2, JWT, and more.
finops:
- name: Zudoku Finops
  service_category: API
  slug: zudoku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zudoku.png
json_schemas:
- name: Zudoku API Reference
  property_count: 5
  slug: api-reference
- name: Zudoku Authentication Configuration
  property_count: 6
  slug: authentication
- name: Zudoku Plugin
  property_count: 2
  slug: plugin
- name: Zudoku Theme Configuration
  property_count: 3
  slug: theme
- name: Zudoku Configuration
  property_count: 11
  slug: zudoku-config
jsonld:
- class_count: 12
  name: Zudoku Context
  property_count: 7
  slug: zudoku-context
layout: provider
modified: '2026-05-19'
name: Zudoku
nav: Providers
network: true
overview: 'Zudoku publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Configuration API, API References API, Authentication API, and 3 more. Tagged areas include Developer Tools and Documentation.


  The Zudoku catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zudoku''s developer surface includes documentation, authentication, API reference, and 6 more developer resources.'
plans:
- name: Zudoku Plans Pricing
  plan_count: 3
  slug: zudoku-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Zudoku Rate Limits
  slug: zudoku-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Zudoku API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: zudoku-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 45.8
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 62.2
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zudoku/refs/heads/main/screenshots/zudoku-2026-06-20T201959.png
security:
- kind: domain-security
  name: Zudoku Domain Security
  slug: zudoku-domain-security
  summary_line: TLSv1.3 · HSTS
slug: zudoku
tags:
- Developer Tools
- Documentation
---
