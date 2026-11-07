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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ApplyKoala offers a developer portal with guides and pricing but no public machine‑readable API specification was found.
  name: ApplyKoala API
  slug: applykoala-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/applykoala-com/plans/applykoala-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/applykoala-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/applykoala-com/llms/applykoala-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applykoala-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/applykoala-com/well-known/applykoala-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applykoala-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/applykoala-com/hosts/applykoala-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applykoala-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/applykoala-com/vendors/applykoala-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applykoala-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shangxiang0907
- group: auth
  href: https://artifacts.apis.io/applykoala-com/security/applykoala-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applykoala-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://applykoala.com/
- group: docs
  title: ''
  type: Documentation
  url: https://applykoala.com/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://applykoala.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://applykoala.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://applykoala.com/privacy
- group: company
  title: ''
  type: About
  url: https://applykoala.com/about
coverage:
  checked: '2026-11-01'
  detail: The provider's documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://applykoala.com/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: ApplyKoala provides a free AI‑enhanced job application tracker that lets users paste job postings, organize them, and use a Chrome extension to auto‑fill applications. The platform offers features like AI‑driven resume keyword checking, mock interviews, and job market insights, all without requiring sign‑up. It targets job seekers looking to streamline their application process with AI assistance.
image: https://applykoala.com/og.png
layout: provider
modified: '2026-11-01'
name: ApplyKoala
nav: Providers
network: true
overview: 'ApplyKoala is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Job-Tracker, Artificial Intelligence, Free, Chrome Extension, and Recruiting.


  ApplyKoala''s developer surface includes documentation, pricing, and 11 more developer resources.'
plans:
- name: Applykoala Com Plans Pricing
  plan_count: 3
  slug: applykoala-com-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 21.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Applykoala Com Domain Security
  slug: applykoala-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: applykoala-com
tags:
- Job-Tracker
- Artificial Intelligence
- Free
- Chrome Extension
- Recruiting
website: https://applykoala.com/
---
