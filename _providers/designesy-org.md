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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Designesy platform as documented
  name: Designesy API
  slug: designesy-api
- description: 'designesy-org API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: designesy-org API
  slug: designesy-org-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/designesy-org/plans/designesy-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/designesy-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/designesy-org/rules/designesy-org-rules.yml
  title: ''
  type: Spectral
  url: rules/designesy-org-rules.yml
- group: design
  href: https://artifacts.apis.io/designesy-org/json-ld/designesy-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/designesy-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/designesy-org/vocabulary/designesy-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/designesy-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/designesy-org/data-model/designesy-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/designesy-org-data-model.yml
- group: operate
  href: https://artifacts.apis.io/designesy-org/changelog/designesy-org-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/designesy-org-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/LE-VAI/designesy-org/security/policy
- group: design
  href: https://artifacts.apis.io/designesy-org/conformance/designesy-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/designesy-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/designesy-org/llms/designesy-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/designesy-org-llms.txt
- group: auth
  href: https://artifacts.apis.io/designesy-org/well-known/designesy-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/designesy-org-security.txt
- group: auth
  href: https://artifacts.apis.io/designesy-org/well-known/designesy-org-designesy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/designesy-org-designesy-security.txt
- group: agent
  href: https://artifacts.apis.io/designesy-org/well-known/designesy-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/designesy-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/designesy-org/hosts/designesy-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/designesy-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/designesy-org/vendors/designesy-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/designesy-org-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.designesy.org/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.designesy.org/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.designesy.org/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.designesy.org/changelog
- group: auth
  href: https://artifacts.apis.io/designesy-org/security/designesy-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/designesy-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/designesy-org/security/designesy-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/designesy-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://designesy.org/
coverage:
  checked: '2026-11-05'
  detail: Documentation is provided but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://www.designesy.org/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: 'designesy-org is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://www.designesy.org/opengraph-image?016133b894aee7f5
json_schemas:
- name: GetContractsDesignSystemJsonResponse
  property_count: 1
  slug: designesy-org-get-contracts-design-system-json-response
- name: GetKitsDesignReviewJsonResponse
  property_count: 1
  slug: designesy-org-get-kits-design-review-json-response
- name: GetOpenResponse
  property_count: 1
  slug: designesy-org-get-open-response
- name: PostApiMcpRequest
  property_count: 3
  slug: designesy-org-post-api-mcp-request
- name: PostApiScoreRequest
  property_count: 2
  slug: designesy-org-post-api-score-request
jsonld:
- class_count: 5
  name: Designesy Org Context
  property_count: 8
  slug: designesy-org-context
layout: provider
modified: '2026-11-05'
name: designesy-org
nav: Providers
network: true
overview: 'designesy-org is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Design verification, Design contracts, UI scoring, Accessibility checks, and Motion Graphics.


  The designesy-org catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  designesy-org''s developer surface includes changelog, pricing, documentation, and 18 more developer resources.'
plans:
- name: Designesy Org Plans Pricing
  plan_count: 4
  slug: designesy-org-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: designesy-org API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: designesy-org-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 26.3
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Designesy Org Domain Security
  slug: designesy-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Designesy Org Vulnerability Disclosure
  slug: designesy-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: designesy-org
tags:
- Design verification
- Design contracts
- UI scoring
- Accessibility checks
- Motion Graphics
- Design Tokens
- Developer Tools
website: https://designesy.org/
---
