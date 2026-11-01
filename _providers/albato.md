---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Albato Agentic Access
  operation_count: 18
  slug: albato-agentic-access
  summary_line: 18 operations · 10 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://albato.com/api/v1
  baseurl_source: declared
  description: Manage automation workflows
  name: Albato Automations API
  slug: albato-automations-api
- baseURL: https://albato.com/api/v1
  baseurl_source: declared
  description: Manage app connectors
  name: Albato Connectors API
  slug: albato-connectors-api
- baseURL: https://albato.com/api/v1
  baseurl_source: declared
  description: Monitor automation execution history
  name: Albato Executions API
  slug: albato-executions-api
- baseURL: https://albato.com/api/v1
  baseurl_source: declared
  description: Manage embedded teams (customer accounts)
  name: Albato Teams API
  slug: albato-teams-api
- baseURL: https://albato.com/api/v1
  baseurl_source: declared
  description: Manage automation templates
  name: Albato Templates API
  slug: albato-templates-api
- baseURL: https://albato.com/api/v1
  baseurl_source: declared
  description: Manage team users
  name: Albato Users API
  slug: albato-users-api
artifact_total: 72
collections:
- collection_type: postman
  name: Albato Automations API
  slug: postman-albato-automations-api
- collection_type: postman
  name: Albato Automations Connectors API
  slug: postman-albato-connectors-api
- collection_type: postman
  name: Albato Automations Executions API
  slug: postman-albato-executions-api
- collection_type: postman
  name: Albato Automations Teams API
  slug: postman-albato-teams-api
- collection_type: postman
  name: Albato Automations Templates API
  slug: postman-albato-templates-api
- collection_type: postman
  name: Albato Automations Users API
  slug: postman-albato-users-api
- collection_type: open
  name: Albato Automations API
  slug: open-albato-automations-api
- collection_type: open
  name: Albato Automations Connectors API
  slug: open-albato-connectors-api
- collection_type: open
  name: Albato Automations Executions API
  slug: open-albato-executions-api
- collection_type: open
  name: Albato Automations Teams API
  slug: open-albato-teams-api
- collection_type: open
  name: Albato Automations Templates API
  slug: open-albato-templates-api
- collection_type: open
  name: Albato Automations Users API
  slug: open-albato-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/albato/plans/albato-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/albato-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/albato/rate-limits/albato-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/albato-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/albato/finops/albato-finops.yml
  title: ''
  type: FinOps
  url: finops/albato-finops.yml
- group: other
  href: https://artifacts.apis.io/albato/overlays/albato-automations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/albato-automations-overlay.yaml
- group: build
  href: https://artifacts.apis.io/albato/packages/albato-packages.yml
  title: ''
  type: Packages
  url: packages/albato-packages.yml
- group: agent
  href: https://artifacts.apis.io/albato/well-known/albato-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/albato-well-known.yml
- group: agent
  href: https://artifacts.apis.io/albato/mcp/albato-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/albato-mcp.yml
- group: design
  href: https://artifacts.apis.io/albato/conformance/albato-conformance.yml
  title: ''
  type: Conformance
  url: conformance/albato-conformance.yml
- group: design
  href: https://artifacts.apis.io/albato/errors/albato-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/albato-problem-types.yml
- group: design
  href: https://artifacts.apis.io/albato/lifecycle/albato-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/albato-lifecycle.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/albato/overview
- group: agent
  href: https://artifacts.apis.io/albato/agentic-access/albato-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/albato-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/albato/security/albato-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/albato-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/albato/security/albato-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/albato-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/albato/authentication/albato-authentication.yml
  title: ''
  type: Authentication
  url: authentication/albato-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/albato
- group: company
  title: ''
  type: Website
  url: https://albato.com
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.albato.com/en
- group: start
  title: Albato Embedded iPaaS
  type: GettingStarted
  url: https://albato.com/embedded
- group: commercial
  title: ''
  type: Pricing
  url: https://albato.com/pricing
- group: commercial
  title: Albato Embedded Pricing
  type: Pricing
  url: https://albato.com/embedded/pricing
- group: company
  title: ''
  type: Blog
  url: https://albato.com/blog/all
- group: other
  title: ''
  type: CaseStudies
  url: https://albato.com/blog/case-studies
- group: operate
  title: ''
  type: FAQ
  url: https://wiki.albato.com/en/collections/8343168-faq
- group: other
  title: ''
  type: Licensing
  url: https://albato.com/license
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://albato.com/privacy
- group: company
  title: ''
  type: FacebookGroup
  url: https://www.facebook.com/groups/albatocommunity
- group: operate
  title: ''
  type: RoadMap
  url: https://roadmap.albato.com/public
- group: design
  href: https://artifacts.apis.io/albato/rules/albato-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/albato-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/albato/vocabulary/albato-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/albato-vocabulary.yaml
- group: design
  href: https://artifacts.apis.io/albato/json-ld/albato-albato-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/albato-albato-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://albato.com/llms.txt
created: '2025-06-06'
description: Albato is a no-code automation platform and embedded iPaaS that enables businesses to automate workflows by connecting 1,000+ apps without writing code. Supports multi-step automations with triggers, actions, conditions, and delays. Albato Embedded allows SaaS companies to offer white-label native integrations to their customers.
examples:
- key_count: 9
  name: Albato Albato Automations Automation Example
  slug: albato-albato-automations-automation-example
- key_count: 4
  name: Albato Albato Automations Automation Step Example
  slug: albato-albato-automations-automation-step-example
- key_count: 7
  name: Albato Albato Automations Execution Example
  slug: albato-albato-automations-execution-example
- key_count: 7
  name: Albato Albato Embedded Connector Example
  slug: albato-albato-embedded-connector-example
- key_count: 7
  name: Albato Albato Embedded Team Example
  slug: albato-albato-embedded-team-example
- key_count: 5
  name: Albato Albato Embedded Template Example
  slug: albato-albato-embedded-template-example
- key_count: 6
  name: Albato Albato Embedded User Example
  slug: albato-albato-embedded-user-example
features:
- description: Visual automation builder for creating multi-step workflows connecting 1,000+ apps without writing code, with conditions, delays, and data transformations.
  name: No-Code Automation Builder
- description: Pre-built connectors for CRM, marketing, e-commerce, communication, and productivity apps including HubSpot, Salesforce, Google Workspace, Slack, Shopify, and more.
  name: 1,000+ App Integrations
- description: White-label integration platform for SaaS companies to embed Albato's automation capabilities natively in their products with full branding control.
  name: Albato Embedded iPaaS
- description: Support for complex automations with sequential and conditional steps, delays, loops, and data transformations without coding.
  name: Multi-Step Workflows
- description: Webhook-based real-time triggers for instant event processing and scheduled polling triggers for API-based app integrations.
  name: Real-Time and Scheduled Triggers
- description: Build custom API connectors from any REST API using the App Integrator without development handoff, supporting all major auth methods.
  name: Custom App Integrator
- description: Detailed execution history with step-level logging, success/error rates, real-time notifications, and dashboard insights.
  name: Execution Monitoring
- description: Built-in data mapping, field transformation, and JavaScript code steps for processing data between connected apps.
  name: Data Transformation
finops:
- has_sources: true
  method: derived
  name: Albato Finops
  primary_unit: subscription
  service_category: ''
  slug: albato-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/albato.png
integrations:
- description: CRM and marketing automation for contact and deal management.
  name: HubSpot
- description: Enterprise CRM for sales pipeline and opportunity workflows.
  name: Salesforce
- description: Google Sheets, Gmail, Drive, Calendar, and Forms integrations.
  name: Google Workspace
- description: Team messaging integration for workflow notifications and alerts.
  name: Slack
- description: E-commerce integration for order, product, and customer automation.
  name: Shopify
- description: Payment processing integration for subscription and payment workflows.
  name: Stripe
- description: Workspace integration for task and project data synchronization.
  name: Notion
- description: Database integration for spreadsheet and grid data workflows.
  name: Airtable
json_schemas:
- name: Automation
  property_count: 9
  slug: albato-albato-automations-automation
- name: AutomationStep
  property_count: 4
  slug: albato-albato-automations-automation-step
- name: Execution
  property_count: 7
  slug: albato-albato-automations-execution
- name: Connector
  property_count: 7
  slug: albato-albato-embedded-connector
- name: Team
  property_count: 7
  slug: albato-albato-embedded-team
- name: Template
  property_count: 5
  slug: albato-albato-embedded-template
- name: User
  property_count: 6
  slug: albato-albato-embedded-user
json_structures:
- name: Albato Albato Automations Automation Step Structure
  property_count: 4
  slug: albato-albato-automations-automation-step-structure
- name: Albato Albato Automations Automation Structure
  property_count: 9
  slug: albato-albato-automations-automation-structure
- name: Albato Albato Automations Execution Structure
  property_count: 7
  slug: albato-albato-automations-execution-structure
- name: Albato Albato Embedded Connector Structure
  property_count: 7
  slug: albato-albato-embedded-connector-structure
- name: Albato Albato Embedded Team Structure
  property_count: 7
  slug: albato-albato-embedded-team-structure
- name: Albato Albato Embedded Template Structure
  property_count: 5
  slug: albato-albato-embedded-template-structure
- name: Albato Albato Embedded User Structure
  property_count: 6
  slug: albato-albato-embedded-user-structure
jsonld:
- class_count: 0
  name: Albato Albato Context
  property_count: 36
  slug: albato-albato-context
layout: provider
mcp_servers:
- description: Remote MCP server over HTTP; 16 tools listed. A candidate, not confirmed as published by the provider.
  name: Albato MCP Server
  slug: albato
modified: '2026-05-19'
name: Albato
nav: Providers
network: true
overview: 'Albato publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Automations API, Connectors API, Executions API, and 3 more. Tagged areas include No-Code Automation, Workflow Automation, Embedded iPaaS, App Integration, and Integration.


  The Albato catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Albato''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, FAQ, and 26 more developer resources.'
plans:
- name: Albato Plans Pricing
  plan_count: 6
  slug: albato-plans-pricing
- name: Albato Price Estimates
  plan_count: 0
  slug: albato-price-estimates
random_paper: 3
rate_limits:
- limit_count: 5
  name: Albato Rate Limits
  slug: albato-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Albato — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: albato-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Albato API Rules
  rule_count: 31
  severity_counts:
    error: 16
    hint: 0
    info: 0
    warn: 15
  slug: albato-spectral-rules
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 81.0
    catalog_earned_first_party: 12.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 68.4
    contract_governance: 31.8
    contract_quality: 62.7
    developer_ergonomics: 36.9
    discoverability: 71.7
    operational_transparency: 13.2
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/albato/albato-2026-06-20T171504.png
security:
- kind: authentication
  name: Albato Authentication
  slug: albato-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Albato Domain Security
  slug: albato-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Albato Trust Center
  slug: albato-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: albato
tags:
- No-Code Automation
- Workflow Automation
- Embedded iPaaS
- App Integration
- Integration
- Webhook
- White Label
use_cases:
- description: Sync leads between CRM and marketing tools, automate email campaigns, and route prospects based on behavioral conditions.
  name: CRM and Marketing Automation
- description: Automate order notifications, inventory updates, fulfillment triggers, and customer communication across e-commerce platforms.
  name: E-Commerce Order Processing
- description: Use Albato Embedded to offer customers white-labeled integrations in your SaaS product without in-house iPaaS development.
  name: SaaS Native Integration Delivery
- description: Route tickets, trigger alerts, and sync customer data between helpdesk, CRM, and communication platforms automatically.
  name: Customer Support Automation
- description: Keep data consistent across business systems with bidirectional syncs, scheduled automations, and event-driven updates.
  name: Data Synchronization
website: https://albato.com
---
