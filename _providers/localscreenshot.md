---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Localscreenshot Agentic Access
  operation_count: 1
  slug: localscreenshot-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Take a screenshot of any public web page via the localscreenshot service.
  name: Screenshot API
  slug: screenshot-api
artifact_total: 6
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/agentic-access/localscreenshot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/localscreenshot-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/plans/localscreenshot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/localscreenshot-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/rules/localscreenshot-rules.yml
  title: ''
  type: Spectral
  url: rules/localscreenshot-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/cli/localscreenshot-cli.yml
  title: ''
  type: CLI
  url: cli/localscreenshot-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/changelog/localscreenshot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/localscreenshot-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/authentication/localscreenshot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/localscreenshot-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/lifecycle/localscreenshot-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/localscreenshot-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/lifecycle/localscreenshot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/localscreenshot-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/errors/localscreenshot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/localscreenshot-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/conformance/localscreenshot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/localscreenshot-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/llms/localscreenshot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/localscreenshot-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/well-known/localscreenshot-cursor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/localscreenshot-cursor-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/well-known/localscreenshot-ampcode-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/localscreenshot-ampcode-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/well-known/localscreenshot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/localscreenshot-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/hosts/localscreenshot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/localscreenshot-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/vendors/localscreenshot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/localscreenshot-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/packages/localscreenshot-packages.yml
  title: ''
  type: SDKs
  url: packages/localscreenshot-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/packages/localscreenshot-packages.yml
  title: ''
  type: Packages
  url: packages/localscreenshot-packages.yml
- group: start
  title: ''
  type: Login
  url: https://localscreenshot.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/localscreenshot/refs/heads/main/security/localscreenshot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/localscreenshot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://localscreenshot.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.localscreenshot.com/overview
- group: docs
  title: ''
  type: APIReference
  url: https://api.localscreenshot.com/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.localscreenshot.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://localscreenshot.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://localscreenshot.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://localscreenshot.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://localscreenshot.com/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://localscreenshot.com/v1/openapi.json
  - status: null
    url: https://api.localscreenshot.com/v1/openapi.json
  - status: 401
    url: https://localscreenshot.com/mcp
  - status: 401
    url: https://api.localscreenshot.com/mcp
  - status: 200
    url: https://localscreenshot.com
  reason: partner-login
  state: gated
created: '2026-10-12'
description: localscreenshot provides a screenshot API designed for AI agents, enabling developers to capture clean, full-page screenshots of websites across 227 countries. The service offers a simple RESTful interface, pricing with a free tier of 50 credits per month, and comprehensive documentation. It supports integration with popular AI platforms like ChatGPT, Claude, Cursor, and more, allowing seamless inclusion of visual content in AI-driven workflows.
layout: provider
modified: '2026-10-12'
name: localscreenshot
nav: Providers
network: true
overview: 'localscreenshot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Screenshots, Artificial Intelligence, and Automation.


  The localscreenshot catalog on APIs.io includes 1 Spectral governance ruleset.


  localscreenshot''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, pricing, and 21 more developer resources.'
plans:
- name: Localscreenshot Plans Pricing
  plan_count: 3
  slug: localscreenshot-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: localscreenshot API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: localscreenshot-rules
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 46.5
    catalog_earned_first_party: 12.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 60.7
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Localscreenshot Authentication
  slug: localscreenshot-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Localscreenshot Domain Security
  slug: localscreenshot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: localscreenshot
tags:
- Company
- Screenshots
- Artificial Intelligence
- Automation
website: https://localscreenshot.com
---
