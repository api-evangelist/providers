---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/adwhispr-com/llms/adwhispr-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adwhispr-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adwhispr-com/well-known/adwhispr-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adwhispr-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adwhispr-com/hosts/adwhispr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adwhispr-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adwhispr-com/vendors/adwhispr-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adwhispr-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://adwhispr.com/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://adwhispr.com/blog/connect-tiktok-ads-to-chatgpt
- group: auth
  href: https://artifacts.apis.io/adwhispr-com/security/adwhispr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adwhispr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adwhispr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://adwhispr.com/docs
- group: company
  title: ''
  type: Blog
  url: https://adwhispr.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adwhispr.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adwhispr.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://adwhispr.com/support
- group: start
  title: ''
  type: SignUp
  url: https://adwhispr.com/sign-up
coverage:
  checked: '2026-11-01'
  detail: Docs are public HTML but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found.
  evidence:
  - status: 200
    url: https://adwhispr.com/docs
  - status: 404
    url: https://adwhispr.com/openapi.json
  - status: 404
    url: https://api.adwhispr.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AdWhispr is an AI‑powered marketing agent that discovers competitors' winning ads, clones them for your brand, and launches campaigns across Meta, TikTok, Google and X. It provides a chat‑driven interface, prompt cookbook, and automation tools for ad research, creative generation, and real‑time campaign management, empowering marketers to accelerate performance and reduce creative costs.
image: https://adwhispr.com/adwhispr-logo.png
layout: provider
modified: '2026-10-31'
name: AdWhispr
nav: Providers
network: true
overview: 'AdWhispr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Advertising, Automation, and AdTech.


  AdWhispr''s developer surface includes changelog, getting-started guide, documentation, engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 6
scopes:
- name: Adwhispr Com Scopes
  scope_count: 0
  slug: adwhispr-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 21.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adwhispr Com Authentication
  slug: adwhispr-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adwhispr Com Domain Security
  slug: adwhispr-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adwhispr-com
tags:
- Artificial Intelligence
- Marketing
- Advertising
- Automation
- AdTech
website: https://adwhispr.com/
---
