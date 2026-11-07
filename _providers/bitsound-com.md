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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bitsound Com Agentic Access
  operation_count: 1
  slug: bitsound-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://bitsound.com
  baseurl_source: declared
  description: The Releases API from Bitsound — 1 operation(s) for releases.
  name: Bitsound Releases API
  slug: bitsound-com-releases-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/bitsound-com/agentic-access/bitsound-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bitsound-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bitsound-com/rules/bitsound-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bitsound-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bitsound-com/conformance/bitsound-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitsound-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bitsound-com/llms/bitsound-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitsound-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bitsound-com/well-known/bitsound-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitsound-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitsound-com/hosts/bitsound-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitsound-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitsound.com/terms
- group: operate
  title: ''
  type: Support
  url: https://bitsound.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitsound.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://bitsound.com/artists/fred-phage/releases
- group: company
  title: ''
  type: Blog
  url: https://bitsound.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://bitsound.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/bitsound-com/security/bitsound-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitsound-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitsound.com/
created: '2026-11-02'
description: Bitsound is an Austrian music store founded in 1998 that sells lossless audio files (FLAC, ALAC, WAV up to 24‑bit) directly from artists. It offers a subscription‑free, DRM‑free experience, returning 90% of revenue to creators. Customers can browse artists, discover new releases, and purchase high‑quality files without copy protection.
image: https://bitsound.com/og-image.png
layout: provider
modified: '2026-11-02'
name: Bitsound
nav: Providers
network: true
overview: 'Bitsound publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Releases API. Tagged areas include Company.


  The Bitsound catalog on APIs.io includes 1 Spectral governance ruleset.


  Bitsound''s developer surface includes support, changelog, engineering blog, API reference, and 10 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Bitsound API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: bitsound-com-rules
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 31.8
    contract_quality: 35.5
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - austria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitsound Com Domain Security
  slug: bitsound-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitsound-com
tags:
- Company
website: https://bitsound.com/
---
