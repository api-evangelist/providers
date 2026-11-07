---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/dmca-com/plans/dmca-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dmca-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dmca-com/llms/dmca-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dmca-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dmca-com/hosts/dmca-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dmca-com-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.dmca.com/Support/default.aspx?r=m
- group: start
  title: ''
  type: SignUp
  url: https://www.dmca.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dmca.com/Privacy.aspx
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dmca.com/Pricing.aspx?r=m
- group: company
  title: ''
  type: Blog
  url: https://blog.dmca.com/
- group: auth
  href: https://artifacts.apis.io/dmca-com/security/dmca-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dmca-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dmca.com/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on the provider's documentation page.
  evidence:
  - status: 301
    url: https://www.dmca.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DMCA.com is a content protection and takedown service founded in 2006. It helps creators, brands, and individuals worldwide remove stolen content from the internet. The company offers free reviews and a range of protection plans, leveraging a team of experts to enforce copyrights and combat piracy.
image: https://www.dmca.com/img/homescr.png
layout: provider
modified: '2026-11-05'
name: DMCA.com
nav: Providers
network: true
overview: 'DMCA.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Content Protection, Takedowns, Monitoring, Compliance, and Watermarking.


  DMCA.com''s developer surface includes support, signup flow, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Dmca Com Plans Pricing
  plan_count: 23
  slug: dmca-com-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dmca Com Domain Security
  slug: dmca-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dmca-com
tags:
- Content Protection
- Takedowns
- Monitoring
- Compliance
- Watermarking
- Badges
website: https://www.dmca.com/
---
