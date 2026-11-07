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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/validis/well-known/validis-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/validis-status-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.validis.com/privacy-security/
- group: agent
  href: https://artifacts.apis.io/validis/llms/validis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/validis-llms.txt
- group: agent
  href: https://artifacts.apis.io/validis/well-known/validis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/validis-well-known.yml
- group: other
  href: https://artifacts.apis.io/validis/hosts/validis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/validis-hosts.yml
- group: other
  href: https://artifacts.apis.io/validis/vendors/validis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/validis-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.validis.com/hc/en-gb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.validis.com/
- group: auth
  title: ''
  type: Security
  url: https://www.validis.com/in-practice/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.validis.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.validis.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.validis.com/
- group: auth
  href: https://artifacts.apis.io/validis/security/validis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/validis-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/validis/security/validis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/validis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://validis.com/
coverage:
  checked: '2026-10-21'
  detail: API documentation page returns HTML without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.validis.com/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Validis provides a financial data infrastructure that extracts, standardizes, and delivers transaction‑level accounting data via portal, API, or MCP server. It serves audit, commercial lending, specialist lending, and M&A due‑diligence teams, enabling faster data‑driven workflows and AI integration.
layout: provider
modified: '2026-10-21'
name: Validis
nav: Providers
network: true
overview: 'Validis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Audit, Commercial Lending, Specialist Lending, M&A Due Diligence, and Financial Data Infrastructure.


  Validis'' developer surface includes support, engineering blog, documentation, and 12 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 51.8
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/validis/validis-2026-11-03T145610.png
security:
- kind: domain-security
  name: Validis Domain Security
  slug: validis-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Validis Trust Center
  slug: validis-trust-center
  summary_line: SOC 2, ISO 27001
slug: validis
tags:
- Audit
- Commercial Lending
- Specialist Lending
- M&A Due Diligence
- Financial Data Infrastructure
website: https://validis.com/
---
