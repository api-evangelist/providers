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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Charityapi Agentic Access
  operation_count: 3
  slug: charityapi-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Typeahead search across nonprofit organization names
  name: CharityAPI Autocomplete API
  slug: charityapi-autocomplete-api
- description: Look up US nonprofit organization records by EIN
  name: CharityAPI Organizations API
  slug: charityapi-organizations-api
- description: Verify whether an EIN is a tax-deductible public charity
  name: CharityAPI Public Charity Check API
  slug: charityapi-public-charity-check-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Charity Autocomplete API
  slug: open-charityapi-autocomplete-api
- collection_type: open
  name: Charity Autocomplete Organizations API
  slug: open-charityapi-organizations-api
- collection_type: open
  name: Charity Autocomplete Public Charity Check API
  slug: open-charityapi-public-charity-check-api
- collection_type: open
  name: CharityAPI
  slug: open-charityapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/charityapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charityapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/charityapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.charityapi.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.charityapi.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.charityapi.org/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.charityapi.org/blog
- group: start
  title: ''
  type: Signup
  url: https://www.charityapi.org/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.charityapi.org/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.charityapi.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.charityapi.org/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/charityapi-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/charityapi-organization-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/charityapi-public-charity-check-schema.json
created: '2025-03-01'
description: CharityAPI provides a simple REST API for data about US nonprofits and charities sourced directly from IRS filings. Developers can retrieve nonprofit records by EIN, verify whether an organization is a public charity (501c3) with tax-deductible status, and integrate organization name autocomplete to power donation, vetting, and compliance workflows.
finops:
- name: Charityapi Finops
  service_category: API
  slug: charityapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/charityapi.png
json_schemas:
- name: CharityAPI Organization
  property_count: 20
  slug: charityapi-organization
- name: CharityAPI Public Charity Check
  property_count: 2
  slug: charityapi-public-charity-check
jsonld:
- class_count: 0
  name: Charityapi Context
  property_count: 2
  slug: charityapi-context
layout: provider
modified: '2026-05-19'
name: CharityAPI
nav: Providers
network: true
overview: 'CharityAPI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Autocomplete API, Organizations API, and Public Charity Check API. Tagged areas include 501c3, Charities, Donations, EIN, and IRS.


  The CharityAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CharityAPI''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, and 8 more developer resources.'
plans:
- name: Charityapi Plans Pricing
  plan_count: 3
  slug: charityapi-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Charityapi Rate Limits
  slug: charityapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CharityAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: charityapi-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 60.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 60.5
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/charityapi/refs/heads/main/screenshots/charityapi-2026-06-20T174221.png
security:
- kind: authentication
  name: Charityapi Authentication
  slug: charityapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Charityapi Domain Security
  slug: charityapi-domain-security
  summary_line: TLSv1.3
slug: charityapi
tags:
- 501c3
- Charities
- Donations
- EIN
- IRS
- Non-Profit
- Tax Compliance
- Verification
website: https://www.charityapi.org/
---
