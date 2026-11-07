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
  href: https://artifacts.apis.io/clingsystems/security/clingsystems-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/clingsystems-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/clingsystems/llms/clingsystems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clingsystems-llms.txt
- group: auth
  href: https://artifacts.apis.io/clingsystems/well-known/clingsystems-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clingsystems-security.txt
- group: agent
  href: https://artifacts.apis.io/clingsystems/well-known/clingsystems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clingsystems-well-known.yml
- group: other
  href: https://artifacts.apis.io/clingsystems/hosts/clingsystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clingsystems-hosts.yml
- group: other
  href: https://artifacts.apis.io/clingsystems/vendors/clingsystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clingsystems-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clingsystems.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clingsystems.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clingsystems
- group: auth
  href: https://artifacts.apis.io/clingsystems/security/clingsystems-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clingsystems-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clingsystems/security/clingsystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clingsystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clingsystems.com
coverage:
  checked: '2026-10-09'
  detail: The public website provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://clingsystems.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Clingsystems (Cling Systems AB) brokers surplus and end‑of‑life batteries, helping owners sell them to buyers while handling compliance, waste classification and cross‑border shipping. Their mission is to accelerate circular battery value chains, offering a marketplace, inventory visibility and transparent pricing to unlock value that would otherwise be lost.
image: https://clingsystems.com/opengraph-image?2b1fbbf34287da78
layout: provider
modified: '2026-10-08'
name: Clingsystems
nav: Providers
network: true
overview: Clingsystems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Battery, Marketplace, Circular Economy, Sustainability, and Sweden.
random_paper: 21
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 12.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clingsystems/clingsystems-2026-11-03T124432.png
security:
- kind: domain-security
  name: Clingsystems Domain Security
  slug: clingsystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clingsystems Vulnerability Disclosure
  slug: clingsystems-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clingsystems
tags:
- Battery
- Marketplace
- Circular Economy
- Sustainability
- Sweden
website: https://clingsystems.com
---
