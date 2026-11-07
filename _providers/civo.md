---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Civo Cloud API (v2) covers the Civo cloud platform -- instances, Kubernetes clusters, networks and VPCs, firewalls, volumes, databases, object stores, regions, disk images and webhooks. Requests c
  name: Civo Cloud API
  slug: civo-cloud-api
- baseURL: https://civo.com
  baseurl_source: declared
  description: 'Civo API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Civo API
  slug: civo-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/civo/plans/civo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/civo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/civo/rules/civo-rules.yml
  title: ''
  type: Spectral
  url: rules/civo-rules.yml
- group: design
  href: https://artifacts.apis.io/civo/vocabulary/civo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/civo-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/civo/cli/civo-cli.yml
  title: ''
  type: CLI
  url: cli/civo-cli.yml
- group: design
  href: https://artifacts.apis.io/civo/conventions/civo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/civo-conventions.yml
- group: auth
  href: https://artifacts.apis.io/civo/authentication/civo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/civo-authentication.yml
- group: design
  href: https://artifacts.apis.io/civo/lifecycle/civo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/civo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/civo/errors/civo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/civo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/civo/conformance/civo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/civo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/civo/llms/civo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/civo-llms.txt
- group: agent
  href: https://artifacts.apis.io/civo/well-known/civo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/civo-well-known.yml
- group: other
  href: https://artifacts.apis.io/civo/hosts/civo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/civo-hosts.yml
- group: other
  href: https://artifacts.apis.io/civo/vendors/civo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/civo-vendors.yml
- group: build
  href: https://artifacts.apis.io/civo/packages/civo-packages.yml
  title: ''
  type: SDKs
  url: packages/civo-packages.yml
- group: build
  href: https://artifacts.apis.io/civo/packages/civo-packages.yml
  title: ''
  type: Packages
  url: packages/civo-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.civo.com/marketplace/category/security
- group: other
  title: ''
  type: Leadership
  url: https://www.civo.com/marketplace/category/management
- group: auth
  href: https://artifacts.apis.io/civo/security/civo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/civo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.civo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.civo.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.civo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.civo.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.civo.com/docs/database/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.civo.com
- group: company
  title: ''
  type: Blog
  url: https://www.civo.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.civo.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/civo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.civo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.civo.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.civo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.civo.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.civo.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.civo.com
- group: design
  title: ''
  type: Webhooks
  url: https://www.civo.com/api/webhooks
- group: company
  title: ''
  type: About
  url: https://www.civo.com/about
created: '2026-10-18'
description: Civo is a sovereign cloud and AI platform ("Civo - Sovereign Cloud and AI Platform") offering public cloud services including managed Kubernetes, compute instances, databases and the Konstruct IDP, private cloud via CivoStack Enterprise and Civo FlexCore, and Civo AI GPU workloads. Developers manage resources through the Civo Cloud API (api.civo.com), documented at civo.com/api, along with webhooks, a dashboard, documentation and a public GitHub organization.
image: https://www.civo.com/cms/api/media/file/homepage-social-1200x630.png
layout: provider
modified: '2026-10-18'
name: Civo
nav: Providers
network: true
overview: 'Civo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Kubernetes, Cloud Computing, and Infrastructure.


  The Civo catalog on APIs.io includes 1 Spectral governance ruleset.


  Civo''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 28 more developer resources.'
plans:
- name: Civo Plans Pricing
  plan_count: 1
  slug: civo-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Civo Rate Limits
  slug: civo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Civo API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: civo-rules
scopes:
- name: Civo Scopes
  scope_count: 0
  slug: civo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.3
  facets:
    access_clarity: 43.4
    contract_governance: 35.6
    contract_quality: 11.7
    developer_ergonomics: 48.8
    discoverability: 75.0
    operational_transparency: 19.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/civo/civo-2026-11-03T124246.png
security:
- kind: authentication
  name: Civo Authentication
  slug: civo-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Civo Domain Security
  slug: civo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: civo
tags:
- Company
- Cloud
- Kubernetes
- Cloud Computing
- Infrastructure
- Artificial Intelligence
- GPU
- Sovereign Cloud
website: https://www.civo.com
---
