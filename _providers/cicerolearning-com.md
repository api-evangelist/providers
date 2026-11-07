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
  band: human-only
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Cicero Learning platform
  name: Cicero Learning API
  slug: cicero-learning-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/cicerolearning-com/llms/cicerolearning-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cicerolearning-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cicerolearning-com/well-known/cicerolearning-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cicerolearning-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cicerolearning-com/hosts/cicerolearning-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cicerolearning-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cicerolearning-com/vendors/cicerolearning-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cicerolearning-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cicerolearning-com/security/cicerolearning-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cicerolearning-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cicerolearning.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://cicerolearning.com/book-a-consult
- group: operate
  title: ''
  type: Support
  url: https://cicerolearning.com/contact
- group: company
  title: ''
  type: Blog
  url: https://cicerolearning.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cicerolearning.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cicerolearning.com/privacy-policy
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 307
    url: https://admin.cicerolearning.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Cicero Learning provides personalized one-to-one online tutoring for homeschoolers, worldschoolers, and students seeking flexible education. With over 150 teachers across 14 time zones, they offer accredited courses from primary through high school, including AP and college prep. The platform matches each student with a dedicated teacher, tailoring lessons to individual goals and schedules, and supports microschools and homeschooling curricula.
image: https://cicerolearning.com/og-default.jpg
layout: provider
modified: '2026-11-03'
name: Cicero Learning
nav: Providers
network: true
overview: 'Cicero Learning is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Tutoring, Homeschool, Worldschooling, and Personalized Learning.


  Cicero Learning''s developer surface includes getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cicerolearning Com Domain Security
  slug: cicerolearning-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cicerolearning-com
tags:
- Education
- Tutoring
- Homeschool
- Worldschooling
- Personalized Learning
website: https://cicerolearning.com/
---
