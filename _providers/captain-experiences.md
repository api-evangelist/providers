---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides access to booking fishing and hunting trips, locations, guides, and trip details.
  name: Captain Experiences API
  slug: captain-experiences-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/captain-experiences/refs/heads/main/llms/captain-experiences-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/captain-experiences-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/captain-experiences/refs/heads/main/hosts/captain-experiences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/captain-experiences-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/captain-experiences/refs/heads/main/vendors/captain-experiences-vendors.yml
  title: ''
  type: Vendors
  url: vendors/captain-experiences-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://captainexperiences.com/policies/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://captainexperiences.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://captainexperiences.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://captainexperiences.com/guides
- group: company
  title: ''
  type: Blog
  url: https://captainexperiences.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/captainexperiences
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/captain-experiences/refs/heads/main/security/captain-experiences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/captain-experiences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://captainexperiences.com/
coverage:
  checked: '2026-10-07'
  detail: The provider's documentation pages are plain HTML/JS with no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://captainexperiences.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Captain Experiences provides guided fishing and hunting trips across North America and the Caribbean. Their platform lets users browse locations, book experienced captains, and customize outdoor adventures ranging from half‑day fishing trips to multi‑day hunting expeditions. The service emphasizes local expertise, safety, and sustainable wildlife practices, offering detailed trip itineraries, gear rentals, and customer reviews to help plan memorable experiences.
image: https://captainexperiences.com/images/pwa/icon384.png
layout: provider
modified: '2026-10-06'
name: Captain Experiences
nav: Providers
network: true
overview: 'Captain Experiences is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Outdoors, Travel, Fishing, and Hunting.


  Captain Experiences'' developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Captain Experiences Domain Security
  slug: captain-experiences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: captain-experiences
tags:
- Company
- Outdoors
- Travel
- Fishing
- Hunting
website: https://captainexperiences.com/
---
