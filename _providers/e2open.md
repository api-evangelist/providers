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
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: E2Open Agentic Access
  operation_count: 9
  slug: e2open-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 6
apis:
- description: E2open supply chain platform APIs enable supply chain event management, transportation management, customs compliance, and end-to-end shipment visibility. The platform supports REST/JSON, XML, and EDI
  name: E2open Supply Chain Platform API
  slug: e2open-supply-chain-api
- description: E2open Transportation Management API provides appointment scheduling, carrier integration, and real-time rating capabilities. REST endpoints allow carriers to POST documents, retrieve current rates, m
  name: E2open Transportation Management API
  slug: e2open-transportation-management-api
- description: Ocean shipping booking management
  name: e2open Bookings API
  slug: e2open-bookings-api
- description: Ocean carrier schedule lookup
  name: e2open Schedules API
  slug: e2open-schedules-api
- description: Bill of lading shipping instructions
  name: e2open Shipping Instructions API
  slug: e2open-shipping-instructions-api
- description: Container and shipment tracking
  name: e2open Tracking API
  slug: e2open-tracking-api
artifact_total: 17
collections:
- collection_type: open
  name: INTTRA Ocean Execution API (e2open)
  slug: open-inttra-ocean-execution
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/e2open-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/e2open-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/e2open-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/e2open-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/e2open
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/e2open
- group: company
  title: ''
  type: Website
  url: https://www.e2open.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/openapi/inttra-ocean-execution-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/json-schema/e2open-shipment-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/json-ld/e2open-context.jsonld
- group: start
  title: ''
  type: Portal
  url: https://apidocs.inttra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.e2open.com/e2open-network-connectivity/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.e2open.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inttra.com/legal/
- group: start
  title: ''
  type: GettingStarted
  url: https://marketplace.e2open.com/
- group: operate
  title: ''
  type: Support
  url: https://knowledge.e2open.com/knowledgecenter/inttra-resources/
description: Supply chain software with a connected network and SaaS platform help you seize opportunities, predict disruptions, and drive efficiency and sustainability.
finops:
- name: E2Open Finops
  service_category: Supply Chain
  slug: e2open-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/e2open.png
json_schemas:
- name: e2open / INTTRA Ocean Shipment
  property_count: 19
  slug: e2open-shipment
jsonld:
- class_count: 4
  name: E2Open Context
  property_count: 28
  slug: e2open-context
layout: provider
modified: '2026-05-19'
name: e2open
nav: Providers
network: true
overview: 'e2open publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Schedules API, Shipping Instructions API, and 1 more.


  The e2open catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  e2open''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, and 11 more developer resources.'
plans:
- name: E2Open Plans Pricing
  plan_count: 3
  slug: e2open-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 3
  name: E2Open Rate Limits
  slug: e2open-rate-limits
rules:
- name: e2open API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: e2open-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.9
  delta: -3.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.9
    developer_ergonomics: 43.5
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 58.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/screenshots/e2open-2026-06-20T180355.png
security:
- kind: authentication
  name: E2Open Authentication
  slug: e2open-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: E2Open Domain Security
  slug: e2open-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: E2Open Vulnerability Disclosure
  slug: e2open-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: e2open
website: https://www.e2open.com/
---
