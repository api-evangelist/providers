---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
- description: RESTful JSON API providing programmatic access to Brandfolder resources including organizations, brandfolders, collections, sections, assets, attachments, tags, custom fields, labels, invitations, use
  name: Brandfolder API
  slug: brandfolder-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/brandfolder-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brandfolder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandfolder.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smartsheet.com/api/brandfolder
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Brandfolder
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brandfolder-inc-
- group: company
  title: ''
  type: Blog
  url: https://brandfolder.engineering/
- group: commercial
  title: ''
  type: Pricing
  url: https://brandfolder.com/contact/sales/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brandfolder.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Brandfolder
- group: commercial
  title: ''
  type: Plans
  url: plans/brandfolder-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brandfolder-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brandfolder-finops.yml
created: 2026-06-13
description: Brandfolder is a digital asset management (DAM) platform and Smartsheet company that provides a RESTful API for managing brand assets, collections, sections, tags, share links, webhooks, and asset distribution permissions. The API enables organizations to push Brandfolder content to other applications, pull data from external sources, and synchronize Brandfolder with other platforms.
finops:
- name: Brandfolder Finops
  service_category: ''
  slug: brandfolder-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brandfolder.png
jsonld:
- class_count: 0
  name: Brandfolder Context
  property_count: 13
  slug: brandfolder-context
layout: provider
modified: 2026-06-13
name: Brandfolder
nav: Providers
network: true
overview: 'Brandfolder publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Asset Management, DAM, Brand Management, Assets, and Media.


  The Brandfolder catalog on APIs.io includes 1 JSON-LD context.


  Brandfolder''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Brandfolder Plans Pricing
  plan_count: 2
  slug: brandfolder-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 0
  name: Brandfolder Rate Limits
  slug: brandfolder-rate-limits
score:
  band: thin
  composite: 32.6
  delta: -4.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 36.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brandfolder/refs/heads/main/screenshots/brandfolder-2026-06-20T173633.png
security:
- kind: domain-security
  name: Brandfolder Domain Security
  slug: brandfolder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Brandfolder Trust Center
  slug: brandfolder-trust-center
  summary_line: SOC 2, HIPAA
slug: brandfolder
tags:
- Digital Asset Management
- DAM
- Brand Management
- Assets
- Media
- Collections
- Smartsheet
website: https://brandfolder.com
---
