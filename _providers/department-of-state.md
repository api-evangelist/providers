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
  scored_at: '2026-09-04'
api_count: 9
apis:
- description: Country-by-country travel advisories (Levels 1-4) issued by the Bureau of Consular Affairs, with RSS distribution.
  name: State Department Travel Advisories
  slug: travel-advisories
- description: Per-country pages covering entry/exit requirements, local laws, safety, health, and U.S. embassy contacts.
  name: Country Information Pages
  slug: country-information
- description: Voluntary enrollment system for U.S. citizens traveling or residing abroad to receive embassy alerts.
  name: Smart Traveler Enrollment Program (STEP)
  slug: smart-traveler-enrollment-program
- description: Reference information on nonimmigrant and immigrant visa categories, processing times, and reciprocity schedules.
  name: U.S. Visa Information
  slug: visa-information
- description: Public-facing passport application, renewal, and status-check resources from the Bureau of Consular Affairs.
  name: U.S. Passport Services
  slug: passport-services
- description: Department-wide policy and procedural manuals issued by the Office of Directives Management.
  name: Foreign Affairs Manual (FAM) and Handbook (FAH)
  slug: foreign-affairs-manual
- description: Government-internal name-check system used during visa and passport adjudication. Referenced here for completeness; no public API.
  name: ConsularLookout (CLASS)
  slug: consular-lookout-class
- description: State Department-wide enterprise case-management platform. Internal system; referenced here for organizational completeness.
  name: eCASE Enterprise Case Management
  slug: ecase
- description: Public datasets published by the State Department through the federal open-data catalog.
  name: State Department Open Data on data.gov
  slug: state-data-gov
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-state-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usstatedept
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/statedept
- group: start
  title: ''
  type: Portal
  url: https://www.state.gov/
- group: start
  title: ''
  type: Portal
  url: https://travel.state.gov/
- group: docs
  title: ''
  type: Reference
  url: https://fam.state.gov/
created: '2024-12-03'
description: The U.S. Department of State leads U.S. foreign policy, conducts diplomacy with foreign governments, issues U.S. passports and visas, supports U.S. citizens abroad, and publishes country-specific information and travel advisories. The Department does not currently operate a unified developer portal; instead, integrators work from public RSS feeds, web pages, the Foreign Affairs Manual, and references to internal systems (ConsularLookout, eCASE) that are not publicly accessible.
finops:
- name: Department Of State Finops
  service_category: API
  slug: department-of-state-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-state.png
jsonld:
- class_count: 0
  name: State Context
  property_count: 5
  slug: state-context
layout: provider
modified: '2026-04-28'
name: Department of State
nav: Providers
network: true
overview: 'Department of State publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Foreign Affairs, Travel, Consular, and Visas.


  The Department of State catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Department of State''s developer surface includes developer portal and 5 more developer resources.'
plans:
- name: Department Of State Plans Pricing
  plan_count: 3
  slug: department-of-state-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Department Of State Rate Limits
  slug: department-of-state-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Department of State API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: state-rules
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Department Of State Domain Security
  slug: department-of-state-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-state
tags:
- Federal-Government
- Foreign Affairs
- Travel
- Consular
- Visas
- Passports
website: https://www.state.gov/
---
