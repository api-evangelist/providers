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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/http-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/httpwg
- group: company
  title: ''
  type: Website
  url: https://developer.mozilla.org/en-US/docs/Web/HTTP
- group: docs
  title: ''
  type: Reference
  url: https://httpwg.org/specs/
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/http-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/http-request.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/http-response.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/http-problem-details.json
- group: design
  title: ''
  type: Rules
  url: rules/http-rules.yml
created: '2025'
description: HTTP (Hypertext Transfer Protocol) is the foundation-level protocol for data communication on the World Wide Web, defining how messages are formatted and transmitted between clients and servers. It operates as a request-response protocol enabling browsers, APIs, and other clients to interact with web servers using standard methods like GET, POST, PUT, and DELETE.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/http.png
json_schemas:
- name: HTTP Problem Details
  property_count: 5
  slug: http-problem-details
- name: HTTP Request Message
  property_count: 5
  slug: http-request
- name: HTTP Response Message
  property_count: 5
  slug: http-response
jsonld:
- class_count: 15
  name: Http Context
  property_count: 20
  slug: http-context
layout: provider
modified: '2026-04-28'
name: HTTP
nav: Providers
network: true
overview: 'HTTP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Networking, Protocol, Standards, and Web.


  The HTTP catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
random_paper: 100
rules:
- name: HTTP API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: http-jsonschema-spectral-rules
- name: HTTP API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: http-rules
score:
  band: emerging
  composite: 17.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 17.7
    developer_ergonomics: 6.5
    discoverability: 40.7
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 17.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/http/refs/heads/main/screenshots/http-2026-06-20T182903.png
security:
- kind: domain-security
  name: Http Domain Security
  slug: http-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: http
tags:
- Networking
- Protocol
- Standards
- Web
website: https://developer.mozilla.org/en-US/docs/Web/HTTP
---
