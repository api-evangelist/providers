---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Smart hospitality software API providing access to reservations, housekeeping, channel management, and analytics.
  name: umnify API
  slug: umnify-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/umnify/llms/umnify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/umnify-llms.txt
- group: other
  href: https://artifacts.apis.io/umnify/hosts/umnify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/umnify-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://umnify.com/register/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://umnify.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://umnify.com/news/
- group: company
  title: ''
  type: Blog
  url: https://umnify.com/blog/author/daniel/
- group: auth
  href: https://artifacts.apis.io/umnify/security/umnify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/umnify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://umnify.com/
coverage:
  checked: '2026-10-28'
  detail: API base URL returns HTTP 403, indicating access requires authentication.
  evidence:
  - status: 403
    url: https://api.umnify.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-28'
description: umnify provides smart hospitality software solutions for hotels and apartment houses, offering a suite of applications that streamline operations, enhance guest experiences, and improve revenue management. Their platform includes tools for reservations, housekeeping, channel management, and analytics, targeting the German market and expanding internationally.
image: https://umnify.com/wp-content/uploads/2024/06/Uminfy_Logo-1.png
layout: provider
modified: '2026-10-28'
name: umnify
nav: Providers
network: true
overview: 'umnify is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Software, Hotel Management, German Market, and SaaS.


  umnify''s developer surface includes signup flow, engineering blog, and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Umnify Domain Security
  slug: umnify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: umnify
tags:
- Hospitality
- Software
- Hotel Management
- German Market
- SaaS
website: https://umnify.com/
---
