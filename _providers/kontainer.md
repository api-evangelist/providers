---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Oauth API from Kontainer DAM & PIM — 1 operation(s) for oauth.
  name: Kontainer DAM & PIM OAuth API
  slug: kontainer-oauth-api
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/plans/kontainer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kontainer-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/rules/kontainer-rules.yml
  title: ''
  type: Spectral
  url: rules/kontainer-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/json-ld/kontainer-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kontainer-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/vocabulary/kontainer-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kontainer-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/data-model/kontainer-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kontainer-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/conformance/kontainer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kontainer-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/llms/kontainer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kontainer-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/well-known/kontainer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kontainer-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/hosts/kontainer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kontainer-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://kontainer.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kontainer/refs/heads/main/security/kontainer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kontainer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kontainer.com
- group: docs
  title: ''
  type: Documentation
  url: https://app.kontainer.com/api/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://app.kontainer.com/docs?api-docs.json
- group: start
  title: ''
  type: GettingStarted
  url: https://kontainer.com/register
- group: operate
  title: ''
  type: Support
  url: https://kontainer.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://kontainer.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kontainer.com/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://kontainer.com/register
coverage:
  checked: '2026-10-05'
  detail: Documentation is only available as HTML pages without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://app.kontainer.com/api/documentation
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-05'
description: Kontainer provides a market‑leading Digital Asset Management (DAM) and Product Information Management (PIM) platform. It offers a GDPR‑secure, user‑friendly solution for organizing, sharing, and controlling assets such as images, videos, and brand guidelines. Features include automated workflows, consent and license management, multichannel product data hub, and integrations with CMS, Adobe Creative Cloud, and e‑commerce platforms, serving both internal teams and external partners.
image: https://cms.kontainer.com/wp-content/uploads/2022/01/Edit_product_PIM_Kontainer.jpg?v=1715170929
json_schemas:
- name: PostOauthTokenRequest
  property_count: 1
  slug: kontainer-post-oauth-token-request
- name: PostOauthTokenResponse
  property_count: 4
  slug: kontainer-post-oauth-token-response
jsonld:
- class_count: 2
  name: Kontainer Context
  property_count: 1
  slug: kontainer-context
layout: provider
modified: '2026-10-05'
name: Kontainer DAM & PIM
nav: Providers
network: true
overview: 'Kontainer DAM & PIM is listed with 1 API on the [APIs.io](https://apis.io/) network: OAuth API. Tagged areas include Digital Asset Management, Product Information Management, and Asset Management.


  The Kontainer DAM & PIM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kontainer DAM & PIM''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Kontainer Plans Pricing
  plan_count: 4
  slug: kontainer-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Kontainer DAM & PIM API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: kontainer-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 58.8
    catalog_earned_first_party: 12.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 19.9
    developer_ergonomics: 33.3
    discoverability: 57.1
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
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Kontainer Domain Security
  slug: kontainer-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: kontainer
tags:
- Digital Asset Management
- Product Information Management
- Asset Management
website: https://kontainer.com
---
