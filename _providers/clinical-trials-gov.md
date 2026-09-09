---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-08'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Clinical Trials Gov Agentic Access
  operation_count: 9
  slug: clinical-trials-gov-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: 'RETIRED. The Classic API was withdrawn in June 2024 and its endpoints now return HTTP 404 (probed 2026-09-06: /api/query/full_studies and /api/info/data_vrs both 404). It is retained here only so cons'
  name: ClinicalTrials.gov Classic API
  slug: classic-api
- description: ClinicalTrials.gov provides bulk CSV and JSON downloads of the full study registry through the data-api download endpoints. These artifacts support large-scale analytics, archival, and offline mirrors
  name: ClinicalTrials.gov Bulk Downloads
  slug: bulk-downloads
- description: AACT (Aggregate Analysis of ClinicalTrials.gov) is a publicly available relational database of all ClinicalTrials.gov study content maintained by the Clinical Trials Transformation Initiative (CTTI) a
  name: AACT Database
  slug: aact
- baseURL: https://clinicaltrials.gov/api/v2
  baseurl_source: declared
  description: The Stats API from ClinicalTrials.gov — 3 operation(s) for stats.
  name: ClinicalTrials.gov Stats API
  slug: clinical-trials-gov-stats-api
- baseURL: https://clinicaltrials.gov/api/v2
  baseurl_source: declared
  description: The Studies API from ClinicalTrials.gov — 5 operation(s) for studies.
  name: ClinicalTrials.gov Studies API
  slug: clinical-trials-gov-studies-api
- baseURL: https://clinicaltrials.gov/api/v2
  baseurl_source: declared
  description: The Version API from ClinicalTrials.gov — 1 operation(s) for version.
  name: ClinicalTrials.gov Version API
  slug: clinical-trials-gov-version-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClinicalTrials.gov Data API v2 Stats API
  slug: open-clinical-trials-gov-stats-api
- collection_type: open
  name: ClinicalTrials.gov Data API v2 Stats Studies API
  slug: open-clinical-trials-gov-studies-api
- collection_type: open
  name: ClinicalTrials.gov Data API v2 Stats Version API
  slug: open-clinical-trials-gov-version-api
- collection_type: open
  name: ClinicalTrials.gov Data API v2
  slug: open-clinical-trials-gov
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clinical-trials-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clinical-trials-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clinicaltrials.gov/
- group: company
  title: ''
  type: About
  url: https://clinicaltrials.gov/about-site
- group: docs
  title: ''
  type: Documentation
  url: https://clinicaltrials.gov/data-api/api
- group: start
  title: ''
  type: Portal
  url: https://clinicaltrials.gov/data-api
- group: other
  title: ''
  type: X-Glossary
  url: https://clinicaltrials.gov/study-basics/glossary
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nlm.nih.gov/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clinicaltrials.gov/about-site/terms-conditions
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clinical-trials-gov-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clinical-trials-gov-rules.yml
- group: docs
  title: ''
  type: APIReference
  url: https://clinicaltrials.gov/data-api/api
- group: start
  title: ''
  type: GettingStarted
  url: https://clinicaltrials.gov/data-api/about-api
- group: operate
  title: ''
  type: Support
  url: https://support.nlm.nih.gov/
- group: operate
  title: ''
  type: FAQ
  url: https://clinicaltrials.gov/policy/faq
- group: company
  title: ''
  type: Newsroom
  url: https://clinicaltrials.gov/about-site/news-and-updates
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://clinicaltrials.gov/about-site/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: https://clinicaltrials.gov/about-site/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clinical-trials-gov-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://clinicaltrials.gov/data-api/about-api/api-migration
- group: build
  title: ''
  type: Packages
  url: packages/clinical-trials-gov-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clinical-trials-gov-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clinical-trials-gov-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clinical-trials-gov-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clinical-trials-gov-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clinical-trials-gov-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clinical-trials-gov-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clinical-trials-gov-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clinical-trials-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clinical-trials-gov-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2024-01-01'
description: ClinicalTrials.gov is the U.S. National Institutes of Health (NIH) registry and results database of publicly and privately supported clinical studies of human participants conducted around the world. Operated by the National Library of Medicine (NLM), it provides a modern REST API (data-api v2) that returns study records, study metadata, search areas, and field definitions in JSON. The predecessor classic API remains available for legacy consumers but is being phased out in favor of the v2 API. Data is in the public domain and freely accessible without authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clinical-trials-gov.png
jsonld:
- class_count: 0
  name: Clinical Trials Gov Context
  property_count: 7
  slug: clinical-trials-gov-context
layout: provider
mcp_servers:
- description: A CANDIDATE tool list derived from the ClinicalTrials.gov Data API v2 OpenAPI operations. The National Library of Medicine does not publish an MCP server for ClinicalTrials.gov — no hosted endpoint, n
  name: ClinicalTrials.gov Data API v2 (candidate MCP surface)
  slug: clinicaltrialsgov-data-api-v2-candidate-mcp-surface
modified: '2026-09-06'
name: ClinicalTrials.gov
nav: Providers
network: true
overview: 'ClinicalTrials.gov publishes 3 APIs on the [APIs.io](https://apis.io/) network: Stats API, Studies API, and Version API. Tagged areas include Clinical Trials, Government, Health, NIH, and Open Data.


  The ClinicalTrials.gov catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClinicalTrials.gov''s developer surface includes documentation, developer portal, API reference, getting-started guide, support, FAQ, release notes, and 24 more developer resources.'
plans:
- name: Clinical Trials Gov Plans Pricing
  plan_count: 1
  slug: clinical-trials-gov-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Clinical Trials Gov Rate Limits
  slug: clinical-trials-gov-rate-limits
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: ClinicalTrials.gov API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: clinical-trials-gov-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 63.0
    catalog_earned_first_party: 8.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 72.7
    contract_quality: 43.5
    developer_ergonomics: 28.0
    discoverability: 66.7
    governance: 72.7
    operational_transparency: 0.0
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/clinical-trials-gov/refs/heads/main/screenshots/clinical-trials-gov-2026-06-20T174525.png
security:
- kind: authentication
  name: Clinical Trials Gov Authentication
  slug: clinical-trials-gov-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Clinical Trials Gov Domain Security
  slug: clinical-trials-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clinical-trials-gov
tags:
- Clinical Trials
- Government
- Health
- NIH
- Open Data
- Public Health
- Research
website: https://clinicaltrials.gov/
---
