---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'RadPod API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: RadPod API
  slug: radpod-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/radpod/plans/radpod-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/radpod-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/radpod/rules/radpod-rules.yml
  title: ''
  type: Spectral
  url: rules/radpod-rules.yml
- group: design
  href: https://artifacts.apis.io/radpod/vocabulary/radpod-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/radpod-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/radpod/cli/radpod-cli.yml
  title: ''
  type: CLI
  url: cli/radpod-cli.yml
- group: operate
  href: https://artifacts.apis.io/radpod/changelog/radpod-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/radpod-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://getcompound.ai/security
- group: auth
  href: https://artifacts.apis.io/radpod/authentication/radpod-authentication.yml
  title: ''
  type: Authentication
  url: authentication/radpod-authentication.yml
- group: design
  href: https://artifacts.apis.io/radpod/conformance/radpod-conformance.yml
  title: ''
  type: Conformance
  url: conformance/radpod-conformance.yml
- group: agent
  href: https://artifacts.apis.io/radpod/llms/radpod-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/radpod-llms.txt
- group: other
  href: https://artifacts.apis.io/radpod/hosts/radpod-hosts.yml
  title: ''
  type: Hosts
  url: hosts/radpod-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getcompound.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://getcompound.ai/help
- group: auth
  title: ''
  type: Security
  url: https://getcompound.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getcompound.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://getcompound.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://getcompound.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://getcompound.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://getcompound.ai/help/getting-started-overview
- group: auth
  href: https://artifacts.apis.io/radpod/security/radpod-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/radpod-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/radpod/security/radpod-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/radpod-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getcompound.ai/
created: '2026-10-22'
description: RadPod, operating as Compound, provides an AI platform for buy‑side finance, turning data rooms, filings, PDFs and Excel models into finished analyses, decks, and memos. The service leverages advanced large language models to automate financial research, offering secure, high‑performance AI agents that help firms accelerate decision‑making and reduce manual effort.
image: https://getcompound.ai/og-compound-v2.png
layout: provider
modified: '2026-10-22'
name: RadPod
nav: Providers
network: true
overview: 'RadPod is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Finance, Platform, and Automation.


  The RadPod catalog on APIs.io includes 1 Spectral governance ruleset.


  RadPod''s developer surface includes CLI, changelog, authentication, support, pricing, engineering blog, getting-started guide, and 14 more developer resources.'
plans:
- name: Radpod Plans Pricing
  plan_count: 6
  slug: radpod-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: RadPod API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: radpod-rules
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 10.5
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Radpod Authentication
  slug: radpod-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Radpod Domain Security
  slug: radpod-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Radpod Trust Center
  slug: radpod-trust-center
  summary_line: SOC 2, GDPR
slug: radpod
tags:
- Company
- AI
- Finance
- Platform
- Automation
website: https://getcompound.ai/
---
