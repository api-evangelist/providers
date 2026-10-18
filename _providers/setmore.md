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
  href: https://raw.githubusercontent.com/api-evangelist/setmore/refs/heads/main/vendors/setmore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/setmore-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/setmore/refs/heads/main/llms/setmore-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/setmore-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/setmore/refs/heads/main/hosts/setmore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/setmore-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.setmore.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.setmore.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.setmore.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.setmore.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.setmore.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.setmore.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.setmore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.setmore.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/setmore/refs/heads/main/security/setmore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/setmore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.setmore.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.setmore.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Setmore provides free online appointment scheduling software for businesses of all sizes. Its platform enables customers to book appointments, manage staff schedules, accept payments, and integrate with popular calendars and marketing tools. Setmore aims to help businesses deliver their magic by connecting them with customers through a seamless, customizable booking experience across web, mobile, and social channels.
image: https://assets.setmore.com/website/v2/images/og-images/homepage/setmore-og-website-homepage.jpg
layout: provider
modified: '2026-10-13'
name: Setmore
nav: Providers
network: true
overview: 'Setmore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Scheduling, Software-as-a-Service, Appointment, BusinessTools, and Company.


  Setmore''s developer surface includes support, engineering blog, documentation, and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Setmore Domain Security
  slug: setmore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: setmore
tags:
- Scheduling
- Software-as-a-Service
- Appointment
- BusinessTools
- Company
website: https://www.setmore.com
---
