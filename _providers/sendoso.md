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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sendoso Agentic Access
  operation_count: 10
  slug: sendoso-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 5
apis:
- description: Browse available gifts and products
  name: Sendoso Inventory API
  slug: sendoso-inventory-api
- description: Manage recipient contacts
  name: Sendoso Recipients API
  slug: sendoso-recipients-api
- description: Sending analytics and reports
  name: Sendoso Reports API
  slug: sendoso-reports-api
- description: Create and manage gift sends
  name: Sendoso Sends API
  slug: sendoso-sends-api
- description: Team and budget management
  name: Sendoso Teams API
  slug: sendoso-teams-api
artifact_total: 24
collections:
- collection_type: postman
  name: Sendoso Sending Platform Inventory API
  slug: postman-sendoso-inventory-api
- collection_type: postman
  name: Sendoso Sending Platform Inventory Recipients API
  slug: postman-sendoso-recipients-api
- collection_type: postman
  name: Sendoso Sending Platform Inventory Reports API
  slug: postman-sendoso-reports-api
- collection_type: postman
  name: Sendoso Sending Platform Inventory Sends API
  slug: postman-sendoso-sends-api
- collection_type: postman
  name: Sendoso Sending Platform Inventory Teams API
  slug: postman-sendoso-teams-api
- collection_type: open
  name: Sendoso Sending Platform API
  slug: open-sendoso-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sendoso/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sendoso-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendoso-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendoso-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendoso
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendoso
- group: company
  title: ''
  type: Website
  url: https://sendoso.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.sendoso.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sendoso.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.sendoso.com/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://sendoso.com/webhooks/
- group: company
  title: ''
  type: Blog
  url: https://sendoso.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://sendoso.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendoso.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendoso.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendoso.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/sendoso/main/openapi/sendoso-api-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/sendoso/main/rules/sendoso-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/sendoso/main/json-schema/sendoso-send-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/sendoso/main/json-structure/sendoso-send-structure.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/sendoso/main/examples/sendoso-create-send-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/sendoso/main/examples/sendoso-list-sends-example.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/sendoso/main/json-ld/sendoso-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/sendoso/main/vocabulary/sendoso-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.sendoso.com/llms.txt
created: '2026-05-02'
description: Sendoso is a corporate gifting and direct mail platform that enables sales, marketing, and customer success teams to send physical and digital gifts at scale. The Sendoso Sending Platform provides personalized gift sending, branded swag, e-gift cards, direct mail, and charitable donations. Sendoso integrates with Salesforce, HubSpot, Outreach, Marketo, and other CRM and sales engagement tools to automate gift-sending at scale.
examples:
- key_count: 2
  name: Sendoso Create Send Example
  slug: sendoso-create-send-example
- key_count: 2
  name: Sendoso List Sends Example
  slug: sendoso-list-sends-example
finops:
- name: Sendoso Finops
  service_category: API
  slug: sendoso-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendoso.png
json_schemas:
- name: Sendoso Send
  property_count: 14
  slug: sendoso-send
json_structures:
- name: Sendoso Send Structure
  property_count: 0
  slug: sendoso-send-structure
jsonld:
- class_count: 27
  name: Sendoso Context
  property_count: 5
  slug: sendoso-context
layout: provider
modified: '2026-05-02'
name: Sendoso
nav: Providers
network: true
overview: 'Sendoso publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Inventory API, Recipients API, Reports API, and 2 more. Tagged areas include Corporate Gifting, Direct Mail, Sales Engagement, Marketing Automation, and CRM Integration.


  The Sendoso catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sendoso''s developer surface includes authentication, developer portal, documentation, engineering blog, pricing, code examples, and 19 more developer resources.'
plans:
- name: Sendoso Plans Pricing
  plan_count: 3
  slug: sendoso-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Sendoso Rate Limits
  slug: sendoso-rate-limits
rules:
- name: Sendoso API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sendoso-jsonschema-spectral-rules
- name: Sendoso API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 2
  slug: sendoso-rules
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 66.9
    developer_ergonomics: 34.8
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendoso/refs/heads/main/screenshots/sendoso-2026-06-20T193656.png
security:
- kind: authentication
  name: Sendoso Authentication
  slug: sendoso-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sendoso Domain Security
  slug: sendoso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sendoso
tags:
- Corporate Gifting
- Direct Mail
- Sales Engagement
- Marketing Automation
- CRM Integration
website: https://sendoso.com/
---
