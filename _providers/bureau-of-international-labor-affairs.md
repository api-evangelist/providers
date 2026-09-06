---
access_model:
  confidence: high
  label: Free public data — self-service API key
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - https://dataportal.dol.gov/registration
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.1
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: ILAB's datasets are served through the U.S. Department of Labor Open Data Portal API (https://apiprod.dol.gov/v4) under the agency segment 'ilab'. The catalogue route /v4/datasets answers anonymously;
  name: DOL Open Data Portal API — ILAB datasets
  slug: dol-ilab-data-api
- description: 'The Sweat & Toil programme''s data now ships under the LaborShield, ImportWatch, SourcingStrong and SupplyChainTrace names. Seven tables are published through the DOL Open Data Portal API: Child_Labor_'
  name: ILAB Sweat & Toil / LaborShield dataset family
  slug: ilab-sweat-and-toil-data
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-international-labor-affairs-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/bureau-of-international-labor-affairs
- group: company
  title: ''
  type: Website
  url: https://www.dol.gov/agencies/ilab
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dol.gov/general/privacynotice
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=dol-gov&q=ilab
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dataportal.dol.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://dataportal.dol.gov/user-guide
- group: docs
  title: ''
  type: APIReference
  url: https://dataportal.dol.gov/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://dataportal.dol.gov/getting-started
- group: operate
  title: ''
  type: Support
  url: https://dataportal.dol.gov/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://dataportal.dol.gov/registration
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataportal.dol.gov/registration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USDepartmentofLabor
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-international-labor-affairs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bureau-of-international-labor-affairs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-international-labor-affairs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-international-labor-affairs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bureau-of-international-labor-affairs-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bureau-of-international-labor-affairs-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bureau-of-international-labor-affairs-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-international-labor-affairs-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-international-labor-affairs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bureau-of-international-labor-affairs-plans-pricing.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-international-labor-affairs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/bureau-of-international-labor-affairs-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bureau-of-international-labor-affairs-mcp.yml
created: '2024-11-25'
description: 'ILAB is the U.S. Department of Labor bureau that strengthens global labor standards, enforces labor commitments in trade agreements, promotes equity, and combats child labor, forced labor and human trafficking. ILAB operates no API of its own: its seven public datasets — the Child Labor Report and the ImportWatch and LaborShield families, all derived from ILAB''s three flagship reports — are served through the department-wide DOL Open Data Portal API at apiprod.dol.gov/v4, under the agency segment ''ilab'', with a free X-API-KEY credential.'
finops:
- name: Bureau Of International Labor Affairs Finops
  service_category: API
  slug: bureau-of-international-labor-affairs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-international-labor-affairs.png
layout: provider
modified: '2026-09-05'
name: Bureau of International Labor Affairs
nav: Providers
network: true
overview: 'Bureau of International Labor Affairs publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, International, Labor, Standards, and Child Labor.


  Bureau of International Labor Affairs'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Bureau Of International Labor Affairs Plans Pricing
  plan_count: 1
  slug: bureau-of-international-labor-affairs-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Bureau Of International Labor Affairs Rate Limits
  slug: bureau-of-international-labor-affairs-rate-limits
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.0
    catalog_earned_first_party: 16.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  previous_composite: 14.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-international-labor-affairs/refs/heads/main/screenshots/bureau-of-international-labor-affairs-2026-06-20T173810.png
security:
- kind: authentication
  name: Bureau Of International Labor Affairs Authentication
  slug: bureau-of-international-labor-affairs-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bureau Of International Labor Affairs Domain Security
  slug: bureau-of-international-labor-affairs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of International Labor Affairs Vulnerability Disclosure
  slug: bureau-of-international-labor-affairs-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: bureau-of-international-labor-affairs
tags:
- Federal-Government
- International
- Labor
- Standards
- Child Labor
- Forced Labor
- Human Trafficking
website: https://www.dol.gov/agencies/ilab
---
