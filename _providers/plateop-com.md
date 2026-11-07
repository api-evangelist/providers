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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Het gratis deel van een Plate-op-aankooprapport: registergegevens, keuringen, tellerstandoordeel en terugroepacties voor één voertuig, als JSON met bron en peildatum per feit. Geen persoonsgegevens, g'
  name: Plate-op Public Vehicle Report API
  slug: public-vehicle-report
- baseURL: https://nederland.plateop.com
  baseurl_source: declared
  description: 'Het gratis deel van een Plate-op-aankooprapport: registergegevens, keuringen, tellerstandoordeel en terugroepacties voor één voertuig, als JSON met bron en peildatum per feit. Geen persoonsgegevens, g'
  name: 'Plate-op: publiek voertuigrapport op kenteken .well-known API'
  slug: plate-op-publiek-voertuigrapport-op-kenteken-well-known-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/plateop-com/rules/plateop-com-rules.yml
  title: ''
  type: Spectral
  url: rules/plateop-com-rules.yml
- group: design
  href: https://artifacts.apis.io/plateop-com/json-ld/plateop-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/plateop-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/plateop-com/vocabulary/plateop-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/plateop-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/plateop-com/conformance/plateop-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plateop-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/plateop-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/plateop-com/data-model/plateop-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plateop-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/plateop-com/errors/plateop-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plateop-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/plateop-com/llms/plateop-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plateop-com-llms.txt
- group: other
  href: https://artifacts.apis.io/plateop-com/hosts/plateop-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plateop-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/plateop-com/vendors/plateop-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plateop-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/plateop-com/security/plateop-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plateop-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plateop.com/
created: '2026-10-30'
description: 'plateop-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://plateop.com/og-image.png
json_schemas:
- name: RapportKentekenResponse
  property_count: 16
  slug: plateop-com-rapport-kenteken-response
jsonld:
- class_count: 2
  name: Plateop Com Context
  property_count: 18
  slug: plateop-com-context
layout: provider
modified: '2026-10-30'
name: plateop-com
nav: Providers
network: true
overview: 'plateop-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Plate-op: publiek voertuigrapport op kenteken .well-known API, and 1 more. Tagged areas include Company.


  The plateop-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: plateop-com API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: plateop-com-rules
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 41.2
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 11.2
    discoverability: 46.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.3
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/plateop-com/plateop-com-2026-11-03T141258.png
security:
- kind: domain-security
  name: Plateop Com Domain Security
  slug: plateop-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: public-vehicle-report
  slug: plateop-com-public-vehicle-report
slug: plateop-com
tags:
- Company
website: https://plateop.com/
---
