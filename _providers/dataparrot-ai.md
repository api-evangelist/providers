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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API documentation for Data Parrot AI providing revenue intelligence features.
  name: Data Parrot API
  slug: data-parrot-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/dataparrot-ai/plans/dataparrot-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dataparrot-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dataparrot-ai/changelog/dataparrot-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dataparrot-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/dataparrot-ai/security/dataparrot-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dataparrot-ai-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/dataparrot-ai/llms/dataparrot-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataparrot-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/dataparrot-ai/well-known/dataparrot-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dataparrot-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/dataparrot-ai/well-known/dataparrot-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataparrot-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dataparrot-ai/hosts/dataparrot-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataparrot-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataparrot-ai/vendors/dataparrot-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataparrot-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataparrot.ai/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://dataparrot.ai/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataparrot.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://dataparrot.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://dataparrot.ai/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://dataparrot.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://dataparrot.ai/md/docs/getting-started/custom-ai-properties-in-hubspot
- group: docs
  title: ''
  type: Documentation
  url: https://help.dataparrot.ai/
- group: auth
  href: https://artifacts.apis.io/dataparrot-ai/security/dataparrot-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dataparrot-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dataparrot-ai/security/dataparrot-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataparrot-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataparrot.ai/
coverage:
  checked: '2026-11-05'
  detail: Docs site https://dataparrot.ai/docs returns a JavaScript challenge preventing static retrieval of API specs.
  evidence:
  - status: 403
    url: https://dataparrot.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Data Parrot AI provides an AI‑powered revenue intelligence platform that transforms CRM data into actionable insights. It helps CEOs and CROs see deal health, pipeline status, sales activity, and customer engagement, enabling faster decision‑making and higher win rates across the organization.
image: https://dataparrot.ai/screenshots/deals.png
layout: provider
modified: '2026-11-05'
name: Data Parrot
nav: Providers
network: true
overview: 'Data Parrot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Revenue Intelligence, CRM, Sales Analytics, and Data Platform.


  Data Parrot''s developer surface includes changelog, signup flow, pricing, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Dataparrot Ai Plans Pricing
  plan_count: 4
  slug: dataparrot-ai-plans-pricing
random_paper: 1
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dataparrot Ai Domain Security
  slug: dataparrot-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dataparrot Ai Vulnerability Disclosure
  slug: dataparrot-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dataparrot-ai
tags:
- Artificial Intelligence
- Revenue Intelligence
- CRM
- Sales Analytics
- Data Platform
- Company
website: https://dataparrot.ai/
---
