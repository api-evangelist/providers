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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/duchamp-app/plans/duchamp-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duchamp-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/duchamp-app/llms/duchamp-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duchamp-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/duchamp-app/well-known/duchamp-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duchamp-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/duchamp-app/hosts/duchamp-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duchamp-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/duchamp-app/vendors/duchamp-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duchamp-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://duchamp.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://duchamp.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://duchamp.app/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duchamp-app
- group: auth
  href: https://artifacts.apis.io/duchamp-app/security/duchamp-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duchamp-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duchamp.app/
coverage:
  checked: '2026-11-06'
  detail: Documentation pages are rendered client‑side JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://duchamp.app/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: Duchamp (뒤샹) is a competitive advertising analysis tool that aggregates Meta ads for competitors, providing daily updates on new, paused, and long-running ads. It offers AI‑enhanced insights via Claude Code·Codex MCP, delivering ad copy, landing pages, keyframes, and transcription data for deep market research.
image: https://duchamp.app/opengraph-image.png?opengraph-image.1e2v4xjwtbxsd.png
layout: provider
modified: '2026-11-06'
name: Duchamp
nav: Providers
network: true
overview: 'Duchamp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Competitive Intelligence, Artificial Intelligence, and Marketing.


  Duchamp''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Duchamp App Plans Pricing
  plan_count: 2
  slug: duchamp-app-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Duchamp App Domain Security
  slug: duchamp-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: duchamp-app
tags:
- Company
- Advertising
- Competitive Intelligence
- Artificial Intelligence
- Marketing
- Analytics
website: https://duchamp.app/
---
