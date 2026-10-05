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
  href: https://raw.githubusercontent.com/api-evangelist/bondevalue/refs/heads/main/hosts/bondevalue-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bondevalue-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bondblox.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bondblox.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://bondblox.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bondevalue/refs/heads/main/security/bondevalue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bondevalue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bondblox.com
coverage:
  checked: '2026-10-02'
  detail: OpenAPI spec at https://api.bondblox.com/openapi.json requires authentication (403 Missing Authentication Token).
  evidence:
  - status: 403
    url: https://api.bondblox.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-02'
description: Bondevalue provides a digital platform for tracking and trading bonds, offering curated bond portfolios, market data, and trading tools to investors. The service is regulated by the Monetary Authority of Singapore as a Recognised Market Operator, delivering transparent bond pricing and portfolio management through its BondbloX platform.
image: https://d1j8yrnro58sx2.cloudfront.net/logo-200x200-oneline.jpg
layout: provider
modified: '2026-10-02'
name: Bondevalue
nav: Providers
network: true
overview: Bondevalue is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Bonds, Investment, Platform, and Singapore.
random_paper: 5
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 5
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bondevalue Domain Security
  slug: bondevalue-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bondevalue
tags:
- Fintech
- Bonds
- Investment
- Platform
- Singapore
website: https://bondblox.com
---
