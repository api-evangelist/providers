---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - '{''url'': ''https://developers.icy.tools/'', ''status'': 301, ''note'': ''declared website redirects to https://www.quicknode.com/?utm_source=icy.tools — a different registrable domain (icy.tools -> quicknode.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 1
apis:
- description: GraphQL based NFT API
  name: icy.tools
  slug: icytools
artifact_total: 4
common:
- group: company
  title: ''
  type: Blog
  url: https://www.quicknode.com/blog
- group: auth
  href: https://artifacts.apis.io/icy-tools/security/icy-tools-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/icy-tools-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/icy-tools/security/icy-tools-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/icy-tools-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/icy-tools/security/icy-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/icy-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developers.icy.tools/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: GraphQL based NFT API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/icy-tools.png
layout: provider
modified: '2026-10-06'
name: icy.tools
nav: Providers
network: true
overview: 'icy.tools is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency and Public APIs.


  icy.tools'' developer surface includes engineering blog and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 10.5
  previous_composite: 8.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/icy-tools/icy-tools-2026-06-20T183202.png
security:
- kind: domain-security
  name: Icy Tools Domain Security
  slug: icy-tools-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Icy Tools Vulnerability Disclosure
  slug: icy-tools-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Icy Tools Trust Center
  slug: icy-tools-trust-center
  summary_line: SOC 2, ISO 27001
slug: icy-tools
tags:
- Cryptocurrency
- Public APIs
website: https://developers.icy.tools/
---
