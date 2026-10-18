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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coverstar/refs/heads/main/llms/coverstar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coverstar-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coverstar/refs/heads/main/hosts/coverstar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coverstar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coverstar/refs/heads/main/vendors/coverstar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coverstar-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coverstar/refs/heads/main/security/coverstar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coverstar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coverstar.app
- group: docs
  title: ''
  type: Documentation
  url: https://help.coverstar.app/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.coverstar.app/hc/en-us/articles/33465077115668-Privacy-Policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.coverstar.app/hc/en-us/articles/33484714669332-Terms-of-Service
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's documented hosts.
  evidence:
  - status: 200
    url: https://help.coverstar.app/hc/en-us
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: CoverStar is a safe social platform designed as an alternative to TikTok for children and teens aged 9-16. It emphasizes creativity, positivity, and safety through AI‑assisted and human moderation, with no direct messages and strict content controls. The app offers avatar‑based creation, live streaming, challenges, and a marketplace for creative expression, aiming to provide a secure online community for young users.
image: https://coverstar.app/img/coverstar-og-image.jpg
layout: provider
modified: '2026-10-12'
name: CoverStar
nav: Providers
network: true
overview: 'CoverStar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Kids, Safety, and Creative.


  CoverStar''s developer surface includes documentation and 7 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coverstar Domain Security
  slug: coverstar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coverstar
tags:
- Company
- Social
- Kids
- Safety
- Creative
website: https://coverstar.app
---
