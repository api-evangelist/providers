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
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/devrelay-so/plans/devrelay-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/devrelay-so-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/devrelay-so/llms/devrelay-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/devrelay-so-llms.txt
- group: agent
  href: https://artifacts.apis.io/devrelay-so/well-known/devrelay-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/devrelay-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/devrelay-so/hosts/devrelay-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devrelay-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/devrelay-so/vendors/devrelay-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devrelay-so-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devrelay.so/terms
- group: auth
  title: ''
  type: Security
  url: https://devrelay.so/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devrelay.so/privacy
- group: auth
  href: https://artifacts.apis.io/devrelay-so/security/devrelay-so-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/devrelay-so-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/devrelay-so/security/devrelay-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devrelay-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devrelay.so/
- group: commercial
  title: ''
  type: Pricing
  url: https://devrelay.so/pricing
- group: company
  title: ''
  type: Blog
  url: https://devrelay.so/blog
coverage:
  checked: '2026-11-05'
  detail: Docs are served as a JavaScript‑rendered Next.js site with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://devrelay.so/pricing
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DevRelay is an AI DevRel employee that turns GitHub releases into posts, changelogs, and documentation updates. It automates the creation of marketing content, ensuring human approval before publishing. The service offers free and paid plans, integrates with GitHub, and provides a web interface for managing releases and generated content.
image: https://devrelay.so/og.png
layout: provider
modified: '2026-11-05'
name: DevRelay
nav: Providers
network: true
overview: 'DevRelay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, DevRel, Automation, GitHub, and Content.


  DevRelay''s developer surface includes pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Devrelay So Plans Pricing
  plan_count: 2
  slug: devrelay-so-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devrelay So Domain Security
  slug: devrelay-so-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Devrelay So Vulnerability Disclosure
  slug: devrelay-so-vulnerability-disclosure
  summary_line: no policy recorded
slug: devrelay-so
tags:
- Artificial Intelligence
- DevRel
- Automation
- GitHub
- Content
website: https://devrelay.so/
---
