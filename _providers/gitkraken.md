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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://github.com
  baseurl_source: declared
  description: 'GitKraken API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: GitKraken API
  slug: gitkraken-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gitkraken/refs/heads/main/plans/gitkraken-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gitkraken-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gitkraken/refs/heads/main/rules/gitkraken-rules.yml
  title: ''
  type: Spectral
  url: rules/gitkraken-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitkraken/refs/heads/main/authentication/gitkraken-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gitkraken-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gitkraken/refs/heads/main/conformance/gitkraken-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gitkraken-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gitkraken/refs/heads/main/llms/gitkraken-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gitkraken-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gitkraken/refs/heads/main/vendors/gitkraken-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gitkraken-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gitkraken.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.gitkraken.com/gitkraken-client/terms-and-conditions/
- group: operate
  title: ''
  type: Roadmap
  url: https://gitkraken.com/git-client/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gitkraken.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://gitkraken.com/media/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/gitkraken/gk-cli/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://help.gitkraken.com/gitkraken-desktop/how-to-install/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gitkraken/refs/heads/main/security/gitkraken-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gitkraken-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gitkraken.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.gitkraken.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://gitkraken.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://gitkraken.com/blog
coverage:
  checked: 2026-09-22
  detail: Documentation is HTML pages without a machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://api.gitkraken.com/openapi.json
  - status: 200
    url: https://api.gitkraken.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: GitKraken provides a suite of developer tools for Git workflow, including a visual Git client, GitLens IDE extensions, AI‑assisted code assistance, and the GitKraken MCP platform. The company focuses on improving developer productivity, collaboration, and DevEx through integrated desktop, cloud, and AI solutions, serving millions of developers and enterprises worldwide.
image: https://gitkraken.com/wp-content/uploads/2026/06/GK_Default_OG-Image-1024x538.png
layout: provider
modified: '2026-09-22'
name: GitKraken
nav: Providers
network: true
overview: 'GitKraken publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Git, Artificial Intelligence, Collaboration, and Platform.


  The GitKraken catalog on APIs.io includes 1 Spectral governance ruleset.


  GitKraken''s developer surface includes authentication, changelog, getting-started guide, documentation, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Gitkraken Plans Pricing
  plan_count: 4
  slug: gitkraken-plans-pricing
random_paper: 14
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: GitKraken API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: gitkraken-rules
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 11.9
    developer_ergonomics: 35.7
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 48.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gitkraken Authentication
  slug: gitkraken-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Gitkraken Domain Security
  slug: gitkraken-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gitkraken
tags:
- Developer Tools
- Git
- Artificial Intelligence
- Collaboration
- Platform
website: https://www.gitkraken.com/
---
