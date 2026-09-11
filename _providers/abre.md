---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abre-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abre.com/
- group: company
  title: ''
  type: About
  url: https://abre.com/our-story/
- group: operate
  title: ''
  type: Support
  url: https://help.abre.io/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.abre.io/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://help.abre.io/hc/en-us/articles/4405261788699-Abre-Status
- group: company
  title: ''
  type: Blog
  url: https://abre.com/resource/
- group: commercial
  title: ''
  type: Pricing
  url: https://abre.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abre.com/privacyandcompliance/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abre.com/privacyandcompliance/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://abre.com/privacyandcompliance/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://abre.com/privacyandcompliance/service-level-agreement/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abreio
- group: company
  title: ''
  type: Careers
  url: https://abre.com/join-our-team/
- group: company
  title: ''
  type: Partners
  url: https://marketplace.abre.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abre-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abre-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/abre-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/abre-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abre-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/abre-packages.yml
coverage:
  checked: '2026-09-06'
  detail: Abre sells a managed Data-as-a-Service engagement to K-12 districts and is a client of other people's APIs rather than a publisher of one — its help center's six "API" articles are all guides for calling INTO Abre's ingestion (OneRoster 1.1, ClassLink, SchoolDay/GG4L, third-party assessment feeds), the only real API host candidate, auth.abre.io, is a catch-all that answers 200 "Please provide authentication parameters" even for a negative-control path that cannot exist, and developers.abre.com / docs.abre.com / api.abre.com are all unmapped Cloudways placeholder domains.
  evidence:
  - status: 403
    url: https://api.abre.com/
  - status: 403
    url: https://developers.abre.com/
  - status: 403
    url: https://docs.abre.com/
  - status: 404
    url: https://abre.com/openapi.json
  - status: 404
    url: https://abre.com/.well-known/agent-card.json
  - status: 200
    url: https://auth.abre.io/.well-known/abre-negative-control-7f3ab91c.json
  - status: 200
    url: https://help.abre.io/api/v2/help_center/articles/search.json?query=webhook
  - status: 200
    url: https://api.github.com/orgs/abreio/repos?per_page=100
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'Abre is a K-12 education data platform, founded in 2017 in Cincinnati, Ohio, that consolidates student, staff and operational data from a district''s student information system and its EdTech tools into a single interface built around a Student360 learner profile. The platform ships as a set of role-based apps — Analytics and Insight dashboards, Assessment, Health & Wellness, MTSS & Intervention, Student Success & ePortfolio, Staff Development, Communication & Engagement, Curriculum, Learn and Focus — plus a marketplace of shareable dashboard packs, plans, forms, courses and surveys. Abre is sold to districts as a managed Data-as-a-Service engagement rather than as a developer product: it is a heavy CONSUMER of other people''s APIs and publishes none of its own. Districts feed Abre through five documented rostering paths — an automated SIS integration over SFTP, SchoolDay (GG4L) School Passport, ClassLink OneRoster, OneRoster ZIP files dropped on SFTP, and a native 1EdTech
  OneRoster 1.1 REST API sync authenticated with OAuth 2.0 — and sign in through OAuth 2.0 SSO with Google, Microsoft, Apple, ClassLink, Clever, GG4L or Facebook. As of this profiling pass Abre publishes no developer portal, no API reference, no OpenAPI or other machine-readable contract, no SDKs and no public MCP or agent surface; its public technical surface is a Zendesk help center of integration guides for the APIs it ingests.'
image: https://abre.com/wp-content/uploads/2021/09/abre_logo_light.svg
layout: provider
modified: '2026-09-06'
name: Abre
nav: Providers
network: true
overview: 'Abre is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, K-12, EdTech, and Education Data.


  Abre''s developer surface includes support, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Abre Plans Pricing
  plan_count: 0
  slug: abre-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Abre Rate Limits
  slug: abre-rate-limits
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 21.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 44.4
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abre Domain Security
  slug: abre-domain-security
  summary_line: TLSv1.3 · DMARC
slug: abre
tags:
- Company
- Education
- K-12
- EdTech
- Education Data
- Student Information Systems
- Rostering
- Interoperability
- OneRoster
- Analytics
- Dashboards
- Single Sign On
website: https://abre.com/
---
