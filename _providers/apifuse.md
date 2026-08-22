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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apifuse Agentic Access
  operation_count: 7
  slug: apifuse-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 5
apis:
- description: Integration usage analytics and monitoring.
  name: Apifuse Analytics API
  slug: apifuse-analytics-api
- description: Available connectors and their configurations.
  name: Apifuse Connectors API
  slug: apifuse-connectors-api
- description: Manage and configure embedded integrations.
  name: Apifuse Integrations API
  slug: apifuse-integrations-api
- description: User authentication and management.
  name: Apifuse Users API
  slug: apifuse-users-api
- description: Create and manage integration workflows.
  name: Apifuse Workflows API
  slug: apifuse-workflows-api
artifact_total: 51
collections:
- collection_type: postman
  name: Apifuse Analytics API
  slug: postman-apifuse-analytics-api
- collection_type: postman
  name: Apifuse Analytics Connectors API
  slug: postman-apifuse-connectors-api
- collection_type: postman
  name: Apifuse Analytics Integrations API
  slug: postman-apifuse-integrations-api
- collection_type: postman
  name: Apifuse Analytics Users API
  slug: postman-apifuse-users-api
- collection_type: postman
  name: Apifuse Analytics Workflows API
  slug: postman-apifuse-workflows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apifuse Analytics API
  slug: open-apifuse-analytics-api
- collection_type: open
  name: Apifuse Analytics Connectors API
  slug: open-apifuse-connectors-api
- collection_type: open
  name: Apifuse Analytics Integrations API
  slug: open-apifuse-integrations-api
- collection_type: open
  name: Apifuse Analytics Users API
  slug: open-apifuse-users-api
- collection_type: open
  name: Apifuse Analytics Workflows API
  slug: open-apifuse-workflows-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apifuse/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apifuse-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apifuse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apifuse-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/api-fuse
- group: company
  title: ''
  type: Website
  url: https://apifuse.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apifuse.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apifuse.io/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://apifuse.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://apifuse.io/blog
- group: start
  title: ''
  type: Signup
  url: https://app.apifuse.io/register
- group: start
  title: ''
  type: Login
  url: https://app.apifuse.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apifuse
created: '2026-03-16'
description: Apifuse is a native integration platform that enables SaaS companies to build and embed integrations directly into their products. It provides a white-label integration solution with pre-built connectors across 20+ categories, an embeddable UI, workflow automation, and analytics tools that help developers add native integrations without building from scratch.
examples:
- key_count: 4
  name: Apifuse Analytics Example
  slug: apifuse-analytics-example
- key_count: 4
  name: Apifuse Connector Example
  slug: apifuse-connector-example
- key_count: 5
  name: Apifuse Integration Example
  slug: apifuse-integration-example
- key_count: 4
  name: Apifuse Workflow Example
  slug: apifuse-workflow-example
features:
- description: Build a branded integration marketplace within your SaaS product, allowing customers to connect their preferred business tools.
  name: Embedded Integration Marketplace
- description: 150+ pre-built connectors across 20+ categories including CRM, Accounting, Email, Project Management, and more.
  name: Pre-Built Connectors
- description: Visual workflow builder with triggers (polling, realtime, scheduled, webhook) and steps (actions, conditionals, loops, delays, scripts).
  name: Workflow Builder
- description: Fully white-labeled integration UI that embeds seamlessly into your product's look and feel.
  name: White-Label Solution
- description: Build custom connectors for proprietary or internal systems using the Apifuse SDK.
  name: Custom Connector SDK
- description: Track integration usage, task counts, active users, and monitor workflow health in real time.
  name: Analytics and Monitoring
- description: Manage user OAuth connections, API keys, and integration authentication within your platform.
  name: User Authentication
finops:
- name: Apifuse Finops
  service_category: API
  slug: apifuse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apifuse.png
json_schemas:
- name: Analytics
  property_count: 4
  slug: apifuse-analytics
- name: Connector
  property_count: 4
  slug: apifuse-connector
- name: Integration
  property_count: 5
  slug: apifuse-integration
- name: Workflow
  property_count: 4
  slug: apifuse-workflow
json_structures:
- name: Apifuse Analytics Structure
  property_count: 4
  slug: apifuse-analytics-structure
- name: Apifuse Connector Structure
  property_count: 4
  slug: apifuse-connector-structure
- name: Apifuse Integration Structure
  property_count: 5
  slug: apifuse-integration-structure
- name: Apifuse Workflow Structure
  property_count: 4
  slug: apifuse-workflow-structure
jsonld:
- class_count: 6
  name: Apifuse Context
  property_count: 8
  slug: apifuse-context
layout: provider
modified: '2026-05-19'
name: Apifuse
nav: Providers
network: true
overview: 'Apifuse publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Connectors API, Integrations API, and 2 more. Tagged areas include Embedded Integrations, Integration Platform, Integrations, iPaaS, and Marketplace.


  The Apifuse catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apifuse''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Apifuse Plans Pricing
  plan_count: 3
  slug: apifuse-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Apifuse Rate Limits
  slug: apifuse-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apifuse API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apifuse-jsonschema-spectral-rules
- effective_rule_count: 60
  extends:
  - spectral:oas
  name: Apifuse API Rules
  rule_count: 19
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 14
  slug: apifuse-spectral-rules
score:
  band: thin
  composite: 29.2
  delta: -9.6
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 9.8
    contract_quality: 27.6
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apifuse/refs/heads/main/screenshots/apifuse-2026-06-20T172232.png
security:
- kind: authentication
  name: Apifuse Authentication
  slug: apifuse-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apifuse Domain Security
  slug: apifuse-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apifuse
solutions:
- description: Up to 500,000 tasks/month with 6 pre-built connectors for companies starting with embedded integrations.
  name: Growth Plan
- description: Up to 5,000,000 tasks/month with unlimited pre-built connectors for established SaaS companies.
  name: Platform Plan
- description: Custom task volume, fully managed integrations, and dedicated support for enterprise SaaS platforms.
  name: Enterprise Plan
tags:
- Embedded Integrations
- Integration Platform
- Integrations
- iPaaS
- Marketplace
- SaaS
- Workflow Automation
use_cases:
- description: Embed a branded integration marketplace into your SaaS product to let customers connect Salesforce, Mailchimp, DocuSign, and 150+ other tools.
  name: SaaS Integration Marketplace
- description: Allow customers to build no-code automation workflows between their connected apps and your platform.
  name: Workflow Automation
- description: Transform a product into a comprehensive platform by adding native integration capabilities without building each connector from scratch.
  name: Platform Expansion
- description: Keep customer data synchronized across CRM, marketing automation, and your platform in real time.
  name: Customer Data Sync
website: https://apifuse.io/
---
