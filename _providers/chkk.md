---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Chkk provides an Agentic Lifecycle Management Platform for cloud native projects. Documentation is available at the Docs page.
  name: Chkk API
  slug: chkk-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/chkk/plans/chkk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chkk-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/chkk/cli/chkk-cli.yml
  title: ''
  type: CLI
  url: cli/chkk-cli.yml
- group: auth
  href: https://artifacts.apis.io/chkk/authentication/chkk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chkk-authentication.yml
- group: design
  href: https://artifacts.apis.io/chkk/conformance/chkk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chkk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chkk/llms/chkk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chkk-llms.txt
- group: other
  href: https://artifacts.apis.io/chkk/a2a/chkk-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chkk-a2a.yml
- group: agent
  href: https://artifacts.apis.io/chkk/well-known/chkk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chkk-well-known.yml
- group: other
  href: https://artifacts.apis.io/chkk/hosts/chkk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chkk-hosts.yml
- group: other
  href: https://artifacts.apis.io/chkk/vendors/chkk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chkk-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.chkk.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.chkk.io/security/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.chkk.io/security/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chkk.io/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chkk-io
- group: company
  title: ''
  type: Blog
  url: https://www.chkk.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chkk.io/overview/quickstart-chkk-cli
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chkk.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chkk.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/chkk/security/chkk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chkk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chkk.io/
coverage:
  checked: '2026-10-23'
  detail: Docs page renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.chkk.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Chkk provides an agentic lifecycle management platform for cloud‑native software that automates research, analysis, planning, and execution of upgrades and risk assessments. It targets enterprises that run Kubernetes clusters and use open‑source projects such as Istio, Keycloak, and Consul, helping them generate IaC pull requests, detect breaking changes, and streamline upgrade workflows.
image: https://cdn.prod.website-files.com/6536b19a1bb2f6693bdaa5b8/6536b19a1bb2f6693bdaa58c_Hero_Updated.webp
layout: provider
modified: '2026-10-23'
name: Chkk
nav: Providers
network: true
overview: 'Chkk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Lifecycle Management, Kubernetes, Cloud Native, and Enterprise Software.


  Chkk''s developer surface includes CLI, authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 13 more developer resources.'
plans:
- name: Chkk Plans Pricing
  plan_count: 3
  slug: chkk-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chkk Authentication
  slug: chkk-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chkk Domain Security
  slug: chkk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chkk
tags:
- Lifecycle Management
- Kubernetes
- Cloud Native
- Enterprise Software
website: https://www.chkk.io/
---
