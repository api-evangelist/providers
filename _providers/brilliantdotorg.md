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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Educational platform offering problem solving and learning resources.
  name: Brilliant
  slug: brilliant
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brilliantdotorg/refs/heads/main/llms/brilliantdotorg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brilliantdotorg-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brilliantdotorg/refs/heads/main/hosts/brilliantdotorg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brilliantdotorg-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brilliantdotorg/refs/heads/main/vendors/brilliantdotorg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brilliantdotorg-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brilliant.org/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://brilliant.org/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brilliant.org/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://brilliant.org/help/pricing-and-plans/
- group: company
  title: ''
  type: Blog
  url: https://blog.brilliant.org/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brilliantdotorg/refs/heads/main/security/brilliantdotorg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brilliantdotorg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brilliant.org
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://brilliant.org
  - status: 403
    url: https://equityzen.com/company/brilliantdotorg
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Brilliant.org is an online learning platform that offers interactive problem‑solving courses in mathematics, science, and computer programming. It provides a personal tutor named Koji that adapts to each learner, delivering adaptive lessons, practice sets, and instant feedback. The service targets students, educators, and lifelong learners, aiming to develop critical thinking and STEM skills through engaging, gamified content. With millions of users worldwide, Brilliant.org combines educational research with AI‑enhanced tutoring to help learners master concepts efficiently.
image: https://brilliant.org/images/opengraph/og-lohp-1.png
layout: provider
modified: '2026-10-06'
name: Brilliantdotorg
nav: Providers
network: true
overview: 'Brilliantdotorg is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Brilliantdotorg''s developer surface includes support, pricing, engineering blog, and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brilliantdotorg Domain Security
  slug: brilliantdotorg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brilliantdotorg
tags:
- Company
website: https://brilliant.org
---
