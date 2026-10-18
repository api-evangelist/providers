---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Loqate Agentic Access
  operation_count: 3
  slug: loqate-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.loqate.com
  baseurl_source: declared
  description: The Plants API from Loqate — 2 operation(s) for plants.
  name: Loqate Plants API
  slug: loqate-plants-api
artifact_total: 9
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/agentic-access/loqate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/loqate-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/plans/loqate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loqate-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/rules/loqate-rules.yml
  title: ''
  type: Spectral
  url: rules/loqate-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/json-ld/loqate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/loqate-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/vocabulary/loqate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/loqate-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/data-model/loqate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/loqate-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/cli/loqate-cli.yml
  title: ''
  type: CLI
  url: cli/loqate-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/changelog/loqate-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/loqate-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/authentication/loqate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/loqate-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/errors/loqate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/loqate-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/conformance/loqate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loqate-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/llms/loqate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loqate-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/a2a/loqate-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/loqate-a2a.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/hosts/loqate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loqate-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/vendors/loqate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/loqate-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.loqate.com/anz/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.loqate.com/en-us/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loqate.com/en-us/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.loqate.com/en-us/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.loqate.com/developers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.loqate.com/release-notes/all-loqate
- group: company
  title: ''
  type: Blog
  url: https://www.loqate.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.loqate.com/getting-started/country-improvement-program
- group: docs
  title: ''
  type: Documentation
  url: https://docs.loqate.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.loqate.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/loqate/refs/heads/main/security/loqate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loqate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.loqate.com/
coverage:
  checked: '2026-10-13'
  detail: API reference pages exist but no OpenAPI spec was found at the API host.
  evidence:
  - status: 404
    url: https://api.loqate.com/openapi.json
  - status: 404
    url: https://api.loqate.com/openapi.yaml
  - status: 404
    url: https://api.loqate.com/swagger.json
  - status: 404
    url: https://api.loqate.com/v1/openapi.json
  - status: 404
    url: https://api.loqate.com/api-docs
  - status: 404
    url: https://api.loqate.com/docs
  - status: 404
    url: https://api.loqate.com/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Loqate provides global address validation, capture, and data enrichment services, offering APIs for address verification, email, phone, and bank validation, as well as geocoding and store finder solutions. It serves enterprises across e‑commerce, fintech, travel, and logistics with scalable, secure, and compliant data quality tools.
image: https://www.loqate.com/media/ugzjtvos/opengraph.png
json_schemas:
- name: NewPlant
  property_count: 0
  slug: loqate-new-plant
- name: Plant
  property_count: 2
  slug: loqate-plant
jsonld:
- class_count: 2
  name: Loqate Context
  property_count: 4
  slug: loqate-context
layout: provider
modified: '2026-10-13'
name: Loqate
nav: Providers
network: true
overview: 'Loqate publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Plants API. Tagged areas include Address Validation, Data Quality, Email Verification, Phone Validation, and Retail.


  The Loqate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Loqate''s developer surface includes CLI, changelog, authentication, pricing, engineering blog, getting-started guide, documentation, and 20 more developer resources.'
plans:
- name: Loqate Plans Pricing
  plan_count: 3
  slug: loqate-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Loqate API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: loqate-rules
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 54.2
    developer_ergonomics: 59.5
    discoverability: 75.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Loqate Authentication
  slug: loqate-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Loqate Domain Security
  slug: loqate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: loqate
tags:
- Address Validation
- Data Quality
- Email Verification
- Phone Validation
- Retail
- Fintech
- Logistics
website: https://www.loqate.com/
---
