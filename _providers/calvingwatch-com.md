---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: documented
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
  score: 18.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Calvingwatch Com Agentic Access
  operation_count: 6
  slug: calvingwatch-com-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://calvingwatch.com
  baseurl_source: declared
  description: Read-only, non-personal CalvingWatch facts.
  name: CalvingWatch Public knowledge API
  slug: calvingwatch-com-public-knowledge-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/calvingwatch-com/agentic-access/calvingwatch-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/calvingwatch-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/calvingwatch-com/rules/calvingwatch-com-rules.yml
  title: ''
  type: Spectral
  url: rules/calvingwatch-com-rules.yml
- group: design
  href: https://artifacts.apis.io/calvingwatch-com/json-ld/calvingwatch-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/calvingwatch-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/calvingwatch-com/vocabulary/calvingwatch-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/calvingwatch-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/calvingwatch-com/data-model/calvingwatch-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/calvingwatch-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/calvingwatch-com/security/calvingwatch-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/calvingwatch-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/calvingwatch-com/errors/calvingwatch-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/calvingwatch-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/calvingwatch-com/conformance/calvingwatch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calvingwatch-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calvingwatch-com/llms/calvingwatch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calvingwatch-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/calvingwatch-com/well-known/calvingwatch-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/calvingwatch-com-security.txt
- group: agent
  href: https://artifacts.apis.io/calvingwatch-com/well-known/calvingwatch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calvingwatch-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/calvingwatch-com/hosts/calvingwatch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calvingwatch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/calvingwatch-com/vendors/calvingwatch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calvingwatch-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calvingwatch.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://calvingwatch.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calvingwatch.com/privacy/
- group: auth
  href: https://artifacts.apis.io/calvingwatch-com/security/calvingwatch-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/calvingwatch-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/calvingwatch-com/security/calvingwatch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calvingwatch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calvingwatch.com/
created: '2026-11-04'
description: CalvingWatch provides AI-powered calving alerts using existing shed cameras. Farmers receive notifications when cows show calving signs, helping monitor livestock without new hardware. The Irish company Maranox Technologies Limited develops the service, offering mobile apps for iOS and Android, and operates a testing program with farms. Their platform processes camera images to detect repeated calving evidence, aiming to improve farm management and animal welfare.
image: https://calvingwatch.com/assets/calvingwatch-hero-nz.png
json_schemas:
- name: PublicKnowledge
  property_count: 0
  slug: calvingwatch-com-public-knowledge
- name: PublicPage
  property_count: 3
  slug: calvingwatch-com-public-page
jsonld:
- class_count: 2
  name: Calvingwatch Com Context
  property_count: 4
  slug: calvingwatch-com-context
layout: provider
modified: '2026-11-04'
name: CalvingWatch
nav: Providers
network: true
overview: 'CalvingWatch publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Public knowledge API. Tagged areas include Company, Agriculture, Artificial Intelligence, Livestock, and Monitoring.


  The CalvingWatch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CalvingWatch''s developer surface includes support and 18 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: CalvingWatch API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: calvingwatch-com-rules
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 50.5
    developer_ergonomics: 2.4
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calvingwatch Com Domain Security
  slug: calvingwatch-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Calvingwatch Com Vulnerability Disclosure
  slug: calvingwatch-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: calvingwatch-com
tags:
- Company
- Agriculture
- Artificial Intelligence
- Livestock
- Monitoring
- Ireland
website: https://calvingwatch.com/
---
