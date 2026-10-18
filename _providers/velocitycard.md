---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Cards API from VelocityCard Card Issuing — 4 operation(s) for cards.
  name: VelocityCard Card Issuing Cards API
  slug: velocitycard-cards-api
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/plans/velocitycard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/velocitycard-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/rules/velocitycard-rules.yml
  title: ''
  type: Spectral
  url: rules/velocitycard-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/json-ld/velocitycard-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/velocitycard-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/vocabulary/velocitycard-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/velocitycard-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/data-model/velocitycard-data-model.yml
  title: ''
  type: DataModel
  url: data-model/velocitycard-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/conformance/velocitycard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/velocitycard-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/llms/velocitycard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/velocitycard-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/hosts/velocitycard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/velocitycard-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/vendors/velocitycard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/velocitycard-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.velocitycard.io/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.velocitycard.io/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.velocitycard.io/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.velocitycard.io/press
- group: company
  title: ''
  type: Blog
  url: https://www.velocitycard.io/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/velocitycard/refs/heads/main/security/velocitycard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/velocitycard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.velocitycard.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.velocitycard.io/card-issuing-api
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.velocitycard.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: VelocityCard provides a card issuing platform and banking-as-a-service (BaaS) solutions for businesses, fintechs, and banks. It enables issuance of virtual and physical cards, spend controls, and real‑time transaction monitoring. The service emphasizes low cost, rapid program launch, and no asset minimums, targeting commercial card programs and digital payment infrastructure.
image: https://www.velocitycard.io/og/homepage.jpg
json_schemas:
- name: PostV1CardsIssueRequest
  property_count: 8
  slug: velocitycard-post-v1-cards-issue-request
- name: PostV1CardsIssueResponse
  property_count: 3
  slug: velocitycard-post-v1-cards-issue-response
jsonld:
- class_count: 2
  name: Velocitycard Context
  property_count: 11
  slug: velocitycard-context
layout: provider
modified: '2026-10-11'
name: VelocityCard Card Issuing
nav: Providers
network: true
overview: 'VelocityCard Card Issuing is listed with 1 API on the [APIs.io](https://apis.io/) network: Cards API. Tagged areas include Card Issuing, Banking as a Service, Embedded Finance, Commercial Cards, and Payments.


  The VelocityCard Card Issuing catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  VelocityCard Card Issuing''s developer surface includes signup flow, engineering blog, documentation, and 14 more developer resources.'
plans:
- name: Velocitycard Plans Pricing
  plan_count: 3
  slug: velocitycard-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: VelocityCard Card Issuing API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: velocitycard-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 20.9
    developer_ergonomics: 11.9
    discoverability: 66.1
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Velocitycard Domain Security
  slug: velocitycard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: velocitycard
tags:
- Card Issuing
- Banking as a Service
- Embedded Finance
- Commercial Cards
- Payments
- Expense Management
website: https://www.velocitycard.io
---
