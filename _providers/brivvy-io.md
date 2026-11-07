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
    agent_card: conformant
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
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Brivvy provides AI‑powered writing tools via a developer API documented at https://docs.brivvy.io/
  name: Brivvy API
  slug: brivvy-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/brivvy-io/plans/brivvy-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brivvy-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/brivvy-io/changelog/brivvy-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brivvy-io-changelog.yml
- group: agent
  href: https://artifacts.apis.io/brivvy-io/llms/brivvy-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brivvy-io-llms.txt
- group: other
  href: https://artifacts.apis.io/brivvy-io/a2a/brivvy-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/brivvy-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/brivvy-io/well-known/brivvy-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brivvy-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/brivvy-io/hosts/brivvy-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brivvy-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/brivvy-io/vendors/brivvy-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brivvy-io-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://brivvy.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.brivvy.io/quickstart
- group: auth
  href: https://artifacts.apis.io/brivvy-io/security/brivvy-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brivvy-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brivvy.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brivvy.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://brivvy.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://brivvy.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brivvy.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brivvy.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brivvy.io/legal/privacy
coverage:
  checked: '2026-11-03'
  detail: Documentation is publicly available at https://docs.brivvy.io/ but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec could be found.
  evidence:
  - status: 404
    url: https://docs.brivvy.io/openapi.json
  - status: 403
    url: https://api.brivvy.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Brivvy builds AI‑powered writing tools that help modern teams create consistent brand voice across blogs, emails, and posts. Founded by Colin Pace, the platform offers voice creation, template management, and real‑time content generation, integrating with popular AI models like Claude, ChatGPT, Gemini, and Cursor. It aims to eliminate brand‑voice drift and improve workflow efficiency for marketing and product teams.
image: https://framerusercontent.com/images/1kLa4VaxPiy61BRhNwDLzPrC6K4.png
layout: provider
modified: '2026-11-03'
name: Brivvy
nav: Providers
network: true
overview: 'Brivvy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Writing, Marketing, and Collaboration.


  Brivvy''s developer surface includes changelog, getting-started guide, documentation, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Brivvy Io Plans Pricing
  plan_count: 3
  slug: brivvy-io-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brivvy Io Domain Security
  slug: brivvy-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brivvy-io
tags:
- Company
- Artificial Intelligence
- Writing
- Marketing
- Collaboration
- Voice
- Software-as-a-Service
website: https://brivvy.io/
---
