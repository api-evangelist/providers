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
api_count: 1
apis:
- description: The Zip Procurement API is a REST-based interface for automating and integrating enterprise procurement workflows. It provides endpoints for managing intake requests, vendor onboarding, approval routi
  name: Zip Procurement API
  slug: zip-procurement-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/zip-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zip.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ziphq.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ziphq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/theziphq/
- group: company
  title: ''
  type: Blog
  url: https://zip.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://zip.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zip.com
- group: other
  title: ''
  type: X
  url: https://x.com/theziphq
- group: commercial
  title: ''
  type: Plans
  url: plans/zip-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zip-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zip-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/zip-context.jsonld
created: '2026-06-13'
description: Zip is an AI-powered procurement orchestration platform that provides a REST API for managing the full intake-to-pay lifecycle. The API enables developers to build custom integrations that extract, create, and update procurement data including intake requests, vendor onboarding, approval workflows, and contract management. Authentication is handled via API keys passed as Basic Auth credentials, with separate sandbox and production environments available. Zip's platform serves enterprise customers by creating a single front door for all corporate purchase requests and routing them through configurable approval chains before connecting to ERPs and financial systems. The API supports webhook callbacks for async event notifications when procurement workflows complete, enabling deep integration with existing enterprise toolchains.
finops:
- name: Zip Finops
  service_category: ''
  slug: zip-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zip.png
jsonld:
- class_count: 11
  name: Zip Context
  property_count: 26
  slug: zip-context
layout: provider
modified: '2026-06-13'
name: Zip
nav: Providers
network: true
overview: 'Zip publishes 1 API on the [APIs.io](https://apis.io/) network: Procurement API. Tagged areas include Procurement, Spend Management, Intake to Pay, Approval Workflows, and Vendor Management.


  The Zip catalog on APIs.io includes 1 JSON-LD context.


  Zip''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Zip Plans Pricing
  plan_count: 1
  slug: zip-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 2
  name: Zip Rate Limits
  slug: zip-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 50.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 36.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zip/refs/heads/main/screenshots/zip-2026-06-20T201914.png
security:
- kind: domain-security
  name: Zip Domain Security
  slug: zip-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Zip Trust Center
  slug: zip-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: zip
tags:
- Procurement
- Spend Management
- Intake to Pay
- Approval Workflows
- Vendor Management
- Contract Management
- Enterprise Software
- FinTech
website: https://zip.com
---
