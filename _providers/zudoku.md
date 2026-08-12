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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Zudoku Agentic Access
  operation_count: 6
  slug: zudoku-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- description: Zudoku is an open-source, developer-first API documentation framework built by Zuplo. It uses a file-based configuration model (zudoku.config.ts) to generate interactive API documentation from OpenAPI
  name: Zudoku Configuration API
  slug: configuration-api
- description: OpenAPI document references for generating API documentation.
  name: Zudoku API References API
  slug: zudoku-api-references-api
- description: Authentication provider configuration.
  name: Zudoku Authentication API
  slug: zudoku-authentication-api
- description: Site navigation and sidebar configuration.
  name: Zudoku Navigation API
  slug: zudoku-navigation-api
- description: Plugin registration and configuration.
  name: Zudoku Plugins API
  slug: zudoku-plugins-api
- description: Theme, branding, and visual customization.
  name: Zudoku Theming API
  slug: zudoku-theming-api
artifact_total: 19
collections:
- collection_type: open
  name: Zudoku Configuration API
  slug: open-zudoku-configuration-api
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
random_paper: 94
rate_limits:
- limit_count: 5
  name: Zudoku Rate Limits
  slug: zudoku-rate-limits
rules:
- name: Zudoku API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: zudoku-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.4
  delta: -7.7
  facets:
    commercial_clarity: 15.8
    contract_quality: 66.4
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 7.9
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
