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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Walgreens Agentic Access
  operation_count: 11
  slug: walgreens-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 7
apis:
- description: Enables developers to offer photo printing services at 8,000+ Walgreens and Duane Reade stores for same-day pickup. Supports native JSON API integration with potential revenue share commissions for qu
  name: Walgreens Photo Prints API
  slug: walgreens-photo-prints
- description: Appointment scheduling and management
  name: Walgreens Appointments API
  slug: walgreens-appointments-api
- description: Vaccine eligibility checking
  name: Walgreens Eligibility API
  slug: walgreens-eligibility-api
- description: Patient registration for vaccine appointments
  name: Walgreens Patients API
  slug: walgreens-patients-api
- description: Prescription refill operations
  name: Walgreens Refills API
  slug: walgreens-refills-api
- description: Store search and details operations
  name: Walgreens Stores API
  slug: walgreens-stores-api
- description: Prescription transfer operations
  name: Walgreens Transfers API
  slug: walgreens-transfers-api
artifact_total: 28
collections:
- collection_type: open
  name: Walgreens Prescription Refill API
  slug: open-walgreens-prescription-refill
- collection_type: open
  name: Walgreens Store Locator API
  slug: open-walgreens-store-locator
- collection_type: open
  name: Walgreens Vaccine Scheduling API
  slug: open-walgreens-vaccine-scheduling
common:
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


  Walgreens'' developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, and 6 more developer resources.'
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
random_paper: 8
rate_limits:
- limit_count: 1
  name: Walgreens Rate Limits
  slug: walgreens-rate-limits
rules:
- name: Walgreens API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: walgreens-jsonschema-spectral-rules
- name: Walgreens API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: walgreens-rules
score:
  band: developing
  composite: 43.5
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 75.8
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 43.5
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
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
