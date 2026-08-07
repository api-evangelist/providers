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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Census Management REST API allows developers to programmatically manage syncs, connections, models, segments, and destinations within Census workspaces and organizations. Supports both workspace-l
  name: Census Management API
  slug: census-management-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/getcensus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getcensus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getcensus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fivetran.com/docs/activations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sutrolabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getcensus
- group: company
  title: ''
  type: Blog
  url: https://www.getcensus.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fivetran.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getcensus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/getcensus
- group: commercial
  title: ''
  type: Plans
  url: plans/getcensus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/getcensus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/getcensus-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://whatsnew.getcensus.com/
- group: other
  title: ''
  type: Terraform
  url: https://docs.getcensus.com/misc/developers/terraform
created: '2026-06-13'
description: Census (now Fivetran Activations) is a reverse ETL platform that syncs data from data warehouses to CRM, marketing, advertising, and other business destinations. It enables data teams to define SQL-based models and segments, then automatically activate that data to over 200 destinations including Salesforce, HubSpot, Facebook Ads, and Google Ads without writing custom integrations.
finops:
- name: Getcensus Finops
  service_category: ''
  slug: getcensus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getcensus.png
layout: provider
modified: '2026-06-13'
name: Census
nav: Providers
network: true
overview: 'Census publishes 1 API on the [APIs.io](https://apis.io/) network: Management API. Tagged areas include Reverse ETL, Data Activation, Data Warehouse, CRM, and Marketing Automation.


  Census'' developer surface includes documentation, engineering blog, pricing, changelog, and 11 more developer resources.'
plans:
- name: Getcensus Plans Pricing
  plan_count: 4
  slug: getcensus-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 2
  name: Getcensus Rate Limits
  slug: getcensus-rate-limits
score:
  band: thin
  composite: 36.2
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 36.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getcensus/refs/heads/main/screenshots/getcensus-2026-06-20T181807.png
security:
- kind: domain-security
  name: Getcensus Domain Security
  slug: getcensus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getcensus Trust Center
  slug: getcensus-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: getcensus
tags:
- Reverse ETL
- Data Activation
- Data Warehouse
- CRM
- Marketing Automation
- Segments
- Syncs
- SQL
website: https://www.getcensus.com/
---
