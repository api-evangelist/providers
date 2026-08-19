---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: State Farm Insurance Agentic Access
  operation_count: 5
  slug: state-farm-insurance-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 6
apis:
- description: The State Farm Auto Insurance API enables partners in automotive, telematics, and financial services to embed State Farm auto insurance products into their platforms. Use cases include in-dealership i
  name: Auto Insurance API
  slug: auto-insurance-api
- description: The State Farm Homeowners Insurance API enables mortgage lenders, real estate platforms, and partner networks to offer homeowners insurance quoting and policy integration. Supports closing day insuran
  name: Homeowners Insurance API
  slug: homeowners-insurance-api
- description: The State Farm B2B Insurance Inquiry API provides home and auto lenders with a programmatic way to verify that borrowers maintain adequate insurance coverage on financed properties and vehicles. Lende
  name: B2B Insurance Inquiry API
  slug: b2b-insurance-inquiry-api
- description: Coverage options and details
  name: State Farm Insurance Coverage API
  slug: state-farm-insurance-coverage-api
- description: Renters insurance policy operations
  name: State Farm Insurance Policies API
  slug: state-farm-insurance-policies-api
- description: Renters insurance quote operations
  name: State Farm Insurance Quotes API
  slug: state-farm-insurance-quotes-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: State Farm Insurance Renters Coverage API
  slug: open-state-farm-insurance-coverage-api
- collection_type: open
  name: State Farm Insurance Renters Coverage Policies API
  slug: open-state-farm-insurance-policies-api
- collection_type: open
  name: State Farm Insurance Renters Coverage Quotes API
  slug: open-state-farm-insurance-quotes-api
- collection_type: open
  name: State Farm Insurance Renters API
  slug: open-state-farm-insurance-renters
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/state-farm-insurance-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/state-farm-insurance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/state-farm-insurance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/state-farm-insurance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/state-farm-insurance-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.statefarm.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.statefarm.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/StateFarmIns
- group: company
  title: ''
  type: Engineering Blog
  url: https://engineering.statefarm.com/blog
- group: start
  title: ''
  type: B2B Portal
  url: https://b2b.statefarm.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/state-farm
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/StateFarm
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.statefarm.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.statefarm.com/customer-care/privacy-security/privacy/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.statefarm.com/customer-care/legal-disclaimer
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/state-farm-insurance-renters-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/state-farm-insurance-renters-policy-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/state-farm-insurance-renters-policy-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/state-farm-insurance-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/state-farm-insurance-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/state-farm-insurance-rules.yml
description: State Farm Insurance refers to the primary insurance operations of State Farm Mutual Automobile Insurance Company and its affiliated entities, headquartered in Bloomington, Illinois. As the largest property and casualty insurer in the United States, State Farm Insurance provides auto, home, renters, life, health, commercial, and farm insurance products to over 83 million policies across 91 million accounts. The company operates through approximately 19,000 exclusive agents and has a robust digital platform. State Farm Insurance maintains a Partner Gateway developer portal (developer.statefarm.com) offering APIs for embedded insurance, partner integrations, and B2B connectivity. The company has also heavily invested in cloud infrastructure on AWS and has open-sourced numerous DevOps and infrastructure tools via its GitHub organization.
examples:
- key_count: 2
  name: State Farm Insurance Create Renters Quote Example
  slug: state-farm-insurance-create-renters-quote-example
finops:
- name: State Farm Insurance Finops
  service_category: Insurance / Financial Services
  slug: state-farm-insurance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/state-farm-insurance.png
json_schemas:
- name: Renters Insurance Policy
  property_count: 9
  slug: state-farm-insurance-renters-policy
json_structures:
- name: State Farm Insurance Renters Policy Structure
  property_count: 0
  slug: state-farm-insurance-renters-policy-structure
jsonld:
- class_count: 11
  name: State Farm Insurance Context
  property_count: 8
  slug: state-farm-insurance-context
layout: provider
modified: '2026-05-19'
name: State Farm Insurance
nav: Providers
network: true
overview: 'State Farm Insurance publishes 3 APIs on the [APIs.io](https://apis.io/) network: Coverage API, Policies API, and Quotes API. Tagged areas include Fortune 100.


  The State Farm Insurance catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  State Farm Insurance''s developer surface includes authentication, GitHub presence, and 19 more developer resources.'
plans:
- name: State Farm Insurance Plans Pricing
  plan_count: 1
  slug: state-farm-insurance-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 1
  name: State Farm Insurance Rate Limits
  slug: state-farm-insurance-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: State Farm Insurance API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: state-farm-insurance-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: State Farm Insurance API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 5
  slug: state-farm-insurance-rules
scopes:
- name: State Farm Insurance Scopes
  scope_count: 3
  slug: state-farm-insurance-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 36.3
  delta: -6.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 25.0
    contract_quality: 63.4
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/state-farm-insurance/refs/heads/main/screenshots/state-farm-insurance-2026-06-20T194522.png
security:
- kind: authentication
  name: State Farm Insurance Authentication
  slug: state-farm-insurance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: State Farm Insurance Domain Security
  slug: state-farm-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: State Farm Insurance Vulnerability Disclosure
  slug: state-farm-insurance-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: state-farm-insurance
tags:
- Fortune 100
website: https://www.statefarm.com
---
