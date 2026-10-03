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
artifact_total: 31
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
description: An index and topic collection covering full-stack API management platforms — solutions that combine an API gateway, developer portal, analytics, monetization, governance, and lifecycle tooling into a unified product. API management platforms sit between API providers and consumers, enforcing security and rate limiting at the gateway, publishing APIs through developer portals, instrumenting traffic for analytics and billing, and supporting design, versioning, deprecation, and policy enforcement across the entire API lifecycle. This collection includes commercial leaders like Apigee, Kong, MuleSoft Anypoint, IBM API Connect, Axway Amplify, Microsoft Azure API Management, AWS API Gateway, and Google Cloud API Gateway, alongside open-source platforms like WSO2, Tyk, Gravitee, KrakenD, and 3scale by Red Hat, plus modern entrants like Zuplo, APIwiz, APIPark, and Apidog.
examples:
- key_count: 12
  name: Management Api Product Example
  slug: management-api-product-example
- key_count: 11
  name: Management Subscription Plan Example
  slug: management-subscription-plan-example
features:
- description: Full-stack management platforms front APIs with a configurable gateway that enforces authentication, rate limiting, quotas, transformation, and routing policies at runtime.
  name: API Gateway and Traffic Control
- description: Management platforms include developer portals where API providers publish documentation, onboard consumers, issue keys, manage applications, and support self-service signup.
  name: Developer Portal Publishing
- description: Platforms support the full API lifecycle including design, version control, environment promotion, deprecation workflows, and retirement across multiple gateway runtimes.
  name: API Lifecycle Management
- description: Built-in analytics dashboards capture traffic volume, latency, error rates, top consumers, top endpoints, and SLA compliance, surfacing business and operational health.
  name: Analytics and Reporting
- description: API management platforms enable subscription plans, usage-based pricing, quotas, and developer billing, turning APIs into revenue-generating products.
  name: Monetization and Billing
- description: Centralized policy catalogs enforce security, schema validation, PII redaction, and organizational standards across all managed APIs, supporting enterprise governance programs.
  name: Policy and Governance Enforcement
- description: Modern management platforms federate multiple gateway runtimes across clouds, regions, and on-prem environments under a unified control plane and policy model.
  name: Multi-Gateway and Multi-Cloud Federation
- description: API catalogs within the management platform make APIs discoverable to internal teams and external consumers, with search, tagging, ownership, and lineage.
  name: Catalog and Discovery
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Google Cloud Apigee API management platform providing gateway, developer portal, analytics, monetization, and policy enforcement.
  name: Apigee
- description: Kong Konnect and Kong Gateway providing a full API management platform with developer portal, analytics, plugin ecosystem, and multi-runtime federation.
  name: Kong
- description: MuleSoft Anypoint Platform combining API design, gateway, developer portal, analytics, and integration runtime for enterprise API management.
  name: MuleSoft Anypoint
- description: IBM API Connect providing API design, gateway runtime, developer portal, analytics, and governance for hybrid and multi-cloud deployments.
  name: IBM API Connect
- description: Axway Amplify API management platform with federation across multiple gateway runtimes, marketplace, and centralized governance.
  name: Axway Amplify
- description: Open-source WSO2 API Manager providing gateway, developer portal, analytics, and lifecycle management for on-premise and cloud deployments.
  name: WSO2 API Manager
- description: Open-source Tyk API gateway and management platform with developer portal, analytics, multi-tenant operator, and self-managed or SaaS deployment.
  name: Tyk
- description: Azure API Management providing gateway, developer portal, analytics, and policy enforcement integrated with the Azure cloud ecosystem.
  name: Microsoft Azure API Management
json_schemas:
- name: APIProduct
  property_count: 12
  slug: management-api-product
- name: SubscriptionPlan
  property_count: 11
  slug: management-subscription-plan
json_structures:
- name: Management Api Product Structure
  property_count: 12
  slug: management-api-product-structure
- name: Management Subscription Plan Structure
  property_count: 11
  slug: management-subscription-plan-structure
jsonld:
- class_count: 11
  name: Management Context
  property_count: 17
  slug: management-context
layout: provider
modified: '2026-05-19'
name: Management
nav: Providers
network: true
overview: 'Management is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API Management, API Lifecycle, Developer Portal, API Analytics, and API Governance.


  The Management catalog on APIs.io includes 1 JSON-LD context.


  Management''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 19
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
slug: management
tags:
- API Management
- API Lifecycle
- Developer Portal
- API Analytics
- API Governance
use_cases:
- description: Product teams use API management platforms to publish public APIs with documentation, signup, key management, rate limits, and subscription plans through a branded developer portal.
  name: Public API Product Launch
- description: Platform engineering teams centralize internal API governance — registering services, enforcing security policies, instrumenting traffic, and providing self-service onboarding for product teams.
  name: Internal Platform API Governance
- description: Companies monetize APIs through subscription tiers, metered usage, and partner programs, billing customers through built-in management platform features.
  name: API Monetization
- description: Enterprises front legacy SOAP, ESB, or mainframe systems with managed REST and GraphQL APIs, exposing modern interfaces while applying security, transformation, and analytics through the gateway.
  name: Legacy System Modernization
- description: B2B providers use developer portals and subscription plans to onboard partners, issue keys, enforce contractual SLAs, and track usage across enterprise integrations.
  name: Partner and B2B API Distribution
- description: Organizations operating across AWS, Azure, and Google Cloud federate gateway runtimes under a unified policy and observability layer to maintain consistent governance.
  name: Multi-Cloud Gateway Federation
- description: Regulated industries use management platforms to enforce auditable policy controls — logging, encryption, PII handling — and to produce compliance reports for auditors.
  name: Compliance and Audit Reporting
- description: Enterprises productize internal capabilities by cataloging APIs, capturing ownership and SLAs, and enabling discovery across product teams through the management portal.
  name: API Productization and Catalog Discovery
website: https://apievangelist.com
---
