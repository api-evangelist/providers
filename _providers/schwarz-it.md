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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Schwarz It Agentic Access
  operation_count: 3
  slug: schwarz-it-agentic-access
  summary_line: 3 operations · 1 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: http://localhost:3001
  baseurl_source: spec
  description: The health-probe API from Schwarz IT — 1 operation(s) for health-probe.
  name: Schwarz IT Health Probe API
  slug: schwarz-it-health-probe-api
- baseURL: http://localhost:3001
  baseurl_source: spec
  description: The lintings API from Schwarz IT — 1 operation(s) for lintings.
  name: Schwarz IT Lintings API
  slug: schwarz-it-lintings-api
- baseURL: http://localhost:3001
  baseurl_source: spec
  description: The rules API from Schwarz IT — 1 operation(s) for rules.
  name: Schwarz IT Rules API
  slug: schwarz-it-rules-api
artifact_total: 12
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/security/schwarz-it-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/schwarz-it-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/agentic-access/schwarz-it-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/schwarz-it-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/rules/schwarz-it-rules.yml
  title: ''
  type: Spectral
  url: rules/schwarz-it-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/json-ld/schwarz-it-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/schwarz-it-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/vocabulary/schwarz-it-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/schwarz-it-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/data-model/schwarz-it-data-model.yml
  title: ''
  type: DataModel
  url: data-model/schwarz-it-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/components/schwarz-it-components.yml
  title: ''
  type: Components
  url: components/schwarz-it-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/conventions/schwarz-it-conventions.yml
  title: ''
  type: Conventions
  url: conventions/schwarz-it-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/lifecycle/schwarz-it-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/schwarz-it-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/errors/schwarz-it-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/schwarz-it-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/conformance/schwarz-it-conformance.yml
  title: ''
  type: Conformance
  url: conformance/schwarz-it-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/overlays/schwarz-it-api-linter-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/schwarz-it-api-linter-service-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/hosts/schwarz-it-hosts.yml
  title: ''
  type: Hosts
  url: hosts/schwarz-it-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/packages/schwarz-it-packages.yml
  title: ''
  type: SDKs
  url: packages/schwarz-it-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/packages/schwarz-it-packages.yml
  title: ''
  type: Packages
  url: packages/schwarz-it-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jobs.schwarz/en/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://jobs.schwarz
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SchwarzIT
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/SchwarzIT/api-linter-rules
created: '2026-10-09'
description: Schwarz IT (Schwarz IT KG, Neckarsulm, Germany) is the IT service company of the Schwarz Group (Lidl, Kaufland), describing itself on GitHub as "the technological heartbeat of the companies of Schwarz Group". It is listed as an affiliated company of Schwarz Digits, the group's IT and digital division, and hosts the Schwarz Digits website. Its public GitHub organization publishes the Schwarz API rule definitions for the Spectral API linter (api-linter-rules), a Spectral IntelliJ plugin, an API-linting-as-a-service project, a Kotlin RFC 9457 problem-details library, community STACKIT Go client and Terraform provider, and SAP/ABAP open-source components.
image: https://avatars.githubusercontent.com/u/25613864?v=4
json_schemas:
- name: CreateLintingDto
  property_count: 2
  slug: schwarz-it-create-linting-dto
- name: CreatedLintingDto
  property_count: 5
  slug: schwarz-it-created-linting-dto
jsonld:
- class_count: 5
  name: Schwarz It Context
  property_count: 18
  slug: schwarz-it-context
layout: provider
modified: '2026-10-09'
name: Schwarz IT
nav: Providers
network: true
overview: 'Schwarz IT publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Health Probe API, Lintings API, and Rules API. Tagged areas include Company, API Governance, API Linting, Spectral, and OpenAPI.


  The Schwarz IT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Schwarz It Plans Pricing
  plan_count: 0
  slug: schwarz-it-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Schwarz It Rate Limits
  slug: schwarz-it-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Schwarz IT API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: schwarz-it-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 52.0
    developer_ergonomics: 8.9
    discoverability: 57.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 26.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/schwarz-it/refs/heads/main/screenshots/schwarz-it-2026-10-11T125550.png
security:
- kind: authentication
  name: Schwarz It Authentication
  slug: schwarz-it-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Schwarz It Domain Security
  slug: schwarz-it-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: schwarz-it
tags:
- Company
- API Governance
- API Linting
- Spectral
- OpenAPI
- Retail
- Germany
website: https://jobs.schwarz
---
