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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cuemarc/refs/heads/main/plans/cuemarc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cuemarc-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuemarc/refs/heads/main/llms/cuemarc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cuemarc-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuemarc/refs/heads/main/hosts/cuemarc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuemarc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuemarc/refs/heads/main/vendors/cuemarc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cuemarc-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cuemarc.com/about/press
- group: other
  title: ''
  type: Leadership
  url: https://cuemarc.com/home/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuemarc/refs/heads/main/security/cuemarc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuemarc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cuemarc.com/
- group: company
  title: ''
  type: Blog
  url: https://cuemarc.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://cuemarc.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.cuemarc.com/sign-up
- group: other
  title: ''
  type: SignIn
  url: https://app.cuemarc.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuemarc.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuemarc.com/data-policy
- group: operate
  title: ''
  type: Support
  url: https://cuemarc.com/contact
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cuemarc.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Cuemarc provides AI-driven listening and reputation management tools for corporate communications, PR, and marketing teams. Their platform monitors large language model outputs to track narrative visibility, manage brand reputation, and identify content gaps. Offering features like real-time alerts, detailed reports, and actionable insights, Cuemarc helps organizations stay ahead of AI-driven reputational risks across pharma, medtech, and other industries.
image: https://cdn.prod.website-files.com/68165623f124bbec2da33b14/6898f320fd37afddcdf528be_31f850e7c4d9438637ab277220e40af2_Cuemarc_Thumbnail_SEO.png
layout: provider
modified: '2026-10-16'
name: Cuemarc
nav: Providers
network: true
overview: 'Cuemarc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Reputation-Management, Marketing, and LLM.


  Cuemarc''s developer surface includes engineering blog, pricing, signup flow, support, and 11 more developer resources.'
plans:
- name: Cuemarc Plans Pricing
  plan_count: 3
  slug: cuemarc-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cuemarc Domain Security
  slug: cuemarc-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cuemarc
tags:
- Company
- Artificial Intelligence
- Reputation-Management
- Marketing
- LLM
website: https://cuemarc.com/
---
