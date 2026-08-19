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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: RESTful JSON API for creating and sending documents for electronic signature, managing templates, uploading files, tracking audit trails, bulk sending via CSV, and receiving webhook event notification
  name: Eversign API
  slug: eversign-api
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/eversign/eversign-php-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/eversign/eversign-php-sdk/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/eversign/eversign-php-sdk/blob/master/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/eversign/eversign-php-sdk/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eversign-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eversign.com
- group: docs
  title: ''
  type: Documentation
  url: https://eversign.com/api/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/eversign
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xodosign
- group: company
  title: ''
  type: Blog
  url: https://eversign.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://eversign.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://eversign.com/status-page
- group: other
  title: ''
  type: X
  url: https://twitter.com/geteversign
- group: commercial
  title: ''
  type: Plans
  url: plans/eversign-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eversign-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eversign-finops.yml
created: '2026-06-13'
description: E-signature and document management platform with a REST API for creating, sending, and managing electronic signature requests, templates, audit trails, bulk sending, embedded signing, and webhook notifications. Now branded as Xodo Sign, formerly eversign.
finops:
- name: Eversign Finops
  service_category: ''
  slug: eversign-finops
graphqls:
- description: This GraphQL schema models the Eversign (Xodo Sign) e-signature REST API. Eversign provides a RESTful JSON API for creating and sending documents for electronic signature, managing templates, uploadin
  name: Eversign GraphQL Schema
  slug: eversign-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eversign.png
jsonld:
- class_count: 0
  name: Eversign Context
  property_count: 20
  slug: eversign-context
layout: provider
modified: '2026-06-13'
name: Eversign
nav: Providers
network: true
overview: 'Eversign publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Signature, Electronic Signatures, Document Management, PDF, and Audit Trail.


  The Eversign catalog on APIs.io includes 1 JSON-LD context.


  Eversign''s developer surface includes documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Eversign Plans Pricing
  plan_count: 6
  slug: eversign-plans-pricing
random_paper: 122
rate_limits:
- limit_count: 6
  name: Eversign Rate Limits
  slug: eversign-rate-limits
score:
  band: developing
  composite: 41.2
  delta: -1.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 52.2
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 42.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eversign/refs/heads/main/screenshots/eversign-2026-06-20T180911.png
security:
- kind: domain-security
  name: Eversign Domain Security
  slug: eversign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eversign
tags:
- E-Signature
- Electronic Signatures
- Document Management
- PDF
- Audit Trail
- Webhooks
- Bulk Sending
website: https://eversign.com
---
