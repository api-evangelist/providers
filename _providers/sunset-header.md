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
api_count: 2
apis:
- description: The Sunset HTTP header field (RFC 8594) communicates the deprecation timeline of API endpoints to consumers. The header value is an HTTP-date timestamp indicating when a URI is expected to become unre
  name: Sunset Header (RFC 8594)
  slug: sunset-header
- description: RFC 9745 defines the Deprecation HTTP response header field, which signals to clients that a resource has been or will be deprecated. It complements the Sunset header by marking the start of the depre
  name: Deprecation HTTP Header Field (RFC 9745)
  slug: deprecation-header
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunset-header-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datatracker.ietf.org/doc/html/rfc8594
- group: docs
  title: ''
  type: IETF Specification
  url: https://www.rfc-editor.org/rfc/rfc8594
created: '2026-03-29'
description: The Sunset HTTP header field (RFC 8594) is an informational IETF specification that allows servers to communicate to clients that a URI is likely to become unresponsive at a specified future point in time. Published in May 2019, it provides a standardized mechanism for API deprecation signaling, enabling clients to plan migrations before service retirement. The header value is an HTTP-date timestamp following RFC 7231 syntax. A complementary sunset link relation type allows resources to reference documentation covering the sunset policy, migration guidance, and alternatives. RFC 9745 (Deprecation HTTP Header Field) extends this pattern by providing a two-phase deprecation + sunset lifecycle where Deprecation marks the start of deprecation and Sunset marks the end-of-life. These two headers are widely adopted in REST API governance practices and API lifecycle management tooling.
examples:
- key_count: 6
  name: Sunset Header Response Example
  slug: sunset-header-response-example
finops:
- name: Sunset Header Finops
  service_category: API
  slug: sunset-header-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sunset-header.png
json_schemas:
- name: Sunset Header
  property_count: 9
  slug: sunset-header
jsonld:
- class_count: 0
  name: Sunset Header Context
  property_count: 15
  slug: sunset-header-context
layout: provider
modified: '2026-05-02'
name: Sunset Header
nav: Providers
network: true
overview: 'Sunset Header publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Deprecation, HTTP Headers, RFC 8594, RFC 9745, and API Lifecycle.


  The Sunset Header catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Sunset Header Plans Pricing
  plan_count: 3
  slug: sunset-header-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Sunset Header Rate Limits
  slug: sunset-header-rate-limits
rules:
- name: Sunset Header API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sunset-header-jsonschema-spectral-rules
score:
  band: thin
  composite: 28.2
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 32.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sunset-header/refs/heads/main/screenshots/sunset-header-2026-06-20T194702.png
security:
- kind: domain-security
  name: Sunset Header Domain Security
  slug: sunset-header-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sunset-header
tags:
- API Deprecation
- HTTP Headers
- RFC 8594
- RFC 9745
- API Lifecycle
- REST APIs
- Standards
website: https://datatracker.ietf.org/doc/html/rfc8594
---
