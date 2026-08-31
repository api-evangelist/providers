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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: E2Open Agentic Access
  operation_count: 9
  slug: e2open-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
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
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: INTTRA Ocean Execution API (e2open) Bookings API
  slug: open-e2open-bookings-api
- collection_type: open
  name: INTTRA Ocean Execution API (e2open) Bookings Schedules API
  slug: open-e2open-schedules-api
- collection_type: open
  name: INTTRA Ocean Execution API (e2open) Bookings Shipping Instructions API
  slug: open-e2open-shipping-instructions-api
- collection_type: open
  name: INTTRA Ocean Execution API (e2open) Bookings Tracking API
  slug: open-e2open-tracking-api
- collection_type: open
  name: INTTRA Ocean Execution API (e2open)
  slug: open-inttra-ocean-execution
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/e2open-capability-edges.yml
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


  e2open''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, and 12 more developer resources.'
plans:
- name: E2Open Plans Pricing
  plan_count: 3
  slug: e2open-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: E2Open Rate Limits
  slug: e2open-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: e2open API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: e2open-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 67.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 62.2
    developer_ergonomics: 54.8
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
