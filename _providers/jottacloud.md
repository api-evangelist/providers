---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Jottacloud API is documented on the help center but no machine‑readable contract (OpenAPI, GraphQL, etc.) was found.
  name: Jottacloud API
  slug: jottacloud-api-2
- description: 'Jottacloud API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Jottacloud API
  slug: jottacloud-api
artifact_total: 8
asyncapis:
- description: ''
  name: Jottacloud Webhooks
  slug: jottacloud-webhooks
common:
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jottacloud.com/
- group: commercial
  href: https://artifacts.apis.io/jottacloud/plans/jottacloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jottacloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/jottacloud/rules/jottacloud-rules.yml
  title: ''
  type: Spectral
  url: rules/jottacloud-rules.yml
- group: design
  href: https://artifacts.apis.io/jottacloud/vocabulary/jottacloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jottacloud-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jottacloud/asyncapi/jottacloud-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jottacloud-webhooks.yml
- group: build
  href: https://artifacts.apis.io/jottacloud/cli/jottacloud-cli.yml
  title: ''
  type: CLI
  url: cli/jottacloud-cli.yml
- group: operate
  href: https://artifacts.apis.io/jottacloud/changelog/jottacloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jottacloud-changelog.yml
- group: auth
  href: https://artifacts.apis.io/jottacloud/security/jottacloud-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/jottacloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jottacloud/authentication/jottacloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jottacloud-authentication.yml
- group: design
  href: https://artifacts.apis.io/jottacloud/conformance/jottacloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jottacloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jottacloud/llms/jottacloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jottacloud-llms.txt
- group: auth
  href: https://artifacts.apis.io/jottacloud/well-known/jottacloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jottacloud-security.txt
- group: auth
  href: https://artifacts.apis.io/jottacloud/well-known/jottacloud-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jottacloud-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/jottacloud/well-known/jottacloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jottacloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/jottacloud/hosts/jottacloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jottacloud-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jottacloud.com/en/articles/2050941-desktop-easy-setup-disable-sync-and-move-sync-folder
- group: auth
  href: https://artifacts.apis.io/jottacloud/security/jottacloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jottacloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jottacloud/security/jottacloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jottacloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jottacloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jottacloud.com/
- group: company
  title: ''
  type: Blog
  url: https://jottacloud.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://jottacloud.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://jottacloud.com/signup/free?lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jottacloud.com/en/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jottacloud.com/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://jottacloud.com/en/contact
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://docs.jottacloud.com/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Jottacloud is a Norwegian cloud storage and backup service founded in 2008, offering secure, renewable‑energy‑powered storage for personal and business users. It provides web, desktop and mobile apps, automatic device backup, AI‑powered photo search, and compliance with European privacy laws. Over 1.9 million users trust Jottacloud for its reliability, encryption, and transparent pricing plans.
image: https://jottacloud.com/cms_uploads/_640x480_fit_center-center_75_none/61802/macinuse1-6_2024-07-02-095643_nnaj.jpg
layout: provider
modified: '2026-10-28'
name: Jottacloud
nav: Providers
network: true
overview: 'Jottacloud is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Storage, Backup, Norwegian, and Renewable Energy.


  The Jottacloud catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Jottacloud''s developer surface includes CLI, changelog, authentication, getting-started guide, documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Jottacloud Plans Pricing
  plan_count: 11
  slug: jottacloud-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Jottacloud API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: jottacloud-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 17.3
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - norway
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 46.1
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
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/jottacloud/jottacloud-2026-11-03T134231.png
security:
- kind: authentication
  name: Jottacloud Authentication
  slug: jottacloud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jottacloud Domain Security
  slug: jottacloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jottacloud Vulnerability Disclosure
  slug: jottacloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jottacloud
tags:
- Company
- Cloud Storage
- Backup
- Norwegian
- Renewable Energy
website: https://jottacloud.com/
---
