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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Blitz Cloud platform
  name: Blitz Cloud API
  slug: blitz-cloud-api-2
- description: 'BlitzWorks API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BlitzWorks API
  slug: blitz-cloud-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/blitz-cloud/plans/blitz-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blitz-cloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blitz-cloud/rules/blitz-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/blitz-cloud-rules.yml
- group: design
  href: https://artifacts.apis.io/blitz-cloud/vocabulary/blitz-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blitz-cloud-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/blitz-cloud/cli/blitz-cloud-cli.yml
  title: ''
  type: CLI
  url: cli/blitz-cloud-cli.yml
- group: operate
  href: https://artifacts.apis.io/blitz-cloud/changelog/blitz-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blitz-cloud-changelog.yml
- group: design
  href: https://artifacts.apis.io/blitz-cloud/conformance/blitz-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blitz-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blitz-cloud/llms/blitz-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blitz-cloud-llms.txt
- group: other
  href: https://artifacts.apis.io/blitz-cloud/hosts/blitz-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blitz-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/blitz-cloud/vendors/blitz-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blitz-cloud-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blitz.cloud/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blitz.cloud/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blitz.cloud/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://blitz.cloud/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://blitz.cloud/changelog/
- group: company
  title: ''
  type: Blog
  url: https://blitz.cloud/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://blitz.cloud/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://blitz.cloud/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/blitz-cloud/security/blitz-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blitz-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blitz.cloud/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at the API host.
  evidence:
  - status: 404
    url: https://api.blitz.cloud/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Deploy your app, API or bot from GitHub and keep it online around the clock in the EU, with nightly backups. Try it free, Pro from 7 EUR a month. blitz.cloud puts apps online under an address that belongs to you, offering EU servers, backups, and AI integration.
image: https://blitz.cloud/og.png
layout: provider
modified: '2026-11-02'
name: BlitzWorks
nav: Providers
network: true
overview: 'BlitzWorks is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hosting, EU, Application, Bots, and Artificial Intelligence.


  The BlitzWorks catalog on APIs.io includes 1 Spectral governance ruleset.


  BlitzWorks'' developer surface includes CLI, changelog, documentation, engineering blog, pricing, getting-started guide, and 13 more developer resources.'
plans:
- name: Blitz Cloud Plans Pricing
  plan_count: 3
  slug: blitz-cloud-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 63
  extends:
  - spectral:oas
  name: BlitzWorks API Rules
  rule_count: 22
  severity_counts:
    error: 20
    hint: 0
    info: 1
    warn: 1
  slug: blitz-cloud-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blitz Cloud Domain Security
  slug: blitz-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blitz-cloud
tags:
- Hosting
- EU
- Application
- Bots
- Artificial Intelligence
- Company
website: https://blitz.cloud/
---
