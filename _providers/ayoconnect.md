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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ayoconnect Agentic Access
  operation_count: 3
  slug: ayoconnect-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: //dev0.openapi.ayopop.id/api
  baseurl_source: spec
  description: The Bill API from Ayoconnect — 3 operation(s) for bill.
  name: Ayoconnect Bill API
  slug: ayoconnect-bill-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/ayoconnect/agentic-access/ayoconnect-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ayoconnect-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ayoconnect/rules/ayoconnect-rules.yml
  title: ''
  type: Spectral
  url: rules/ayoconnect-rules.yml
- group: design
  href: https://artifacts.apis.io/ayoconnect/json-ld/ayoconnect-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ayoconnect-context.jsonld
- group: design
  href: https://artifacts.apis.io/ayoconnect/vocabulary/ayoconnect-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ayoconnect-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ayoconnect/data-model/ayoconnect-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ayoconnect-data-model.yml
- group: operate
  href: https://artifacts.apis.io/ayoconnect/changelog/ayoconnect-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ayoconnect-changelog.yml
- group: auth
  href: https://artifacts.apis.io/ayoconnect/authentication/ayoconnect-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ayoconnect-authentication.yml
- group: design
  href: https://artifacts.apis.io/ayoconnect/errors/ayoconnect-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ayoconnect-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ayoconnect/conformance/ayoconnect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ayoconnect-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ayoconnect/llms/ayoconnect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ayoconnect-llms.txt
- group: other
  href: https://artifacts.apis.io/ayoconnect/hosts/ayoconnect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ayoconnect-hosts.yml
- group: other
  href: https://artifacts.apis.io/ayoconnect/vendors/ayoconnect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ayoconnect-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ayoconnect.id/docs/setup-and-connection
- group: auth
  href: https://artifacts.apis.io/ayoconnect/security/ayoconnect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ayoconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ayoconnect.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ayoconnect.com/api-documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ayoconnect.id/
- group: company
  title: ''
  type: Blog
  url: https://www.ayoconnect.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ayoconnect.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ayoconnect.com/privacy-policy
created: '2026-10-19'
description: Ayoconnect provides a comprehensive payment platform in Indonesia, offering solutions such as payment gateway, recurring payments, direct debit, instant transfers, virtual cards, and digital product integrations. It serves businesses seeking seamless, scalable payment processing and financial services, backed by robust APIs and extensive documentation.
image: https://cdn.prod.website-files.com/62b35c994f35a868d97f78dd/67a061928af8f263184e2f51_website_ayo_og_image.jpg
json_schemas:
- name: InquiryResponse
  property_count: 4
  slug: ayoconnect-inquiry-response
- name: PaymentResponse
  property_count: 4
  slug: ayoconnect-payment-response
- name: StatusResponse
  property_count: 4
  slug: ayoconnect-status-response
jsonld:
- class_count: 4
  name: Ayoconnect Context
  property_count: 4
  slug: ayoconnect-context
layout: provider
modified: '2026-10-19'
name: Ayoconnect
nav: Providers
network: true
overview: 'Ayoconnect publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Bill API. Tagged areas include Company, Payments, Fintech, and Indonesia.


  The Ayoconnect catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ayoconnect''s developer surface includes changelog, authentication, getting-started guide, documentation, engineering blog, support, and 14 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Ayoconnect API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: ayoconnect-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.8
    catalog_earned_first_party: 0.0
    catalog_gap: 73.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 49.3
    developer_ergonomics: 50.0
    discoverability: 39.3
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ayoconnect Authentication
  slug: ayoconnect-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ayoconnect Domain Security
  slug: ayoconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ayoconnect
tags:
- Company
- Payments
- Fintech
- Indonesia
website: https://www.ayoconnect.com/
---
