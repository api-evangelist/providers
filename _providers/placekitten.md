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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Placekitten Agentic Access
  operation_count: 2
  slug: placekitten-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Placeholder image retrieval
  name: PlaceKitten Image API
  slug: placekitten-image-api
artifact_total: 13
collections:
- collection_type: open
  name: PlaceKitten
  slug: open-placekitten
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/placekitten-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/placekitten-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://placekitten.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: other
  title: ''
  type: Archive
  url: https://web.archive.org/web/*/placekitten.com
created: '2026-05-28'
description: 'Placeholder kitten image service. Free, no-auth REST contract: /{width}/{height} for color, /g/{width}/{height} for grayscale. Created by Mark James, inspired by placehold.it.'
examples:
- key_count: 4
  name: Placekitten Getgrayscalekittenimage Example
  slug: placekitten-getGrayscaleKittenImage-example
- key_count: 4
  name: Placekitten Getkittenimage Example
  slug: placekitten-getKittenImage-example
- key_count: 3
  name: Placekitten Html Embed Example
  slug: placekitten-html-embed-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/placekitten.png
json_schemas:
- name: PlaceKittenImageRequest
  property_count: 3
  slug: placekitten-image-request
- name: PlaceKittenImageResponse
  property_count: 5
  slug: placekitten-image-response
json_structures:
- name: Placekitten Image Request Structure
  property_count: 0
  slug: placekitten-image-request-structure
jsonld:
- class_count: 2
  name: Placekitten Context
  property_count: 6
  slug: placekitten-context
layout: provider
modified: '2026-05-30'
name: PlaceKitten
nav: Providers
network: true
overview: 'PlaceKitten publishes 1 API on the [APIs.io](https://apis.io/) network: Image API. Tagged areas include Animals, Public APIs, Placeholder, Images, and Deprecated.


  The PlaceKitten catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
random_paper: 32
rules:
- name: PlaceKitten API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: placekitten-jsonschema-spectral-rules
- name: PlaceKitten API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: placekitten-rules
score:
  band: thin
  composite: 31.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 69.8
    developer_ergonomics: 0.0
    discoverability: 66.7
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Placekitten Domain Security
  slug: placekitten-domain-security
  summary_line: TLSv1.3
slug: placekitten
tags:
- Animals
- Public APIs
- Placeholder
- Images
- Deprecated
website: https://placekitten.com/
---
