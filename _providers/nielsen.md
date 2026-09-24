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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nielsen/refs/heads/main/vendors/nielsen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nielsen-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nielsen/refs/heads/main/llms/nielsen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nielsen-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nielsen/refs/heads/main/well-known/nielsen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nielsen-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nielsen/refs/heads/main/hosts/nielsen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nielsen-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.nielsen.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nielsen.com/legal/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://help.nielsen.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nielsen.com/legal/privacy-principles/
- group: company
  title: ''
  type: Newsroom
  url: https://www.nielsen.com/insights/topic/media/
- group: other
  title: ''
  type: Leadership
  url: https://www.nielsen.com/about-us/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nielsen/refs/heads/main/security/nielsen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nielsen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nielsen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nielsen.com/solutions/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nielsen.com/solutions/
coverage:
  checked: 2026-09-22
  detail: Help portal requires sign‑in and provides no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://help.nielsen.com/hc/en-us
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: Nielsen provides audience measurement, media planning, and data analytics services worldwide, delivering insights across TV, digital, audio, and sports media. Their platforms help brands understand consumer behavior and optimize marketing strategies through comprehensive cross‑media measurement and audience segmentation.
image: https://www.nielsen.com/wp-content/uploads/sites/2/2024/01/home-page-meta-1200x675-1.jpg
layout: provider
modified: '2026-09-22'
name: Nielsen
nav: Providers
network: true
overview: 'Nielsen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audience Measurement, Media Analytics, DataInsights, and Marketing.


  Nielsen''s developer surface includes support, documentation, getting-started guide, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nielsen Domain Security
  slug: nielsen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nielsen
tags:
- Company
- Audience Measurement
- Media Analytics
- DataInsights
- Marketing
website: https://nielsen.com/
---
