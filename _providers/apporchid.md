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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Enterprise semantic layer and decision intelligence platform API
  name: AppOrchid API
  slug: apporchid-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apporchid/refs/heads/main/changelog/apporchid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apporchid-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apporchid/refs/heads/main/llms/apporchid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apporchid-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apporchid/refs/heads/main/hosts/apporchid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apporchid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apporchid/refs/heads/main/vendors/apporchid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apporchid-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apporchid/refs/heads/main/packages/apporchid-packages.yml
  title: ''
  type: SDKs
  url: packages/apporchid-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apporchid/refs/heads/main/packages/apporchid-packages.yml
  title: ''
  type: Packages
  url: packages/apporchid-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apporchid.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.apporchid.com/category/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.apporchid.com/category/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.apporchid.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apporchid.com/getting-started/4.5-20260309-public
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apporchid.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apporchid/refs/heads/main/security/apporchid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apporchid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apporchid.com/
coverage:
  checked: 2026-09-25
  detail: Docs are served as a JavaScript SPA preventing direct spec retrieval.
  evidence:
  - status: 200
    url: https://docs.apporchid.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: AppOrchid provides an enterprise semantic layer and decision intelligence platform that unifies structured and unstructured data, enabling AI-ready insights, conversational analytics, and composable AI solutions. Their platform offers semantic SQL, easy answers, and AI suite tools for modern enterprises to build context-aware applications and drive next‑gen analytics.
image: https://cdn.prod.website-files.com/67d54aec2485fd10feb66f7e/6852c91fb9dcff446a5782cb_AO%20OG.jpg
layout: provider
modified: '2026-09-25'
name: AppOrchid
nav: Providers
network: true
overview: 'AppOrchid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Semantic Layer, Decision Intelligence, Enterprise AI, Data Fabric, and Conversational Analytics.


  AppOrchid''s developer surface includes changelog, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apporchid Domain Security
  slug: apporchid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: apporchid
tags:
- Semantic Layer
- Decision Intelligence
- Enterprise AI
- Data Fabric
- Conversational Analytics
- Knowledge Graph
- Semantic SQL
website: https://www.apporchid.com/
---
