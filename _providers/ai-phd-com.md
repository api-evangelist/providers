---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation is not publicly machine‑readable; the provider offers courses via website.
  name: AI PhD API
  slug: ai-phd-api
artifact_total: 3
common:
- group: operate
  href: https://artifacts.apis.io/ai-phd-com/changelog/ai-phd-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ai-phd-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/ai-phd-com/security/ai-phd-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ai-phd-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/ai-phd-com/llms/ai-phd-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-phd-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/ai-phd-com/well-known/ai-phd-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ai-phd-com-security.txt
- group: agent
  href: https://artifacts.apis.io/ai-phd-com/well-known/ai-phd-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai-phd-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ai-phd-com/hosts/ai-phd-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-phd-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-phd-com/vendors/ai-phd-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-phd-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai-phd.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai-phd.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://ai-phd.com/changelog
- group: auth
  href: https://artifacts.apis.io/ai-phd-com/security/ai-phd-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ai-phd-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ai-phd-com/security/ai-phd-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-phd-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-phd.com/
coverage:
  checked: '2026-11-01'
  detail: Provider's documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://ai-phd.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AI PhD offers AI education through a series of beginner-friendly courses and learning paths. It provides live AI‑instructed lessons, a single‑payment model, and a growing catalog of topics covering prompt engineering, AI agents, and automation. The platform aims to make AI accessible without subscriptions, delivering up‑to‑date content and hands‑on projects for learners at any level.
image: https://ai-phd.com/brand/ai-phd/og.png
layout: provider
modified: '2026-11-01'
name: AI PhD
nav: Providers
network: true
overview: 'AI PhD is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Artificial Intelligence, Courses, Learning, and Platform.


  AI PhD''s developer surface includes changelog and 12 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 18.4
  previous_composite: 14.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Phd Com Domain Security
  slug: ai-phd-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ai Phd Com Vulnerability Disclosure
  slug: ai-phd-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ai-phd-com
tags:
- Education
- Artificial Intelligence
- Courses
- Learning
- Platform
website: https://ai-phd.com/
---
