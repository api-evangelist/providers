---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
  score: 0.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chamberlaincoffee/refs/heads/main/well-known/chamberlaincoffee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chamberlaincoffee-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chamberlaincoffee/refs/heads/main/hosts/chamberlaincoffee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chamberlaincoffee-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chamberlaincoffee/refs/heads/main/vendors/chamberlaincoffee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chamberlaincoffee-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chamberlaincoffee.com/pages/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chamberlaincoffee.com/pages/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://chamberlaincoffee.com/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chamberlaincoffee/refs/heads/main/security/chamberlaincoffee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chamberlaincoffee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chamberlaincoffee.com
coverage:
  checked: '2026-10-08'
  detail: No public developer program or API documentation is available; the only API endpoint discovered (/api/mcp) returns 404.
  evidence:
  - status: 404
    url: https://chamberlaincoffee.com/api/mcp
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Chamberlain Coffee is a lifestyle coffee brand offering cold brew, matcha, and other specialty beverages. Founded by Emma Chamberlain, the company focuses on realness and community, providing a range of coffee products through its online store and retail partners. The brand emphasizes sustainability, quality sourcing, and a modern aesthetic that resonates with a youthful audience.
layout: provider
modified: '2026-10-08'
name: Chamberlaincoffee
nav: Providers
network: true
overview: Chamberlaincoffee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Coffee, Cold Brew, Matcha, Beverages, and Organic.
random_paper: 20
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chamberlaincoffee Domain Security
  slug: chamberlaincoffee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chamberlaincoffee
tags:
- Coffee
- Cold Brew
- Matcha
- Beverages
- Organic
website: https://chamberlaincoffee.com
---
