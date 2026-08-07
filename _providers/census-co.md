---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 3
apis:
- description: REST API for managing reverse ETL syncs, sources, destinations, datasets, models, and segments programmatically. Used to provision, update, and monitor Census workspaces, schedule syncs, and integrate
  name: Census Management API
  slug: census-management-api
- description: REST API for embedding reverse ETL inside SaaS products, giving customers more than 200 prebuilt connectors out of the box. Combines Management API operations with Connect Links to streamline credenti
  name: Census Embedded API
  slug: census-embedded-api
- description: Client-side workflow that streamlines collection of end-user credentials and programmatically creates reverse ETL pipelines, in combination with the Census Management API.
  name: Census Connect
  slug: census-connect
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/census-co-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/census-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getcensus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getcensus.com/
- group: other
  title: ''
  type: Activations
  url: https://fivetran.com/docs/activations
- group: start
  title: ''
  type: Signup
  url: https://www.getcensus.com/
created: '2026-05-23'
description: Census, now operating as Fivetran Activations following its acquisition by Fivetran, is a reverse ETL and data activation platform that turns the data warehouse into the operational source of truth for go-to-market and product teams. The platform configures managed, no-code reverse ETL pipelines that move modeled data from warehouses like Snowflake, BigQuery, Databricks, and Redshift into more than 200 SaaS destinations across CRM, marketing automation, advertising, customer success, product, finance, and productivity tools. Census also offers an Audience Hub for visual segment building, an Embedded product for white-labeling reverse ETL inside customer-facing applications, and a Connect workflow for collecting end-user credentials and programmatically creating sync pipelines. Developers integrate through the Census Management API, Embedded API, Connect Links, custom destination APIs, and a Terraform provider. This profile covers the Census product line and is distinct from
  the US Census Bureau public APIs.
finops:
- name: Census Co Finops
  service_category: API
  slug: census-co-finops
graphqls:
- description: This conceptual GraphQL schema represents the Census (Fivetran Activations) reverse ETL and data activation platform. Census enables engineering and data teams to synchronize modeled warehouse data in
  name: Census GraphQL Schema
  slug: census-co-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/census-co.png
layout: provider
modified: '2026-05-23'
name: Census
nav: Providers
network: true
overview: 'Census publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Census, Reverse ETL, Data Activation, Embedded, and Audience Hub.


  Census'' developer surface includes documentation, signup flow, and 4 more developer resources.'
plans:
- name: Census Co Plans Pricing
  plan_count: 1
  slug: census-co-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Census Co Rate Limits
  slug: census-co-rate-limits
score:
  band: thin
  composite: 30.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 48.1
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/census-co/refs/heads/main/screenshots/census-co-2026-06-20T174117.png
security:
- kind: domain-security
  name: Census Co Domain Security
  slug: census-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Census Co Trust Center
  slug: census-co-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: census-co
tags:
- Census
- Reverse ETL
- Data Activation
- Embedded
- Audience Hub
- Connect
- Warehouse
- Snowflake
- BigQuery
- Databricks
- Salesforce
- HubSpot
- Marketing
website: https://www.getcensus.com/
---
