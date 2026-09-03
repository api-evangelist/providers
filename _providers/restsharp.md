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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: RestSharp is a simple REST and HTTP API client library for .NET, wrapping HttpClient with a fluent API for making HTTP requests with automatic serialization and deserialization of request and response
  name: RestSharp
  slug: restsharp
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restsharp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://restsharp.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://restsharp.dev/docs/intro/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/restsharp
- group: build
  title: ''
  type: NuGet Package
  url: https://www.nuget.org/packages/RestSharp
- group: commercial
  title: ''
  type: License
  url: https://github.com/restsharp/RestSharp/blob/dev/LICENSE.txt
- group: operate
  title: ''
  type: Support
  url: https://github.com/restsharp/RestSharp/issues
created: '2026-03-27'
description: RestSharp is a simple REST and HTTP API client library for .NET that wraps HttpClient with a fluent API for making HTTP requests with automatic serialization and deserialization of request and response bodies. Supports JSON, XML, and CSV formats, OAuth1/OAuth2 authentication, async operations, and multi-part form uploads. Available on NuGet as RestSharp (9,800+ GitHub stars, Apache-2.0 license, .NET Foundation project).
examples:
- key_count: 6
  name: Restsharp Bearer Auth Example
  slug: restsharp-bearer-auth-example
- key_count: 6
  name: Restsharp Get Request Example
  slug: restsharp-get-request-example
- key_count: 6
  name: Restsharp Post Json Example
  slug: restsharp-post-json-example
finops:
- name: Restsharp Finops
  service_category: API
  slug: restsharp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restsharp.png
json_schemas:
- name: RestClientOptions
  property_count: 12
  slug: restsharp-rest-client-options
- name: RestRequest
  property_count: 6
  slug: restsharp-rest-request
json_structures:
- name: Restsharp Rest Client Options Structure
  property_count: 0
  slug: restsharp-rest-client-options-structure
- name: Restsharp Rest Request Structure
  property_count: 0
  slug: restsharp-rest-request-structure
jsonld:
- class_count: 25
  name: Restsharp Context
  property_count: 4
  slug: restsharp-context
layout: provider
modified: '2026-05-02'
name: RestSharp
nav: Providers
network: true
overview: 'RestSharp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, Apache License, C#, HTTP Client, and NuGet.


  The RestSharp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RestSharp''s developer surface includes documentation, support, and 5 more developer resources.'
plans:
- name: Restsharp Plans Pricing
  plan_count: 3
  slug: restsharp-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Restsharp Rate Limits
  slug: restsharp-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RestSharp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restsharp-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 21.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/restsharp/refs/heads/main/screenshots/restsharp-2026-06-20T193032.png
security:
- kind: domain-security
  name: Restsharp Domain Security
  slug: restsharp-domain-security
  summary_line: TLSv1.3
slug: restsharp
tags:
- .NET
- Apache License
- C#
- HTTP Client
- NuGet
- Open-Source
- SDK
website: https://restsharp.dev/
---
