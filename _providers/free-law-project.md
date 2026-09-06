---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Free Law Project Agentic Access
  operation_count: 15
  slug: free-law-project-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 1
apis:
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: User-defined alerts on search queries.
  name: Free Law Project Alerts API
  slug: free-law-project-alerts-api
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: Opinions, clusters, dockets, and courts.
  name: Free Law Project Case Law API
  slug: free-law-project-case-law-api
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: Citation lookup and verification.
  name: Free Law Project Citations API
  slug: free-law-project-citations-api
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: Federal and state judge financial disclosure filings.
  name: Free Law Project Financial Disclosures API
  slug: free-law-project-financial-disclosures-api
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: Judges, positions, education, and political affiliations.
  name: Free Law Project Judges API
  slug: free-law-project-judges-api
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: Oral argument audio recordings.
  name: Free Law Project Oral Arguments API
  slug: free-law-project-oral-arguments-api
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: PACER dockets, entries, and documents.
  name: Free Law Project PACER API
  slug: free-law-project-pacer-api
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: RECAP archive of public PACER documents.
  name: Free Law Project RECAP API
  slug: free-law-project-recap-api
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: Full-text and faceted search across CourtListener data.
  name: Free Law Project Search API
  slug: free-law-project-search-api
- baseURL: https://www.courtlistener.com/api/rest/v4
  baseurl_source: declared
  description: User tags for organizing dockets.
  name: Free Law Project Tags API
  slug: free-law-project-tags-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts API
  slug: open-free-law-project-alerts-api
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts Case Law API
  slug: open-free-law-project-case-law-api
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts Citations API
  slug: open-free-law-project-citations-api
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts Financial Disclosures API
  slug: open-free-law-project-financial-disclosures-api
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts Judges API
  slug: open-free-law-project-judges-api
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts Oral Arguments API
  slug: open-free-law-project-oral-arguments-api
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts PACER API
  slug: open-free-law-project-pacer-api
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts RECAP API
  slug: open-free-law-project-recap-api
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts Search API
  slug: open-free-law-project-search-api
- collection_type: open
  name: Free Law Project / CourtListener REST Alerts Tags API
  slug: open-free-law-project-tags-api
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
random_paper: 16
rate_limits:
- limit_count: 5
  name: Free Law Project Rate Limits
  slug: free-law-project-rate-limits
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.7
    developer_ergonomics: 23.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
