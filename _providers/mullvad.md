---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://am.i.mullvad.net
  baseurl_source: declared
  description: 'Mullvad VPN API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Mullvad VPN API
  slug: mullvad-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/mullvad/plans/mullvad-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mullvad-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mullvad/rules/mullvad-rules.yml
  title: ''
  type: Spectral
  url: rules/mullvad-rules.yml
- group: design
  href: https://artifacts.apis.io/mullvad/vocabulary/mullvad-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mullvad-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://mullvad.net/en/help/how-report-bug-or-vulnerability/
- group: design
  href: https://artifacts.apis.io/mullvad/conformance/mullvad-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mullvad-conformance.yml
- group: auth
  href: https://artifacts.apis.io/mullvad/well-known/mullvad-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mullvad-security.txt
- group: agent
  href: https://artifacts.apis.io/mullvad/well-known/mullvad-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mullvad-well-known.yml
- group: other
  href: https://artifacts.apis.io/mullvad/hosts/mullvad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mullvad-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mullvad.net/en/help/terms-service
- group: operate
  title: ''
  type: Support
  url: https://mullvad.net/en/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mullvad.net/en/help/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://mullvad.net/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://mullvad.net/en/press
- group: start
  title: ''
  type: Login
  url: https://mullvad.net/en/account/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mullvad
- group: company
  title: ''
  type: Blog
  url: https://mullvad.net/en/blog
- group: auth
  href: https://artifacts.apis.io/mullvad/security/mullvad-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mullvad-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mullvad/security/mullvad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mullvad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mullvad.net/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on api.mullvad.net despite public documentation pages.
  evidence:
  - status: 404
    url: https://api.mullvad.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Mullvad VPN is a Swedish VPN service focused on privacy and security. It offers a no‑logs VPN with strong encryption, anonymous accounts, and a commitment to open‑source software. The company operates a global network of servers, provides a privacy‑focused browser, and publishes extensive documentation on usage, security, and open‑source contributions.
image: https://mullvad.net/press/MullvadVPN_logo_Round_RGB_Color_positive.png
layout: provider
modified: '2026-10-28'
name: Mullvad VPN
nav: Providers
network: true
overview: 'Mullvad VPN is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, VPN, Privacy, Open Source, and Security.


  The Mullvad VPN catalog on APIs.io includes 1 Spectral governance ruleset.


  Mullvad VPN''s developer surface includes support, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Mullvad Plans Pricing
  plan_count: 1
  slug: mullvad-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Mullvad VPN API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: mullvad-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 43.4
    contract_governance: 35.6
    contract_quality: 10.7
    developer_ergonomics: 3.6
    discoverability: 67.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 31.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mullvad/mullvad-2026-11-03T135911.png
security:
- kind: domain-security
  name: Mullvad Domain Security
  slug: mullvad-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mullvad Vulnerability Disclosure
  slug: mullvad-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mullvad
tags:
- Company
- VPN
- Privacy
- Open Source
- Security
website: https://mullvad.net/
---
