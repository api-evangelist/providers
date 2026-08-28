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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: GraphQL API for querying IT asset, software, user, and site data discovered and inventoried by Lansweeper. Authentication is via Personal Access Token or OAuth Bearer token; all requests are HTTP POST
  name: Lansweeper Data API
  slug: data-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lansweeper-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lansweeper
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lansweeper
- group: company
  title: ''
  type: Website
  url: https://www.lansweeper.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lansweeper.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lansweeper.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.lansweeper.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.lansweeper.com/feed/
created: '2026-05-11'
description: Lansweeper is an IT asset discovery and management platform that automatically scans and inventories hardware, software, users, and cloud resources across on-premises, cloud, and OT environments. It provides a unified technology asset intelligence platform used for IT asset management (ITAM), cybersecurity asset management (CAAM), software asset management, and compliance. The Lansweeper Data API is a GraphQL endpoint that exposes the technology asset intelligence stored in your Lansweeper sites using Bearer token authentication.
graphqls:
- description: GraphQL API for querying IT asset, software, user, and site data discovered and inventoried by Lansweeper. Authentication is via Personal Access Token or OAuth Bearer token; all requests are HTTP POST
  name: Lansweeper GraphQL API
  slug: lansweeper-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lansweeper.png
layout: provider
modified: '2026-05-11'
name: Lansweeper
nav: Providers
network: true
overview: 'Lansweeper publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IT Asset Management, Asset Discovery, Cybersecurity Asset Management, Network Discovery, and Software Asset Management.


  Lansweeper''s developer surface includes documentation, pricing, signup flow, engineering blog, and 4 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 16.7
  delta: 2.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lansweeper/refs/heads/main/screenshots/lansweeper-2026-06-20T184316.png
security:
- kind: domain-security
  name: Lansweeper Domain Security
  slug: lansweeper-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lansweeper
tags:
- IT Asset Management
- Asset Discovery
- Cybersecurity Asset Management
- Network Discovery
- Software Asset Management
- GraphQL
website: https://www.lansweeper.com
---
