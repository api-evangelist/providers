---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: operate
  href: https://artifacts.apis.io/changeio/changelog/changeio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/changeio-changelog.yml
- group: auth
  href: https://artifacts.apis.io/changeio/authentication/changeio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/changeio-authentication.yml
- group: agent
  href: https://artifacts.apis.io/changeio/llms/changeio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/changeio-llms.txt
- group: agent
  href: https://artifacts.apis.io/changeio/well-known/changeio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/changeio-well-known.yml
- group: other
  href: https://artifacts.apis.io/changeio/hosts/changeio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/changeio-hosts.yml
- group: other
  href: https://artifacts.apis.io/changeio/vendors/changeio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/changeio-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://getchange.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://link.getchange.io/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://getchange.io/press
- group: other
  title: ''
  type: Leadership
  url: https://getchange.io/team/amar-shah
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getchange.io/blog-categories/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.getchange.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://getchange.io/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getchange.io/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getchange.io/
- group: auth
  href: https://artifacts.apis.io/changeio/security/changeio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/changeio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getchange.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://getchange.io/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Change offers a donations and compliance platform that enables businesses and legal teams to automate charitable giving, handle state filing requirements, and manage nonprofit verifications. The cloud‑based solution provides a Donations API, disbursement tools, and a dashboard for tracking contributions and legal documents. It serves companies, law firms, and charitable fundraising platforms that need to run compliant giving campaigns worldwide.
image: https://cdn.prod.website-files.com/661448530b1a9425667dbbd8/663fc14146ab7f9c07f94bf9_0mDMUY6.png
layout: provider
modified: '2026-10-26'
name: Change.io
nav: Providers
network: true
overview: 'Change.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Donations, Compliance, Nonprofit Verification, Disbursements, and Corporate Giving.


  Change.io''s developer surface includes changelog, authentication, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Changeio Plans Pricing
  plan_count: 0
  slug: changeio-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/changeio/changeio-2026-11-03T123823.png
security:
- kind: authentication
  name: Changeio Authentication
  slug: changeio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Changeio Domain Security
  slug: changeio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: changeio
tags:
- Donations
- Compliance
- Nonprofit Verification
- Disbursements
- Corporate Giving
- Legal Teams
- Charitable Registrations
website: https://getchange.io/
---
