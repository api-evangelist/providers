---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: The Southwest Airlines internal flight booking API powers the southwest.com website for searching and booking flights. It provides flight availability, pricing, schedules, and air booking shopping cap
  name: Southwest Airlines Flight API
  slug: southwest-flight-api
- description: The Rapid Rewards loyalty program API enables management of points balances, redemption, and tier status for Southwest Airlines frequent fliers.
  name: Southwest Airlines Rapid Rewards API
  slug: southwest-rapid-rewards-api
- description: The Southwest Airlines in-flight network provides a JSON API available at getconnected.southwestwifi.com/current.json while onboard the aircraft. It delivers real-time flight information including spe
  name: Southwest Airlines In-Flight Network API
  slug: southwest-inflight-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/southwest-airlines-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/southwest-airlines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.southwest.com
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.southwest.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SouthwestAir
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/southwest-airlines
- group: other
  title: ''
  type: X
  url: https://twitter.com/SouthwestAir
- group: other
  title: ''
  type: Open Source
  url: https://github.com/SouthwestAir/.github
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/json-ld/southwest-airlines-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/vocabulary/southwest-airlines-vocabulary.yml
created: '2026-03-21'
description: Southwest Airlines is one of the world's most profitable airlines and the largest domestic air carrier in the United States by number of passengers. The company provides scheduled air transportation in the United States and near-international markets, known for its low fares, no baggage fees policy, and customer service. Southwest Airlines is a Fortune 500 company headquartered in Dallas, Texas.
examples:
- key_count: 10
  name: Southwest Airlines Flight Example
  slug: southwest-airlines-flight-example
- key_count: 7
  name: Southwest Airlines Reservation Example
  slug: southwest-airlines-reservation-example
finops:
- name: Southwest Airlines Finops
  service_category: Travel & Distribution
  slug: southwest-airlines-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for Southwest Airlines covering the airline's core flight, booking, loyalty, and ancillary service domains.
  name: Southwest Airlines GraphQL Schema
  slug: southwest-airlines-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/southwest-airlines.png
json_schemas:
- name: Southwest Airlines Flight
  property_count: 12
  slug: southwest-airlines-flight
- name: Southwest Airlines Reservation
  property_count: 7
  slug: southwest-airlines-reservation
json_structures:
- name: Southwest Airlines Flight Structure
  property_count: 0
  slug: southwest-airlines-flight-structure
jsonld:
- class_count: 8
  name: Southwest Airlines Context
  property_count: 16
  slug: southwest-airlines-context
layout: provider
modified: '2026-05-02'
name: Southwest Airlines
nav: Providers
network: true
overview: 'Southwest Airlines publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Airlines, Aviation, and Travel.


  The Southwest Airlines catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Southwest Airlines Plans Pricing
  plan_count: 1
  slug: southwest-airlines-plans-pricing
press:
- date: '2026-05-25'
  title: Southwest Airlines has banned robots from flights, a policy ...
  url: https://www.facebook.com/KING5News/posts/southwest-airlines-has-banned-robots-from-flights-a-policy-change-that-came-afte/1452439983594853/
- date: '2026-05-25'
  title: Southwest Airlines Co. News and Press Releases
  url: https://www.prnewswire.com/news/southwest-airlines-co./
- date: '2026-05-25'
  title: Southwest Airlines recently changed their baggage policy ...
  url: https://www.facebook.com/Fox32Chicago/posts/southwest-airlines-recently-changed-their-baggage-policy-after-a-passenger-at-da/1449339787239217/
- date: '2026-05-25'
  title: Southwest Airlines Transforms Customer Experience with ...
  url: https://aws.amazon.com/video/watch/6d31bc3cfa4/
- date: '2026-05-25'
  title: Southwest uses AI to modernize management software
  url: https://www.pwc.com/us/en/library/case-studies/southwest-ai-software-update.html
random_paper: 114
rate_limits:
- limit_count: 1
  name: Southwest Airlines Rate Limits
  slug: southwest-airlines-rate-limits
rules:
- name: Southwest Airlines API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: southwest-airlines-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 74.1
    developer_ergonomics: 0.0
    discoverability: 55.6
    governance: 68.8
    operational_transparency: 10.5
  previous_composite: 36.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/southwest-airlines/refs/heads/main/screenshots/southwest-airlines-2026-06-20T194230.png
security:
- kind: domain-security
  name: Southwest Airlines Domain Security
  slug: southwest-airlines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Southwest Airlines Vulnerability Disclosure
  slug: southwest-airlines-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: southwest-airlines
tags:
- Fortune 500
- Airlines
- Aviation
- Travel
website: https://www.southwest.com
---
