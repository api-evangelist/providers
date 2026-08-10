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
api_count: 2
apis:
- description: The Reprise Data API allows teams to pull real-time, click-level demo engagement data directly from Reprise into data warehouses, data lakes, or downstream platforms. It supports analytics data includ
  name: Reprise Data API
  slug: data-api
- description: The Reprise HTML Environment Data API enables dynamic data injection into HTML-based demo environments. It supports portal ID configuration, time period parameters for pulling demo data, and authentic
  name: Reprise HTML Environment Data API
  slug: html-environment-data-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/reprise-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reprise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reprise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reprise.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/GetReprise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getreprise
- group: company
  title: ''
  type: Blog
  url: https://www.reprise.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reprise.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reprise.com/
- group: other
  title: ''
  type: X
  url: https://x.com/getreprise
- group: commercial
  title: ''
  type: Plans
  url: plans/reprise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reprise-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reprise-finops.yml
created: 2026-06-13
description: Reprise is the leading enterprise demo automation platform that enables sales and marketing teams to create guided product tours, sandbox demos, and interactive leave-behind experiences without engineering involvement. The platform supports screen capture, data injection, and fully cloned environments to produce pixel-perfect, customizable product demonstrations at scale. Reprise offers a Data API for pulling real-time click-level engagement data into data warehouses and downstream platforms, along with pre-built integrations with Salesforce, HubSpot, Marketo, and Google Analytics. With over 20 million demos served, Reprise is trusted by enterprise customers including Databricks, ServiceNow, Cloudera, and iCIMS.
finops:
- name: Reprise Finops
  service_category: ''
  slug: reprise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reprise.png
jsonld:
- class_count: 0
  name: Reprise Context
  property_count: 0
  slug: reprise-context
layout: provider
modified: 2026-06-13
name: Reprise
nav: Providers
network: true
overview: 'Reprise publishes 1 API on the [APIs.io](https://apis.io/) network: Data API. Tagged areas include Demo Automation, Product Tours, Sales Demos, Interactive Demos, and Sandbox Environments.


  The Reprise catalog on APIs.io includes 1 JSON-LD context.


  Reprise''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Reprise Plans Pricing
  plan_count: 3
  slug: reprise-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 0
  name: Reprise Rate Limits
  slug: reprise-rate-limits
score:
  band: thin
  composite: 33.4
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 40.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reprise/refs/heads/main/screenshots/reprise-2026-06-20T192911.png
security:
- kind: domain-security
  name: Reprise Domain Security
  slug: reprise-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Reprise Trust Center
  slug: reprise-trust-center
  summary_line: SOC 2
slug: reprise
tags:
- Demo Automation
- Product Tours
- Sales Demos
- Interactive Demos
- Sandbox Environments
- Enterprise Sales
- Marketing Technology
- Sales Enablement
website: https://www.reprise.com/
---
