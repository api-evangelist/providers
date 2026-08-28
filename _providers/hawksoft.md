---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hawksoft Agentic Access
  operation_count: 9
  slug: hawksoft-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 5
apis:
- description: Agencies and their offices
  name: HawkSoft Agencies API
  slug: hawksoft-agencies-api
- description: File attachments on client records
  name: HawkSoft Attachments API
  slug: hawksoft-attachments-api
- description: Client records including contacts, policies, coverages, vehicles, and drivers
  name: HawkSoft Clients API
  slug: hawksoft-clients-api
- description: Write-back activity log notes
  name: HawkSoft Log Entries API
  slug: hawksoft-log-entries-api
- description: Payment receipts on client records
  name: HawkSoft Receipts API
  slug: hawksoft-receipts-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HawkSoft Partner Agencies API
  slug: open-hawksoft-agencies-api
- collection_type: open
  name: HawkSoft Partner Agencies Attachments API
  slug: open-hawksoft-attachments-api
- collection_type: open
  name: HawkSoft Partner Agencies Clients API
  slug: open-hawksoft-clients-api
- collection_type: open
  name: HawkSoft Partner Agencies Log Entries API
  slug: open-hawksoft-log-entries-api
- collection_type: open
  name: HawkSoft Partner Agencies Receipts API
  slug: open-hawksoft-receipts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hawksoft-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hawksoft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hawksoft-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hawksoft.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hawksoft-inc-
- group: docs
  title: ''
  type: Documentation
  url: https://partner.hawksoft.app/
- group: start
  title: ''
  type: SignUp
  url: https://www.hawksoft.com/about/partners/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hawksoft.com/terms/api/
- group: company
  title: ''
  type: Blog
  url: https://blog.hawksoft.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/hawksoft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hawksoft-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hawksoft-finops.yml
created: '2026-07-10'
description: HawkSoft is an insurance agency management system (AMS) for independent property and casualty agencies, covering client management, policy tracking, documentation, accounting, and workflow automation. HawkSoft operates a gated Partner API program that lets vetted third-party technology vendors and agencies read agency, office, client, contact, policy, coverage, vehicle, driver, and log data, and (with 2-way integration) write activities back into HawkSoft as log notes, attachments, and payment receipts. The Partner API documentation is publicly readable at partner.hawksoft.app, but credentials are issued only to approved API Partners, and an agency must opt in to share its data. Endpoints are versioned (V1.8 and V3.0, with V3.0 built on the HawkSoft 6 cloud data model).
finops:
- name: Hawksoft Finops
  service_category: Insurance Software
  slug: hawksoft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hawksoft.png
layout: provider
modified: '2026-07-10'
name: HawkSoft
nav: Providers
network: true
overview: 'HawkSoft publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agencies API, Attachments API, Clients API, and 2 more. Tagged areas include Insurance, Agency Management System, AMS, Insurtech, and Property and Casualty.


  HawkSoft''s developer surface includes authentication, documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Hawksoft Plans Pricing
  plan_count: 2
  slug: hawksoft-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Hawksoft Rate Limits
  slug: hawksoft-rate-limits
score:
  band: thin
  composite: 31.1
  delta: 1.5
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 13.1
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 24.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hawksoft/refs/heads/main/screenshots/hawksoft-2026-07-25T220807.png
security:
- kind: authentication
  name: Hawksoft Authentication
  slug: hawksoft-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hawksoft Domain Security
  slug: hawksoft-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hawksoft
tags:
- Insurance
- Agency Management System
- AMS
- Insurtech
- Property and Casualty
- Partner API
- Gated API
website: https://www.hawksoft.com
---
