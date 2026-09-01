---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The Probe42 API provides programmatic access to curated intelligence on Indian companies — company profiles, financials, directors, and charges — for embedding due-diligence and business-intelligence '
  name: Probe42 API
  slug: probe42-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://probe42.in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.probe42.in/v1/
- group: start
  title: ''
  type: Login
  url: https://apiportal.probe42.in/v1/
- group: company
  title: ''
  type: Blog
  url: https://resources.probe42.in/
- group: operate
  title: ''
  type: Support
  url: https://probe42.in/contactus.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://probe42.in/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://probe42.in/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/probe42
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/probe-information-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/probe-information-domain-security.yml
created: '2026-07-17'
description: Probe Information Services (Probe42) is an Indian company-intelligence and business-data platform that collects, cleans, and curates information on roughly one million Indian companies from 743 public-domain sources through a five-step verification process. Its products — Probe42 Business, Probe42 Banking, and the Probe42 API — deliver company profiles, financials, director and charge data, and risk signals used by banks, NBFCs, fintechs, and sales teams for onboarding, KYC/due-diligence, credit assessment, and lead intelligence. The Probe42 API lets developers embed this company data directly inside their own applications. Surfaced as an Accel portfolio company and added to the API Evangelist network for enrichment; the public API surface is gated behind developer-portal authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/probe-information.png
layout: provider
modified: '2026-07-20'
name: Probe Information
nav: Providers
network: true
overview: 'Probe Information publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Intelligence, Company Data, Financial Data, and Due Diligence.


  Probe Information''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Probe Information Domain Security
  slug: probe-information-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: probe-information
tags:
- Company
- Business Intelligence
- Company Data
- Financial Data
- Due Diligence
- KYC
- Banking
- India
website: https://probe42.in
---
