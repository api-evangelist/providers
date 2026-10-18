---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Baloise Agentic Access
  operation_count: 17
  slug: baloise-agentic-access
  summary_line: 17 operations · 10 acting
api_count: 4
apis:
- description: The contracts API from Baloise — 2 operation(s) for contracts.
  name: Baloise Contracts API
  slug: baloise-contracts-api
- baseURL: /v0.8
  baseurl_source: spec
  description: The DB API from Baloise — 2 operation(s) for db.
  name: Baloise DB API
  slug: baloise-db-api
- description: The documents API from Baloise — 1 operation(s) for documents.
  name: Baloise Documents API
  slug: baloise-documents-api
- baseURL: /v0.8
  baseurl_source: spec
  description: The JBoss API from Baloise — 1 operation(s) for jboss.
  name: Baloise J Boss API
  slug: baloise-jboss-api
- baseURL: /v0.8
  baseurl_source: spec
  description: The Middlewares API from Baloise — 1 operation(s) for middlewares.
  name: Baloise Middlewares API
  slug: baloise-middlewares-api
- baseURL: /v0.8
  baseurl_source: spec
  description: The orders API from Baloise — 2 operation(s) for orders.
  name: Baloise Orders API
  slug: baloise-orders-api
- baseURL: /v0.8
  baseurl_source: spec
  description: The pgsql API from Baloise — 2 operation(s) for pgsql.
  name: Baloise Pgsql API
  slug: baloise-pgsql-api
- description: The version API from Baloise — 1 operation(s) for version.
  name: Baloise Version API
  slug: baloise-version-api
- baseURL: /v0.8
  baseurl_source: spec
  description: The VMs API from Baloise — 2 operation(s) for vms.
  name: Baloise VMs API
  slug: baloise-vms-api
artifact_total: 17
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/vendors/baloise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baloise-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/agentic-access/baloise-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/baloise-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/rules/baloise-rules.yml
  title: ''
  type: Spectral
  url: rules/baloise-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/json-ld/baloise-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/baloise-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/vocabulary/baloise-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/baloise-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/data-model/baloise-data-model.yml
  title: ''
  type: DataModel
  url: data-model/baloise-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/components/baloise-components.yml
  title: ''
  type: Components
  url: components/baloise-components.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/cli/baloise-cli.yml
  title: ''
  type: CLI
  url: cli/baloise-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/conventions/baloise-conventions.yml
  title: ''
  type: Conventions
  url: conventions/baloise-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/lifecycle/baloise-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/baloise-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/errors/baloise-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/baloise-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/conformance/baloise-conformance.yml
  title: ''
  type: Conformance
  url: conformance/baloise-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/overlays/baloise-corellia-contracts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/baloise-corellia-contracts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/hosts/baloise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baloise-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/packages/baloise-packages.yml
  title: ''
  type: SDKs
  url: packages/baloise-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/packages/baloise-packages.yml
  title: ''
  type: Packages
  url: packages/baloise-packages.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/baloise-incubator/spectral-ruleset
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/baloise
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/baloise-incubator
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/baloise-incubator/spectral-ruleset
- group: other
  title: ''
  type: OpenSource
  url: https://baloise.github.io/open-source/
created: '2026-10-09'
description: Baloise Group is a Basel, Switzerland-based insurance and pension group (GitHub org 'Baloise Group', Aeschengraben 21, 4002 Basel) that publishes open-source work through its baloise and baloise-incubator GitHub organizations. Its API-related open source includes a custom Spectral API linter ruleset for the Zalando RESTful API Guidelines, the Corellia B2B Web-API specification for insurance contract data, the GitOps CLI and the Baloise Design System. Its former website, www.baloise.com, now redirects to the Helvetia Baloise Group corporate site (helvetia-baloise.com) following the Helvetia-Baloise merger.
image: https://avatars.githubusercontent.com/u/4548858?v=4
json_schemas:
- name: Cancellation
  property_count: 2
  slug: baloise-cancellation
- name: Contract
  property_count: 13
  slug: baloise-contract
- name: Document
  property_count: 5
  slug: baloise-document
jsonld:
- class_count: 50
  name: Baloise Context
  property_count: 101
  slug: baloise-context
layout: provider
modified: '2026-10-09'
name: Baloise
nav: Providers
network: true
overview: 'Baloise publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contracts API, DB API, Documents API, and 6 more. Tagged areas include Company, Insurance, Financial Services, Switzerland, and Open Source.


  The Baloise catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Baloise''s developer surface includes CLI and 21 more developer resources.'
plans:
- name: Baloise Plans Pricing
  plan_count: 0
  slug: baloise-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Baloise Rate Limits
  slug: baloise-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Baloise API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: baloise-rules
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.6
    developer_ergonomics: 16.1
    discoverability: 62.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 24.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 4.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/baloise/refs/heads/main/screenshots/baloise-2026-10-11T101514.png
slug: baloise
tags:
- Company
- Insurance
- Financial Services
- Switzerland
- Open Source
- API Governance
- Spectral
- Linting
---
