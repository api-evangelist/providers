---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dognote-app/well-known/dognote-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dognote-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/dognote-app/hosts/dognote-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dognote-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/dognote-app/vendors/dognote-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dognote-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.dognote.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.dognote.app/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rrebase
- group: docs
  title: ''
  type: Documentation
  url: https://help.dognote.app/
- group: auth
  href: https://artifacts.apis.io/dognote-app/security/dognote-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dognote-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dognote.app/
coverage:
  checked: '2026-11-05'
  detail: Documentation is served as a JavaScript-rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://help.dognote.app/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DogNote is a pet journal mobile application for iOS and Android that helps owners log events, care activities, and important information about their dogs and cats. The app consolidates pet health records, vaccination dates, feeding schedules, and daily activities into a single digital journal, providing reminders and insights to improve pet care.
image: https://dognote.app/page-preview.png
layout: provider
modified: '2026-11-05'
name: DogNote
nav: Providers
network: true
overview: 'DogNote is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pets, Mobile App, Journals, Health, and DogNote.


  DogNote''s developer surface includes documentation and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dognote App Domain Security
  slug: dognote-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dognote-app
tags:
- Pets
- Mobile App
- Journals
- Health
- DogNote
website: https://dognote.app/
---
