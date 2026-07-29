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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Sorry™ REST API provides programmatic access to manage status pages, components, incident notices, notice updates, and subscriber lists. Supports Bearer token authentication and rate limiting of 1
  name: Sorry Status Page API
  slug: sorry-status-page-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sorry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sorry-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sorry-as-a-service
- group: start
  title: ''
  type: Portal
  url: https://www.sorryapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sorryapp.com/v1
- group: company
  title: ''
  type: Website
  url: https://www.sorryapp.com/
- group: operate
  title: ''
  type: Status API
  url: https://www.sorryapp.com/status-api/
- group: other
  title: ''
  type: Dashboard
  url: https://app.sorryapp.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sorry-app
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sorryapp.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.sorryapp.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sorryapp.com/
- group: commercial
  title: ''
  type: Terms
  url: https://www.sorryapp.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sorryapp.com/privacy/
created: '2026-03-16'
description: Sorry™ (SorryApp) is a status page platform that enables teams to communicate planned and unplanned service interruptions to their customers. The Sorry REST API provides full programmatic control over status pages, components, incident notices, notice updates, and subscriber management. Build automated incident communication workflows that integrate with monitoring tools, alerting platforms, and customer notification systems.
examples:
- key_count: 2
  name: Sorry Create Notice Example
  slug: sorry-create-notice-example
finops:
- name: Sorry Finops
  service_category: API
  slug: sorry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sorry.png
json_schemas:
- name: Sorry Notice
  property_count: 12
  slug: sorry-notice
- name: Sorry Status Page
  property_count: 11
  slug: sorry-page
json_structures:
- name: Sorry Notice Structure
  property_count: 0
  slug: sorry-notice-structure
jsonld:
- class_count: 6
  name: Sorry Context
  property_count: 16
  slug: sorry-context
layout: provider
modified: '2026-05-02'
name: Sorry
nav: Providers
network: true
overview: 'Sorry publishes 1 API on the [APIs.io](https://apis.io/) network: Status Page API. Tagged areas include Status Pages, Incident Management, Developer Tools, Monitoring, and Notifications.


  The Sorry catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sorry''s developer surface includes developer portal, documentation, pricing, engineering blog, terms of service, and 9 more developer resources.'
plans:
- name: Sorry Plans Pricing
  plan_count: 3
  slug: sorry-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Sorry Rate Limits
  slug: sorry-rate-limits
rules:
- name: Sorry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sorry-jsonschema-spectral-rules
- name: Sorry API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 7
  slug: sorry-rules
score:
  band: developing
  composite: 51.2
  delta: -4.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.1
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 55.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sorry/refs/heads/main/screenshots/sorry-2026-06-20T194215.png
security:
- kind: domain-security
  name: Sorry Domain Security
  slug: sorry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sorry Vulnerability Disclosure
  slug: sorry-vulnerability-disclosure
  summary_line: disclosure policy published
slug: sorry
tags:
- Status Pages
- Incident Management
- Developer Tools
- Monitoring
- Notifications
website: https://www.sorryapp.com/
---
