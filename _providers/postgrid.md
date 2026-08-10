---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
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
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: A REST API for programmatically sending letters, postcards, checks, and self-mailers. Handles printing, postage, and delivery with support for templates, contacts, tracking, webhooks, and both test an
  name: PostGrid Print & Mail API
  slug: print-mail-api
- description: A REST API for real-time address autocomplete, verification, and standardization for US and Canadian addresses. Supports CASS-certified validation, geocoding (latitude/longitude), freeform address par
  name: PostGrid US & Canada Address Verification API
  slug: address-verification-api
- description: A REST API for verifying, standardizing, and autocompleting addresses across 245+ countries worldwide. Supports real-time lookups and bulk verification workflows. Authenticated via x-api-key header.
  name: PostGrid International Address Verification API
  slug: international-address-verification-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postgrid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.postgrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.postgrid.com/
- group: other
  title: ''
  type: Developers
  url: https://www.postgrid.com/developers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postgrid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/postgrid
- group: other
  title: ''
  type: X
  url: https://x.com/postgridinc
- group: company
  title: ''
  type: Blog
  url: https://www.postgrid.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.postgrid.com/updates-and-releases/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.postgrid.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.postgrid.com/
- group: operate
  title: ''
  type: Support
  url: https://www.postgrid.com/help-support/
- group: commercial
  title: ''
  type: Plans
  url: plans/postgrid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/postgrid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/postgrid-finops.yml
created: '2026-06-12'
description: PostGrid is a physical mail automation platform that provides REST APIs for sending printed letters, postcards, checks, and self-mailers at scale. It offers a Print & Mail API that enables developers to programmatically trigger and manage direct mail campaigns with full personalization and tracking support. PostGrid also provides US & Canada Address Verification and International Address Verification APIs covering 245+ countries for real-time autocomplete, standardization, geocoding, and bulk batch verification. The platform supports both test and live API environments, integrates natively with Salesforce, HubSpot, Zapier, and Marketo, and handles postage, printing, and delivery end-to-end.
finops:
- name: Postgrid Finops
  service_category: ''
  slug: postgrid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postgrid.png
jsonld:
- class_count: 8
  name: Postgrid Context
  property_count: 0
  slug: postgrid-context
layout: provider
modified: '2026-06-12'
name: PostGrid
nav: Providers
network: true
overview: 'PostGrid publishes 1 API on the [APIs.io](https://apis.io/) network: Print & Mail API. Tagged areas include Direct Mail, Print & Mail, Address Verification, Address Validation, and Postcards.


  The PostGrid catalog on APIs.io includes 1 JSON-LD context.


  PostGrid''s developer surface includes documentation, engineering blog, changelog, pricing, support, and 10 more developer resources.'
plans:
- name: Postgrid Plans Pricing
  plan_count: 13
  slug: postgrid-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 3
  name: Postgrid Rate Limits
  slug: postgrid-rate-limits
score:
  band: thin
  composite: 40.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 40.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postgrid/refs/heads/main/screenshots/postgrid-2026-06-20T191958.png
security:
- kind: domain-security
  name: Postgrid Domain Security
  slug: postgrid-domain-security
  summary_line: TLSv1.3 · DMARC
slug: postgrid
tags:
- Direct Mail
- Print & Mail
- Address Verification
- Address Validation
- Postcards
- Letters
- Checks
- Physical Mail
- Mail Automation
- Address Autocomplete
- Geocoding
website: https://www.postgrid.com/
---
