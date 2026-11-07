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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/criptonoticias-com-br/llms/criptonoticias-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/criptonoticias-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/criptonoticias-com-br/well-known/criptonoticias-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/criptonoticias-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/criptonoticias-com-br/hosts/criptonoticias-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/criptonoticias-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/criptonoticias-com-br/vendors/criptonoticias-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/criptonoticias-com-br-vendors.yml
- group: auth
  href: https://artifacts.apis.io/criptonoticias-com-br/security/criptonoticias-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/criptonoticias-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.criptonoticias.com.br/
coverage:
  checked: '2026-11-04'
  detail: The site provides cryptocurrency news and has no developer documentation or API contracts.
  evidence:
  - status: 200
    url: https://www.criptonoticias.com.br/
  reason: not-a-software-company
  state: none
created: '2026-11-04'
description: CriptoNoticias BR is a Portuguese-language aggregator of cryptocurrency news in Brazil. It curates stories from multiple sources, summarizing them with AI and providing original links. The platform offers up-to-date market insights, project analyses, and educational content for Brazilian crypto enthusiasts, aiming to foster informed participation in the digital asset ecosystem.
image: https://www.criptonoticias.com.br/og/og-default.png
layout: provider
modified: '2026-11-04'
name: CriptoNoticias BR
nav: Providers
network: true
overview: CriptoNoticias BR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, News, Brazil, Aggregator, and Media.
random_paper: 0
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Criptonoticias Com Br Domain Security
  slug: criptonoticias-com-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: criptonoticias-com-br
tags:
- Cryptocurrency
- News
- Brazil
- Aggregator
- Media
website: https://www.criptonoticias.com.br/
---
