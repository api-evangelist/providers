---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: ReDoc is an open-source API documentation renderer for OpenAPI specifications, originally created by Rebilly and now maintained by Redocly. It generates a responsive three-panel documentation layout f
  name: ReDoc
  slug: redoc
artifact_total: 12
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/redoc-a2a.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redoc-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://redocly.com/docs/redoc
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Redocly/redoc
- group: start
  title: ''
  type: LiveDemo
  url: https://redocly.github.io/redoc/
- group: build
  title: ''
  type: npm
  url: https://www.npmjs.com/package/redoc
- group: other
  title: ''
  type: CDN
  url: https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js
- group: docs
  title: ''
  type: Reference
  url: https://redocly.com/docs/redoc/config
- group: docs
  title: ''
  type: Reference
  url: https://redocly.com/docs/api-reference-docs/specification-extensions/
- group: start
  title: ''
  type: GettingStarted
  url: https://redocly.com/docs/redoc/deployment
- group: build
  title: ''
  type: CLI
  url: https://redocly.com/docs/cli/commands/build-docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Redocly/redoc/blob/main/CHANGELOG.md
- group: other
  title: ''
  type: Docker
  url: https://hub.docker.com/r/redocly/redoc
- group: company
  title: ''
  type: Website
  url: https://redocly.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Redocly
- group: other
  title: ''
  type: X
  url: https://twitter.com/Redocly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redocly
- group: commercial
  title: ''
  type: License
  url: https://github.com/Redocly/redoc/blob/main/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://redocly.com/blog/feed.xml
created: '2026-03-18'
description: ReDoc is an open-source API documentation renderer for OpenAPI specifications by Redocly. It generates a responsive three-panel documentation layout from OpenAPI 3.1, 3.0, and Swagger 2.0 definitions. The left panel provides a search bar and navigation menu, the central panel displays documentation content, and the right panel shows request and response examples. ReDoc is available as a CLI tool, HTML custom element, React component, and Docker image. It supports vendor extensions for logos, tag groups, custom code samples, and internal operations.
examples:
- key_count: 3
  name: Redoc Html Tag Example
  slug: redoc-html-tag-example
- key_count: 4
  name: Redoc React Example
  slug: redoc-react-example
- key_count: 2
  name: Redoc Vendor Extensions Example
  slug: redoc-vendor-extensions-example
finops:
- name: Redoc Finops
  service_category: API
  slug: redoc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: ReDoc Configuration
  property_count: 39
  slug: redoc-configuration
json_structures:
- name: Redoc Configuration Structure
  property_count: 0
  slug: redoc-configuration-structure
jsonld:
- class_count: 0
  name: Redoc Context
  property_count: 8
  slug: redoc-context
layout: provider
modified: '2026-05-02'
name: ReDoc
nav: Providers
network: true
overview: 'ReDoc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Documentation, Developer Tools, Documentation, OpenAPI, and Reference.


  The ReDoc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ReDoc''s developer surface includes documentation, GitHub presence, getting-started guide, CLI, changelog, engineering blog, and 13 more developer resources.'
plans:
- name: Redoc Plans Pricing
  plan_count: 3
  slug: redoc-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Redoc Rate Limits
  slug: redoc-rate-limits
rules:
- name: ReDoc API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: redoc-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.0
  delta: -4.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 43.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redoc/refs/heads/main/screenshots/redoc-2026-06-20T192730.png
security:
- kind: domain-security
  name: Redoc Domain Security
  slug: redoc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: redoc
tags:
- API Documentation
- Developer Tools
- Documentation
- OpenAPI
- Reference
- Renderer
website: https://redocly.com/
---
