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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Spaceapi Agentic Access
  operation_count: 1
  slug: spaceapi-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: SpaceAPI directory listing operations
  name: SpaceAPI Directory API
  slug: spaceapi-directory-api
artifact_total: 13
collections:
- collection_type: open
  name: SpaceAPI Collector
  slug: open-spaceapi-collector
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spaceapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spaceapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spaceapi.io
- group: docs
  title: ''
  type: Documentation
  url: https://spaceapi.io/how-to-use/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SpaceApi
- group: other
  title: ''
  type: Directory
  url: https://directory.spaceapi.io/
created: '2024-11-07'
description: SpaceAPI is an open standard for hackerspaces, makerspaces, fablabs, and similar community spaces to publish real-time information about their spaces in a machine-readable JSON format. It provides a central directory (collector) that aggregates endpoints from participating spaces around the world, enabling applications to discover and display space status, location, contact, and operational information.
examples:
- key_count: 4
  name: Spaceapi List Spaces Example
  slug: spaceapi-list-spaces-example
finops:
- name: Spaceapi Finops
  service_category: API
  slug: spaceapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spaceapi.png
json_schemas:
- name: SpaceAPI Directory Entry
  property_count: 1
  slug: spaceapi-directory-entry
json_structures:
- name: Spaceapi Directory Entry Structure
  property_count: 0
  slug: spaceapi-directory-entry-structure
jsonld:
- class_count: 8
  name: Spaceapi Context
  property_count: 7
  slug: spaceapi-context
layout: provider
modified: '2026-05-19'
name: SpaceAPI
nav: Providers
network: true
overview: 'SpaceAPI publishes 1 API on the [APIs.io](https://apis.io/) network: Directory API. Tagged areas include Co-Working, Event Spaces, Maker Spaces, Hackerspaces, and Community.


  The SpaceAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SpaceAPI''s developer surface includes documentation, GitHub presence, and 4 more developer resources.'
plans:
- name: Spaceapi Plans Pricing
  plan_count: 3
  slug: spaceapi-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Spaceapi Rate Limits
  slug: spaceapi-rate-limits
rules:
- name: SpaceAPI API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: spaceapi-jsonschema-spectral-rules
- name: SpaceAPI API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: spaceapi-rules
score:
  band: thin
  composite: 37.1
  delta: -8.4
  facets:
    commercial_clarity: 15.8
    contract_quality: 66.4
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
security:
- kind: domain-security
  name: Spaceapi Domain Security
  slug: spaceapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: spaceapi
tags:
- Co-Working
- Event Spaces
- Maker Spaces
- Hackerspaces
- Community
- Open Standard
website: https://spaceapi.io
---
