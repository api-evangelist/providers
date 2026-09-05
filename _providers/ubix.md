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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: The UBIX Insights API enables programmatic access to AI-generated analytics, insights, and model outputs from the UBIX platform. Supports integration with existing business intelligence tools, CRM sys
  name: UBIX Insights API
  slug: ubix-insights-api
- description: API for the UBIX DataSpace module enabling data ingestion, transformation, and management across enterprise data sources. Supports connecting to 80+ pre-built connectors including ERP systems, CRM pla
  name: UBIX DataSpace API
  slug: ubix-dataspace-api
- description: API for the UBIX ModelSpace module enabling programmatic management of AI/ML models including creation, training, versioning, and deployment. Supports no-code and API-driven model lifecycle management
  name: UBIX ModelSpace API
  slug: ubix-modelspace-api
- description: 'Conversational AI API enabling natural language interaction with enterprise data and AI models. Supports iterative data exploration, insight generation, and business question answering through a chat '
  name: UBIX ChatUBIX API
  slug: ubix-chatubix-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubix-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ubixlabs
- group: company
  title: ''
  type: Blog
  url: https://www.ubixlabs.com/blog/rss.xml
created: '2024-01-01'
description: UBIX Labs is a no-code, cloud-based AI platform designed to democratize artificial intelligence for business users. The platform provides end-to-end AI capabilities including data integration, model development, deployment, and conversational AI through modular components. UBIX offers over 80 pre-built connectors and an Insights API for seamless integration with existing enterprise systems across 12+ industry verticals.
finops:
- name: Ubix Finops
  service_category: API
  slug: ubix-finops
image: https://www.ubixlabs.com/favicon.ico
jsonld:
- class_count: 6
  name: Ubix Context
  property_count: 11
  slug: ubix-context
layout: provider
modified: '2026-05-03'
name: UBIX Labs
nav: Providers
network: true
overview: 'UBIX Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Machine-Learning, Data Integration, and No-Code.


  The UBIX Labs catalog on APIs.io includes 1 JSON-LD context.


  UBIX Labs'' developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Ubix Plans Pricing
  plan_count: 3
  slug: ubix-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Ubix Rate Limits
  slug: ubix-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 16.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 23.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ubix/refs/heads/main/screenshots/ubix-2026-06-20T195933.png
security:
- kind: domain-security
  name: Ubix Domain Security
  slug: ubix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ubix
tags:
- Artificial Intelligence
- Analytics
- Machine-Learning
- Data Integration
- No-Code
- Enterprise
- Generative AI
website: https://www.ubixlabs.com
---
