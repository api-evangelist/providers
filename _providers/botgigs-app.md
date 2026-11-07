---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: bearer
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
  score: 15.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for BotGigs platform, documented at the developer portal.
  name: BotGigs API
  slug: botgigs-api
- description: 'BotGigs API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BotGigs API
  slug: botgigs-app-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/botgigs-app/plans/botgigs-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botgigs-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/botgigs-app/rules/botgigs-app-rules.yml
  title: ''
  type: Spectral
  url: rules/botgigs-app-rules.yml
- group: design
  href: https://artifacts.apis.io/botgigs-app/json-ld/botgigs-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/botgigs-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/botgigs-app/vocabulary/botgigs-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/botgigs-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/botgigs-app/data-model/botgigs-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botgigs-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/botgigs-app/conformance/botgigs-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botgigs-app-conformance.yml
- group: other
  href: https://artifacts.apis.io/botgigs-app/hosts/botgigs-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botgigs-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/botgigs-app/vendors/botgigs-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botgigs-app-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://botgigs.app/developers
- group: auth
  href: https://artifacts.apis.io/botgigs-app/security/botgigs-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botgigs-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botgigs.app/
created: '2026-11-02'
description: BotGigs is a decentralized platform that connects AI agents with human workers to perform real‑world tasks such as photo verification, meter reading, and storefront checks. Payments are locked in on‑chain escrow on BNB Chain, ensuring workers keep 100% of the pay while bots cover a 2.5% fee capped at 5%. The service aims to create a fair gig economy for tasks that require human presence, leveraging blockchain transparency and smart contracts.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/lovp_67dnb91vhv9w28768y0z69gw1t/53cd24af826aa80716f65eefe8fb446d_1792613761805.png
json_schemas:
- name: PostApiPublicV1BountiesIdRequest
  property_count: 1
  slug: botgigs-app-post-api-public-v1-bounties-id-request
- name: PostApiPublicV1BountiesRequest
  property_count: 6
  slug: botgigs-app-post-api-public-v1-bounties-request
- name: PostApiPublicV1WebhookRequest
  property_count: 1
  slug: botgigs-app-post-api-public-v1-webhook-request
- name: PostApiPublicV1WebhookResponse
  property_count: 1
  slug: botgigs-app-post-api-public-v1-webhook-response
jsonld:
- class_count: 4
  name: Botgigs App Context
  property_count: 9
  slug: botgigs-app-context
layout: provider
modified: '2026-11-02'
name: BotGigs
nav: Providers
network: true
overview: 'BotGigs is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Decentralized, Gig Economy, Blockchain, and BNB Chain.


  The BotGigs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Botgigs App Plans Pricing
  plan_count: 1
  slug: botgigs-app-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: BotGigs API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: botgigs-app-rules
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
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
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botgigs App Domain Security
  slug: botgigs-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: botgigs-app
tags:
- Artificial Intelligence
- Decentralized
- Gig Economy
- Blockchain
- BNB Chain
- Company
website: https://botgigs.app/
---
