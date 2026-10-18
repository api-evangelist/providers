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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kargo-com/refs/heads/main/well-known/kargo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kargo-com-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.kargo.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kargo-com/refs/heads/main/hosts/kargo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kargo-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kargo-com/refs/heads/main/vendors/kargo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kargo-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.kargo.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kargo-com/refs/heads/main/security/kargo-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kargo-com-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kargo-com/refs/heads/main/security/kargo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kargo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kargo.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kargo.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kargo.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://blog.kargo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kargo
coverage:
  checked: '2026-10-14'
  detail: Docs at /assets-and-specs are served as a JavaScript shell, preventing machine-readable contract extraction.
  evidence:
  - status: 200
    url: https://www.kargo.com/assets-and-specs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Kargo provides a premium advertising platform that unifies technology, media, and creative to deliver digital ad experiences across all screens. Leveraging data intelligence and a proprietary creative engine, Kargo enables brands to create, activate, and measure campaigns on CTV, social, open web, and emerging platforms, offering end‑to‑end solutions from strategy to performance analytics.
layout: provider
modified: '2026-10-14'
name: Kargo
nav: Providers
network: true
overview: 'Kargo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Media, Technology, Marketing, and Platform.


  Kargo''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
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
  name: Kargo Com Domain Security
  slug: kargo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kargo Com Trust Center
  slug: kargo-com-trust-center
  summary_line: ISO 27001
slug: kargo-com
tags:
- Advertising
- Media
- Technology
- Marketing
- Platform
- Company
website: https://www.kargo.com
---
