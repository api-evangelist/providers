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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/g2crowd-com/llms/g2crowd-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/g2crowd-com-llms.txt
- group: other
  href: https://artifacts.apis.io/g2crowd-com/hosts/g2crowd-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/g2crowd-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/g2crowd-com/vendors/g2crowd-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/g2crowd-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/g2crowd-com/security/g2crowd-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/g2crowd-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://g2crowd.com/
created: '2026-10-20'
description: G2 Software Solutions provides a platform that aggregates software reviews and ratings from users and experts, helping businesses make informed technology purchasing decisions. The service offers detailed product comparisons, market insights, and analytics across a wide range of software categories, supporting B2B buyers in evaluating solutions based on real-world feedback and performance data.
layout: provider
modified: '2026-10-20'
name: G2 Software Solutions
nav: Providers
network: true
overview: G2 Software Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Reviews, B2B, and Analytics.
random_paper: 4
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: G2Crowd Com Domain Security
  slug: g2crowd-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: g2crowd-com
tags:
- Company
- Software
- Reviews
- B2B
- Analytics
website: https://g2crowd.com/
---
