---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Buildxact Agentic Access
  operation_count: 13
  slug: buildxact-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 5
apis:
- description: Buildxact's webhook surface lets partner and customer integrations receive real-time notifications when events occur inside the construction-management platform — including Estimate Accepted, Lead Cre
  name: Buildxact Webhooks
  slug: buildxact-webhooks
- description: First-party login and bearer token refresh.
  name: Buildxact Authentication API
  slug: buildxact-authentication-api
- description: Line items inside an estimate (materials, labor, assemblies).
  name: Buildxact Estimate Items API
  slug: buildxact-estimate-items-api
- description: Construction estimates — the top-level pricing document for a job.
  name: Buildxact Estimates API
  slug: buildxact-estimates-api
- description: Tax rates and inclusivity rules applied to estimate totals.
  name: Buildxact Tax Context API
  slug: buildxact-tax-context-api
artifact_total: 22
asyncapis:
- description: Buildxact webhook delivery channel. Subscribers register a target URL inside the Buildxact web app ("My Business > API"), pick the events they want, and verify each payload with a signing secret. Some
  name: Buildxact Webhooks
  slug: buildxact-webhooks-asyncapi
collections:
- collection_type: open
  name: Buildxact Public API
  slug: open-buildxact-public-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/buildxact-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/buildxact-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buildxact-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buildxact-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.buildxact.com
- group: other
  title: ''
  type: AustraliaSite
  url: https://www.buildxact.com/au/
- group: other
  title: ''
  type: USSite
  url: https://www.buildxact.com/us/
- group: other
  title: ''
  type: UKSite
  url: https://www.buildxact.com/uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.buildxact.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.buildxact.com
- group: operate
  title: ''
  type: APIHelpArticle
  url: https://help.buildxact.com/en/articles/4510284-buildxact-application-programming-interface-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buildxact.com/us/pricing/
- group: commercial
  title: ''
  type: Plans
  url: https://help.buildxact.com/en/articles/11559145-which-buildxact-subscription-plan-is-right-for-my-business
- group: build
  title: ''
  type: AccountingIntegrations
  url: https://www.buildxact.com/us/features/construction-accounting-software/
- group: other
  title: ''
  type: BluAI
  url: https://www.buildxact.com/us/features/blu/
- group: other
  title: ''
  type: Company
  url: https://www.buildxact.com/au/company/
- group: company
  title: ''
  type: Blog
  url: https://www.buildxact.com/us/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.buildxact.com/us/contact/
- group: start
  title: ''
  type: Trial
  url: https://www.buildxact.com/us/free-trial/
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/buildxact
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Buildxact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buildxact.com/au/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buildxact.com/au/privacy-policy/
created: '2026-05-25'
description: Buildxact is a Melbourne, Australia-headquartered construction estimating and project management SaaS for residential builders, remodelers, trade contractors, and building-material suppliers. Founded in 2011, the company operates regional offices in Austin, Texas (North America), and serves customers across Australia, New Zealand, the United Kingdom, the United States, and Canada. The platform spans the full residential job lifecycle — lead capture, digital takeoffs, AI-assisted estimating ("Blu"), customer quoting and e-signatures, supplier/dealer price-list integration, purchase orders, scheduling (Gantt), timesheets, variations/change orders, invoicing, and two-way accounting sync with Xero and QuickBooks Online. Buildxact exposes a public REST API and webhook surface at developer.buildxact.com, available to Merchant and Manufacturer partners as well as customer subscribers, using a Microsoft Azure API Management gateway (Ocp-Apim-Subscription-Key + bearer token). Endpoints
  support OData filtering and sorting, with a separate UAT/staging environment. In 2024, Autodesk announced an agreement to acquire Buildxact, positioning the product as a residential construction front-end alongside Autodesk's broader AEC portfolio.
examples:
- key_count: 3
  name: Buildxact Estimate Accepted Event Example
  slug: buildxact-estimate-accepted-event-example
- key_count: 3
  name: Buildxact List Estimates Example
  slug: buildxact-list-estimates-example
finops:
- name: Buildxact Finops
  service_category: Construction Management Software
  slug: buildxact-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buildxact.png
json_schemas:
- name: Buildxact Estimate Item
  property_count: 12
  slug: buildxact-estimate-item
- name: Buildxact Estimate
  property_count: 14
  slug: buildxact-estimate
jsonld:
- class_count: 0
  name: Buildxact Context
  property_count: 5
  slug: buildxact-context
layout: provider
modified: '2026-05-25'
name: Buildxact
nav: Providers
network: true
overview: 'Buildxact publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Authentication API, Estimate Items API, and 2 more. Tagged areas include Construction, Residential Construction, Construction Management, Estimating, and Takeoffs.


  The Buildxact catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Buildxact''s developer surface includes authentication, pricing, engineering blog, GitHub presence, and 19 more developer resources.'
plans:
- name: Buildxact Plans Pricing
  plan_count: 4
  slug: buildxact-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Buildxact Rate Limits
  slug: buildxact-rate-limits
rules:
- name: Buildxact API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: buildxact-asyncapi-spectral-rules
- name: Buildxact API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: buildxact-jsonschema-spectral-rules
- name: Buildxact API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: buildxact-rules
score:
  band: developing
  composite: 53.5
  delta: -3.5
  facets:
    commercial_clarity: 71.1
    contract_quality: 76.6
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buildxact/refs/heads/main/screenshots/buildxact-2026-06-20T173758.png
security:
- kind: authentication
  name: Buildxact Authentication
  slug: buildxact-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Buildxact Domain Security
  slug: buildxact-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Buildxact Vulnerability Disclosure
  slug: buildxact-vulnerability-disclosure
  summary_line: disclosure policy published
slug: buildxact
tags:
- Construction
- Residential Construction
- Construction Management
- Estimating
- Takeoffs
- Job Management
- Project Management
- Quoting
- Scheduling
- Purchase Orders
- Invoicing
- Supplier Integration
- Material Pricing
- Builders
- Remodelers
- Trades
- SaaS
- Australia
- Autodesk
website: https://www.buildxact.com
---
