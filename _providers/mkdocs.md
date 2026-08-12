---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mkdocs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mkdocs.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.mkdocs.org/user-guide/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mkdocs.org/getting-started/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mkdocs/mkdocs
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mkdocs-config-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mkdocs-plugin-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mkdocs-context.jsonld
created: '2026-03-18'
description: MkDocs is a fast, simple, and beautiful static site generator designed for building project documentation from Markdown source files. Written in Python, it reads a single YAML configuration file (mkdocs.yml) and converts a directory of Markdown documents into a self-contained static HTML site. MkDocs supports multiple built-in themes (mkdocs, readthedocs), a rich plugin ecosystem via Python entry points, live-reloading development server, and one-command deployment to GitHub Pages.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mkdocs.png
json_schemas:
- name: MkDocs Configuration
  property_count: 30
  slug: mkdocs-config
- name: MkDocs Plugin
  property_count: 6
  slug: mkdocs-plugin
jsonld:
- class_count: 0
  name: Mkdocs Context
  property_count: 7
  slug: mkdocs-context
layout: provider
modified: '2026-04-28'
name: MkDocs
nav: Providers
network: true
overview: 'MkDocs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Documentation, Markdown, Open Source, Python, and Static Site Generator.


  The MkDocs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MkDocs'' developer surface includes documentation, getting-started guide, GitHub presence, and 5 more developer resources.'
random_paper: 61
rules:
- name: MkDocs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: mkdocs-jsonschema-spectral-rules
score:
  band: emerging
  composite: 18.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 8.1
    developer_ergonomics: 19.6
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 18.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mkdocs/refs/heads/main/screenshots/mkdocs-2026-06-20T185621.png
security:
- kind: domain-security
  name: Mkdocs Domain Security
  slug: mkdocs-domain-security
  summary_line: TLSv1.3
slug: mkdocs
tags:
- Documentation
- Markdown
- Open Source
- Python
- Static Site Generator
website: https://www.mkdocs.org
---
