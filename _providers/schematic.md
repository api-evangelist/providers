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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 97
  human_in_the_loop: 3
  name: Schematic Agentic Access
  operation_count: 218
  slug: schematic-agentic-access
  summary_line: 218 operations · 97 acting · 3 human-in-the-loop
api_count: 20
apis:
- description: The accesstokens API from Schematic — 1 operation(s) for accesstokens.
  name: Schematic accesstokens API
  slug: schematic-accesstokens-api
- description: The accounts API from Schematic — 12 operation(s) for accounts.
  name: Schematic accounts API
  slug: schematic-accounts-api
- description: The billing API from Schematic — 17 operation(s) for billing.
  name: Schematic billing API
  slug: schematic-billing-api
- description: The checkout API from Schematic — 7 operation(s) for checkout.
  name: Schematic checkout API
  slug: schematic-checkout-api
- description: The companies API from Schematic — 29 operation(s) for companies.
  name: Schematic companies API
  slug: schematic-companies-api
- description: The components API from Schematic — 4 operation(s) for components.
  name: Schematic components API
  slug: schematic-components-api
- description: The componentspublic API from Schematic — 1 operation(s) for componentspublic.
  name: Schematic componentspublic API
  slug: schematic-componentspublic-api
- description: The credits API from Schematic — 20 operation(s) for credits.
  name: Schematic credits API
  slug: schematic-credits-api
- description: The dataexports API from Schematic — 2 operation(s) for dataexports.
  name: Schematic dataexports API
  slug: schematic-dataexports-api
- description: The entitlements API from Schematic — 16 operation(s) for entitlements.
  name: Schematic entitlements API
  slug: schematic-entitlements-api
- description: The events API from Schematic — 5 operation(s) for events.
  name: Schematic events API
  slug: schematic-events-api
- description: The features API from Schematic — 11 operation(s) for features.
  name: Schematic features API
  slug: schematic-features-api
- description: The insights API from Schematic — 6 operation(s) for insights.
  name: Schematic insights API
  slug: schematic-insights-api
- description: The integrationsapi API from Schematic — 6 operation(s) for integrationsapi.
  name: Schematic integrationsapi API
  slug: schematic-integrationsapi-api
- description: The planbundle API from Schematic — 2 operation(s) for planbundle.
  name: Schematic planbundle API
  slug: schematic-planbundle-api
- description: The plangroups API from Schematic — 2 operation(s) for plangroups.
  name: Schematic plangroups API
  slug: schematic-plangroups-api
- description: The planmigrations API from Schematic — 5 operation(s) for planmigrations.
  name: Schematic planmigrations API
  slug: schematic-planmigrations-api
- description: The plans API from Schematic — 14 operation(s) for plans.
  name: Schematic plans API
  slug: schematic-plans-api
- description: The scheduledcheckout API from Schematic — 2 operation(s) for scheduledcheckout.
  name: Schematic scheduledcheckout API
  slug: schematic-scheduledcheckout-api
- description: The webhooks API from Schematic — 6 operation(s) for webhooks.
  name: Schematic webhooks API
  slug: schematic-webhooks-api
artifact_total: 39
collections:
- collection_type: open
  name: Schematic API
  slug: open-schematic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/schematic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schematic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/schematic-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://schematichq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.schematichq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.schematichq.com/api-reference
- group: company
  title: ''
  type: Blog
  url: https://schematichq.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SchematicHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/schematichq
- group: commercial
  title: ''
  type: Pricing
  url: https://schematichq.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://schematichq.com/changelog
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/vocabulary/schematic-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/examples/schematic-check-flag-example.json
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/SchematicHQ/schematic-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.schematichq.com/llms.txt
created: '2026-03-27'
description: Schematic is a feature and entitlement management platform for SaaS companies, providing pricing, packaging, and metering capabilities. It enables engineering and product teams to manage feature flags, define subscription plans, track feature usage, and control customer entitlements without code changes. Schematic raised $6.5M in April 2026 and launched an official Stripe App for entitlement management as a first-class billing primitive. Customers include Plotly, Automox, Florence, Blackcloak, Sema4.ai, and Pagos.
examples:
- key_count: 10
  name: Schematic Check Flag Example
  slug: schematic-check-flag-example
- key_count: 10
  name: Schematic Create Plan Example
  slug: schematic-create-plan-example
- key_count: 10
  name: Schematic Track Event Example
  slug: schematic-track-event-example
- key_count: 10
  name: Schematic Upsert Company Example
  slug: schematic-upsert-company-example
finops:
- name: Schematic Finops
  service_category: API
  slug: schematic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/schematic.png
json_schemas:
- name: Schematic Company
  property_count: 10
  slug: schematic-company
- name: Schematic Feature
  property_count: 7
  slug: schematic-feature
- name: Schematic Plan
  property_count: 11
  slug: schematic-plan
json_structures:
- name: Schematic Api Structure
  property_count: 0
  slug: schematic-api-structure
jsonld:
- class_count: 29
  name: Schematic Context
  property_count: 4
  slug: schematic-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Schematic
nav: Providers
network: true
overview: 'Schematic publishes 20 APIs on the [APIs.io](https://apis.io/) network, including accesstokens API, accounts API, billing API, and 17 more. Tagged areas include Billing, Entitlements, Feature Flags, Feature Management, and FinOps.


  The Schematic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Schematic''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, changelog, code examples, and 8 more developer resources.'
plans:
- name: Schematic Plans Pricing
  plan_count: 3
  slug: schematic-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Schematic Rate Limits
  slug: schematic-rate-limits
rules:
- name: Schematic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: schematic-jsonschema-spectral-rules
- name: Schematic API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 8
  slug: schematic-rules
score:
  band: developing
  composite: 54.9
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.8
    developer_ergonomics: 37.0
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/screenshots/schematic-2026-06-20T193553.png
security:
- kind: authentication
  name: Schematic Authentication
  slug: schematic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Schematic Domain Security
  slug: schematic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: schematic
tags:
- Billing
- Entitlements
- Feature Flags
- Feature Management
- FinOps
- Metering
- Pricing
- SaaS
website: https://schematichq.com/
---
