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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Tinyproxy is a lightweight HTTP/HTTPS proxy daemon for POSIX operating systems with minimal system resource requirements. Provides forward proxying, HTTPS CONNECT tunneling, domain filtering, access c
  name: Tinyproxy
  slug: tinyproxy
artifact_total: 9
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tinyproxy/tinyproxy/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/tinyproxy/tinyproxy/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/tinyproxy/tinyproxy/blob/master/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/tinyproxy/tinyproxy/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://tinyproxy.github.io/
- group: docs
  title: ''
  type: Documentation
  url: https://tinyproxy.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tinyproxy
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tinyproxy/tinyproxy
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/json-schema/tinyproxy-config-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/json-structure/tinyproxy-config-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/json-ld/tinyproxy-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/vocabulary/tinyproxy-vocabulary.yml
created: '2026-03-27'
description: Tinyproxy is a lightweight, open-source HTTP/HTTPS proxy daemon designed for POSIX operating systems. It is ideal for use cases in embedded deployments, small networks, and environments where a full-featured HTTP proxy is required with minimal system resource usage. Configuration is file-based with an internal statistics monitoring page.
examples:
- key_count: 3
  name: Tinyproxy Config Example
  slug: tinyproxy-config-example
finops:
- name: Tinyproxy Finops
  service_category: API
  slug: tinyproxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tinyproxy.png
json_schemas:
- name: Tinyproxy Configuration
  property_count: 29
  slug: tinyproxy-config
json_structures:
- name: Tinyproxy Config Structure
  property_count: 0
  slug: tinyproxy-config-structure
jsonld:
- class_count: 23
  name: Tinyproxy Context
  property_count: 2
  slug: tinyproxy-context
layout: provider
modified: '2026-05-03'
name: Tinyproxy
nav: Providers
network: true
overview: 'Tinyproxy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Forward Proxy, Proxy, HTTP, Networking, and Open-Source.


  The Tinyproxy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tinyproxy''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Tinyproxy Plans Pricing
  plan_count: 3
  slug: tinyproxy-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Tinyproxy Rate Limits
  slug: tinyproxy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tinyproxy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tinyproxy-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 18.7
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 60.0
  previous_composite: 29.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tinyproxy/refs/heads/main/screenshots/tinyproxy-2026-06-20T195408.png
slug: tinyproxy
tags:
- Forward Proxy
- Proxy
- HTTP
- Networking
- Open-Source
website: https://tinyproxy.github.io/
---
