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
api_count: 3
apis:
- description: Public-facing website of the Defense Nuclear Facilities Safety Board providing organizational information, board members, hearings, and publications. The site does not expose a developer API.
  name: DNFSB Website
  slug: defense-nuclear-facilities-safety-board-website
- description: Library of formal recommendations, technical reports, letters, and weekly site-representative reports published by the Defense Nuclear Facilities Safety Board. Documents are available for download but
  name: DNFSB Recommendations and Reports
  slug: defense-nuclear-facilities-safety-board-recommendations
- description: Online portal that publishes records released under the Freedom of Information Act and frequently requested documents. Records are browsable and downloadable but there is no documented API.
  name: DNFSB FOIA Reading Room
  slug: defense-nuclear-facilities-safety-board-foia
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defense-nuclear-facilities-safety-board-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defense-nuclear-facilities-safety-board
- group: company
  title: ''
  type: Website
  url: https://www.dnfsb.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.dnfsb.gov/documents
- group: company
  title: ''
  type: News
  url: https://www.dnfsb.gov/news
- group: operate
  title: ''
  type: ContactUs
  url: https://www.dnfsb.gov/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dnfsb.gov/privacy-and-security
- group: other
  title: ''
  type: FOIA
  url: https://www.dnfsb.gov/foia
created: '2024-12-03'
description: The Defense Nuclear Facilities Safety Board (DNFSB) is an independent organization within the executive branch of the United States Government chartered to provide recommendations and advice to the President and the Secretary of Energy on public health and safety issues at Department of Energy defense nuclear facilities. The DNFSB publishes recommendations, letters, technical reports, weekly site-representative reports, and rulemaking notices through its public website and FOIA reading room. The agency does not publish a developer-oriented API; programmatic users rely on document downloads, RSS feeds, and Federal Register integrations.
finops:
- name: Defense Nuclear Facilities Safety Board Finops
  service_category: API
  slug: defense-nuclear-facilities-safety-board-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defense-nuclear-facilities-safety-board.png
layout: provider
modified: '2026-04-28'
name: Defense Nuclear Facilities Safety Board
nav: Providers
network: true
overview: 'Defense Nuclear Facilities Safety Board publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Defense, DNFSB, Energy, Federal-Government, and Health.


  Defense Nuclear Facilities Safety Board''s developer surface includes documentation, product news, and 6 more developer resources.'
plans:
- name: Defense Nuclear Facilities Safety Board Plans Pricing
  plan_count: 3
  slug: defense-nuclear-facilities-safety-board-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Defense Nuclear Facilities Safety Board Rate Limits
  slug: defense-nuclear-facilities-safety-board-rate-limits
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defense-nuclear-facilities-safety-board/refs/heads/main/screenshots/defense-nuclear-facilities-safety-board-2026-06-20T175836.png
security:
- kind: domain-security
  name: Defense Nuclear Facilities Safety Board Domain Security
  slug: defense-nuclear-facilities-safety-board-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: defense-nuclear-facilities-safety-board
tags:
- Defense
- DNFSB
- Energy
- Federal-Government
- Health
- Independent Agency
- Nuclear
- Safety
website: https://www.dnfsb.gov
---
