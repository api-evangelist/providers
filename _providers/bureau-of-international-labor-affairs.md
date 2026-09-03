---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: ILAB provides data on child labor, forced labor, and human trafficking across countries. The DOL developer API provides programmatic access to ILAB datasets including country-level labor standards ass
  name: DOL ILAB Data API
  slug: dol-ilab-data-api
- description: The Sweat and Toil dataset covers child labor and forced labor in over 130 countries, including goods identified as produced by child or forced labor, country advancement levels, and suggested actions
  name: ILAB Sweat and Toil Data
  slug: ilab-sweat-and-toil-data
artifact_total: 6
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
- group: start
  title: ''
  type: Portal
  url: https://developer.dol.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dol.gov/general/privacynotice
- group: other
  title: ''
  type: Data Research
  url: https://www.dol.gov/agencies/ilab/our-work/data-research
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=dol-gov&q=ilab
created: '2024-11-25'
description: ILAB strengthens global labor standards; enforces labor commitments; promotes equity; and combats child labor, forced labor, and human trafficking.
finops:
- name: Bureau Of International Labor Affairs Finops
  service_category: API
  slug: bureau-of-international-labor-affairs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-international-labor-affairs.png
layout: provider
modified: '2026-04-23'
name: Bureau of International Labor Affairs
nav: Providers
network: true
overview: 'Bureau of International Labor Affairs publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, International, Labor, Standards, and Child Labor.


  Bureau of International Labor Affairs'' developer surface includes developer portal and 6 more developer resources.'
plans:
- name: Bureau Of International Labor Affairs Plans Pricing
  plan_count: 3
  slug: bureau-of-international-labor-affairs-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Bureau Of International Labor Affairs Rate Limits
  slug: bureau-of-international-labor-affairs-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-international-labor-affairs/refs/heads/main/screenshots/bureau-of-international-labor-affairs-2026-06-20T173810.png
security:
- kind: domain-security
  name: Bureau Of International Labor Affairs Domain Security
  slug: bureau-of-international-labor-affairs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
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
