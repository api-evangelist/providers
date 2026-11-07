---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
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
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Lexoo website at lexoo.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Lexoo Website (WordPress REST)
  slug: lexoo-com-website-wordpress-rest
- description: Lexoo's WordPress site publishes a standard RSS 2.0 feed at /feed/ for its main content stream. The feed is well-formed and reachable but currently carries no items, because the site publishes pages o
  name: Lexoo RSS Feed
  slug: rss-feed
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/lexoo/security/lexoo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lexoo-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/lexoo/llms/lexoo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lexoo-llms.txt
- group: company
  title: ''
  type: Website
  url: https://lexoo.com/
- group: company
  title: ''
  type: About
  url: https://lexoo.com/team/
- group: operate
  title: ''
  type: Contact
  url: mailto:team@lexoo.com
- group: other
  title: ''
  type: Product
  url: https://lexoo.com/contract-review/
- group: other
  title: ''
  type: Product
  url: https://lexoo.com/multi-country-projects/
- group: other
  title: ''
  type: Product
  url: https://lexoo.com/scale-ups-start-ups/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lexoolimited
created: '2026-07-17'
description: 'Lexoo is a commercial legal services provider that operates as an outsourced in-house legal team for businesses, concentrating on commercial contract review and negotiation. The company handles routine contract work at fixed rates per agreement with a stated maximum two-day turnaround, so internal legal and sales teams are freed for more strategic work. Alongside contract review, Lexoo runs multi-country projects that engage local counsel across more than 70 countries for work such as terms and conditions localisation and regulatory research, and it builds playbooks and training materials that let client teams handle standard agreements independently. The practice is led by Nathalie Lambert and serves scale-ups and start-ups, with published client references including Trustpilot, Nielsen, ComplyAdvantage, Xeneta, Chattermill and Jokr. Lexoo is not an API-first company: it publishes no developer portal, documentation or SDKs, and its only machine-readable surfaces are the standard
  WordPress REST API and RSS feed exposed by its marketing site.'
image: https://lexoo.com/wp-content/uploads/2024/10/cropped-lexoo-logo-IN-Copy-192x192.png
layout: provider
modified: '2026-07-19'
name: Lexoo
nav: Providers
network: true
overview: Lexoo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Legal Services, Contract Review, Compliance, and Professional Services.
random_paper: 23
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 6.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lexoo/lexoo-2026-07-25T225002.png
security:
- kind: domain-security
  name: Lexoo Domain Security
  slug: lexoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lexoo
tags:
- Legal
- Legal Services
- Contract Review
- Compliance
- Professional Services
- Legal Tech
- Consulting
website: https://lexoo.com/
---
