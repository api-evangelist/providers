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
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.3
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Programmatic access to the TypeScript compiler. The Compiler API allows developers to parse TypeScript files into ASTs, perform type checking, emit JavaScript, and transform code programmatically.
  name: TypeScript Compiler API
  slug: typescript-compiler-api
- description: API for editor integration and language tooling. The Language Service API provides completions, diagnostics, quick fixes, rename, go-to-definition, find references, and other IDE features that power e
  name: TypeScript Language Service API
  slug: typescript-language-service-api
- description: The TypeScript Transform API enables custom AST transformations during compilation. Transformers can modify, add, or remove nodes in the TypeScript AST before code emission.
  name: TypeScript Transform API
  slug: typescript-transform-api
artifact_total: 13
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/microsoft/TypeScript/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/typescript-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.typescriptlang.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.typescriptlang.org/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/TypeScript
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/typescript/
- group: operate
  title: ''
  type: Community
  url: https://www.typescriptlang.org/community
- group: build
  title: ''
  type: npm
  url: https://www.npmjs.com/package/typescript
- group: other
  title: ''
  type: Playground
  url: https://www.typescriptlang.org/play
- group: other
  title: ''
  type: Handbook
  url: https://www.typescriptlang.org/docs/handbook/intro.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.typescriptlang.org/docs/handbook/release-notes/overview.html
- group: build
  title: ''
  type: GitHubIssues
  url: https://github.com/microsoft/TypeScript/issues
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/typescript
- group: design
  title: ''
  type: JSONLD
  url: json-ld/typescript-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/typescript-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/typescript-diagnostic-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/typescript-compiler-options-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/typescript-diagnostic-structure.json
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/microsoft/TypeScript-Maintainer-Skills
created: '2024-01-01'
description: TypeScript is a strongly typed programming language that builds on JavaScript, adding optional static type checking and other features. Developed and maintained by Microsoft, TypeScript compiles to plain JavaScript and is widely used for large-scale web applications, Node.js services, and developer tooling. The TypeScript Compiler API and Language Service API enable programmatic compilation, type checking, code transformation, and IDE integrations.
finops:
- name: Typescript Finops
  service_category: API
  slug: typescript-finops
image: https://www.typescriptlang.org/favicon-32x32.png
json_schemas:
- name: TypeScript Compiler Options
  property_count: 19
  slug: typescript-compiler-options
- name: TypeScript Diagnostic
  property_count: 7
  slug: typescript-diagnostic
json_structures:
- name: Typescript Diagnostic Structure
  property_count: 6
  slug: typescript-diagnostic-structure
jsonld:
- class_count: 15
  name: Typescript Context
  property_count: 13
  slug: typescript-context
layout: provider
modified: '2026-05-19'
name: TypeScript
nav: Providers
network: true
overview: 'TypeScript publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Compiler, JavaScript, Language Service, Programming Language, and Static Typing.


  The TypeScript catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TypeScript''s developer surface includes documentation, engineering blog, release notes, and 16 more developer resources.'
plans:
- name: Typescript Plans Pricing
  plan_count: 3
  slug: typescript-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Typescript Rate Limits
  slug: typescript-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TypeScript API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: typescript-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.9
  delta: -6.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 15.5
    developer_ergonomics: 25.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 32.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/typescript/refs/heads/main/screenshots/typescript-2026-06-20T195902.png
security:
- kind: domain-security
  name: Typescript Domain Security
  slug: typescript-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: ts-maintain-reduce-repro
  slug: ts-maintain-reduce-repro
slug: typescript
tags:
- Compiler
- JavaScript
- Language Service
- Programming Language
- Static Typing
- Web Development
website: https://www.typescriptlang.org
---
