---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: The GraphQL API behind the Adventus.io recruiter and student applications. Exposes 47 queries and 30 mutations across students, student documents, academic achievements, notes, activities, messaging t
  name: Adventus.io GraphQL API
  slug: adventusio-graphql
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://adventus.io/
- group: start
  title: ''
  type: Login
  url: https://app.adventus.io/admin/login
- group: start
  title: ''
  type: SignUp
  url: https://signup.adventus.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://adventus.io/pricing-recruiters-new/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adventus.io/website-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adventus.io/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://adventus.io/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://blog.adventus.io/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.adventus.io/rss.xml
- group: company
  title: ''
  type: About
  url: https://adventus.io/company/
- group: company
  title: ''
  type: Careers
  url: https://adventus.io/careers/
- group: auth
  title: ''
  type: Compliance
  url: https://adventus.io/recruiters/security/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adventusio
- group: commercial
  title: ''
  type: Plans
  url: plans/adventusio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adventusio-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adventusio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adventusio-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/adventusio-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adventusio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adventusio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-09'
description: 'Adventus.io operates an international student recruitment marketplace that connects education institutions, recruitment agents and students. Recruiters manage student records, documents, academic achievements, applications and orders through a single platform; institutions publish courses, intakes and admissions criteria and receive applications back. The platform is backed by a live GraphQL API at api.adventus.io/graphql (47 queries, 30 mutations) which fronts an internal REST v2 origin, plus Adventus Drive analytics and Adventus Connect institution invitations. There is no public developer portal: the schema is discoverable by anonymous introspection but all student, order and institution data requires a bearer token issued to a partner account.'
image: https://adventus.io/wp-content/uploads/2026/07/adv_favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Adventus.io MCP Server
  slug: adventusio-mcp-server
modified: '2026-09-09'
name: Adventus.io
nav: Providers
network: true
overview: 'Adventus.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, International Education, Student Recruitment, and Marketplace.


  Adventus.io''s developer surface includes signup flow, pricing, support, engineering blog, and 17 more developer resources.'
plans:
- name: Adventusio Plans Pricing
  plan_count: 2
  slug: adventusio-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Adventusio Rate Limits
  slug: adventusio-rate-limits
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 16.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adventusio Authentication
  slug: adventusio-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adventusio Domain Security
  slug: adventusio-domain-security
  summary_line: TLSv1.2 · DMARC
slug: adventusio
tags:
- Company
- Education
- International Education
- Student Recruitment
- Marketplace
- GraphQL
- Higher Education
- EdTech
- Admissions
- Analytics
website: https://adventus.io/
---
