---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Walgreens Agentic Access
  operation_count: 11
  slug: walgreens-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 3
apis:
- description: Enables developers to offer photo printing services at 8,000+ Walgreens and Duane Reade stores for same-day pickup. Supports native JSON API integration with potential revenue share commissions for qu
  name: Walgreens Photo Prints API
  slug: walgreens-photo-prints
- baseURL: https://services.walgreens.com
  baseurl_source: declared
  description: Appointment scheduling and management
  name: Walgreens Appointments API
  slug: walgreens-appointments-api
- baseURL: https://services.walgreens.com
  baseurl_source: declared
  description: Vaccine eligibility checking
  name: Walgreens Eligibility API
  slug: walgreens-eligibility-api
- baseURL: https://services.walgreens.com
  baseurl_source: declared
  description: Patient registration for vaccine appointments
  name: Walgreens Patients API
  slug: walgreens-patients-api
- baseURL: https://services.walgreens.com
  baseurl_source: declared
  description: Prescription refill operations
  name: Walgreens Refills API
  slug: walgreens-refills-api
- baseURL: https://services.walgreens.com
  baseurl_source: declared
  description: Store search and details operations
  name: Walgreens Stores API
  slug: walgreens-stores-api
- baseURL: https://services.walgreens.com
  baseurl_source: declared
  description: Prescription transfer operations
  name: Walgreens Transfers API
  slug: walgreens-transfers-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Walgreens Prescription Refill Appointments API
  slug: open-walgreens-appointments-api
- collection_type: open
  name: Walgreens Prescription Refill Appointments Eligibility API
  slug: open-walgreens-eligibility-api
- collection_type: open
  name: Walgreens Prescription Refill Appointments Patients API
  slug: open-walgreens-patients-api
- collection_type: open
  name: Walgreens Prescription Refill API
  slug: open-walgreens-prescription-refill
- collection_type: open
  name: Walgreens Prescription Refill Appointments Refills API
  slug: open-walgreens-refills-api
- collection_type: open
  name: Walgreens Store Locator API
  slug: open-walgreens-store-locator
- collection_type: open
  name: Walgreens Prescription Refill Appointments Stores API
  slug: open-walgreens-stores-api
- collection_type: open
  name: Walgreens Prescription Refill Appointments Transfers API
  slug: open-walgreens-transfers-api
- collection_type: open
  name: Walgreens Vaccine Scheduling API
  slug: open-walgreens-vaccine-scheduling
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/walgreens-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/walgreens-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/walgreens-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/walgreens-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/walgreens-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Walgreens-LSG
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/walgreens
- group: company
  title: ''
  type: Website
  url: https://www.walgreens.com
- group: start
  title: ''
  type: Portal
  url: https://developer.walgreens.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.walgreens.com/apis
- group: company
  title: ''
  type: Blog
  url: https://developer.walgreens.com/blog
- group: start
  title: ''
  type: Signup
  url: https://developer.walgreens.com/user/register
created: '2025-03-01'
description: Walgreens is one of the largest pharmacy-led health and wellbeing companies in the United States, operating over 8,000 locations nationwide. The Walgreens Developer Program provides APIs enabling third-party applications to integrate pharmacy prescription management, vaccine scheduling, retail shopping, store locations, and product inventory. The APIs support seamless healthcare delivery, prescription refills, immunization appointments, and retail e-commerce integrations for mobile and web applications.
examples:
- key_count: 2
  name: Walgreens Check Vaccine Eligibility Example
  slug: walgreens-check-vaccine-eligibility-example
- key_count: 2
  name: Walgreens Get Vaccine Timeslots Example
  slug: walgreens-get-vaccine-timeslots-example
- key_count: 2
  name: Walgreens Hold Vaccine Appointment Example
  slug: walgreens-hold-vaccine-appointment-example
- key_count: 2
  name: Walgreens Search Stores Example
  slug: walgreens-search-stores-example
finops:
- name: Walgreens Finops
  service_category: Retail / Pharmacy Partner API
  slug: walgreens-finops
graphqls:
- description: 'This conceptual GraphQL schema represents the Walgreens API surface, covering the four public REST APIs available through the Walgreens Developer Program: Store Locator, Prescription Refill, Vaccine S'
  name: Walgreens GraphQL Schema
  slug: walgreens-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/walgreens.png
json_schemas:
- name: Walgreens Store
  property_count: 17
  slug: walgreens-store
- name: Walgreens Vaccine Appointment
  property_count: 9
  slug: walgreens-vaccine-appointment
json_structures:
- name: Walgreens Store Structure
  property_count: 0
  slug: walgreens-store-structure
jsonld:
- class_count: 40
  name: Walgreens Context
  property_count: 4
  slug: walgreens-context
layout: provider
modified: '2026-05-19'
name: Walgreens
nav: Providers
network: true
overview: 'Walgreens publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Eligibility API, Patients API, and 3 more. Tagged areas include Pharmacy, Healthcare, Retail, Prescriptions, and Vaccines.


  The Walgreens catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Walgreens'' developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Walgreens Plans Pricing
  plan_count: 1
  slug: walgreens-plans-pricing
press:
- date: '2026-05-25'
  title: Walgreens Boots Alliance and Microsoft establish strategic ...
  url: https://news.microsoft.com/source/2019/01/15/walgreens-boots-alliance-and-microsoft-establish-strategic-partnership-to-transform-health-care-delivery/
- date: '2026-05-25'
  title: 'Customer Story: Walgreens'
  url: https://www.databricks.com/customers/walgreens
- date: '2026-05-25'
  title: Walgreens, Freenome Team Up, New AI Products from ...
  url: https://www.clinicalresearchnewsonline.com/news/2023/06/29/walgreens-freenome-team-up-new-ai-products-from-objectivehealth-saama-more
- date: '2026-05-25'
  title: Walgreens to use Microsoft's cloud, AI platform
  url: https://www.healthcaredive.com/news/walgreens-to-use-microsofts-cloud-ai-platform/546110/
- date: '2026-05-25'
  title: Walgreens Turns to Digital Transformation | AVI Blog
  url: https://www.avi.com/content-hub/walgreens-turns-to-digital-transformation-to-enhance-the-customer-experience/
random_paper: 2
rate_limits:
- limit_count: 1
  name: Walgreens Rate Limits
  slug: walgreens-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Walgreens API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: walgreens-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Walgreens API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: walgreens-rules
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 45.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 70.8
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/walgreens/refs/heads/main/screenshots/walgreens-2026-06-20T201206.png
security:
- kind: authentication
  name: Walgreens Authentication
  slug: walgreens-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Walgreens Domain Security
  slug: walgreens-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Walgreens Vulnerability Disclosure
  slug: walgreens-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: walgreens
tags:
- Pharmacy
- Healthcare
- Retail
- Prescriptions
- Vaccines
- Fortune 100
website: https://www.walgreens.com
---
