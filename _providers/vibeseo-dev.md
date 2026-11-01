---
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
  score: 18.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/vibeseo-dev/plans/vibeseo-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vibeseo-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/vibeseo-dev/llms/vibeseo-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vibeseo-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/vibeseo-dev/well-known/vibeseo-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vibeseo-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/vibeseo-dev/hosts/vibeseo-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vibeseo-dev-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vibeseo.dev/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vibeseo.dev/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://vibeseo.dev/login
- group: auth
  href: https://artifacts.apis.io/vibeseo-dev/security/vibeseo-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vibeseo-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vibeseo.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://vibeseo.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://vibeseo.dev/blog/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the API host or documentation pages.
  evidence:
  - status: 404
    url: https://api.vibeseo.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: VibeSEO provides an AI‑powered SEO platform that creates, publishes, and optimizes website content to rank highly on Google and emerging AI search assistants. The service offers automated article generation, keyword research, backlink analysis, and continuous monitoring of brand mentions across AI models like ChatGPT and Gemini. Pricing is usage‑based with credit packs, and the platform integrates with popular site builders and browsers to streamline SEO workflows for businesses of all sizes.
image: https://vibeseo.dev/brand/vibeseo-og.jpg
layout: provider
modified: '2026-10-30'
name: vibeseo-dev
nav: Providers
network: true
overview: 'vibeseo-dev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, SEO, Marketing, and Automation.


  vibeseo-dev''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Vibeseo Dev Plans Pricing
  plan_count: 3
  slug: vibeseo-dev-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vibeseo Dev Domain Security
  slug: vibeseo-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vibeseo-dev
tags:
- Company
- AI
- SEO
- Marketing
- Automation
website: https://vibeseo.dev/
---
