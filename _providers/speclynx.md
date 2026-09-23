---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-23'
api_count: 6
apis:
- description: Stop wrestling with OpenAPI specs. SpecLynx OpenAPI Toolkit delivers the most effective way to author and manage your API specs, bringing unprecedented ease, pinpoint accuracy, and unmatched power dir
  name: SpecLynx
  slug: speclynx
- description: A VS Code extension providing semantic editing, real-time validation, linting, and live preview for OpenAPI, AsyncAPI, and Arazzo specifications. Features context-aware autocompletion, Go to Definitio
  name: SpecLynx OpenAPI Toolkit
  slug: openapi-toolkit
- description: 'A browser-based OpenAPI editor with real-time validation, smart autocompletion, and live preview. No installation required — runs entirely client-side with all processing in-browser. Supports OpenAPI '
  name: SpecLynx Editor
  slug: editor
- description: A command-line interface for overlay operations, dereferencing, bundling, format conversion (JSON/YAML), and validation of OpenAPI, AsyncAPI, Arazzo, and JSON Schema documents.
  name: SpecLynx CLI
  slug: cli
- description: An LSP-compatible npm library (@speclynx/apidom-ls) providing 13 intelligent editing capabilities for API description languages, including validation, completion, hover documentation, Go to Definition
  name: SpecLynx Language Service
  slug: language-service
- description: A unified semantic parsing engine that underpins all SpecLynx products. ApiDOM parses OpenAPI, AsyncAPI, Arazzo, and JSON Schema specifications into a semantic data model with lossless preservation of
  name: SpecLynx ApiDOM
  slug: apidom
artifact_total: 30
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/speclynx
- group: commercial
  title: ''
  type: License
  url: https://github.com/speclynx/vscode-openapi-toolkit/blob/main/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/speclynx/refs/heads/main/security/speclynx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/speclynx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://speclynx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://speclynx.com/openapi-toolkit/
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.visualstudio.com/items?itemName=SpecLynx.vscode-openapi-toolkit
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/speclynx/vscode-openapi-toolkit
- group: other
  title: ''
  type: OpenVSX
  url: https://open-vsx.org/extension/SpecLynx/vscode-openapi-toolkit
- group: operate
  title: ''
  type: Contact
  url: mailto:info@speclynx.com
- group: agent
  title: ''
  type: LlmsText
  url: https://speclynx.com/llms.txt
created: '2026-01-02'
description: SpecLynx provides enterprise-ready API tooling for authors and maintainers of OpenAPI, AsyncAPI, and Arazzo specifications. Built by veterans with 15+ years of Swagger and OpenAPI development experience, SpecLynx products prioritize security (specs never leave your machine), accuracy, and developer productivity. Core products include a VS Code extension, browser-based editor, CLI, language service library, and the ApiDOM semantic parsing engine. Every SpecLynx product is open source under the Apache-2.0 license; there are no paid plans.
examples:
- key_count: 5
  name: Speclynx Validation Result Example
  slug: speclynx-validation-result-example
features:
- name: Semantic Editing
- name: Context-Aware Autocompletion
- name: Real-Time Validation
- name: Spectral Integration
- name: Semantic Validation
- name: Live Preview
- name: Scalar Renderer
- name: SwaggerUI Renderer
- name: Go to Definition
- name: Find References
- name: JSON/YAML Conversion
- name: Formatting
- name: Dereferencing
- name: Overlay Support
- name: No Telemetry
- name: Offline-First
- name: Multi-Spec Support
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/speclynx.png
json_schemas:
- name: SpecLynx Completion Item
  property_count: 9
  slug: speclynx-completion-item
- name: SpecLynx Validation Result
  property_count: 7
  slug: speclynx-validation-result
json_structures:
- name: Speclynx Product Structure
  property_count: 0
  slug: speclynx-product-structure
jsonld:
- class_count: 5
  name: Speclynx Context
  property_count: 11
  slug: speclynx-context
layout: provider
modified: '2026-05-02'
name: SpecLynx
nav: Providers
network: true
overview: 'SpecLynx publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, AsyncAPI, Developer Tools, JSON-Schema, and OpenAPI.


  The SpecLynx catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SpecLynx''s developer surface includes documentation and 9 more developer resources.'
random_paper: 6
rules:
- effective_rule_count: 5
  extends: []
  name: SpecLynx API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: speclynx-jsonschema-spectral-rules
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.3
    catalog_earned_first_party: 0.0
    catalog_gap: 65.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 14.7
    developer_ergonomics: 19.0
    discoverability: 72.2
    operational_transparency: 2.6
  previous_composite: 16.2
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/speclynx/refs/heads/main/screenshots/speclynx-2026-06-20T194256.png
security:
- kind: domain-security
  name: Speclynx Domain Security
  slug: speclynx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: speclynx
tags:
- API Design
- AsyncAPI
- Developer Tools
- JSON-Schema
- OpenAPI
- Toolkit
- VS Code
website: https://speclynx.com/
---
