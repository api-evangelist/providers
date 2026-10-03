---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 35
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering the broad integration tooling market, including iPaaS and embedded-iPaaS platforms, workflow automation tools, unified API providers, ETL and reverse-ETL data pipelines, and orchestration engines. Integration platforms reduce the cost of connecting disparate SaaS, on-premise, and AI systems by offering pre-built connectors, declarative flow builders, managed authentication, and normalized data models. This collection includes general-purpose iPaaS leaders like Zapier, Make, and Workato, embedded-iPaaS providers like Paragon and Cobalt, unified API platforms like Merge, Apideck, Nango, and StackOne, data integration and ELT platforms like Fivetran, Airbyte, and Stitch, reverse-ETL tools like Hightouch and Census, and workflow orchestration engines like Airflow, Prefect, Dagster, and Kestra.
examples:
- key_count: 11
  name: Integrations Connection Example
  slug: integrations-connection-example
- key_count: 12
  name: Integrations Integration Flow Example
  slug: integrations-integration-flow-example
features:
- description: Integration platforms ship hundreds to thousands of pre-built connectors so engineering teams can wire up SaaS systems without authoring custom HTTP clients for each provider.
  name: Pre-Built Connector Libraries
- description: iPaaS and workflow automation tools like Zapier, Make, and n8n expose drag-and-drop or node-based canvases that let non-developers compose multi-step automations across APIs.
  name: Visual Workflow Builders
- description: Embedded-iPaaS vendors like Paragon, Cobalt, and Integration.app give SaaS companies a white-labeled integration marketplace they can ship inside their own product.
  name: Embedded Integration Marketplaces
- description: Unified API providers like Merge, Apideck, Nango, and StackOne collapse dozens of category-specific APIs (HRIS, CRM, ATS, accounting) into a single normalized schema and auth surface.
  name: Unified API Normalization
- description: Data integration platforms like Fivetran, Airbyte, and Stitch land data from SaaS sources and databases into cloud warehouses on managed schedules with schema evolution handling.
  name: Managed ETL and ELT Pipelines
- description: Reverse-ETL tools like Hightouch, Census, and Polytomic push warehouse-modeled data back out to SaaS systems of action so sales, marketing, and support teams can act on it.
  name: Reverse ETL and Operational Sync
- description: Orchestration engines like Apache Airflow, Prefect, Dagster, and Kestra schedule, retry, and observe data and integration pipelines as declarative DAGs.
  name: Workflow Orchestration and Scheduling
- description: Integration platforms handle OAuth dance, token refresh, secret rotation, and per-tenant connection storage so consuming applications never have to manage credentials directly.
  name: Managed Authentication and Connection Storage
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: General-purpose workflow automation platform with 7,000+ connected apps and a no-code trigger/action builder used by millions of small businesses.
  name: Zapier
- description: Visual scenario builder (formerly Integromat) for multi-step, branching automations with strong data-transformation primitives.
  name: Make
- description: Enterprise iPaaS and intelligent automation platform with strong recipes-as-code model and embedded offering.
  name: Workato
- description: Source-available, self-hostable workflow automation tool with code nodes and an open node ecosystem.
  name: n8n
- description: Salesforce-owned enterprise iPaaS and API management platform built around the Anypoint Platform and DataWeave.
  name: MuleSoft
- description: Unified API for HRIS, ATS, CRM, ticketing, accounting, and file-storage integrations across 200+ providers.
  name: Merge
- description: Embedded iPaaS that ships an in-product integration marketplace and workflow builder for SaaS vendors.
  name: Paragon
- description: Managed ELT platform that lands data from 500+ SaaS sources and databases into cloud warehouses with schema evolution.
  name: Fivetran
- description: Open-source ELT platform with a community connector marketplace and a managed cloud offering.
  name: Airbyte
- description: Reverse-ETL platform that syncs modeled warehouse data into SaaS systems of action across sales, marketing, and support.
  name: Hightouch
- description: Widely deployed open-source workflow orchestrator that defines pipelines as Python DAGs with rich scheduling and retry semantics.
  name: Apache Airflow
- description: Open-source unified API and managed authentication layer for OAuth integrations across 400+ apps.
  name: Nango
json_schemas:
- name: Connection
  property_count: 11
  slug: integrations-connection
- name: IntegrationFlow
  property_count: 12
  slug: integrations-integration-flow
json_structures:
- name: Integrations Connection Structure
  property_count: 11
  slug: integrations-connection-structure
- name: Integrations Integration Flow Structure
  property_count: 12
  slug: integrations-integration-flow-structure
jsonld:
- class_count: 8
  name: Integrations Context
  property_count: 19
  slug: integrations-context
layout: provider
modified: '2026-05-19'
name: Integrations
nav: Providers
network: true
overview: 'Integrations is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, iPaaS, Embedded iPaaS, Workflow Automation, and Data Integration.


  The Integrations catalog on APIs.io includes 1 JSON-LD context.


  Integrations'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: integrations
tags:
- Integration
- iPaaS
- Embedded iPaaS
- Workflow Automation
- Data Integration
- Unified API
- ETL
- Reverse ETL
- Data Pipeline
- Orchestration
use_cases:
- description: SaaS vendors use embedded iPaaS like Paragon, Cobalt, or Integration.app to ship an in-product "Integrations" tab that lets their customers connect to Salesforce, HubSpot, Slack, and Google Workspace without leaving the product.
  name: SaaS Product Integration Marketplace
- description: Applicant-tracking and HR-tech vendors use unified APIs like Merge, Kombo, or Knit to onboard customers running BambooHR, Workday, ADP, and Greenhouse against a single normalized employee model.
  name: Unified HRIS and ATS Sync
- description: Analytics and data teams use Fivetran, Airbyte, or Stitch to land Stripe, Salesforce, HubSpot, NetSuite, and PostgreSQL data into Snowflake, BigQuery, or Redshift on managed schedules.
  name: SaaS-to-Warehouse Data Replication
- description: Data teams use Hightouch, Census, or Polytomic to push warehouse-modeled customer segments back into Salesforce, HubSpot, Braze, and Intercom so go-to-market teams act on consistent definitions.
  name: Reverse ETL for Customer 360
- description: Operations and revenue-ops teams use Zapier, Make, n8n, or Pabbly Connect to glue together calendars, forms, CRMs, and Slack channels without writing code.
  name: Citizen-Developer Workflow Automation
- description: Platform teams use n8n, Pipedream, Trigger.dev, Prefect, or Dagster to orchestrate event-driven internal workflows that span webhooks, queues, databases, and AI calls.
  name: Event-Driven Internal Pipelines
- description: Large enterprises use Boomi, MuleSoft, Informatica, SnapLogic, and TIBCO to connect ERP, CRM, on-premise databases, and message buses with governance, monitoring, and SLAs.
  name: Enterprise Application Integration
- description: AI-application teams use integration platforms and unified APIs to expose hundreds of SaaS actions as governed tools that agents can invoke with managed credentials and audit logs.
  name: AI Agent Tool and Action Integration
website: https://apievangelist.com
---
