---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: Alium API provides access to AI‑synthesized interview data and insights for brands.
  name: Alium API
  slug: alium-api-2
- baseURL: https://app.alium.io
  baseurl_source: declared
  description: The Alium API API from Alium — 2 operation(s) for alium api.
  name: Alium Alium API
  slug: alium-alium-api-api
- baseURL: https://app.alium.io
  baseurl_source: declared
  description: The Vendors API from Alium — 2 operation(s) for vendors.
  name: Alium Vendors API
  slug: alium-vendors-api
artifact_total: 7
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/alium/refs/heads/main/rate-limits/alium-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/alium-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alium/refs/heads/main/rules/alium-rules.yml
  title: ''
  type: Spectral
  url: rules/alium-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alium/refs/heads/main/authentication/alium-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alium-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alium/refs/heads/main/conformance/alium-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alium-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alium/refs/heads/main/well-known/alium-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alium-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alium/refs/heads/main/hosts/alium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alium-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alium/refs/heads/main/vendors/alium-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alium-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alium.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alium.io/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.alium.io/press
- group: company
  title: ''
  type: Blog
  url: https://www.alium.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alium.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alium/refs/heads/main/security/alium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alium.io/
coverage:
  checked: '2026-10-05'
  detail: Docs are served as a Docusaurus JavaScript app with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.alium.io/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-24'
description: Alium provides a platform where brands can access in‑depth, AI‑synthesized interviews with technology vendors. The service gathers compensated research from over 1,000 brand leaders, delivering actionable insights on vendor performance, risk, and suitability. Alium’s AI analyses these conversations to help marketers, CISOs, and IT directors make data‑driven decisions about technology partners.
image: http://static1.squarespace.com/static/5fd7cf5506a6f75916ae8f42/t/680b90f04bbb2150bb9d9b56/1749484506289/alium_icon_83x68_purple_white_a_RGB_04302021.png?format=1500w
layout: provider
modified: '2026-09-24'
name: Alium
nav: Providers
network: true
overview: 'Alium is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Alium API, Vendors API, and 1 more. Tagged areas include Vendor research, Marketing intelligence, E-Commerce, and Enterprise tech.


  The Alium catalog on APIs.io includes 1 Spectral governance ruleset.


  Alium''s developer surface includes authentication, engineering blog, documentation, and 11 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 4
  name: Alium Rate Limits
  slug: alium-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Alium API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: alium-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 46.5
    catalog_earned_first_party: 12.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 24.9
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 11.9
    developer_ergonomics: 23.8
    discoverability: 55.4
    operational_transparency: 31.6
  previous_composite: 0.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Alium Authentication
  slug: alium-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alium Domain Security
  slug: alium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alium
tags:
- Vendor research
- Marketing intelligence
- E-Commerce
- Enterprise tech
website: https://www.alium.io/
---
