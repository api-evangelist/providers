---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apipark Agentic Access
  operation_count: 5
  slug: apipark-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: The AI Models API from APIPark — 1 operation(s) for ai models.
  name: APIPark AI Models API
  slug: apipark-ai-models-api
- description: The Services API from APIPark — 1 operation(s) for services.
  name: APIPark Services API
  slug: apipark-services-api
- description: The Subscriptions API from APIPark — 1 operation(s) for subscriptions.
  name: APIPark Subscriptions API
  slug: apipark-subscriptions-api
- description: The Teams API from APIPark — 1 operation(s) for teams.
  name: APIPark Teams API
  slug: apipark-teams-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: APIPark AI Models API
  slug: open-apipark-ai-models-api
- collection_type: open
  name: APIPark AI Models Services API
  slug: open-apipark-services-api
- collection_type: open
  name: APIPark AI Models Subscriptions API
  slug: open-apipark-subscriptions-api
- collection_type: open
  name: APIPark AI Models Teams API
  slug: open-apipark-teams-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/APIParkLab/APIPark/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/APIParkLab/APIPark/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/APIParkLab/APIPark/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apipark-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apipark-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apipark-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apipark
- group: company
  title: ''
  type: Website
  url: https://apipark.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apipark.com/docs/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/APIParkLab
- group: company
  title: ''
  type: Blog
  url: https://apipark.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.apipark.com/docs/release
created: '2025-03-01'
description: APIPark is an open-source, cloud-native AI gateway and API developer portal that helps developers and enterprises manage, integrate, and deploy AI and API services. It supports 100+ AI models from all major AI providers, provides API lifecycle management, authentication, rate limiting, and cluster deployment for large-scale traffic. Teams can combine AI models with custom prompts to create new AI-powered services such as sentiment analysis, translation, or data analysis.
examples:
- key_count: 5
  name: Apipark Ai Model Example
  slug: apipark-ai-model-example
- key_count: 7
  name: Apipark Service Example
  slug: apipark-service-example
features:
- description: Unified AI gateway supporting 100+ AI models from OpenAI, Anthropic, Google, Meta, Mistral, and other major providers.
  name: AI Gateway
- description: Combine AI models with custom system prompts to create new API services for specific use cases.
  name: Prompt Engineering
- description: Full-featured developer portal for publishing, discovering, and subscribing to API services.
  name: API Developer Portal
- description: Team-based multi-tenancy for separating API services and subscriptions across organizational units.
  name: Multi-Tenant Teams
- description: Complete API lifecycle from service creation through publication, subscription, and deprecation.
  name: API Lifecycle Management
- description: Built-in API key authentication, rate limiting, and traffic management for all published services.
  name: Rate Limiting and Authentication
- description: Cloud-native cluster deployment supporting large-scale production traffic with high availability.
  name: Cluster Deployment
finops:
- name: Apipark Finops
  service_category: API
  slug: apipark-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apipark.png
json_schemas:
- name: APIPark AI Model
  property_count: 5
  slug: apipark-ai-model
- name: APIPark Service
  property_count: 7
  slug: apipark-service
json_structures:
- name: Apipark Ai Model Structure
  property_count: 5
  slug: apipark-ai-model-structure
- name: Apipark Service Structure
  property_count: 7
  slug: apipark-service-structure
jsonld:
- class_count: 13
  name: Apipark Context
  property_count: 1
  slug: apipark-context
layout: provider
modified: '2026-05-19'
name: APIPark
nav: Providers
network: true
overview: 'APIPark publishes 4 APIs on the [APIs.io](https://apis.io/) network, including AI Models API, Services API, Subscriptions API, and 1 more. Tagged areas include AI Gateway, API Gateway, API Management, Developer Portal, and LLM.


  The APIPark catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIPark''s developer surface includes authentication, documentation, engineering blog, changelog, and 8 more developer resources.'
plans:
- name: Apipark Plans Pricing
  plan_count: 3
  slug: apipark-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Apipark Rate Limits
  slug: apipark-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: APIPark API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apipark-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 64.6
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apipark/refs/heads/main/screenshots/apipark-2026-06-20T172255.png
security:
- kind: authentication
  name: Apipark Authentication
  slug: apipark-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apipark Domain Security
  slug: apipark-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apipark
solutions:
- description: Free, Apache 2.0 licensed self-hosted deployment for organizations with full control over infrastructure.
  name: Open Source
- description: Managed cloud deployment for teams who prefer not to manage infrastructure.
  name: Cloud
- description: Enterprise support, SLA guarantees, and professional services for large-scale deployments.
  name: Enterprise
tags:
- AI Gateway
- API Gateway
- API Management
- Developer Portal
- LLM
- Open-Source
use_cases:
- description: Standardize access to 100+ AI models through a unified API interface, enabling model switching without code changes.
  name: AI API Standardization
- description: Combine AI models with custom prompts to create specialized AI-powered APIs for specific domains.
  name: AI Service Creation
- description: Govern AI model access, usage costs, and rate limits across multiple teams from a centralized portal.
  name: Enterprise AI Governance
- description: Build an internal API marketplace for teams to discover and subscribe to AI and traditional API services.
  name: Internal API Marketplace
website: https://apipark.com/
---
