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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
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
overview: 'Accord is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Insurance, United Kingdom, and Mortgages.


  Accord''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Accord Plans Pricing
  plan_count: 1
  slug: accord-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Accord Rate Limits
  slug: accord-rate-limits
score:
  band: emerging
  composite: 20.5
  delta: 0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 42.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.8
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
slug: accord
tags:
- Financial Services
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
