---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Agencyzoom Agentic Access
  operation_count: 36
  slug: agencyzoom-agentic-access
  summary_line: 36 operations · 21 acting
api_count: 8
apis:
- description: The Authentication API from AgencyZoom — 3 operation(s) for authentication.
  name: AgencyZoom Authentication API
  slug: agencyzoom-authentication-api
- description: The Configuration API from AgencyZoom — 5 operation(s) for configuration.
  name: AgencyZoom Configuration API
  slug: agencyzoom-configuration-api
- description: The Customers API from AgencyZoom — 4 operation(s) for customers.
  name: AgencyZoom Customers API
  slug: agencyzoom-customers-api
- description: The Email API from AgencyZoom — 2 operation(s) for email.
  name: AgencyZoom Email API
  slug: agencyzoom-email-api
- description: The Leads API from AgencyZoom — 8 operation(s) for leads.
  name: AgencyZoom Leads API
  slug: agencyzoom-leads-api
- description: The Opportunities API from AgencyZoom — 4 operation(s) for opportunities.
  name: AgencyZoom Opportunities API
  slug: agencyzoom-opportunities-api
- description: The Pipelines API from AgencyZoom — 2 operation(s) for pipelines.
  name: AgencyZoom Pipelines API
  slug: agencyzoom-pipelines-api
- description: The Policies API from AgencyZoom — 3 operation(s) for policies.
  name: AgencyZoom Policies API
  slug: agencyzoom-policies-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AgencyZoom Authentication API
  slug: open-agencyzoom-authentication-api
- collection_type: open
  name: AgencyZoom Authentication Configuration API
  slug: open-agencyzoom-configuration-api
- collection_type: open
  name: AgencyZoom Authentication Customers API
  slug: open-agencyzoom-customers-api
- collection_type: open
  name: AgencyZoom Authentication Email API
  slug: open-agencyzoom-email-api
- collection_type: open
  name: AgencyZoom Authentication Leads API
  slug: open-agencyzoom-leads-api
- collection_type: open
  name: AgencyZoom Authentication Opportunities API
  slug: open-agencyzoom-opportunities-api
- collection_type: open
  name: AgencyZoom Authentication Pipelines API
  slug: open-agencyzoom-pipelines-api
- collection_type: open
  name: AgencyZoom Authentication Policies API
  slug: open-agencyzoom-policies-api
- collection_type: open
  name: AgencyZoom API
  slug: open-agencyzoom
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agencyzoom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agencyzoom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agencyzoom-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agencyzoom
- group: company
  title: ''
  type: Website
  url: https://agencyzoom.com
- group: docs
  title: ''
  type: Documentation
  url: https://app.agencyzoom.com/openapi/
- group: commercial
  title: ''
  type: Pricing
  url: https://agencyzoom.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.agencyzoom.com/signup
created: '2026-05-11'
description: AgencyZoom is a sales automation and customer retention platform built specifically for property and casualty insurance agencies, combining lead management, sales pipelines, automated onboarding, and producer performance analytics in one workflow. The platform integrates with major agency management systems and rating engines to consolidate prospect and policy data. AgencyZoom exposes a REST API documented via OpenAPI for accessing contacts, policies, pipeline, and activity data.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agencyzoom.png
layout: provider
modified: '2026-05-11'
name: AgencyZoom
nav: Providers
network: true
overview: 'AgencyZoom publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Configuration API, Customers API, and 5 more. Tagged areas include Insurance, Insurtech, CRM, Sales Automation, and Agency Management.


  AgencyZoom''s developer surface includes authentication, documentation, pricing, signup flow, and 4 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 27.5
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 49.8
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agencyzoom/refs/heads/main/screenshots/agencyzoom-2026-06-20T165842.png
security:
- kind: authentication
  name: Agencyzoom Authentication
  slug: agencyzoom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agencyzoom Domain Security
  slug: agencyzoom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agencyzoom
tags:
- Insurance
- Insurtech
- CRM
- Sales Automation
- Agency Management
- Customer Retention
website: https://agencyzoom.com
---
