---
access_model:
  confidence: high
  label: Free public federal data — no key, no account
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-07'
api_count: 5
apis:
- description: The Office of Fair Housing and Equal Opportunity (FHEO) administers and enforces federal laws that prohibit discrimination in housing based on race, color, national origin, religion, sex, familial sta
  name: Fair Housing and Equal Opportunity
  slug: fair-housing-and-equal-opportunity
- description: An anonymously callable ArcGIS REST feature service publishing the locations, jurisdictions, regions and award amounts of Fair Housing Assistance Program grantees — the state and local agencies that F
  name: Fair Housing Assistance Program (FHAP) Grantees
  slug: fhap-grantees
- description: An anonymously callable ArcGIS REST feature service publishing the locations, components and award amounts of Fair Housing Initiatives Program grantees — the private non-profit organizations funded un
  name: Fair Housing Initiatives Program (FHIP) Grantees
  slug: fhip-grantees
- description: An anonymously callable ArcGIS REST feature service publishing census tract polygons flagged as Racially or Ethnically Concentrated Areas of Poverty, the geography that anchors FHEO's Affirmatively Fu
  name: Racially or Ethnically Concentrated Areas of Poverty (R/ECAP)
  slug: recap
- description: The ArcGIS Server folder behind HUD's Affirmatively Furthering Fair Housing Data and Mapping Tool, FHEO's own analysis surface for program participants. Publishes AffhtMapService and AFFHTReportServic
  name: AFFH Data and Mapping Tool (AFFH-T) Services
  slug: affh-t
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.hud.gov
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hudgis-hud.opendata.arcgis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hud.gov/program_offices/fair_housing_equal_opp
- group: other
  title: ''
  type: X-ProgramOffice
  url: https://www.hud.gov/program_offices/fair_housing_equal_opp
- group: other
  title: ''
  type: X-OpenData
  url: https://hudgis-hud.opendata.arcgis.com/search?tags=fheo
- group: other
  title: ''
  type: X-HUDUser
  url: https://www.huduser.gov/portal/home.html
- group: operate
  title: ''
  type: Support
  url: https://www.hud.gov/program_offices/fair_housing_equal_opp/contact_fheo
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.hud.gov/contactus
- group: company
  title: ''
  type: Blog
  url: https://www.hud.gov/press
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hud.gov/aboutus/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/office-of-fair-housing-and-equal-opportunity
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hudgov
- group: auth
  title: ''
  type: Security
  url: https://www.hud.gov/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/fair-housing-and-equal-opportunity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fair-housing-and-equal-opportunity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fair-housing-and-equal-opportunity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fair-housing-and-equal-opportunity-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fair-housing-and-equal-opportunity-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fair-housing-and-equal-opportunity-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/fair-housing-and-equal-opportunity-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fair-housing-and-equal-opportunity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fair-housing-and-equal-opportunity-rate-limits.yml
- group: design
  title: ''
  type: X-ArcGISServiceMetadata
  url: arcgis/fair-housing-and-equal-opportunity-arcgis.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fair-housing-and-equal-opportunity-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fair-housing-and-equal-opportunity-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fair-housing-and-equal-opportunity-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fair-housing-and-equal-opportunity-llms.txt
created: '2024-12-03'
description: The mission of the Office of Fair Housing and Equal Opportunity (FHEO) is to eliminate housing discrimination, promote economic opportunity, and achieve diverse, inclusive communities by leading the nation in the enforcement, administration, development, and public understanding of federal fair housing policies and laws. FHEO administers the Fair Housing Assistance Program (FHAP) and the Fair Housing Initiatives Program (FHIP), enforces Title VIII of the Civil Rights Act, and owns the Affirmatively Furthering Fair Housing (AFFH) rule and its Data and Mapping Tool. FHEO does not run a developer portal of its own; its program data is published as anonymously callable ArcGIS REST feature services inside HUD's ArcGIS Online organization and through the HUD Open Data site, and its AFFH-T map and report services run on HUD's eGIS ArcGIS Server.
finops:
- name: Fair Housing And Equal Opportunity Finops
  service_category: API
  slug: fair-housing-and-equal-opportunity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fair-housing-and-equal-opportunity.png
layout: provider
modified: '2026-09-07'
name: Fair Housing and Equal Opportunity
nav: Providers
network: true
overview: 'Fair Housing and Equal Opportunity publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AFFH, ArcGIS, Equal Opportunity, Fair Housing, and Federal-Government.


  Fair Housing and Equal Opportunity''s developer surface includes documentation, support, engineering blog, authentication, and 23 more developer resources.'
plans:
- name: Fair Housing And Equal Opportunity Plans Pricing
  plan_count: 0
  slug: fair-housing-and-equal-opportunity-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Fair Housing And Equal Opportunity Rate Limits
  slug: fair-housing-and-equal-opportunity-rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 10.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/fair-housing-and-equal-opportunity/refs/heads/main/screenshots/fair-housing-and-equal-opportunity-2026-06-20T181015.png
security:
- kind: authentication
  name: Fair Housing And Equal Opportunity Authentication
  slug: fair-housing-and-equal-opportunity-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fair Housing And Equal Opportunity Domain Security
  slug: fair-housing-and-equal-opportunity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fair Housing And Equal Opportunity Vulnerability Disclosure
  slug: fair-housing-and-equal-opportunity-vulnerability-disclosure
  summary_line: disclosure policy published
slug: fair-housing-and-equal-opportunity
tags:
- AFFH
- ArcGIS
- Equal Opportunity
- Fair Housing
- Federal-Government
- Geospatial
- Housing
- HUD
- Open Data
website: https://www.hud.gov
---
