---
agent_readiness:
  band: agent-aware
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Collaborative platform API for gathering feedback, forms, moodboards and comparisons.
  name: EncoreHQ API
  slug: encorehq-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/encorehq-co/plans/encorehq-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/encorehq-co-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/encorehq-co/llms/encorehq-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/encorehq-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/encorehq-co/well-known/encorehq-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/encorehq-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/encorehq-co/hosts/encorehq-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/encorehq-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/encorehq-co/vendors/encorehq-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/encorehq-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://encorehq.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://encorehq.co/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://encorehq.co/pricing
- group: start
  title: ''
  type: Login
  url: https://encorehq.co/login
- group: auth
  href: https://artifacts.apis.io/encorehq-co/security/encorehq-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/encorehq-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://encorehq.co/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL spec found despite public website and docs links.
  evidence:
  - status: 404
    url: https://api.encorehq.co/openapi.json
  - status: 404
    url: https://api.encorehq.co/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: EncoreHQ provides a collaborative platform for gathering feedback through forms, moodboards, comparisons, and visual workflows. Teams can create interactive questionnaires, collect image‑based ratings, and compare options side‑by‑side, helping product and design teams make data‑driven decisions. The service supports multiple use‑cases ranging from wedding planners to interior designers, offering customizable templates and real‑time results to streamline stakeholder communication and decision making.
image: https://encorehq.co/site/og/home.png
layout: provider
modified: '2026-10-30'
name: encorehq-co
nav: Providers
network: true
overview: 'encorehq-co is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Feedback, Design, Product, and SaaS.


  encorehq-co''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Encorehq Co Plans Pricing
  plan_count: 3
  slug: encorehq-co-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Encorehq Co Domain Security
  slug: encorehq-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: encorehq-co
tags:
- Collaboration
- Feedback
- Design
- Product
- SaaS
website: https://encorehq.co/
---
