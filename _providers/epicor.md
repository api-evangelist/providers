---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Epicor Kinetic Open REST API exposes all ERP capabilities through OData v4 compliant endpoints covering business objects, processes, reports, Business Activity Queries (BAQs), and custom Epicor Fu
  name: Epicor Kinetic Open REST API
  slug: epicor-kinetic-rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epicor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.epicor.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.epicor.com/en/products/enterprise-resource-planning-erp/epicor-kinetic/tools-and-technology/open-rest-api/
- group: company
  title: ''
  type: Blog
  url: https://www.epicor.com/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/epicor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epicorsoftware
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@epicor
- group: commercial
  title: ''
  type: Pricing
  url: https://www.epicor.com/en/resources/contact-us/
- group: company
  title: ''
  type: About
  url: https://www.epicor.com/en/about/
- group: operate
  title: ''
  type: Support
  url: https://www.epicor.com/en/products/epicor-connected-process-control/
created: '2026-06-05'
description: Epicor Software Corporation provides industry-specific enterprise resource planning software for manufacturing, distribution, retail, and service industries. Epicor Kinetic, the flagship ERP platform, exposes an Open REST API built on OData v4 that gives developers service-based access to all business objects, processes, reports, BAQs, and Epicor Functions using standard HTTP methods and API key authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epicor.png
jsonld:
- class_count: 23
  name: Epicor Context
  property_count: 9
  slug: epicor-context
layout: provider
modified: '2026-06-05'
name: Epicor
nav: Providers
network: true
overview: 'Epicor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, Manufacturing, Distribution, Enterprise, and REST.


  The Epicor catalog on APIs.io includes 1 JSON-LD context.


  Epicor''s developer surface includes documentation, engineering blog, YouTube channel, pricing, support, and 5 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epicor/refs/heads/main/screenshots/epicor-2026-06-20T180754.png
security:
- kind: domain-security
  name: Epicor Domain Security
  slug: epicor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: epicor
tags:
- ERP
- Manufacturing
- Distribution
- Enterprise
- REST
- Fortune 500
website: https://www.epicor.com
---
