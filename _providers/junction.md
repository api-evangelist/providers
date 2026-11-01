---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: derived
    idempotency: derived
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.4
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 11
asyncapis:
- description: ''
  name: Junction Webhooks
  slug: junction-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/junction/rate-limits/junction-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/junction-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/junction/plans/junction-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/junction-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/junction/rules/junction-rules.yml
  title: ''
  type: Spectral
  url: rules/junction-rules.yml
- group: design
  href: https://artifacts.apis.io/junction/json-ld/junction-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/junction-context.jsonld
- group: design
  href: https://artifacts.apis.io/junction/vocabulary/junction-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/junction-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/junction/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/junction/asyncapi/junction-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/junction-webhooks.yml
- group: design
  href: https://artifacts.apis.io/junction/data-model/junction-data-model.yml
  title: ''
  type: DataModel
  url: data-model/junction-data-model.yml
- group: build
  href: https://artifacts.apis.io/junction/cli/junction-cli.yml
  title: ''
  type: CLI
  url: cli/junction-cli.yml
- group: operate
  href: https://artifacts.apis.io/junction/changelog/junction-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/junction-changelog.yml
- group: design
  href: https://artifacts.apis.io/junction/conventions/junction-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/junction-conventions.yml
- group: design
  href: https://artifacts.apis.io/junction/conventions/junction-conventions.yml
  title: ''
  type: Conventions
  url: conventions/junction-conventions.yml
- group: design
  href: https://artifacts.apis.io/junction/errors/junction-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/junction-problem-types.yml
- group: design
  href: https://artifacts.apis.io/junction/conformance/junction-conformance.yml
  title: ''
  type: Conformance
  url: conformance/junction-conformance.yml
- group: agent
  href: https://artifacts.apis.io/junction/llms/junction-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/junction-llms.txt
- group: other
  href: https://artifacts.apis.io/junction/a2a/junction-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/junction-a2a.yml
- group: agent
  href: https://artifacts.apis.io/junction/well-known/junction-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/junction-well-known.yml
- group: other
  href: https://artifacts.apis.io/junction/hosts/junction-hosts.yml
  title: ''
  type: Hosts
  url: hosts/junction-hosts.yml
- group: other
  href: https://artifacts.apis.io/junction/vendors/junction-vendors.yml
  title: ''
  type: Vendors
  url: vendors/junction-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.junction.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.junction.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.junction.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.junction.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.junction.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.junction.com/changelog/core/api
- group: company
  title: ''
  type: Blog
  url: https://www.junction.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.junction.com/home/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.junction.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.junction.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/junction/security/junction-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/junction-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.junction.com/
created: '2026-10-21'
description: Junction provides seamless lab testing and wearable device data integration, enabling healthcare providers to scale personalized, predictive care across a nationwide network of labs. Their API unifies lab results, wearable metrics, and operational support into a single platform, helping clinicians focus on patient outcomes and improve care efficiency.
image: https://cdn.prod.website-files.com/67bf6726a5412da9f551ac77/68a4ca9bdccbf1d3ce0c2617_Frame%201597885742.png
jsonld:
- class_count: 120
  name: Junction Context
  property_count: 245
  slug: junction-context
layout: provider
modified: '2026-10-21'
name: Junction
nav: Providers
network: true
overview: 'Junction publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Lab Testing, and Wearables.


  The Junction catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Junction''s developer surface includes CLI, changelog, support, pricing, engineering blog, getting-started guide, documentation, and 24 more developer resources.'
plans:
- name: Junction Plans Pricing
  plan_count: 2
  slug: junction-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Junction Rate Limits
  slug: junction-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Junction API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 3
  slug: junction-rules
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 54.8
    catalog_earned_first_party: 16.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 59.1
    developer_ergonomics: 44.6
    discoverability: 39.3
    operational_transparency: 60.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Junction Domain Security
  slug: junction-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: junction-book-phlebotomy-appointment
  slug: junction-book-phlebotomy-appointment
- name: junction-checkout-flow
  slug: junction-checkout-flow
- name: junction-create-and-retrieve-user
  slug: junction-create-and-retrieve-user
- name: junction-insurance-payor-and-icd-validation
  slug: junction-insurance-payor-and-icd-validation
- name: junction-link-create-demo-connection
  slug: junction-link-create-demo-connection
slug: junction
tags:
- Company
- Healthcare
- Lab Testing
- Wearables
website: https://www.junction.com/
---
