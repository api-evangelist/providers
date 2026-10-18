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
  href: https://raw.githubusercontent.com/api-evangelist/stc/refs/heads/main/hosts/stc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stc/refs/heads/main/vendors/stc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stc.com.sa/en/content-page/terms.html
- group: operate
  title: ''
  type: Support
  url: https://www.stc.com.sa/content/stc/sa/en/personal/support/faqs.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stc.com.sa/en/content-page/privacy.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.stc.com.sa/content/stc/sa/en/business/Industrial/media/audience-engagement.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stc/refs/heads/main/security/stc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stc.com.sa/
coverage:
  checked: '2026-10-13'
  detail: The provider's website does not expose any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.stc.com.sa/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: stc (Saudi Telecom Company) is the leading telecommunications provider in Saudi Arabia, offering a wide range of services including mobile, fixed-line, broadband internet, and digital solutions for consumers and businesses. The company operates a extensive network infrastructure and provides innovative digital platforms, aiming to connect people and enterprises across the Kingdom and beyond.
layout: provider
modified: '2026-10-13'
name: stc
nav: Providers
network: true
overview: 'stc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Saudi Arabia, Mobile, Broadband, and Digital Services.


  stc''s developer surface includes support and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 5
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
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 11.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stc Domain Security
  slug: stc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: stc
tags:
- Telecommunications
- Saudi Arabia
- Mobile
- Broadband
- Digital Services
- Company
website: https://www.stc.com.sa/
---
