---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 14
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accordproject
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/accordproject
- group: company
  title: ''
  type: Website
  url: https://www.accord-mortgages.co.uk/
- group: start
  title: ''
  type: Login
  url: https://www.accord-mortgages.co.uk/intermediary-login
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: A UK-based financial services company operating within the Allianz group, providing insurance and financial products to retail and business customers across the United Kingdom.
features:
- description: Online sourcing of Accord mortgage products by authorized intermediaries through the broker portal.
  name: Intermediary Mortgage Sourcing
- description: Broker-portal-driven Decision in Principle (DIP) for borrower mortgage applications.
  name: Decision in Principle
- description: Online submission and tracking of full mortgage applications by intermediaries.
  name: Application Submission
- description: Existing-customer product transfer and rate-switch workflows handled through the broker portal.
  name: Product Switching
finops:
- name: Accord Finops
  service_category: Financial Services / Mortgages
  slug: accord-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accord.png
integrations:
- description: Twenty7Tec sourcing platform is a primary integration channel for broker mortgage sourcing.
  name: Twenty7Tec
- description: Iress sourcing platform connects intermediaries to Accord mortgage products.
  name: Iress
- description: Mortgage Brain sourcing and CRM platform integrates with Accord for intermediary distribution.
  name: Mortgage Brain
- description: Accord Mortgages is the intermediary-only lender of the Yorkshire Building Society Group.
  name: Yorkshire Building Society
layout: provider
modified: '2026-05-16'
name: Accord
nav: Providers
network: true
overview: 'Accord is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Insurance, United Kingdom, and Mortgages.


  Accord''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Accord Plans Pricing
  plan_count: 1
  slug: accord-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Accord Rate Limits
  slug: accord-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 31.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
slug: accord
tags:
- Financial-Services
- Insurance
- United Kingdom
- Mortgages
use_cases:
- description: Authorized intermediaries originating residential and buy-to-let mortgages on behalf of UK borrowers.
  name: Broker-Originated Mortgages
- description: Comparing and selecting Accord mortgage products through broker sourcing systems.
  name: Mortgage Product Sourcing
- description: Existing-borrower product transfers managed through Accord's intermediary channel.
  name: Customer Retention
website: https://www.accord-mortgages.co.uk/
---
