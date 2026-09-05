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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: State Farm Agentic Access
  operation_count: 5
  slug: state-farm-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: The State Farm Auto Insurance API supports partner integrations for automobile insurance quoting, policy management, and claims inquiry. This API enables auto dealers, telematics platforms, and financ
  name: Auto Insurance API
  slug: auto-insurance-api
- description: The State Farm B2B Insurance Inquiry API is designed for lenders, mortgage servicers, and financial institutions that need to verify homeowner and auto insurance policy status for collateral protectio
  name: B2B Insurance Inquiry API
  slug: b2b-insurance-inquiry-api
- baseURL: https://api.statefarm.com/v1
  baseurl_source: declared
  description: Coverage options and details
  name: State Farm Coverage API
  slug: state-farm-coverage-api
- baseURL: https://api.statefarm.com/v1
  baseurl_source: declared
  description: Renters insurance policy operations
  name: State Farm Policies API
  slug: state-farm-policies-api
- baseURL: https://api.statefarm.com/v1
  baseurl_source: declared
  description: Renters insurance quote operations
  name: State Farm Quotes API
  slug: state-farm-quotes-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: State Farm Renters Insurance Coverage API
  slug: open-state-farm-coverage-api
- collection_type: open
  name: State Farm Renters Insurance Coverage Policies API
  slug: open-state-farm-policies-api
- collection_type: open
  name: State Farm Renters Insurance Coverage Quotes API
  slug: open-state-farm-quotes-api
- collection_type: open
  name: State Farm Renters Insurance API
  slug: open-state-farm-renters-insurance
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/state-farm-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/state-farm-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/state-farm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/state-farm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/state-farm-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/state-farm-scopes.yml
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
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.statefarm.com/customer-care/privacy-security/privacy/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.statefarm.com/customer-care/legal-disclaimer
- group: operate
  title: ''
  type: FAQ
  url: https://developer.statefarm.com/faq
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/state-farm-renters-insurance-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/state-farm-renters-policy-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/state-farm-renters-policy-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/state-farm-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/state-farm-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/state-farm-rules.yml
description: State Farm is the largest property and casualty insurance provider in the United States, headquartered in Bloomington, Illinois. Founded in 1922, the company offers a comprehensive range of insurance products including auto, home, renters, life, health, business, and farm/ranch insurance, as well as banking and financial services. State Farm operates through a network of approximately 19,000 agents across the US and Canada. The company has invested heavily in its digital transformation, operating a Partner Gateway developer portal at developer.statefarm.com that exposes APIs enabling partners, agents, and third-party platforms to integrate with State Farm's insurance products and services. State Farm is a mutual company owned by its policyholders, consistently ranked among the Fortune 50.
examples:
- key_count: 2
  name: State Farm Create Renters Quote Example
  slug: state-farm-create-renters-quote-example
finops:
- name: State Farm Finops
  service_category: Insurance / Financial Services
  slug: state-farm-finops
graphqls:
- description: State Farm is the largest property and casualty insurance provider in the United States, offering auto, home, renters, life, health, business, and farm/ranch insurance through approximately 19,000 age
  name: State Farm GraphQL Schema
  slug: state-farm-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/state-farm.png
json_schemas:
- name: Renters Insurance Policy
  property_count: 9
  slug: state-farm-renters-policy
json_structures:
- name: State Farm Renters Policy Structure
  property_count: 0
  slug: state-farm-renters-policy-structure
jsonld:
- class_count: 18
  name: State Farm Context
  property_count: 11
  slug: state-farm-context
layout: provider
modified: '2026-05-19'
name: State Farm
nav: Providers
network: true
overview: 'State Farm publishes 3 APIs on the [APIs.io](https://apis.io/) network: Coverage API, Policies API, and Quotes API.


  The State Farm catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  State Farm''s developer surface includes authentication, GitHub presence, FAQ, and 19 more developer resources.'
plans:
- name: State Farm Plans Pricing
  plan_count: 1
  slug: state-farm-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: State Farm Rate Limits
  slug: state-farm-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: State Farm API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: state-farm-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: State Farm API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 5
  slug: state-farm-rules
scopes:
- name: State Farm Scopes
  scope_count: 3
  slug: state-farm-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 28.8
    contract_quality: 64.9
    developer_ergonomics: 26.2
    discoverability: 53.7
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/state-farm/refs/heads/main/screenshots/state-farm-2026-06-20T194520.png
security:
- kind: authentication
  name: State Farm Authentication
  slug: state-farm-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: State Farm Domain Security
  slug: state-farm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: State Farm Vulnerability Disclosure
  slug: state-farm-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: state-farm
website: https://www.statefarm.com
---
