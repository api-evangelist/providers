---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Branddock offers an API for managing brand identity and AI‑generated content, as described in the marketing documentation.
  name: Branddock API
  slug: branddock-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/branddock-app/plans/branddock-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/branddock-app-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/branddock-app/changelog/branddock-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/branddock-app-changelog.yml
- group: agent
  href: https://artifacts.apis.io/branddock-app/llms/branddock-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/branddock-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/branddock-app/well-known/branddock-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/branddock-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/branddock-app/hosts/branddock-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branddock-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/branddock-app/vendors/branddock-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branddock-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/branddock-app/packages/branddock-app-packages.yml
  title: ''
  type: SDKs
  url: packages/branddock-app-packages.yml
- group: build
  href: https://artifacts.apis.io/branddock-app/packages/branddock-app-packages.yml
  title: ''
  type: Packages
  url: packages/branddock-app-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://branddock.app/marketing/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://branddock.app/marketing/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://branddock.app/marketing/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://branddock.app/marketing/changelog
- group: auth
  href: https://artifacts.apis.io/branddock-app/security/branddock-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branddock-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://branddock.app/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.branddock.app/mcp
  - status: 401
    url: https://branddock.app/mcp
  - status: 401
    url: https://app.branddock.app/mcp
  - status: 200
    url: https://branddock.app/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Branddock provides a platform that captures a brand’s identity once and distributes it to AI systems such as Claude, ChatGPT, and custom tools. It offers AI‑team collaboration, campaign text generation, web‑page creation, and brand‑score checking with explanations, ensuring nothing goes live without approval. The service includes templates, team workflows, and integrations with analytics and payment providers, aiming to keep brand consistency across AI outputs.
image: https://branddock.app/marketing/og-image.png
layout: provider
modified: '2026-11-02'
name: Branddock
nav: Providers
network: true
overview: 'Branddock is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Branding, Collaboration, and Automation.


  Branddock''s developer surface includes changelog, pricing, and 12 more developer resources.'
plans:
- name: Branddock App Plans Pricing
  plan_count: 3
  slug: branddock-app-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    mcp: unknown
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
  name: Branddock App Domain Security
  slug: branddock-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: branddock-app
tags:
- Company
- Artificial Intelligence
- Branding
- Collaboration
- Automation
website: https://branddock.app/
---
