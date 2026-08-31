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
  scored_at: '2026-08-30'
api_count: 6
apis:
- description: Mustache is a logic-less template syntax available for HTML, config files, source code, and more. Used widely for API client SDK generation, documentation generation, and configuration templating.
  name: Mustache Templates
  slug: mustache-templates
- description: Handlebars provides the power necessary to let you build semantic templates effectively with no frustration. Widely used in API documentation generation, email templates, and API portal theming.
  name: Handlebars.js
  slug: handlebarsjs
- description: Jinja is a fast, expressive, and extensible templating engine for Python. Used in API code generation (Cookiecutter templates), OpenAPI spec generation, Ansible playbooks, and infrastructure-as-code t
  name: Jinja2
  slug: jinja2
- description: OpenAPI Generator allows generation of API client libraries (SDK generation), server stubs, documentation and configuration automatically given an OpenAPI Spec. Supports 50+ languages and frameworks v
  name: OpenAPI Generator
  slug: openapi-generator
- description: A command-line utility that creates projects from project templates. Widely used for API project bootstrapping including FastAPI, Flask, Django REST, and microservice templates with standardized struc
  name: Cookiecutter
  slug: cookiecutter
- description: Yeoman is a scaffolding tool for modern webapps and APIs. Generators provide templates for REST APIs, Express apps, OpenAPI-first projects, and full-stack applications following community best practic
  name: Yeoman
  slug: yeoman
artifact_total: 14
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/mustache/mustache/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/mustache/mustache/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/mustache/mustache/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/mustache/mustache/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/templates-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mustache.github.io/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mustache/mustache
- group: design
  title: ''
  type: JSONLD
  url: json-ld/templates-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/templates-template-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/templates-vocabulary.yml
created: '2025'
description: A cross-industry subject-matter collection covering API design templates, code templates, documentation templates, API specification templates, and templating engines used in API development and integration workflows. Covers OpenAPI templates, AsyncAPI templates, JSON Schema templates, Postman collection templates, and SDK code generation templates.
examples:
- key_count: 5
  name: Templates Mustache Api Example
  slug: templates-mustache-api-example
finops:
- name: Templates Finops
  service_category: API
  slug: templates-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/templates.png
json_schemas:
- name: API Template
  property_count: 10
  slug: templates-template
jsonld:
- class_count: 10
  name: Templates Context
  property_count: 8
  slug: templates-context
layout: provider
modified: '2026-05-03'
name: Templates
nav: Providers
network: true
overview: 'Templates publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Templates, API Design, Code Generation, Documentation, and OpenAPI.


  The Templates catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Templates Plans Pricing
  plan_count: 3
  slug: templates-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Templates Rate Limits
  slug: templates-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Templates API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: templates-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 50.0
  previous_composite: 23.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/templates/refs/heads/main/screenshots/templates-2026-06-20T195055.png
security:
- kind: domain-security
  name: Templates Domain Security
  slug: templates-domain-security
  summary_line: TLSv1.3 · HSTS
slug: templates
tags:
- Templates
- API Design
- Code Generation
- Documentation
- OpenAPI
- AsyncAPI
website: https://mustache.github.io/
---
