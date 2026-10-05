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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainbuddy/refs/heads/main/hosts/brainbuddy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainbuddy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainbuddy/refs/heads/main/vendors/brainbuddy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainbuddy-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brainbuddyapp.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainbuddy/refs/heads/main/security/brainbuddy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainbuddy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brainbuddyapp.com
coverage:
  checked: '2026-10-03'
  detail: Brainbuddy's website provides no developer documentation or API reference, indicating no developer program.
  evidence:
  - status: 200
    url: https://www.brainbuddyapp.com
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Brainbuddy offers a mobile app focused on helping individuals overcome porn addiction through science-based behavioral therapy, tracking, and community support. The app provides personalized quizzes, progress metrics, and tools to rewire dopamine pathways, aiming to improve users' wellbeing, relationships, and motivation.
layout: provider
modified: '2026-10-03'
name: Brainbuddy
nav: Providers
network: true
overview: Brainbuddy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Addiction, Mobile App, and Wellness.
random_paper: 4
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainbuddy Domain Security
  slug: brainbuddy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brainbuddy
tags:
- Company
- Health
- Addiction
- Mobile App
- Wellness
website: https://www.brainbuddyapp.com
---
