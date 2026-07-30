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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
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
overview: 'Department of State publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Foreign Affairs, Travel, Consular, and Visas.


  The Department of State catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Department of State''s developer surface includes developer portal and 5 more developer resources.'
plans:
- name: Department Of State Plans Pricing
  plan_count: 3
  slug: department-of-state-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Department Of State Rate Limits
  slug: department-of-state-rate-limits
rules:
- name: Department of State API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: state-rules
score:
  band: emerging
  composite: 25.5
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 28.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Department Of State Domain Security
  slug: department-of-state-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-state
tags:
- Federal Government
- Foreign Affairs
- Travel
- Consular
- Visas
- Passports
website: https://www.state.gov/
---
