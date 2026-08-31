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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Us House Of Representatives Agentic Access
  operation_count: 19
  slug: us-house-of-representatives-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- description: ProPublica's Congress API provides access to detailed congressional data including member profiles, voting records, bill sponsorship, and committee activity. This third-party API aggregates and enrich
  name: ProPublica Congress API
  slug: propublica-congress-api
- description: Legislative bills and resolutions
  name: US House of Representatives Bills API
  slug: us-house-of-representatives-bills-api
- description: Congressional committees
  name: US House of Representatives Committees API
  slug: us-house-of-representatives-committees-api
- description: Members of Congress
  name: US House of Representatives Members API
  slug: us-house-of-representatives-members-api
- description: Presidential nominations
  name: US House of Representatives Nominations API
  slug: us-house-of-representatives-nominations-api
- description: International treaties
  name: US House of Representatives Treaties API
  slug: us-house-of-representatives-treaties-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Congress.gov API
  slug: open-congress-gov-api
- collection_type: open
  name: Congress.gov Bills API
  slug: open-us-house-of-representatives-bills-api
- collection_type: open
  name: Congress.gov Bills Committees API
  slug: open-us-house-of-representatives-committees-api
- collection_type: open
  name: Congress.gov Bills Members API
  slug: open-us-house-of-representatives-members-api
- collection_type: open
  name: Congress.gov Bills Nominations API
  slug: open-us-house-of-representatives-nominations-api
- collection_type: open
  name: Congress.gov Bills Treaties API
  slug: open-us-house-of-representatives-treaties-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/us-house-of-representatives-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-house-of-representatives-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/us-house-of-representatives-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-house-of-representatives-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-house-of-representatives-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-house-of-representatives
created: '2024-12-03'
description: The United States House of Representatives is one of the two chambers of the United States Congress, with the other being the Senate. Its main function is to pass federal legislation, which must then be approved by the Senate before it can become law. The House also has the power to impeach government officials, including the President, and to initiate revenue-related bills. Congressional data is made available through the Congress.gov API, a REST API maintained by the Library of Congress that provides access to bills, members, committees, amendments, nominations, and treaties.
examples:
- key_count: 3
  name: Congress Gov List Bills Example
  slug: congress-gov-list-bills-example
finops:
- name: Us House Of Representatives Finops
  service_category: API
  slug: us-house-of-representatives-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-house-of-representatives.png
json_schemas:
- name: Congress.gov Bill
  property_count: 14
  slug: congress-gov-bill
- name: Congress.gov Member
  property_count: 18
  slug: congress-gov-member
json_structures:
- name: Congress Gov Bill Structure
  property_count: 0
  slug: congress-gov-bill-structure
jsonld:
- class_count: 26
  name: Us House Of Representatives Context
  property_count: 5
  slug: us-house-of-representatives-context
layout: provider
modified: '2026-05-19'
name: US House of Representatives
nav: Providers
network: true
overview: 'US House of Representatives publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bills API, Committees API, Members API, and 2 more. Tagged areas include Federal-Government, Legislation, Congress, Legislative Data, and Bills.


  The US House of Representatives catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US House of Representatives'' developer surface includes authentication and 5 more developer resources.'
plans:
- name: Us House Of Representatives Plans Pricing
  plan_count: 3
  slug: us-house-of-representatives-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Us House Of Representatives Rate Limits
  slug: us-house-of-representatives-rate-limits
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: US House of Representatives API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 4
    warn: 6
  slug: congress-gov-api-rules
- effective_rule_count: 5
  extends: []
  name: US House of Representatives API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-house-of-representatives-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 54.5
    contract_quality: 57.3
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 54.5
    operational_transparency: 13.2
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-house-of-representatives/refs/heads/main/screenshots/us-house-of-representatives-2026-06-20T200622.png
security:
- kind: authentication
  name: Us House Of Representatives Authentication
  slug: us-house-of-representatives-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Us House Of Representatives Domain Security
  slug: us-house-of-representatives-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Us House Of Representatives Vulnerability Disclosure
  slug: us-house-of-representatives-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: us-house-of-representatives
tags:
- Federal-Government
- Legislation
- Congress
- Legislative Data
- Bills
- Members
- Committees
---
