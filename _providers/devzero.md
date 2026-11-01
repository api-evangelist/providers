---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://dakr.devzero.io
  baseurl_source: declared
  description: 'Devzero API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-23); not the provider''s own document.'
  name: Devzero API
  slug: devzero-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/devzero/plans/devzero-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/devzero-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/devzero/rules/devzero-rules.yml
  title: ''
  type: Spectral
  url: rules/devzero-rules.yml
- group: design
  href: https://artifacts.apis.io/devzero/vocabulary/devzero-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/devzero-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/devzero/cli/devzero-cli.yml
  title: ''
  type: CLI
  url: cli/devzero-cli.yml
- group: design
  href: https://artifacts.apis.io/devzero/conformance/devzero-conformance.yml
  title: ''
  type: Conformance
  url: conformance/devzero-conformance.yml
- group: agent
  href: https://artifacts.apis.io/devzero/well-known/devzero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/devzero-well-known.yml
- group: other
  href: https://artifacts.apis.io/devzero/hosts/devzero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devzero-hosts.yml
- group: other
  href: https://artifacts.apis.io/devzero/vendors/devzero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devzero-vendors.yml
- group: build
  href: https://artifacts.apis.io/devzero/packages/devzero-packages.yml
  title: ''
  type: SDKs
  url: packages/devzero-packages.yml
- group: build
  href: https://artifacts.apis.io/devzero/packages/devzero-packages.yml
  title: ''
  type: Packages
  url: packages/devzero-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.devzero.io/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.devzero.io/
- group: start
  title: ''
  type: SignUp
  url: https://www.devzero.io/auth/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.devzero.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.devzero.io/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.devzero.io/docs
- group: company
  title: ''
  type: Blog
  url: https://www.devzero.io/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.devzero.io/docs/cli/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.devzero.io/docs/getting-started/quickstart
- group: auth
  href: https://artifacts.apis.io/devzero/security/devzero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devzero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.devzero.io
coverage:
  checked: '2026-10-23'
  detail: Provider documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.devzero.io/docs/cli/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: DevZero provides a platform to automatically right‑size Kubernetes and AI workloads, offering live rightsizing, cost optimization, and zero‑downtime deployments. Users can run the DevZero CLI locally to analyze clusters without sending data to the cloud, and the service integrates with Pulumi, Terraform, and major cloud providers to reduce infrastructure spend and improve efficiency.
layout: provider
modified: '2026-10-23'
name: Devzero
nav: Providers
network: true
overview: 'Devzero is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Kubernetes, Cloud Cost, DevOps, and Artificial Intelligence.


  The Devzero catalog on APIs.io includes 1 Spectral governance ruleset.


  Devzero''s developer surface includes CLI, signup flow, pricing, documentation, engineering blog, API reference, getting-started guide, and 14 more developer resources.'
plans:
- name: Devzero Plans Pricing
  plan_count: 3
  slug: devzero-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Devzero API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: devzero-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 11.9
    developer_ergonomics: 45.2
    discoverability: 62.5
    operational_transparency: 15.8
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
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devzero Domain Security
  slug: devzero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: devzero
tags:
- Company
- Kubernetes
- Cloud Cost
- DevOps
- Artificial Intelligence
website: https://www.devzero.io
---
