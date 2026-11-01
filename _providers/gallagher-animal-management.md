---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: REST API for Command Centre providing events, cardholders, view status, overrides, and inbound events, requiring API key and client certificates.
  name: Command Centre REST API
  slug: command-centre-rest-api
- description: 'Gallagher API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Gallagher API
  slug: gallagher-animal-management-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/gallagher-animal-management/rules/gallagher-animal-management-rules.yml
  title: ''
  type: Spectral
  url: rules/gallagher-animal-management-rules.yml
- group: design
  href: https://artifacts.apis.io/gallagher-animal-management/json-ld/gallagher-animal-management-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gallagher-animal-management-context.jsonld
- group: design
  href: https://artifacts.apis.io/gallagher-animal-management/vocabulary/gallagher-animal-management-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gallagher-animal-management-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gallagher-animal-management/data-model/gallagher-animal-management-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gallagher-animal-management-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.gallagher.com/
- group: auth
  href: https://artifacts.apis.io/gallagher-animal-management/authentication/gallagher-animal-management-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gallagher-animal-management-authentication.yml
- group: design
  href: https://artifacts.apis.io/gallagher-animal-management/errors/gallagher-animal-management-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gallagher-animal-management-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gallagher-animal-management/conformance/gallagher-animal-management-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gallagher-animal-management-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gallagher-animal-management/llms/gallagher-animal-management-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gallagher-animal-management-llms.txt
- group: agent
  href: https://artifacts.apis.io/gallagher-animal-management/well-known/gallagher-animal-management-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gallagher-animal-management-well-known.yml
- group: other
  href: https://artifacts.apis.io/gallagher-animal-management/hosts/gallagher-animal-management-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gallagher-animal-management-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://security.gallagher.com/Terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gallagher.com/PrivacyStatement
- group: company
  title: ''
  type: Newsroom
  url: https://security.gallagher.com/en-US/News
- group: auth
  href: https://artifacts.apis.io/gallagher-animal-management/security/gallagher-animal-management-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gallagher-animal-management-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gallagher-animal-management/security/gallagher-animal-management-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gallagher-animal-management-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://am.gallagher.com/
- group: docs
  title: ''
  type: Documentation
  url: https://am.gallagher.com/en-US/Solutions
- group: start
  title: ''
  type: GettingStarted
  url: https://am.gallagher.com/en-US/
- group: operate
  title: ''
  type: Support
  url: https://am.gallagher.com/en-US/Support
- group: company
  title: ''
  type: Blog
  url: https://am.gallagher.com/en-US/Knowledge-Hub/Articles
coverage:
  checked: '2026-10-28'
  detail: API documentation requires request for an API key and client certificates, with no public machine‑readable specification.
  evidence:
  - status: 200
    url: https://help.security.gallagher.com/knowledge-hub/products/cc-software/configure/interface-options/api/representational-state-transfer-rest-api.md
  reason: customer-only-docs
  state: gated
created: '2026-10-28'
description: Gallagher AM Global provides comprehensive animal management solutions, including electric fencing systems, weighing and electronic identification (EID) systems, and watering systems, helping livestock producers worldwide improve animal welfare, operational efficiency, and data-driven decision making.
image: https://am.gallagher.com/-/media/Project/Animal-Management-Business/Animal-Management-Public-Site/Carousel-Image/NZ-Carousel/Carousel--iSeries-no-green.png
json_schemas:
- name: GetKnowledgeHubProductsCcHardwareControllersController7000An
  property_count: 2
  slug: gallagher-animal-management-get-knowledge-hub-products-cc-hardware-controllers-controller7000-an
- name: GetKnowledgeHubProductsCcSoftwareConfigureInterfaceOptionsAp
  property_count: 3
  slug: gallagher-animal-management-get-knowledge-hub-products-cc-software-configure-interface-options-ap
- name: GetKnowledgeHubProductsCcSoftwareReferenceCommandCentreLimit
  property_count: 1
  slug: gallagher-animal-management-get-knowledge-hub-products-cc-software-reference-command-centre-limit
- name: GetKnowledgeHubProductsCcSoftwareReferenceDatabasesSizesAndE
  property_count: 1
  slug: gallagher-animal-management-get-knowledge-hub-products-cc-software-reference-databases-sizes-and-e
- name: GetKnowledgeHubProductsIntegrationsThirdPartyReadersInvixium
  property_count: 2
  slug: gallagher-animal-management-get-knowledge-hub-products-integrations-third-party-readers-invixium
- name: GetKnowledgeHubProductsIntegrationsThirdPartyReadersInvixium2
  property_count: 3
  slug: gallagher-animal-management-get-knowledge-hub-products-integrations-third-party-readers-invixium2
jsonld:
- class_count: 10
  name: Gallagher Animal Management Context
  property_count: 5
  slug: gallagher-animal-management-context
layout: provider
modified: '2026-10-28'
name: Gallagher
nav: Providers
network: true
overview: 'Gallagher is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Animal Management, Electric Fencing, Weighing, EID, and Watering.


  The Gallagher catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gallagher''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Gallagher Animal Management Plans Pricing
  plan_count: 0
  slug: gallagher-animal-management-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Gallagher Animal Management Rate Limits
  slug: gallagher-animal-management-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Gallagher API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: gallagher-animal-management-rules
scopes:
- name: Gallagher Animal Management Scopes
  scope_count: 0
  slug: gallagher-animal-management-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 21.9
    developer_ergonomics: 40.5
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gallagher Animal Management Authentication
  slug: gallagher-animal-management-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Gallagher Animal Management Domain Security
  slug: gallagher-animal-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gallagher Animal Management Trust Center
  slug: gallagher-animal-management-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, FIPS 140
slug: gallagher-animal-management
tags:
- Animal Management
- Electric Fencing
- Weighing
- EID
- Watering
- Security
website: https://am.gallagher.com/
---
