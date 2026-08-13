---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govwell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://govwell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.govwell.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.govwell.com/en/
- group: start
  title: ''
  type: Login
  url: https://app.govwell.com/login
- group: company
  title: ''
  type: Blog
  url: https://govwell.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://govwell.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://govwell.com/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: security/govwell-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/govwell-llms.txt
created: '2026-07-17'
description: GovWell is a cloud-based AI operating system for modern local and county government, used by municipal and county agencies across 40+ U.S. states to digitize and automate civic services. The platform replaces paper and legacy systems with online workflows for permitting, licensing, planning and zoning, and code enforcement, and layers on AI capabilities including AutoCheck, which automatically reviews applications for errors and missing documentation before submission, and a 24/7 AI Community Assistant that answers resident questions. GovWell serves both government staff, who manage plan reviews, inspections, applications, payments, and renewals, and applicants and contractors, who submit and track requests through a self-service jurisdiction portal. The company is backed by Insight Partners and is an Esri partner. GovWell does not publish a public developer API, SDKs, or a .well-known discovery surface; this profile captures its identity and public trust/security posture.
image: https://cdn.prod.website-files.com/697732d0a9e7ed6e5a43811f/6990ab09889d6924cb697e7f_Open%20Graph%20Image.png
layout: provider
modified: '2026-07-19'
name: GovWell
nav: Providers
network: true
overview: 'GovWell is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, GovTech, Local Government, and Permitting.


  GovWell''s developer surface includes documentation, support, engineering blog, and 7 more developer resources.'
random_paper: 48
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/govwell/refs/heads/main/screenshots/govwell-2026-07-25T220141.png
security:
- kind: domain-security
  name: Govwell Domain Security
  slug: govwell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Govwell Trust Center
  slug: govwell-trust-center
  summary_line: trust center published
slug: govwell
tags:
- Company
- Government
- GovTech
- Local Government
- Permitting
- Licensing
- Code Enforcement
- Planning and Zoning
website: https://govwell.com/
---
