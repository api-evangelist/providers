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
api_count: 1
apis:
- description: API for Clarity Briefs platform (no public machine-readable spec discovered)
  name: Clarity Briefs API
  slug: clarity-briefs-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/claritybriefs-com/hosts/claritybriefs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claritybriefs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/claritybriefs-com/vendors/claritybriefs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claritybriefs-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claritybriefs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claritybriefs.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://claritybriefs.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://claritybriefs.com/news/
- group: start
  title: ''
  type: Login
  url: https://claritybriefs.com/auth/login
- group: company
  title: ''
  type: Blog
  url: https://claritybriefs.com/blog
- group: auth
  href: https://artifacts.apis.io/claritybriefs-com/security/claritybriefs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claritybriefs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claritybriefs.com/
- group: other
  title: ''
  type: Coverage
  url: '#'
created: '2026-11-03'
description: 'claritybriefs-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://claritybriefs.com/static/img/og-image.png
layout: provider
modified: '2026-11-03'
name: claritybriefs-com
nav: Providers
network: true
overview: 'claritybriefs-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  claritybriefs-com''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 40.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Claritybriefs Com Domain Security
  slug: claritybriefs-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: claritybriefs-com
tags:
- Company
website: https://claritybriefs.com/
---
