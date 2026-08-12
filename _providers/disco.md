---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'REST API for the DISCO eDiscovery platform providing access to datasets and metrics covering data-usage change events, review database sizes, and organizational data. Used for invoice reconciliation, '
  name: DISCO API
  slug: disco-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/disco-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/disco-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/disco/refs/heads/main/plans/disco-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/disco/refs/heads/main/rate-limits/disco-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/disco/refs/heads/main/finops/disco-finops.yml
- group: company
  title: ''
  type: Website
  url: https://csdisco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.csdisco.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://csdisco.com/offerings/ediscovery/pricing
- group: company
  title: ''
  type: Blog
  url: https://csdisco.com/blog
- group: operate
  title: ''
  type: Status
  url: https://csdisco.statuspage.io/
- group: operate
  title: ''
  type: Support
  url: https://support.csdisco.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.csdisco.com/hc/en-us/categories/changelog
created: '2026-06-13'
description: DISCO is an AI-powered eDiscovery platform providing a REST API for uploading documents, managing review sets, running AI-assisted review, tagging documents, and exporting productions. The API enables programmatic access to data-usage change events, review database metrics, and organizational data for invoice reconciliation, anomaly detection, and subscription management.
finops:
- name: Disco Finops
  service_category: ''
  slug: disco-finops
graphqls:
- description: DISCO is an AI-powered legal technology platform for e-discovery and case management. The API covers document review, AI-powered coding, search and analytics, production, custodian management, and cas
  name: DISCO GraphQL API
  slug: disco-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/disco.png
jsonld:
- class_count: 7
  name: Disco Context
  property_count: 21
  slug: disco-context
layout: provider
modified: '2026-06-13'
name: DISCO
nav: Providers
network: true
overview: 'DISCO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include eDiscovery, Legal Technology, AI, Document Review, and Litigation.


  The DISCO catalog on APIs.io includes 1 JSON-LD context.


  DISCO''s developer surface includes documentation, pricing, engineering blog, status page, support, changelog, and 6 more developer resources.'
plans:
- name: Disco Plans Pricing
  plan_count: 1
  slug: disco-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 1
  name: Disco Rate Limits
  slug: disco-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.8
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/disco/refs/heads/main/screenshots/disco-2026-06-20T180034.png
security:
- kind: domain-security
  name: Disco Domain Security
  slug: disco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Disco Trust Center
  slug: disco-trust-center
  summary_line: SOC 2, ISO 27001
slug: disco
tags:
- eDiscovery
- Legal Technology
- AI
- Document Review
- Litigation
- Legal
website: https://csdisco.com/
---
