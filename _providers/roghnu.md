---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/roghnu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/roghnu/plans/roghnu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/roghnu-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/roghnu/llms/roghnu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/roghnu-llms.txt
- group: other
  href: https://artifacts.apis.io/roghnu/hosts/roghnu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/roghnu-hosts.yml
- group: other
  href: https://artifacts.apis.io/roghnu/vendors/roghnu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/roghnu-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.roghnu.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.roghnu.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://apps.roghnu.com/login/okta
- group: start
  title: ''
  type: GettingStarted
  url: https://www.roghnu.com/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Roghnu
- group: auth
  href: https://artifacts.apis.io/roghnu/security/roghnu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/roghnu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.roghnu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.roghnu.com/about
- group: docs
  title: ''
  type: APIReference
  url: https://www.roghnu.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.roghnu.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.roghnu.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.roghnu.com/contact-us
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://support.roghnu.com/mcp
  - status: 200
    url: https://roghnu.com/
  reason: partner-login
  state: gated
created: '2026-10-21'
description: Roghnu provides a data portal that gives finance and operations leaders a complete, reliable view of their business data without delays or manual effort. It offers advanced reporting, analytics, and integrations for Sage Intacct and other enterprise systems, enabling automation of data and business operations.
image: http://static1.squarespace.com/static/662a88140606f60074fec974/t/6a0b7d572290bd3a6e71730b/1779137879487/roghnu-logo.png?format=1500w
layout: provider
modified: '2026-10-21'
name: Roghnu
nav: Providers
network: true
overview: 'Roghnu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Finance, Automation, and Analytics.


  Roghnu''s developer surface includes getting-started guide, documentation, API reference, pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Roghnu Plans Pricing
  plan_count: 8
  slug: roghnu-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 24.3
    discoverability: 55.4
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.7
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/roghnu/roghnu-2026-11-03T142610.png
security:
- kind: domain-security
  name: Roghnu Domain Security
  slug: roghnu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: roghnu
tags:
- Company
- Data
- Finance
- Automation
- Analytics
website: https://www.roghnu.com/
---
