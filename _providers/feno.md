---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/feno/llms/feno-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/feno-llms.txt
- group: agent
  href: https://artifacts.apis.io/feno/well-known/feno-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/feno-well-known.yml
- group: other
  href: https://artifacts.apis.io/feno/hosts/feno-hosts.yml
  title: ''
  type: Hosts
  url: hosts/feno-hosts.yml
- group: other
  href: https://artifacts.apis.io/feno/vendors/feno-vendors.yml
  title: ''
  type: Vendors
  url: vendors/feno-vendors.yml
- group: auth
  href: https://artifacts.apis.io/feno/security/feno-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/feno-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://feno.co
- group: company
  title: ''
  type: Blog
  url: https://feno.co/blogs/news
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://feno.co/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://feno.co/pages/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://feno.co/pages/contact
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider’s hosts.
  evidence:
  - status: 0
    url: https://api.feno.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Feno is an oral‑care brand and maker of the Feno Smartbrush — the world’s first AI‑connected electric toothbrush. The Smartbrush uses artificial intelligence to provide smarter, more insightful brushing, cleaning every tooth at once for faster, more effective oral hygiene. Founded to bring advanced technology to everyday dental care, Feno combines hardware, software, and data analytics to improve oral health outcomes for consumers.
image: https://feno.co/cdn/shop/files/Group_1597880995.png?v=1785506308
layout: provider
modified: '2026-10-29'
name: Feno
nav: Providers
network: true
overview: 'Feno is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oral Care, HealthTech, Smartbrush, and AI.


  Feno''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Feno Domain Security
  slug: feno-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: feno
tags:
- Company
- Oral Care
- HealthTech
- Smartbrush
- AI
- Consumer Electronics
website: https://feno.co
---
