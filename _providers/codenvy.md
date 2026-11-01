---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/codenvy/hosts/codenvy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codenvy-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codenvy
- group: auth
  href: https://artifacts.apis.io/codenvy/security/codenvy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codenvy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.codenvy.com
created: '2026-10-29'
description: 'Codenvy is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by heavybit) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: PostImageBuilderV1ComposeRequest
  property_count: 3
  slug: codenvy-post-image-builder-v1-compose-request
jsonld:
- class_count: 1
  name: Codenvy Context
  property_count: 3
  slug: codenvy-context
layout: provider
modified: '2026-10-29'
name: Codenvy
nav: Providers
network: true
overview: 'Codenvy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Codenvy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Codenvy API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: codenvy-rules
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 24.5
    catalog_earned_first_party: 0.0
    catalog_gap: 90.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 8.3
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Codenvy Domain Security
  slug: codenvy-domain-security
  summary_line: DMARC
- kind: vulnerability-disclosure
  name: Codenvy Vulnerability Disclosure
  slug: codenvy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: codenvy
tags:
- Company
website: https://www.codenvy.com
---
