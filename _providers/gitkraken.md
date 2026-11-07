---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
  score: 17.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://github.com
  baseurl_source: declared
  description: The Docker API from GitKraken — 1 operation(s) for docker.
  name: GitKraken Docker API
  slug: gitkraken-docker-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Linux API from GitKraken — 1 operation(s) for linux.
  name: GitKraken Linux API
  slug: gitkraken-linux-api
artifact_total: 7
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://gitkraken.com/feed
- group: commercial
  href: https://artifacts.apis.io/gitkraken/plans/gitkraken-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gitkraken-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gitkraken/rules/gitkraken-rules.yml
  title: ''
  type: Spectral
  url: rules/gitkraken-rules.yml
- group: auth
  href: https://artifacts.apis.io/gitkraken/authentication/gitkraken-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gitkraken-authentication.yml
- group: design
  href: https://artifacts.apis.io/gitkraken/conformance/gitkraken-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gitkraken-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gitkraken/llms/gitkraken-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gitkraken-llms.txt
- group: other
  href: https://artifacts.apis.io/gitkraken/vendors/gitkraken-vendors.yml
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
  href: https://artifacts.apis.io/gitkraken/security/gitkraken-domain-security.yml
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
finops:
- has_sources: true
  method: derived
  name: Gitkraken Finops
  primary_unit: ''
  service_category: ''
  slug: gitkraken-finops
  template: true
image: https://gitkraken.com/wp-content/uploads/2026/06/GK_Default_OG-Image-1024x538.png
layout: provider
modified: '2026-10-06'
name: GitKraken
nav: Providers
network: true
overview: 'GitKraken is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Docker API and Linux API. Tagged areas include Developer Tools, Version Control, Artificial Intelligence, Collaboration, and Platform.


  The GitKraken catalog on APIs.io includes 1 Spectral governance ruleset.


  GitKraken''s developer surface includes authentication, changelog, getting-started guide, documentation, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Gitkraken Plans Pricing
  plan_count: 5
  slug: gitkraken-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 51
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
  composite: 31.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 51.3
    contract_governance: 31.8
    contract_quality: 11.9
    developer_ergonomics: 23.8
    discoverability: 74.1
    operational_transparency: 10.5
  previous_composite: 40.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/gitkraken/gitkraken-2026-10-11T104919.png
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
- Version Control
- Artificial Intelligence
- Collaboration
- Platform
website: https://www.gitkraken.com/
---
