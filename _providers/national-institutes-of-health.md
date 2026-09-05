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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: National Institutes Of Health Agentic Access
  operation_count: 2
  slug: national-institutes-of-health-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.reporter.nih.gov
  baseurl_source: declared
  description: The Projects API from National Institutes of Health — 1 operation(s) for projects.
  name: National Institutes of Health Projects API
  slug: national-institutes-of-health-projects-api
- baseURL: https://api.reporter.nih.gov
  baseurl_source: declared
  description: The Publications API from National Institutes of Health — 1 operation(s) for publications.
  name: National Institutes of Health Publications API
  slug: national-institutes-of-health-publications-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NIH RePORTER Projects API
  slug: open-national-institutes-of-health-projects-api
- collection_type: open
  name: NIH RePORTER Projects Publications API
  slug: open-national-institutes-of-health-publications-api
- collection_type: open
  name: NIH RePORTER API
  slug: open-national-institutes-of-health
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/national-institutes-of-health-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-institutes-of-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-institutes-of-health-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NIHGOV
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-institutes-of-health
- group: company
  title: ''
  type: Website
  url: https://www.nih.gov/
- group: start
  title: ''
  type: Portal
  url: https://api.reporter.nih.gov/
created: '2024-12-03'
description: The National Institutes of Health (NIH), a part of the U.S. Department of Health and Human Services, is the nation's medical research agency making important discoveries that improve health and save lives. NIH operates the RePORTER API for exposing data about NIH-funded research projects and the publications associated with them.
finops:
- name: National Institutes Of Health Finops
  service_category: API
  slug: national-institutes-of-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-institutes-of-health.png
layout: provider
modified: '2026-05-19'
name: National Institutes of Health
nav: Providers
network: true
overview: 'National Institutes of Health publishes 2 APIs on the [APIs.io](https://apis.io/) network: Projects API and Publications API. Tagged areas include Federal-Government, Health, Research, Funding, and Publications.


  National Institutes of Health''s developer surface includes developer portal and 6 more developer resources.'
plans:
- name: National Institutes Of Health Plans Pricing
  plan_count: 3
  slug: national-institutes-of-health-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: National Institutes Of Health Rate Limits
  slug: national-institutes-of-health-rate-limits
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-institutes-of-health/refs/heads/main/screenshots/national-institutes-of-health-2026-06-20T190030.png
security:
- kind: domain-security
  name: National Institutes Of Health Domain Security
  slug: national-institutes-of-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-institutes-of-health
tags:
- Federal-Government
- Health
- Research
- Funding
- Publications
website: https://www.nih.gov/
---
