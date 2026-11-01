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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/tnlmedia-com/hosts/tnlmedia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tnlmedia-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tnlmediagene.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tnlmediagene.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.tnlmediagene.com/news/announce
- group: other
  title: ''
  type: Leadership
  url: https://www.tnlmediagene.com/about/team
- group: auth
  href: https://artifacts.apis.io/tnlmedia-com/security/tnlmedia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tnlmedia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tnlmedia.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://tnlmedia.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: TNL Mediagene is an Asia‑focused digital and technology media group delivering next‑generation content, services, and advertising solutions across multiple markets. The company operates a network of media brands including Business Insider Japan, Cool3c, Digiday Japan, and many others, providing news, insights, and marketing platforms for technology and business audiences. Backed by 500‑global, TNL Mediagene connects brands with engaged readers through innovative digital experiences and partnerships across the region.
image: https://www.tnlmediagene.com/assets/images/og-image.png
layout: provider
modified: '2026-10-25'
name: tnlmedia
nav: Providers
network: true
overview: tnlmedia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Technology, Asia, Digital, and Advertising.
random_paper: 10
score:
  band: minimal
  composite: 9.2
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
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tnlmedia Com Domain Security
  slug: tnlmedia-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tnlmedia-com
tags:
- Media
- Technology
- Asia
- Digital
- Advertising
website: https://tnlmedia.com
---
