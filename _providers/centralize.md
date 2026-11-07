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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/centralize/plans/centralize-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/centralize-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/centralize/llms/centralize-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centralize-llms.txt
- group: agent
  href: https://artifacts.apis.io/centralize/well-known/centralize-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centralize-well-known.yml
- group: other
  href: https://artifacts.apis.io/centralize/hosts/centralize-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centralize-hosts.yml
- group: other
  href: https://artifacts.apis.io/centralize/vendors/centralize-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centralize-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usecentralize.com/tos
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usecentralize.com/
- group: start
  title: ''
  type: SignUp
  url: https://auth.usecentralize.com/en/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usecentralize.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usecentralize.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.usecentralize.com/blog
- group: auth
  href: https://artifacts.apis.io/centralize/security/centralize-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centralize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usecentralize.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.usecentralize.com/api/mcp
  - status: 200
    url: https://www.usecentralize.com/
  reason: partner-login
  state: gated
created: '2026-10-22'
description: Centralize provides a relationship workspace for enterprise deal teams that builds account maps, org charts, and stakeholder maps from a company’s CRM, email, and call data. The platform offers AI‑driven insights and outreach recommendations, integrates with tools such as Salesforce, Slack, Gmail, and Gong, and includes security features like SOC 2 Type 2 compliance, SSO, and encryption. It is positioned for sales, customer success, and leadership teams to coordinate account collaboration and drive deal progress.
image: https://cdn.prod.website-files.com/68b575724770c1e3b217c335/6a67de47d8128dae9c87f9c8_centralize-og-2026.png
layout: provider
modified: '2026-10-22'
name: Centralize
nav: Providers
network: true
overview: 'Centralize is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Account Mapping, CRM Integration, and Enterprise Sales.


  Centralize''s developer surface includes signup flow, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Centralize Plans Pricing
  plan_count: 3
  slug: centralize-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 46.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/centralize/centralize-2026-11-03T123654.png
security:
- kind: domain-security
  name: Centralize Domain Security
  slug: centralize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: centralize
tags:
- Account Mapping
- CRM Integration
- Enterprise Sales
website: https://www.usecentralize.com/
---
