---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/betteryou/refs/heads/main/llms/betteryou-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betteryou-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/betteryou/refs/heads/main/well-known/betteryou-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betteryou-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betteryou/refs/heads/main/hosts/betteryou-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betteryou-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/betteryou/refs/heads/main/vendors/betteryou-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betteryou-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betteryou.com/pages/terms-conditions
- group: start
  title: ''
  type: SignUp
  url: https://betteryou.com/account/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betteryou.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://betteryou.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/betteryou/refs/heads/main/security/betteryou-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betteryou-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betteryou.com
coverage:
  checked: '2026-09-28'
  detail: GraphQL endpoint returns JSON but no SDL or schema, and no OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://betteryou.com/api/graphql
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: BetterYou provides smart nutritional supplementation products designed for optimal absorption and wellbeing. Their range includes vitamin sprays, transdermal magnesium, and targeted supplements for immunity, sleep, energy, and joint health, backed by scientific research and partnerships with academic institutions.
image: https://cdn.shopify.com/s/files/1/0482/1336/0800/files/BetterYou_logo-800x800px.png?v=1778144121
layout: provider
modified: '2026-09-28'
name: BetterYou
nav: Providers
network: true
overview: 'BetterYou is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Supplements, Health, and Wellness.


  BetterYou''s developer surface includes signup flow and 9 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Betteryou Domain Security
  slug: betteryou-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: betteryou
tags:
- Company
- Nutrition
- Supplements
- Health
- Wellness
website: https://betteryou.com
---
