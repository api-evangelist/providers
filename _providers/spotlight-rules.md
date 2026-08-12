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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Spotlight Rules Agentic Access
  operation_count: 1
  slug: spotlight-rules-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: Standalone spotlight on API governance rules — guardrails for API operations delivered as a curated ruleset alongside the rules collection.
  name: Spotlight Rules Feed
  slug: spotlight-rules
- description: Spotlight governance rules feed
  name: Spotlight Rules Rules API
  slug: spotlight-rules-rules-api
artifact_total: 13
collections:
- collection_type: open
  name: Spotlight Rules Feed API
  slug: open-spotlight-rules
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spotlight-rules-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spotlight-rules-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apievangelist.com/
- group: other
  title: ''
  type: Network
  url: https://developer.apievangelist.com/network/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: other
  title: ''
  type: APIsJSON
  url: https://developer.apievangelist.com/apis.json
created: '2024-11-11'
description: Standalone spotlight on API governance rules — guardrails for API operations delivered as a curated ruleset alongside the rules collection.
finops:
- name: Spotlight Rules Finops
  service_category: API
  slug: spotlight-rules-finops
image: https://kinlane-images.s3.amazonaws.com/shared/api-evangelist-logos/api-evangelist-logo-butterfly.png
json_schemas:
- name: Spectral Rule
  property_count: 10
  slug: spectral-rule
- name: Vacuum Rule
  property_count: 3
  slug: vacuum-rule
json_structures:
- name: Spectral Ruleset Structure
  property_count: 0
  slug: spectral-ruleset-structure
jsonld:
- class_count: 24
  name: Spotlight Rules Context
  property_count: 5
  slug: spotlight-rules-context
layout: provider
modified: '2026-05-20'
name: Spotlight Rules
nav: Providers
network: true
overview: 'Spotlight Rules publishes 1 API on the [APIs.io](https://apis.io/) network: Rules API. Tagged areas include Rules, Spotlight, and Governance.


  The Spotlight Rules catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Spotlight Rules Plans Pricing
  plan_count: 3
  slug: spotlight-rules-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 5
  name: Spotlight Rules Rate Limits
  slug: spotlight-rules-rate-limits
rules:
- name: Spotlight Rules API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spotlight-rules-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.7
  delta: -8.4
  facets:
    commercial_clarity: 15.8
    contract_quality: 60.4
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 42.1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/spotlight-rules/refs/heads/main/screenshots/spotlight-rules-2026-06-20T194354.png
security:
- kind: domain-security
  name: Spotlight Rules Domain Security
  slug: spotlight-rules-domain-security
  summary_line: TLSv1.3
slug: spotlight-rules
tags:
- Rules
- Spotlight
- Governance
website: https://developer.apievangelist.com/
---
