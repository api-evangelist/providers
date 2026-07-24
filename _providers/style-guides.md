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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 11
apis:
- description: Microsoft's organization-wide REST API design guidelines, originally published in 2016 and now maintained as separate Azure and Microsoft Graph guideline documents under the umbrella Guidelines.md. Li
  name: Microsoft REST API Guidelines
  slug: microsoft
- description: Google's design review system, modeled on Python PEPs and Rust RFCs. AIPs are numbered, individually reviewable design documents covering resource-oriented design, standard methods, errors, pagination
  name: Google API Improvement Proposals (AIPs)
  slug: google-aip
- description: 'The canonical open community style guide. Maintained by Zalando''s API Guild and widely cited as the reference implementation for an API-First, OpenAPI-based REST and event-driven API program. Roughly '
  name: Zalando RESTful API and Event Guidelines
  slug: zalando
- description: PayPal's API style guide covering service design principles, HTTP methods, hypermedia, naming, URI structure, JSON schema and types, error handling, versioning, and deprecation. The original repositor
  name: PayPal API Design Guidelines
  slug: paypal
- description: adidas group's API guidelines covering general principles, REST conventions, and asynchronous (Kafka / AsyncAPI) event design. Ships with a Spectral ruleset that validates both OpenAPI and AsyncAPI sp
  name: adidas API Guidelines
  slug: adidas
- description: Guidelines for Designing REST APIs at Cisco, developed across Cisco DevNet, Collaboration, and the Application Platform Group. Emphasizes "API-only" communication, aesthetic and behavioral consistency
  name: Cisco REST API Design Guide
  slug: cisco
- description: Atlassian's REST API design guidelines, applied across Jira, Confluence, Crowd, and plugin REST modules. Defines URI conventions (singular resources, versioned paths, expand/start-index/max-results qu
  name: Atlassian REST API Design Guidelines
  slug: atlassian
- description: Heroku's design conventions for the Platform API, documented in the Platform API Reference and the API Compatibility Policy. Notable for versioned media types (application/vnd.heroku+json; version=3),
  name: Heroku Platform API Design Conventions
  slug: heroku
- description: GitLab's developer-facing API style guide for the REST API (v4) and GraphQL API. Mandates Grape DSL parameter validation, Entity-based response payloads, Title Case summary verbs aligned to HTTP metho
  name: GitLab API Style Guide
  slug: gitlab
- description: The Kubernetes API conventions document, maintained by SIG Architecture. Defines the "kind / apiVersion" object envelope, spec/status separation, resourceVersion-based optimistic concurrency, list sem
  name: Kubernetes API Conventions
  slug: kubernetes
- description: The IETF httpapi Working Group is producing the cross-vendor vocabulary that style guides increasingly cite normatively. Includes RFC 9457 Problem Details for HTTP APIs, RFC 9652 Link-Template, RFC 97
  name: IETF HTTPAPI Working Group Drafts and RFCs
  slug: ietf-httpapi
artifact_total: 34
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/style-guides-domain-security.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/style-guides/main/json-schema/style-guide-rule-schema.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/style-guides/main/json-ld/style-guides-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/style-guides/main/vocabulary/style-guides-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://github.com/api-evangelist/style-guides/tree/main/examples
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apievangelist.com/
- group: other
  title: ''
  type: Network
  url: https://developer.apievangelist.com/network/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: other
  title: ''
  type: RelatedTopic
  url: https://github.com/api-evangelist/design-standards
- group: other
  title: ''
  type: RelatedTopic
  url: https://github.com/api-evangelist/rules
- group: other
  title: ''
  type: RelatedTopic
  url: https://github.com/api-evangelist/policies
created: '2026-05-22'
description: A landscape index of public API style guides published by leading technology companies and standards bodies. API style guides codify conventions for resource modeling, URI design, HTTP method use, status codes, error formats, pagination, versioning, deprecation, idempotency, hypermedia, and security so that APIs across an organization (or an industry) behave consistently. This topic repo catalogs the canonical industry style guides, compares the pillars each one chooses to mandate, and provides a shared vocabulary and JSON Schema for describing individual style guide rules.
examples:
- key_count: 13
  name: Adidas Spectral
  slug: adidas-spectral
- key_count: 14
  name: Aip 131 Get
  slug: aip-131-get
- key_count: 13
  name: Aip 158 Pagination
  slug: aip-158-pagination
- key_count: 13
  name: Aip 193 Errors
  slug: aip-193-errors
- key_count: 13
  name: Atlassian Uri Conventions
  slug: atlassian-uri-conventions
- key_count: 11
  name: Cisco Api Only
  slug: cisco-api-only
- key_count: 13
  name: Gitlab Summary Verbs
  slug: gitlab-summary-verbs
- key_count: 14
  name: Heroku Rate Limiting
  slug: heroku-rate-limiting
- key_count: 14
  name: Heroku Stability Levels
  slug: heroku-stability-levels
- key_count: 12
  name: Kubernetes Spec Status
  slug: kubernetes-spec-status
- key_count: 13
  name: Ms Azure Idempotency
  slug: ms-azure-idempotency
- key_count: 13
  name: Ms Azure Versioning
  slug: ms-azure-versioning
- key_count: 13
  name: Paypal Hateoas
  slug: paypal-hateoas
- key_count: 14
  name: Paypal Idempotency
  slug: paypal-idempotency
- key_count: 15
  name: Rfc 9457 Problem Details
  slug: rfc-9457-problem-details
- key_count: 14
  name: Rfc 9745 Deprecation
  slug: rfc-9745-deprecation
- key_count: 14
  name: Zalando 100 Api First
  slug: zalando-100-api-first
- key_count: 14
  name: Zalando 101 Openapi
  slug: zalando-101-openapi
graphqls:
- description: GitLab's developer-facing API style guide for the REST API (v4) and GraphQL API. Mandates Grape DSL parameter validation, Entity-based response payloads, Title Case summary verbs aligned to HTTP metho
  name: API Style Guides GraphQL API
  slug: style-guides-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/api-evangelist-logos/api-evangelist-logo-butterfly.png
json_schemas:
- name: API Style Guide Rule
  property_count: 15
  slug: style-guide-rule
jsonld:
- class_count: 8
  name: Style Guides Context
  property_count: 12
  slug: style-guides-context
layout: provider
modified: '2026-05-22'
name: API Style Guides
nav: Providers
network: true
overview: 'API Style Guides publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Style Guides, API Design, API Governance, REST, and OpenAPI.


  The API Style Guides catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  API Style Guides'' developer surface includes code examples and 10 more developer resources.'
random_paper: 23
rules:
- name: API Style Guides API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: style-guides-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.1
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 30.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/style-guides/refs/heads/main/screenshots/style-guides-2026-06-20T194625.png
security:
- kind: domain-security
  name: Style Guides Domain Security
  slug: style-guides-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: style-guides
tags:
- API Style Guides
- API Design
- API Governance
- REST
- OpenAPI
- Conventions
- Standards
- Documentation
website: https://developer.apievangelist.com/
---
