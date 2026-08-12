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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: State Farm Insurance Cos Agentic Access
  operation_count: 5
  slug: state-farm-insurance-cos-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 5
apis:
- description: The State Farm Partner Gateway API serves as the unified integration layer for all State Farm Insurance Companies subsidiaries, enabling external partners to access insurance products across the State
  name: Partner Gateway API
  slug: partner-gateway-api
- description: The State Farm B2B Lender Services API provides mortgage lenders and auto lenders with programmatic access to verify insurance coverage for collateral assets financed by their borrowers. Lenders can c
  name: B2B Lender Services API
  slug: b2b-lender-services-api
- description: Coverage options and details
  name: State Farm Insurance Companies Coverage API
  slug: state-farm-insurance-cos-coverage-api
- description: Renters insurance policy operations
  name: State Farm Insurance Companies Policies API
  slug: state-farm-insurance-cos-policies-api
- description: Renters insurance quote operations
  name: State Farm Insurance Companies Quotes API
  slug: state-farm-insurance-cos-quotes-api
artifact_total: 20
collections:
- collection_type: open
  name: State Farm Insurance Companies Renters API
  slug: open-state-farm-insurance-cos-renters
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/state-farm-insurance-cos-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/state-farm-insurance-cos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/state-farm-insurance-cos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/state-farm-insurance-cos-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/state-farm-insurance-cos-scopes.yml
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
  url: openapi/_original/state-farm-insurance-cos-renters-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/state-farm-insurance-cos-renters-policy-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/state-farm-insurance-cos-renters-policy-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/state-farm-insurance-cos-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/state-farm-insurance-cos-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/state-farm-insurance-cos-rules.yml
description: State Farm Insurance Companies is the collective name for the group of insurance subsidiaries operating under State Farm Mutual Automobile Insurance Company, the parent organization headquartered in Bloomington, Illinois. The group comprises fourteen property and casualty insurance companies and two life insurance companies including State Farm Mutual Automobile Insurance Company, State Farm Fire and Casualty Company, State Farm Indemnity Company, State Farm Life Insurance Company, State Farm General Insurance Company, State Farm Florida Insurance Company, and State Farm Lloyds, among others. This multi-entity structure allows State Farm to manage its business across different US state regulatory environments. As a group, State Farm Insurance Companies is the largest property and casualty insurer in the United States. The group shares the common digital infrastructure and developer platform operated at developer.statefarm.com.
examples:
- key_count: 2
  name: State Farm Insurance Cos Create Renters Quote Example
  slug: state-farm-insurance-cos-create-renters-quote-example
finops:
- name: State Farm Insurance Cos Finops
  service_category: Insurance / Financial Services
  slug: state-farm-insurance-cos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/state-farm-insurance-cos.png
json_schemas:
- name: Renters Insurance Policy
  property_count: 9
  slug: state-farm-insurance-cos-renters-policy
json_structures:
- name: State Farm Insurance Cos Renters Policy Structure
  property_count: 0
  slug: state-farm-insurance-cos-renters-policy-structure
jsonld:
- class_count: 11
  name: State Farm Insurance Cos Context
  property_count: 8
  slug: state-farm-insurance-cos-context
layout: provider
modified: '2026-05-19'
name: State Farm Insurance Companies
nav: Providers
network: true
overview: 'State Farm Insurance Companies publishes 3 APIs on the [APIs.io](https://apis.io/) network: Coverage API, Policies API, and Quotes API.


  The State Farm Insurance Companies catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  State Farm Insurance Companies'' developer surface includes authentication, GitHub presence, and 18 more developer resources.'
plans:
- name: State Farm Insurance Cos Plans Pricing
  plan_count: 1
  slug: state-farm-insurance-cos-plans-pricing
press:
- date: '2026-05-25'
  title: In the Heartland
  url: https://www.computerworld.com/article/1685844/in-the-heartland.html
- date: '2026-05-25'
  title: '''They''re being so stingy with everything.'' State Farm ...'
  url: https://www.latimes.com/business/story/2025-03-10/state-farm-seeks-emergency-rate-hike-amid-questions-over-finances-fire-response
- date: '2026-05-25'
  title: Paula Jarrett - state farm insurance cos
  url: https://www.linkedin.com/in/paula-jarrett-a40357259
- date: '2026-05-25'
  title: INSURANCE AGENT'S TERMINATION PAYMENT NOT ...
  url: https://www.taxnotes.com/research/federal/court-documents/court-opinions-and-orders/insurance-agents-termination-payment-not-entitled-to-capital-gains-treatment/1plnn
- date: '2026-05-25'
  title: 147 State Farm Insurance Company Stock Photos, High- ...
  url: https://www.gettyimages.in/photos/state-farm-insurance-company
random_paper: 75
rate_limits:
- limit_count: 1
  name: State Farm Insurance Cos Rate Limits
  slug: state-farm-insurance-cos-rate-limits
rules:
- name: State Farm Insurance Companies API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: state-farm-insurance-cos-jsonschema-spectral-rules
- name: State Farm Insurance Companies API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 5
  slug: state-farm-insurance-cos-rules
scopes:
- name: State Farm Insurance Cos Scopes
  scope_count: 3
  slug: state-farm-insurance-cos-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 42.9
  delta: -5.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 66.2
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 10.5
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/state-farm-insurance-cos/refs/heads/main/screenshots/state-farm-insurance-cos-2026-06-20T194526.png
security:
- kind: authentication
  name: State Farm Insurance Cos Authentication
  slug: state-farm-insurance-cos-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: State Farm Insurance Cos Domain Security
  slug: state-farm-insurance-cos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: State Farm Insurance Cos Vulnerability Disclosure
  slug: state-farm-insurance-cos-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: state-farm-insurance-cos
website: https://www.statefarm.com
---
