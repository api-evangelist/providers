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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Vibgrate code‑drift intelligence platform, documented at the developer portal.
  name: Vibgrate API
  slug: vibgrate-api
- description: 'vibgrate-com API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: vibgrate-com API
  slug: vibgrate-com-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/vibgrate-com/plans/vibgrate-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vibgrate-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vibgrate-com/rules/vibgrate-com-rules.yml
  title: ''
  type: Spectral
  url: rules/vibgrate-com-rules.yml
- group: design
  href: https://artifacts.apis.io/vibgrate-com/vocabulary/vibgrate-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vibgrate-com-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/vibgrate-com/cli/vibgrate-com-cli.yml
  title: ''
  type: CLI
  url: cli/vibgrate-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/vibgrate-com/changelog/vibgrate-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vibgrate-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://vibgrate.com/trust/
- group: design
  href: https://artifacts.apis.io/vibgrate-com/conformance/vibgrate-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vibgrate-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vibgrate-com/llms/vibgrate-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vibgrate-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/vibgrate-com/well-known/vibgrate-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vibgrate-com-security.txt
- group: agent
  href: https://artifacts.apis.io/vibgrate-com/well-known/vibgrate-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vibgrate-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/vibgrate-com/hosts/vibgrate-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vibgrate-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/vibgrate-com/vendors/vibgrate-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vibgrate-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/vibgrate-com/packages/vibgrate-com-packages.yml
  title: ''
  type: SDKs
  url: packages/vibgrate-com-packages.yml
- group: build
  href: https://artifacts.apis.io/vibgrate-com/packages/vibgrate-com-packages.yml
  title: ''
  type: Packages
  url: packages/vibgrate-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://vibgrate.com/tags/webhooks/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vibgrate.com/terms
- group: auth
  title: ''
  type: Security
  url: https://vibgrate.com/security
- group: operate
  title: ''
  type: Roadmap
  url: https://vibgrate.com/tags/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vibgrate.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://vibgrate.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://vibgrate.com/tags/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vibgrate
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vibgrate.com/for/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://vibgrate.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://vibgrate.com/cli/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/vibgrate-com/security/vibgrate-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vibgrate-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vibgrate-com/security/vibgrate-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vibgrate-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vibgrate-com/security/vibgrate-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vibgrate-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vibgrate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://vibgrate.com/cli/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://vibgrate.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://vibgrate.com/help
coverage:
  checked: '2026-10-30'
  detail: Developer portal provides only HTML docs with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://vibgrate.com/for/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Vibgrate provides code‑drift intelligence for software teams, helping developers understand how their codebase evolves over time. By scanning repositories locally, Vibgrate identifies outdated dependencies, security vulnerabilities, and architectural drift, delivering concise, token‑efficient context to AI coding assistants. The platform offers a CLI, web dashboard, and integrations with CI/CD pipelines, enabling teams to maintain healthy code health, reduce technical debt, and improve productivity across the software development lifecycle.
image: https://vibgrate.com/img/og/default.png
layout: provider
modified: '2026-10-30'
name: vibgrate-com
nav: Providers
network: true
overview: 'vibgrate-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Code-Drift, Developer Tools, CI/CD, and Security.


  The vibgrate-com catalog on APIs.io includes 1 Spectral governance ruleset.


  vibgrate-com''s developer surface includes CLI, changelog, getting-started guide, documentation, pricing, support, and 26 more developer resources.'
plans:
- name: Vibgrate Com Plans Pricing
  plan_count: 4
  slug: vibgrate-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: vibgrate-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: vibgrate-com-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.6
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 10.4
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 22.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vibgrate-com/vibgrate-com-2026-11-03T145812.png
security:
- kind: domain-security
  name: Vibgrate Com Domain Security
  slug: vibgrate-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Vibgrate Com Vulnerability Disclosure
  slug: vibgrate-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Vibgrate Com Trust Center
  slug: vibgrate-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: vibgrate-com
tags:
- Company
- Code-Drift
- Developer Tools
- CI/CD
- Security
website: https://vibgrate.com/
---
