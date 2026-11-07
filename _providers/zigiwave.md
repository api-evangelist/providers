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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: ZigiOps integration platform API documentation
  name: ZigiOps API
  slug: zigiops-api
- description: 'ZigiWave API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: ZigiWave API
  slug: zigiwave-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/zigiwave/plans/zigiwave-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zigiwave-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zigiwave/rules/zigiwave-rules.yml
  title: ''
  type: Spectral
  url: rules/zigiwave-rules.yml
- group: design
  href: https://artifacts.apis.io/zigiwave/vocabulary/zigiwave-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zigiwave-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/zigiwave/changelog/zigiwave-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zigiwave-changelog.yml
- group: design
  href: https://artifacts.apis.io/zigiwave/conformance/zigiwave-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zigiwave-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zigiwave/llms/zigiwave-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zigiwave-llms.txt
- group: agent
  href: https://artifacts.apis.io/zigiwave/well-known/zigiwave-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zigiwave-well-known.yml
- group: other
  href: https://artifacts.apis.io/zigiwave/hosts/zigiwave-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zigiwave-hosts.yml
- group: other
  href: https://artifacts.apis.io/zigiwave/vendors/zigiwave-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zigiwave-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.zigiwave.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zigiwave.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://zigiwave.com/resources/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.zigiwave.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://zigiwave.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zigiwave.com/security/single-sign-on-setup-for-zigiops
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zigiwave.com/
- group: auth
  href: https://artifacts.apis.io/zigiwave/security/zigiwave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zigiwave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zigiwave.com/
coverage:
  checked: '2026-10-22'
  detail: Documentation pages are served as JavaScript-rendered HTML, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.zigiwave.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: ZigiWave provides ZigiOps, a secure integration platform that automates manual data synchronization between ServiceNow, Jira, Azure DevOps, Salesforce and over 50 other enterprise systems. Available as on‑premises or cloud SaaS, it offers real‑time two‑way sync without storing customer data, targeting ITSM, DevOps and business application integration use cases.
image: https://zigiwave.com/og-home.webp
layout: provider
modified: '2026-10-21'
name: ZigiWave
nav: Providers
network: true
overview: 'ZigiWave is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Automation, ITSM, DevOps, and Software-as-a-Service.


  The ZigiWave catalog on APIs.io includes 1 Spectral governance ruleset.


  ZigiWave''s developer surface includes changelog, support, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Zigiwave Plans Pricing
  plan_count: 3
  slug: zigiwave-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: ZigiWave API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: zigiwave-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 14.3
    discoverability: 65.2
    operational_transparency: 7.9
  previous_composite: 27.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/zigiwave/zigiwave-2026-11-03T150527.png
security:
- kind: domain-security
  name: Zigiwave Domain Security
  slug: zigiwave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zigiwave
tags:
- Integration
- Automation
- ITSM
- DevOps
- Software-as-a-Service
website: https://zigiwave.com/
---
