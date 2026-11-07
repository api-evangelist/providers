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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/crowdhum-com/hosts/crowdhum-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdhum-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crowdhum-com/vendors/crowdhum-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdhum-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crowdhum.com/terms
- group: operate
  title: ''
  type: Support
  url: https://crowdhum.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crowdhum.com/privacy
- group: auth
  href: https://artifacts.apis.io/crowdhum-com/security/crowdhum-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdhum-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdhum.com/
coverage:
  checked: '2026-11-04'
  detail: CrowdHum provides a polling platform but offers no public developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://crowdhum.com/
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: CrowdHum provides a live audience polling platform that enables facilitators to quickly set up interactive polls using QR codes. Participants vote via their phones, with results displayed in real-time visualizations. The service requires no app installation, offers AI‑drafted questions, and delivers polished recap reports after each session. It targets meetings, workshops, conferences, and classrooms, emphasizing ease of use, instant setup, and engaging visual feedback.
layout: provider
modified: '2026-11-04'
name: CrowdHum
nav: Providers
network: true
overview: 'CrowdHum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AudiencePolling, Live Polling, QR Codes, Artificial Intelligence, and FacilitatorTools.


  CrowdHum''s developer surface includes support and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crowdhum Com Domain Security
  slug: crowdhum-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crowdhum-com
tags:
- AudiencePolling
- Live Polling
- QR Codes
- Artificial Intelligence
- FacilitatorTools
website: https://crowdhum.com/
---
