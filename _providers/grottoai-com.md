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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/grottoai-com/hosts/grottoai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/grottoai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/grottoai-com/vendors/grottoai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/grottoai-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.grotto.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grotto.ai/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://grotto.ai/press
- group: company
  title: ''
  type: Blog
  url: https://grotto.ai/blog
- group: auth
  href: https://artifacts.apis.io/grottoai-com/security/grottoai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grottoai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grotto.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://grotto.ai/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Grotto AI is an emerging artificial intelligence platform that provides developers with powerful APIs for natural language processing, image analysis, and data insight generation. Backed by iconiq-capital, the company focuses on delivering scalable AI services that integrate seamlessly into modern applications, enabling businesses to automate content creation, enhance user experiences, and unlock actionable intelligence from unstructured data sources. The platform emphasizes privacy, security, and compliance, offering robust documentation and developer support to accelerate adoption across industries.
image: https://grotto.ai/images/og-default.jpg
layout: provider
modified: '2026-10-25'
name: Grotto AI
nav: Providers
network: true
overview: 'Grotto AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Machine Learning, NLP, and Image Analysis.


  Grotto AI''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Grottoai Com Domain Security
  slug: grottoai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grottoai-com
tags:
- Company
- AI
- Machine Learning
- NLP
- Image Analysis
- Data Insights
website: https://grotto.ai/
---
