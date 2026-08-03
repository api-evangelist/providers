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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Free Law Project Agentic Access
  operation_count: 15
  slug: free-law-project-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 10
apis:
- description: User-defined alerts on search queries.
  name: Free Law Project Alerts API
  slug: free-law-project-alerts-api
- description: Opinions, clusters, dockets, and courts.
  name: Free Law Project Case Law API
  slug: free-law-project-case-law-api
- description: Citation lookup and verification.
  name: Free Law Project Citations API
  slug: free-law-project-citations-api
- description: Federal and state judge financial disclosure filings.
  name: Free Law Project Financial Disclosures API
  slug: free-law-project-financial-disclosures-api
- description: Judges, positions, education, and political affiliations.
  name: Free Law Project Judges API
  slug: free-law-project-judges-api
- description: Oral argument audio recordings.
  name: Free Law Project Oral Arguments API
  slug: free-law-project-oral-arguments-api
- description: PACER dockets, entries, and documents.
  name: Free Law Project PACER API
  slug: free-law-project-pacer-api
- description: RECAP archive of public PACER documents.
  name: Free Law Project RECAP API
  slug: free-law-project-recap-api
- description: Full-text and faceted search across CourtListener data.
  name: Free Law Project Search API
  slug: free-law-project-search-api
- description: User tags for organizing dockets.
  name: Free Law Project Tags API
  slug: free-law-project-tags-api
artifact_total: 17
collections:
- collection_type: open
  name: Free Law Project / CourtListener REST API
  slug: open-free-law-project
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/free-law-project-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/free-law-project-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/free-law-project-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/free-law-project
- group: company
  title: ''
  type: Website
  url: https://free.law/
- group: docs
  title: ''
  type: Documentation
  url: https://www.courtlistener.com/help/api/rest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freelawproject
- group: company
  title: ''
  type: Blog
  url: https://free.law/feeds/all.atom.xml
created: '2025-01-07'
description: Free Law Project is a non-profit organization that seeks to increase access to justice and transparency in the legal system through the use of technology and open data.
finops:
- name: Free Law Project Finops
  service_category: API
  slug: free-law-project-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/free-law-project.png
layout: provider
modified: '2026-05-19'
name: Free Law Project
nav: Providers
network: true
overview: 'Free Law Project publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Case Law API, Citations API, and 7 more. Tagged areas include Courts, Justice, Legal, and Transparency.


  Free Law Project''s developer surface includes authentication, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Free Law Project Plans Pricing
  plan_count: 3
  slug: free-law-project-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Free Law Project Rate Limits
  slug: free-law-project-rate-limits
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.8
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/free-law-project/refs/heads/main/screenshots/free-law-project-2026-06-20T181519.png
security:
- kind: authentication
  name: Free Law Project Authentication
  slug: free-law-project-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Free Law Project Domain Security
  slug: free-law-project-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: free-law-project
tags:
- Courts
- Justice
- Legal
- Transparency
website: https://free.law/
---
