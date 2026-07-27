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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 45.2
  scored_at: '2026-07-27'
api_count: 11
apis:
- description: The Attributes API from Stadia Maps — 1 operation(s) for attributes.
  name: Stadia Maps Attributes API
  slug: stadia-maps-attributes-api
- description: The Autocomplete API from Stadia Maps — 1 operation(s) for autocomplete.
  name: Stadia Maps Autocomplete API
  slug: stadia-maps-autocomplete-api
- description: The Geospatial API from Stadia Maps — 1 operation(s) for geospatial.
  name: Stadia Maps Geospatial API
  slug: stadia-maps-geospatial-api
- description: The Lookups API from Stadia Maps — 1 operation(s) for lookups.
  name: Stadia Maps Lookups API
  slug: stadia-maps-lookups-api
- description: The Match API from Stadia Maps — 1 operation(s) for match.
  name: Stadia Maps Match API
  slug: stadia-maps-match-api
- description: The Place API from Stadia Maps — 1 operation(s) for place.
  name: Stadia Maps Place API
  slug: stadia-maps-place-api
- description: The Reverse API from Stadia Maps — 1 operation(s) for reverse.
  name: Stadia Maps Reverse API
  slug: stadia-maps-reverse-api
- description: The Roads API from Stadia Maps — 1 operation(s) for roads.
  name: Stadia Maps Roads API
  slug: stadia-maps-roads-api
- description: The Routes API from Stadia Maps — 1 operation(s) for routes.
  name: Stadia Maps Routes API
  slug: stadia-maps-routes-api
- description: The Routing API from Stadia Maps — 3 operation(s) for routing.
  name: Stadia Maps Routing API
  slug: stadia-maps-routing-api
- description: The Search API from Stadia Maps — 3 operation(s) for search.
  name: Stadia Maps Search API
  slug: stadia-maps-search-api
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stadia-maps-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stadia-maps
- group: start
  title: ''
  type: Portal
  url: https://stadiamaps.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stadiamaps.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stadiamaps.com/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://stadiamaps.com/pricing/
- group: operate
  title: ''
  type: Contact
  url: https://stadiamaps.com/contact/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.stadiamaps.com/authentication/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stadiamaps
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@stadiamaps/api
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/stadiamaps-api/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/stadiamaps/stadiamaps-mcp-server-ts
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.stadiamaps.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://stadiamaps.com/blog/rss.xml
created: '2024-12-16'
description: Stadia Maps is a cutting-edge mapping platform providing high-quality, detailed maps and location APIs for developers. The platform offers routing and navigation, geocoding and search, elevation data, time zone lookups, isochrone analysis, and account management. Stadia Maps delivers GDPR-compliant EU endpoints, rich map styling options, and official SDKs for TypeScript, Python, Swift, Kotlin, and PHP. Trusted by developers building web, mobile, and data visualization applications worldwide.
examples:
- key_count: 2
  name: Stadia Maps Autocomplete Example
  slug: stadia-maps-autocomplete-example
- key_count: 2
  name: Stadia Maps Route Example
  slug: stadia-maps-route-example
- key_count: 2
  name: Stadia Maps Tz Lookup Example
  slug: stadia-maps-tz-lookup-example
finops:
- name: Stadia Maps Finops
  service_category: API
  slug: stadia-maps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stadia-maps.png
json_schemas:
- name: Stadia Maps Location
  property_count: 4
  slug: stadia-maps-location
- name: Stadia Maps Route
  property_count: 1
  slug: stadia-maps-route
json_structures:
- name: Stadia Maps Location Structure
  property_count: 3
  slug: stadia-maps-location-structure
jsonld:
- class_count: 34
  name: Stadia Maps Context
  property_count: 3
  slug: stadia-maps-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Stadia Maps
nav: Providers
network: true
overview: 'Stadia Maps publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Autocomplete API, Geospatial API, and 8 more. Tagged areas include Mapping, Maps, Geocoding, Routing, and Navigation.


  The Stadia Maps catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stadia Maps'' developer surface includes developer portal, documentation, API reference, pricing, authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Stadia Maps Plans Pricing
  plan_count: 3
  slug: stadia-maps-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Stadia Maps Rate Limits
  slug: stadia-maps-rate-limits
rules:
- name: Stadia Maps API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: stadia-maps-jsonschema-spectral-rules
- name: Stadia Maps API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: stadia-maps-rules
score:
  band: strong
  composite: 62.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.8
    developer_ergonomics: 52.2
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 62.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stadia-maps/refs/heads/main/screenshots/stadia-maps-2026-06-20T194456.png
security:
- kind: domain-security
  name: Stadia Maps Domain Security
  slug: stadia-maps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stadia-maps
tags:
- Mapping
- Maps
- Geocoding
- Routing
- Navigation
- Geospatial
- Location
website: https://stadiamaps.com/
---
