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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cencorpautomation/refs/heads/main/hosts/cencorpautomation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cencorpautomation-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cencorpautomation.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cencorpautomation/refs/heads/main/security/cencorpautomation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cencorpautomation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cencorpautomation.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cencorpautomation.com/privacypolicy
- group: other
  title: ''
  type: CookiePolicy
  url: https://cencorpautomation.com/cookie-policy
- group: operate
  title: ''
  type: Contact
  url: https://cencorpautomation.com/contact
coverage:
  checked: '2026-10-07'
  detail: No public developer program or API documentation is available on the company's website.
  evidence:
  - status: 200
    url: https://cencorpautomation.com
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Cencorpautomation, operating under the brand Cencorp Automation, specializes in back-end automation solutions for the electronics industry. It offers advanced production automation, depaneling, odd-form placement, test handling, and laser processing technologies. The company serves leading automotive, telecom, consumer, and industrial manufacturers, focusing on improving productivity, quality, and traceability across complex manufacturing workflows.
layout: provider
modified: '2026-10-07'
name: Cencorpautomation
nav: Providers
network: true
overview: Cencorpautomation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Depaneling, Placement, Automation, Lasers, and Test Handling.
random_paper: 9
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 8
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
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cencorpautomation Domain Security
  slug: cencorpautomation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cencorpautomation
tags:
- Depaneling
- Placement
- Automation
- Lasers
- Test Handling
- Electronics Manufacturing
website: https://cencorpautomation.com
---
