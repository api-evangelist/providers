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
  score: 3.2
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: The Notary Project specification defines the signature envelope format, trust store and trust policy for container image signing and verification. It supports multiple signature formats and integrates
  name: Notary Project Signing Specification
  slug: notary-spec
- description: Notation is the command-line tool that implements the Notary Project specifications for signing and verifying OCI artifacts stored in container registries. It supports signing with certificates stored
  name: Notation CLI
  slug: notation-cli
- description: notation-go is the official Go library for signing and verifying OCI artifacts using the Notary Project specifications. It provides the programmatic interface used by the Notation CLI and enables Go a
  name: notation-go Library
  slug: notation-go
- description: The Notation plugin extensibility specification defines the interface that third-party plugins must implement to integrate with Notation for key management, signing, and verification operations. Plugi
  name: Notation Plugin Extensibility
  slug: notation-plugin-framework
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notary-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://notaryproject.dev
- group: docs
  title: ''
  type: Documentation
  url: https://notaryproject.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://notaryproject.dev/docs/user-guides/installation/
- group: company
  title: ''
  type: Blog
  url: https://notaryproject.dev/blog/
- group: operate
  title: ''
  type: FAQ
  url: https://notaryproject.dev/docs/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/notaryproject
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/notaryproject/notation
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/notaryproject/notation/releases
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/notary-trust-policy-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/notary-plugin-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/notary-plugin-protocol-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/notary-signature-envelope-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/notary-context.jsonld
created: '2026-03-16'
description: The Notary Project is a CNCF incubating set of specifications and tools for signing and verifying container images and other OCI artifacts. It provides Notation, a CLI and library for signing artifacts stored in OCI-compliant registries. The project defines standards for signature formats, trust policies, and verification workflows to secure software supply chains.
finops:
- name: Notary Finops
  service_category: API
  slug: notary-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/notary.png
json_schemas:
- name: Notary Project Plugin Protocol
  property_count: 0
  slug: notary-plugin-protocol
- name: Notation Plugin Protocol
  property_count: 0
  slug: notary-plugin
- name: Notary Project JWS Signature Envelope
  property_count: 4
  slug: notary-signature-envelope
- name: Notary Project Trust Policy
  property_count: 2
  slug: notary-trust-policy
jsonld:
- class_count: 7
  name: Notary Context
  property_count: 32
  slug: notary-context
layout: provider
modified: '2026-04-28'
name: Notary Project
nav: Providers
network: true
overview: 'Notary Project publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, Container Security, Image Signing, Incubating, and OCI.


  The Notary Project catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Notary Project''s developer surface includes documentation, getting-started guide, engineering blog, FAQ, changelog, and 9 more developer resources.'
plans:
- name: Notary Plans Pricing
  plan_count: 3
  slug: notary-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Notary Rate Limits
  slug: notary-rate-limits
rules:
- name: Notary Project API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: notary-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.8
  delta: -4.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 33.9
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 46.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/notary/refs/heads/main/screenshots/notary-2026-06-20T190421.png
security:
- kind: domain-security
  name: Notary Domain Security
  slug: notary-domain-security
  summary_line: TLSv1.3 · HSTS
slug: notary
tags:
- Cloud Native
- Container Security
- Image Signing
- Incubating
- OCI
- Verification
website: https://notaryproject.dev
---
