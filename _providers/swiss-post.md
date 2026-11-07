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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Developer portal providing API documentation for Swiss Post services.
  name: Swiss Post API
  slug: swiss-post-api-2
- baseURL: https://api.post.ch
  baseurl_source: declared
  description: 'Swiss Post API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Swiss Post API
  slug: swiss-post-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/swiss-post/rules/swiss-post-rules.yml
  title: ''
  type: Spectral
  url: rules/swiss-post-rules.yml
- group: design
  href: https://artifacts.apis.io/swiss-post/json-ld/swiss-post-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/swiss-post-context.jsonld
- group: design
  href: https://artifacts.apis.io/swiss-post/vocabulary/swiss-post-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/swiss-post-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/swiss-post/data-model/swiss-post-data-model.yml
  title: ''
  type: DataModel
  url: data-model/swiss-post-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.post.ch/p/Information-Security
- group: design
  href: https://artifacts.apis.io/swiss-post/conformance/swiss-post-conformance.yml
  title: ''
  type: Conformance
  url: conformance/swiss-post-conformance.yml
- group: auth
  href: https://artifacts.apis.io/swiss-post/well-known/swiss-post-webstamp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swiss-post-webstamp-security.txt
- group: auth
  href: https://artifacts.apis.io/swiss-post/well-known/swiss-post-shop-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swiss-post-shop-security.txt
- group: auth
  href: https://artifacts.apis.io/swiss-post/well-known/swiss-post-service-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swiss-post-service-security.txt
- group: auth
  href: https://artifacts.apis.io/swiss-post/well-known/swiss-post-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swiss-post-security.txt
- group: auth
  href: https://artifacts.apis.io/swiss-post/well-known/swiss-post-promopost-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swiss-post-promopost-security.txt
- group: auth
  href: https://artifacts.apis.io/swiss-post/well-known/swiss-post-post-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swiss-post-post-security.txt
- group: auth
  href: https://artifacts.apis.io/swiss-post/well-known/swiss-post-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swiss-post-help-security.txt
- group: auth
  href: https://artifacts.apis.io/swiss-post/well-known/swiss-post-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swiss-post-developer-security.txt
- group: agent
  href: https://artifacts.apis.io/swiss-post/well-known/swiss-post-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/swiss-post-well-known.yml
- group: other
  href: https://artifacts.apis.io/swiss-post/hosts/swiss-post-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swiss-post-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.post.ch/de
- group: start
  title: ''
  type: SignUp
  url: https://www.post.ch/en/sending-letters/registered-mail/registered-international
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.post.ch/en/pages/footer/data-protection-and-disclaimer/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.post.ch/en/business-solutions/e-mail-encryption/news/2017/incamail-release-4-3
- group: auth
  href: https://artifacts.apis.io/swiss-post/security/swiss-post-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/swiss-post-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/swiss-post/security/swiss-post-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swiss-post-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://post.ch/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.post.ch/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.post.ch/de
- group: company
  title: ''
  type: About
  url: https://www.post.ch/de/ueber-uns
coverage:
  checked: '2026-10-28'
  detail: Developer portal pages render via JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://post.ch/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Swiss Post AG is the national postal service of Switzerland, offering mail, parcel, logistics, financial and digital services. It connects people, businesses and regions with reliable delivery, e‑commerce solutions, sustainability initiatives and innovative digital platforms.
image: https://www.post.ch/-/media/portal-opp/global/logos/logo---die-post_long.svg?vs=1
json_schemas:
- name: PostOrdersOrderkeyApprovalResponse
  property_count: 3
  slug: swiss-post-post-orders-orderkey-approval-response
- name: PostOrdersResponse
  property_count: 3
  slug: swiss-post-post-orders-response
- name: PostPostcardsRequest
  property_count: 2
  slug: swiss-post-post-postcards-request
- name: PostPostcardsResponse
  property_count: 3
  slug: swiss-post-post-postcards-response
- name: PutPostcardsCardkeyBrandingQrtagRequest
  property_count: 4
  slug: swiss-post-put-postcards-cardkey-branding-qrtag-request
- name: PutPostcardsCardkeyBrandingTextRequest
  property_count: 3
  slug: swiss-post-put-postcards-cardkey-branding-text-request
jsonld:
- class_count: 20
  name: Swiss Post Context
  property_count: 20
  slug: swiss-post-context
layout: provider
modified: '2026-10-28'
name: Swiss Post
nav: Providers
network: true
overview: 'Swiss Post is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Postal Service, Logistics, Finance, and Digital Services.


  The Swiss Post catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Swiss Post''s developer surface includes support, signup flow, documentation, and 23 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Swiss Post API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: swiss-post-rules
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 11.9
    discoverability: 58.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/swiss-post/swiss-post-2026-11-03T144201.png
security:
- kind: domain-security
  name: Swiss Post Domain Security
  slug: swiss-post-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Swiss Post Vulnerability Disclosure
  slug: swiss-post-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: swiss-post
tags:
- Company
- Postal Service
- Logistics
- Finance
- Digital Services
- Switzerland
website: https://post.ch/
---
