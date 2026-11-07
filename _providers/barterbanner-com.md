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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/barterbanner-com/hosts/barterbanner-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barterbanner-com-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://barterbanner.com/register.html
- group: auth
  href: https://artifacts.apis.io/barterbanner-com/security/barterbanner-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barterbanner-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barterbanner.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://barterbanner.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://barterbanner.com/privacy
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint requires POST which is disallowed, blocking contract retrieval
  evidence:
  - status: 405
    url: https://barterbanner.com/mcp
  reason: auth-required
  state: gated
created: '2026-11-02'
description: BarterBanner is a network that helps publishers gain new readers by exchanging article placements across participating sites. The service is free to join and operates on an impression‑based credit system, where sites earn credits for displaying others’ content and spend them to have their own articles shown elsewhere. It supports multiple languages, offers a dashboard for tracking impressions and clicks, and emphasizes that no monetary payment is required, only space on the site for exchanged content.
image: https://barterbanner.com/og-image.png
layout: provider
modified: '2026-11-02'
name: BarterBanner
nav: Providers
network: true
overview: 'BarterBanner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Networks, Publishing, ContentExchange, and Multi-Language.


  BarterBanner''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barterbanner Com Domain Security
  slug: barterbanner-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: barterbanner-com
tags:
- Networks
- Publishing
- ContentExchange
- Multi-Language
website: https://barterbanner.com/
---
