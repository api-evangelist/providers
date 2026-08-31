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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Icims Agentic Access
  operation_count: 6
  slug: icims-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 3
apis:
- description: The iCIMS Apply Framework API enables external systems to deliver candidate apply experiences and submit applications into the iCIMS Talent Cloud, supporting integrations with job boards, sourcing cha
  name: iCIMS Apply Framework API
  slug: icims-apply-framework-api
- description: The iCIMS Marketplace Integrations API enables certified partners to build, publish, and manage integrations with the iCIMS Talent Cloud across recruiting, onboarding, assessment, and background scree
  name: iCIMS Marketplace Integrations API
  slug: icims-marketplace-api
- description: Manage candidate workflows linking jobs and people.
  name: iCIMS Workflows API
  slug: icims-workflows-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: iCIMS Workflows API
  slug: open-icims-workflows-api
- collection_type: open
  name: iCIMS Workflows API
  slug: open-icims
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/icims-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/icims-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/icims-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/icims-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iCIMS-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/icims
- group: start
  title: ''
  type: Portal
  url: https://developer-community.icims.com/
- group: company
  title: ''
  type: Website
  url: https://www.icims.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-community.icims.com/
- group: operate
  title: ''
  type: Support
  url: https://www.icims.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.icims.com/feed
created: '2025-01-08'
description: iCIMS is a leading talent cloud company providing applicant tracking and talent acquisition software. The iCIMS developer platform provides APIs for integrating with iCIMS Talent Cloud, enabling access to job postings, applicant workflows, candidate management, and hiring processes.
finops:
- name: Icims Finops
  service_category: API
  slug: icims-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/icims.png
layout: provider
modified: '2026-05-19'
name: iCIMS
nav: Providers
network: true
overview: 'iCIMS publishes 1 API on the [APIs.io](https://apis.io/) network: Workflows API. Tagged areas include Applicant Tracking, HR, Recruiting, and Talent Acquisition.


  iCIMS''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 6 more developer resources.'
plans:
- name: Icims Plans Pricing
  plan_count: 3
  slug: icims-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Icims Rate Limits
  slug: icims-rate-limits
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 33.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/icims/refs/heads/main/screenshots/icims-2026-06-20T183152.png
security:
- kind: authentication
  name: Icims Authentication
  slug: icims-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Icims Domain Security
  slug: icims-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Icims Trust Center
  slug: icims-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: icims
tags:
- Applicant Tracking
- HR
- Recruiting
- Talent Acquisition
website: https://www.icims.com/
---
