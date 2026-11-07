---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Buzzfy provides IoT device management and analytics services.
  name: Buzzfy API
  slug: buzzfy-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/buzzfy-co/plans/buzzfy-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buzzfy-co-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/buzzfy-co/llms/buzzfy-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buzzfy-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/buzzfy-co/well-known/buzzfy-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buzzfy-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/buzzfy-co/hosts/buzzfy-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buzzfy-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/buzzfy-co/vendors/buzzfy-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buzzfy-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buzzfy.co/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://buzzfy.co/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buzzfy.co/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://buzzfy.co/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Buzzfy
- group: auth
  href: https://artifacts.apis.io/buzzfy-co/security/buzzfy-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buzzfy-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buzzfy.co/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.buzzfy.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Buzzfy is an Instagram growth platform that re‑edits creators’ best reels, adding new openings, subtitles, backgrounds or reply stickers, then posts them as trial reels to reach new audiences. It offers analytics and comment‑to‑DM features, helping creators expand their reach without needing a large follower base.
image: https://buzzfy.co/opengraph-image
layout: provider
modified: '2026-11-03'
name: Buzzfy
nav: Providers
network: true
overview: 'Buzzfy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Instagram, Growth, Analytics, and Social Media.


  Buzzfy''s developer surface includes support, pricing, and 10 more developer resources.'
plans:
- name: Buzzfy Co Plans Pricing
  plan_count: 4
  slug: buzzfy-co-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 2.6
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
  name: Buzzfy Co Domain Security
  slug: buzzfy-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buzzfy-co
tags:
- Company
- Instagram
- Growth
- Analytics
- Social Media
website: https://buzzfy.co/
---
