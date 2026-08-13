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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 7
apis:
- description: The TUF specification defines the structure of update repositories including the root, targets, snapshot, and timestamp metadata files. Each metadata file has a defined schema with signatures, expirat
  name: TUF Repository Specification
  slug: tuf-spec
- description: The official Python reference implementation of The Update Framework (TUF) specification. Provides a metadata API for reading and writing TUF metadata files, an ngclient API implementing the TUF clien
  name: TUF Python Reference Implementation
  slug: python-tuf
- description: A Go implementation of The Update Framework (TUF), heavily influenced by python-tuf's design. Provides metadata, TrustedMetadata, and Updater packages implementing the TUF client workflow and specific
  name: TUF Go Implementation
  slug: go-tuf
- description: A Rust implementation of The Update Framework (TUF) specification providing a strongly-typed API for working with TUF metadata, verifying signatures, and implementing the TUF client update workflow.
  name: TUF Rust Implementation
  slug: rust-tuf
- description: A JavaScript/TypeScript implementation of The Update Framework (TUF) for use in Node.js environments and browser-based update systems. Enables TUF-compliant software update verification in the JavaScr
  name: TUF JavaScript Implementation
  slug: tuf-js
- description: 'A TUF repository management and signing tool designed for use in CI/CD pipelines. Enables teams to maintain a TUF repository using GitHub Actions and other CI systems for automated, policy-driven key '
  name: TUF on CI
  slug: tuf-on-ci
- description: The official TUF client conformance test suite for verifying that TUF client implementations correctly implement the TUF specification, including proper handling of all attack vectors and edge cases.
  name: TUF Conformance Test Suite
  slug: tuf-conformance
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tuf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://theupdateframework.io/
- group: docs
  title: ''
  type: Documentation
  url: https://theupdateframework.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://theupdateframework.io/docs/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/theupdateframework
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/theupdateframework/python-tuf
- group: docs
  title: ''
  type: Specification
  url: https://theupdateframework.github.io/specification/latest/
- group: company
  title: ''
  type: Blog
  url: https://theupdateframework.io/resources/news/
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/the-update-framework-tuf/
- group: operate
  title: ''
  type: Community
  url: https://github.com/theupdateframework/community
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tuf-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tuf-root-metadata-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tuf-targets-metadata-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tuf-snapshot-metadata-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tuf-timestamp-metadata-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tuf-vocabulary.yml
created: '2026-03-16'
description: TUF (The Update Framework) is a CNCF graduated framework for securing software update systems. It provides a specification for how software repositories should be structured and how clients should verify updates to protect against key compromise, rollback attacks, and mix-and-match attacks. TUF is used by many package managers and update systems including PyPI, Sigstore, and various Linux distributions. The framework defines a four-role metadata structure (root, targets, snapshot, timestamp) with threshold signing and delegation capabilities for scalable trust management.
examples:
- key_count: 4
  name: Tuf Python Client Usage Example
  slug: tuf-python-client-usage-example
- key_count: 3
  name: Tuf Root Metadata Example
  slug: tuf-root-metadata-example
- key_count: 3
  name: Tuf Targets Metadata Example
  slug: tuf-targets-metadata-example
finops:
- name: Tuf Finops
  service_category: API
  slug: tuf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tuf.png
json_schemas:
- name: TUF Root Metadata
  property_count: 2
  slug: tuf-root-metadata
- name: TUF Snapshot Metadata
  property_count: 2
  slug: tuf-snapshot-metadata
- name: TUF Targets Metadata
  property_count: 2
  slug: tuf-targets-metadata
- name: TUF Timestamp Metadata
  property_count: 2
  slug: tuf-timestamp-metadata
json_structures:
- name: Tuf Root Metadata Structure
  property_count: 0
  slug: tuf-root-metadata-structure
- name: Tuf Targets Metadata Structure
  property_count: 0
  slug: tuf-targets-metadata-structure
jsonld:
- class_count: 0
  name: Tuf Context
  property_count: 12
  slug: tuf-context
layout: provider
modified: '2026-05-03'
name: The Update Framework (TUF)
nav: Providers
network: true
overview: 'The Update Framework (TUF) publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CNCF, Cloud Native, Graduated, Security, and Software Supply Chain.


  The The Update Framework (TUF) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Update Framework (TUF)''s developer surface includes documentation, getting-started guide, engineering blog, and 13 more developer resources.'
plans:
- name: Tuf Plans Pricing
  plan_count: 3
  slug: tuf-plans-pricing
random_paper: 95
rate_limits:
- limit_count: 5
  name: Tuf Rate Limits
  slug: tuf-rate-limits
rules:
- name: The Update Framework (TUF) API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: tuf-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 29.0
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 32.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tuf/refs/heads/main/screenshots/tuf-2026-06-20T195821.png
security:
- kind: domain-security
  name: Tuf Domain Security
  slug: tuf-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tuf
tags:
- CNCF
- Cloud Native
- Graduated
- Security
- Software Supply Chain
- Software Updates
- Verification
website: https://theupdateframework.io/
---
