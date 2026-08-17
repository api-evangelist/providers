---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sophos Agentic Access
  operation_count: 2
  slug: sophos-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Security alerts from Sophos Central
  name: Sophos Alerts API
  slug: sophos-alerts-api
- description: Security events from Sophos Central
  name: Sophos Events API
  slug: sophos-events-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sophos Central SIEM Alerts API
  slug: open-sophos-alerts-api
- collection_type: open
  name: Sophos Central SIEM API
  slug: open-sophos-central-siem
- collection_type: open
  name: Sophos Central SIEM Alerts Events API
  slug: open-sophos-events-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sophos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sophos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sophos-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sophos
- group: start
  title: ''
  type: Portal
  url: https://developer.sophos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sophos.com/intro
- group: company
  title: ''
  type: Website
  url: https://www.sophos.com/
- group: operate
  title: ''
  type: Community
  url: https://community.sophos.com/sophos-central-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sophos
- group: build
  title: ''
  type: PostmanCollection
  url: https://github.com/sophos/sophos-central-apis-postman
- group: operate
  title: ''
  type: Support
  url: https://support.sophos.com/
- group: company
  title: ''
  type: Blog
  url: https://news.sophos.com/
- group: company
  title: ''
  type: Partners
  url: https://www.sophos.com/en-us/partners
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sophos.com/en-us/products
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.sophos.com/llms.txt
created: '2025-02-08'
description: Sophos is a global cybersecurity leader delivering advanced endpoint protection, network security, cloud security, and SIEM integration through the Sophos Central platform. The Sophos Central API enables partners, organizations, and tenants to automate security operations including alert management, event retrieval, endpoint policy enforcement, and threat response.
examples:
- key_count: 2
  name: Sophos List Alerts Example
  slug: sophos-list-alerts-example
finops:
- name: Sophos Finops
  service_category: API
  slug: sophos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sophos.png
json_schemas:
- name: Sophos Alert
  property_count: 12
  slug: sophos-alert
- name: Sophos Event
  property_count: 12
  slug: sophos-event
json_structures:
- name: Sophos Alerts Response Structure
  property_count: 0
  slug: sophos-alerts-response-structure
jsonld:
- class_count: 4
  name: Sophos Context
  property_count: 11
  slug: sophos-context
layout: provider
modified: '2026-05-19'
name: Sophos
nav: Providers
network: true
overview: 'Sophos publishes 2 APIs on the [APIs.io](https://apis.io/) network: Alerts API and Events API. Tagged areas include Cybersecurity, Endpoint Protection, Security, SIEM, and Threat Detection.


  The Sophos catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sophos'' developer surface includes authentication, developer portal, documentation, support, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Sophos Plans Pricing
  plan_count: 3
  slug: sophos-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Sophos Rate Limits
  slug: sophos-rate-limits
rules:
- name: Sophos API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sophos-jsonschema-spectral-rules
- name: Sophos API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 6
  slug: sophos-rules
score:
  band: developing
  composite: 46.2
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 67.2
    developer_ergonomics: 39.1
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sophos/refs/heads/main/screenshots/sophos-2026-06-20T194213.png
security:
- kind: authentication
  name: Sophos Authentication
  slug: sophos-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sophos Domain Security
  slug: sophos-domain-security
  summary_line: TLSv1.2 · DMARC
slug: sophos
tags:
- Cybersecurity
- Endpoint Protection
- Security
- SIEM
- Threat Detection
- Incident Response
website: https://www.sophos.com/
---
