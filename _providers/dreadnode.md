---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for Dreadnode platform providing AI‑driven cybersecurity services.
  name: Dreadnode API
  slug: dreadnode-api-2
- baseURL: https://dreadnode.io
  baseurl_source: declared
  description: 'Dreadnode API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Dreadnode API
  slug: dreadnode-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/dreadnode/plans/dreadnode-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dreadnode-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dreadnode/rules/dreadnode-rules.yml
  title: ''
  type: Spectral
  url: rules/dreadnode-rules.yml
- group: design
  href: https://artifacts.apis.io/dreadnode/vocabulary/dreadnode-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dreadnode-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dreadnode/conformance/dreadnode-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dreadnode-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dreadnode/llms/dreadnode-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreadnode-llms.txt
- group: agent
  href: https://artifacts.apis.io/dreadnode/well-known/dreadnode-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dreadnode-well-known.yml
- group: other
  href: https://artifacts.apis.io/dreadnode/hosts/dreadnode-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreadnode-hosts.yml
- group: other
  href: https://artifacts.apis.io/dreadnode/vendors/dreadnode-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dreadnode-vendors.yml
- group: build
  href: https://artifacts.apis.io/dreadnode/packages/dreadnode-packages.yml
  title: ''
  type: SDKs
  url: packages/dreadnode-packages.yml
- group: build
  href: https://artifacts.apis.io/dreadnode/packages/dreadnode-packages.yml
  title: ''
  type: Packages
  url: packages/dreadnode-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://dreadnode.io/company/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dreadnode
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dreadnode.io/release-notes/
- group: auth
  href: https://artifacts.apis.io/dreadnode/security/dreadnode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreadnode-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreadnode.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dreadnode.io
- group: company
  title: ''
  type: Blog
  url: https://dreadnode.io/research?filter=blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dreadnode.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.dreadnode.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.dreadnode.io/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dreadnode.io/getting-started/quickstart/
coverage:
  checked: '2026-10-29'
  detail: OpenAPI endpoint returned HTML page instead of a machine‑readable spec
  evidence:
  - status: 200
    url: https://trust.dreadnode.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Dreadnode provides AI‑driven infrastructure for cybersecurity teams, offering a platform that enables the deployment, evaluation, and scaling of autonomous cyber agents. The service includes model evaluation, evidence generation, and integration tools to operationalize AI agents securely. Dreadnode’s platform supports offensive‑security evaluations, model scoring, and cost‑effective deployment, aiming to bridge the gap between AI capabilities and practical security operations.
image: https://dreadnode.io/og-default.png
layout: provider
modified: '2026-10-29'
name: Dreadnode
nav: Providers
network: true
overview: 'Dreadnode is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Cybersecurity, Platform, and Infrastructure.


  The Dreadnode catalog on APIs.io includes 1 Spectral governance ruleset.


  Dreadnode''s developer surface includes changelog, documentation, engineering blog, pricing, getting-started guide, and 16 more developer resources.'
plans:
- name: Dreadnode Plans Pricing
  plan_count: 2
  slug: dreadnode-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Dreadnode API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: dreadnode-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 31.0
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: unknown
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
  name: Dreadnode Domain Security
  slug: dreadnode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dreadnode
tags:
- Company
- AI
- Cybersecurity
- Platform
- Infrastructure
website: https://dreadnode.io
---
