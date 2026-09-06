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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The LAPIS specification defines a token-minimal, LLM-native format for describing HTTP APIs. A LAPIS document is organized into up to seven indentation-based sections - [meta], [types], [ops], [webhoo
  name: LAPIS Specification
  slug: lapis-spec
artifact_total: 33
common:
- group: start
  title: LAPIS Online Converter
  type: Portal
  url: https://cr0hn.github.io/LAPIS/
- group: docs
  title: Specification (English)
  type: Documentation
  url: https://github.com/cr0hn/LAPIS/blob/main/spec.en.md
- group: docs
  title: Specification (Spanish)
  type: Documentation
  url: https://github.com/cr0hn/LAPIS/blob/main/spec.es.md
- group: start
  title: Getting Started
  type: GettingStarted
  url: https://github.com/cr0hn/LAPIS#getting-started
- group: build
  title: LAPIS Repository
  type: GitHubRepository
  url: https://github.com/cr0hn/LAPIS
- group: operate
  title: Changelog
  type: ChangeLog
  url: https://github.com/cr0hn/LAPIS/blob/main/CHANGELOG.md
- group: commercial
  title: License (CC BY 4.0)
  type: TermsOfService
  url: https://github.com/cr0hn/LAPIS/blob/main/LICENSE
- group: auth
  title: Code of Conduct
  type: Compliance
  url: https://github.com/cr0hn/LAPIS/blob/main/CODE_OF_CONDUCT.md
- group: auth
  title: Security Policy
  type: Security
  url: https://github.com/cr0hn/LAPIS/blob/main/SECURITY.md
- group: operate
  title: Contributing Guide
  type: Contact
  url: https://github.com/cr0hn/LAPIS/blob/main/CONTRIBUTING.md
- group: build
  title: lapis CLI (lapis-spec on PyPI)
  type: CLI
  url: https://pypi.org/project/lapis-spec/
- group: build
  title: lapis-spec Python Package
  type: SDKs
  url: https://pypi.org/project/lapis-spec/
- group: operate
  title: LAPIS Visual Studio Code Extension
  type: IDESupport
  url: https://github.com/cr0hn/LAPIS/tree/main/tools/ides/vscode
- group: start
  title: Browser-Based OpenAPI to LAPIS Converter
  type: Sandbox
  url: https://cr0hn.github.io/LAPIS/
- group: operate
  title: Issue Tracker
  type: Issues
  url: https://github.com/cr0hn/LAPIS/issues
- group: design
  title: LAPIS Normative Vocabulary
  type: Vocabulary
  url: vocabulary/lapis-vocabulary.yml
- group: docs
  title: LAPIS Document JSON Schema
  type: JSONSchema
  url: json-schema/lapis-document-schema.json
- group: design
  title: LAPIS Document JSON Structure
  type: JSONStructure
  url: json-structure/lapis-document-structure.json
- group: design
  title: LAPIS JSON-LD Context
  type: JSONLD
  url: json-ld/lapis-context.jsonld
- group: build
  title: Invoice Service LAPIS Example
  type: Examples
  url: examples/lapis-invoice-service-example.lapis
- group: build
  title: Meta Section Example
  type: Examples
  url: examples/lapis-meta-section-example.lapis
- group: build
  title: Types Section Example
  type: Examples
  url: examples/lapis-types-section-example.lapis
- group: build
  title: Operations Section Example
  type: Examples
  url: examples/lapis-ops-section-example.lapis
- group: build
  title: Webhooks Section Example
  type: Examples
  url: examples/lapis-webhooks-section-example.lapis
- group: build
  title: Errors Section Example
  type: Examples
  url: examples/lapis-errors-section-example.lapis
- group: build
  title: Limits Section Example
  type: Examples
  url: examples/lapis-limits-section-example.lapis
- group: build
  title: Flows Section Example
  type: Examples
  url: examples/lapis-flows-section-example.lapis
created: '2026-05-06'
description: LAPIS (Lightweight API Specification for Intelligent Systems) is a compact, LLM-native API description format authored by Daniel Garcia (cr0hn). It is designed as the format you convert your OpenAPI specifications to when the consumer is a Large Language Model rather than a code generator or human reader. By replacing JSON/YAML structural overhead with a function-signature syntax, indentation-based sections, and centralized definitions for errors, webhooks, rate limits, and workflows, a typical LAPIS document carries the same semantic information as its OpenAPI source while consuming roughly 70-80 percent fewer tokens. LAPIS is not a runtime format and does not replace MCP, function calling, or OpenAPI itself - it is an intermediate representation optimized for AI agents that need to reason about an API inside a constrained context window.
features:
- description: LAPIS uses operation headers shaped like function signatures (operation_name METHOD /path), input parameters prefixed with > and outputs prefixed with <, so an LLM reads each endpoint as a callable rather than as a deeply nested JSON object.
  name: Function-Signature Syntax for APIs
- description: A LAPIS document is composed of up to seven sections in a fixed order - [meta], [types], [ops], [webhooks], [errors], [limits], and [flows] - with [meta] and [ops] required and the remainder optional based on what the API actually exposes.
  name: Seven-Section Document Model
- description: Errors are declared once in [errors] using HTTP code plus a snake_case identifier, optionally bound to specific operations via @ops:name1,name2, eliminating the per-operation duplication of 400/401/404/429 responses that bloats OpenAPI documents.
  name: Centralized Error Definitions
- description: The [webhooks] section captures both the payload shape and the trigger condition (lines prefixed with !) that fires the event, giving an LLM the why of an event rather than only the what that OpenAPI delivers.
  name: First-Class Webhook Triggers
- description: The [limits] section expresses rate limits, quotas, body size caps, batch size caps, and tiered plan blocks as first-class declarative fields with scope annotations like @key, @global, @ip, @user, and @op:operation_name.
  name: Structured Rate Limits and Quotas
- description: The [flows] section describes how operations chain together using step1 -> step2 -> step3 notation, with branches (|), loops (*), waits (...(condition)), and inter-step data passing (op.field -> next_op(field)) so an agent learns canonical usage patterns alongside individual endpoints.
  name: Multi-Step Workflow Flows
- description: Field-level @since:X.Y annotations let an LLM determine whether a given field exists at the API version declared in [meta], and @deprecated optionally followed by a quoted note marks fields and operations that should not be used by new integrations.
  name: Field Versioning and Deprecation
- description: Operations can carry +paginated, +deprecated, +idempotent, and +stream modifiers appended after the path, signaling pagination, retry safety, streaming response semantics, and deprecation status without verbose extension blocks.
  name: Operation Modifiers
- description: 'Types used by only a single operation can be inlined directly in the parameter list using {field: type, field: type} or [{field: type}] notation, avoiding pollution of [types] with single-use schemas.'
  name: Inline Object Types
- description: For a representative mid-size API (11 operations, 8 types, 3 webhooks, 10 errors, limits, 4 flows), LAPIS measures roughly 1,500 tokens versus 6,500 for the equivalent OpenAPI YAML, a 0.23x ratio driven primarily by removing irrelevant metadata, repeated error definitions, and JSON/YAML key restatement.
  name: 70-80 Percent Token Reduction
- description: Section 14 of the spec defines field-by-field rules for converting OpenAPI 3.x into LAPIS, covering info, servers, securitySchemes, components.schemas, paths, webhooks, x-rateLimit and x-quota extensions, and links, making the conversion fully automatable.
  name: Deterministic OpenAPI Conversion
- description: The specification ships a simplified EBNF grammar covering all seven sections, type expressions, modifiers, annotations, comments, and primitive lexical tokens, providing a normative reference for tool authors building parsers, linters, and highlighters.
  name: Formal EBNF Grammar
- description: The LAPIS specification is published in parallel English (spec.en.md) and Spanish (spec.es.md) editions, with matching walk-through examples (spec-example.en.md and spec-example.es.md) that narrate a sample Invoice Service API in both languages.
  name: Bilingual Specification
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lapis.png
integrations:
- description: OpenAPI is the canonical source format for LAPIS. The lapis-spec Python tool ingests OpenAPI 3.0.x and 3.1.x in JSON or YAML, resolves $ref including circular references, flattens allOf/oneOf/anyOf, deduplicates inline versus named types, and emits a LAPIS document.
  name: OpenAPI 3.0 and 3.1
- description: The reference command-line converter is published to PyPI as lapis-spec and exposes a lapis console script. Installation is pip install lapis-spec or uv pip install lapis-spec, and the CLI accepts -i/--input, -o/--output, and --no-validate flags.
  name: PyPI (lapis-spec)
- description: The LAPIS Language extension (publisher lapis-spec, identifier lapis-lang) provides syntax highlighting for .lapis files, including section headers, scalar types, modifiers, IO markers, annotations, bracket matching, auto-closing pairs, and section folding.
  name: Visual Studio Code
- description: A static JavaScript single-page application at https://cr0hn.github.io/LAPIS/ runs the OpenAPI to LAPIS conversion entirely in the browser via converter.js, highlighter.js, and app.js, supporting drag-and-drop, paste, copy, and download of .lapis files.
  name: Web Browser Converter
- description: LAPIS is positioned alongside (not as a replacement for) MCP and function calling. A LAPIS document is the context-layer description an LLM reads to understand an API; MCP servers and function-calling schemas remain the runtime invocation layer for actually executing operations.
  name: MCP and Function Calling
- description: The specification text is licensed under CC BY 4.0, allowing adaptation, distribution, and commercial use provided attribution is given. The reference tooling (lapis-spec Python package) is MIT licensed, and the VS Code extension is CC BY 4.0.
  name: Creative Commons Attribution 4.0
- description: The browser-based converter is hosted on GitHub Pages from the cr0hn/LAPIS repository at https://cr0hn.github.io/LAPIS/, making it accessible without local installation or API keys.
  name: GitHub Pages
json_schemas:
- name: LapisDocument
  property_count: 8
  slug: lapis-document
json_structures:
- name: Lapis Document Structure
  property_count: 8
  slug: lapis-document-structure
jsonld:
- class_count: 22
  name: Lapis Context
  property_count: 62
  slug: lapis-context
layout: provider
modified: '2026-05-06'
name: LAPIS
nav: Providers
network: true
overview: 'LAPIS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Specification, LLM, AI Agents, OpenAPI, and Token Optimization.


  The LAPIS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LAPIS''s developer surface includes developer portal, documentation, getting-started guide, changelog, CLI, sandbox, code examples, and 20 more developer resources.'
random_paper: 12
rules:
- effective_rule_count: 6
  extends: []
  name: LAPIS API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: lapis-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 25.0
    contract_quality: 21.3
    developer_ergonomics: 59.5
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 31.6
  previous_composite: 33.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lapis/refs/heads/main/screenshots/lapis-2026-06-20T184316.png
slug: lapis
tags:
- Specification
- LLM
- AI Agents
- OpenAPI
- Token Optimization
- Standards
use_cases:
- description: Engineering teams whose AI features pass an OpenAPI specification into prompts on every call convert the spec to LAPIS once and pass the smaller LAPIS document instead, reducing per-call token spend by roughly 70-80 percent on the API description portion of the context window.
  name: Reducing LLM Context Cost
- description: AI coding assistants that need to reason about a third-party API (generating client code, debugging a failing call, suggesting an endpoint) consume LAPIS as the API context layer, freeing more of the context window for the actual user prompt and conversation history.
  name: Powering AI Coding Assistants
- description: AI agents executing multi-step API workflows (create customer, create invoice, send invoice, await payment webhook) load a LAPIS document with a populated [flows] section so the planner has canonical workflow templates rather than having to infer chaining from individual operation descriptions.
  name: Multi-Step API Agent Planning
- description: Integration platforms that build webhook receivers use the [webhooks] section's trigger conditions (!) and headers (@header:X-Event-ID) to generate signature verification and event dispatch logic that knows when each event should fire and what identifying headers to expect.
  name: Webhook-Aware Integrations
- description: Client SDKs and gateway integrations consume the [limits] section to configure backoff, request-throttling, and quota tracking per plan tier (free, pro, enterprise) and per scope (@key, @user, @op:name) without reading provider documentation in prose.
  name: Plan-Aware Rate Limit Enforcement
- description: Tooling vendors and platform teams enforce LAPIS-conformant documents by validating against the EBNF grammar in spec section 16, catching missing required sections, invalid type expressions, and malformed annotations before the document is shipped to downstream consumers.
  name: Specification Linting and Validation
- description: Because LAPIS strips presentation overhead and centralizes errors, limits, and flows, two LAPIS documents from different providers can be diffed and compared more directly than two OpenAPI specifications.
  name: Cross-Provider API Comparison
- description: Platform teams generate LAPIS from internal OpenAPI sources to provide on-call engineers and product stakeholders a quickly readable, function-signature view of the company's services alongside the long-form OpenAPI documentation.
  name: Onboarding Documentation for Internal APIs
website: https://cr0hn.github.io/LAPIS/
---
