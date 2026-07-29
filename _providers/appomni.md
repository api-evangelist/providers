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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Appomni Agentic Access
  operation_count: 4
  slug: appomni-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: Compliance reporting and audit management
  name: AppOmni Compliance API
  slug: appomni-compliance-api
- description: Security policy configuration and management
  name: AppOmni Policies API
  slug: appomni-policies-api
- description: SaaS security event monitoring and management
  name: AppOmni Security Events API
  slug: appomni-security-events-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appomni-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/appomni-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appomni-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appomni-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appomni
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appomni
- group: company
  title: ''
  type: Website
  url: https://www.appomni.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.appomni.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.appomni.com/feed/
created: '2026-03-27'
description: AppOmni is a SaaS security management platform providing continuous monitoring, threat detection, and compliance for enterprise SaaS applications.
examples:
- key_count: 8
  name: Security Event Example
  slug: security-event-example
finops:
- name: Appomni Finops
  service_category: API
  slug: appomni-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appomni.png
json_schemas:
- name: SecurityEvent
  property_count: 8
  slug: security-event
json_structures:
- name: Security Event Structure
  property_count: 0
  slug: security-event-structure
jsonld:
- class_count: 15
  name: Appomni Context
  property_count: 0
  slug: appomni-context
layout: provider
modified: '2026-04-19'
name: AppOmni
nav: Providers
network: true
overview: 'AppOmni publishes 3 APIs on the [APIs.io](https://apis.io/) network: Compliance API, Policies API, and Security Events API. Tagged areas include SaaS Security, Compliance, Threat Detection, CASB, and Zero Trust.


  The AppOmni catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AppOmni''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Appomni Plans Pricing
  plan_count: 3
  slug: appomni-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Appomni Rate Limits
  slug: appomni-rate-limits
rules:
- name: AppOmni API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: appomni-jsonschema-spectral-rules
- name: AppOmni API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: appomni-spectral-rules
score:
  band: developing
  composite: 50.0
  delta: -3.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 75.4
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appomni/refs/heads/main/screenshots/appomni-2026-06-20T172343.png
security:
- kind: authentication
  name: Appomni Authentication
  slug: appomni-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Appomni Domain Security
  slug: appomni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Appomni Trust Center
  slug: appomni-trust-center
  summary_line: SOC 2, FedRAMP
slug: appomni
tags:
- SaaS Security
- Compliance
- Threat Detection
- CASB
- Zero Trust
website: https://www.appomni.com
---
