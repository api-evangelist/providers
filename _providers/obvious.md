---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/obvious/plans/obvious-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/obvious-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/obvious/changelog/obvious-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/obvious-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.obvious.ai/security
- group: auth
  href: https://artifacts.apis.io/obvious/authentication/obvious-authentication.yml
  title: ''
  type: Authentication
  url: authentication/obvious-authentication.yml
- group: agent
  href: https://artifacts.apis.io/obvious/llms/obvious-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/obvious-llms.txt
- group: other
  href: https://artifacts.apis.io/obvious/hosts/obvious-hosts.yml
  title: ''
  type: Hosts
  url: hosts/obvious-hosts.yml
- group: other
  href: https://artifacts.apis.io/obvious/vendors/obvious-vendors.yml
  title: ''
  type: Vendors
  url: vendors/obvious-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.obvious.ai/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.obvious.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.obvious.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.obvious.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.obvious.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://obvious.ai/newsroom
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.obvious.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.obvious.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.obvious.ai/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.obvious.ai/
- group: auth
  href: https://artifacts.apis.io/obvious/security/obvious-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/obvious-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/obvious/security/obvious-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/obvious-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://obvious.ai/
coverage:
  checked: '2026-10-24'
  detail: Obvious provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://obvious.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Obvious is a technology company focused on providing advanced data analytics and AI-driven insights for businesses. Founded by a collective of seasoned entrepreneurs, the company leverages cutting‑edge machine learning models to transform raw data into actionable intelligence, helping clients optimize operations, improve decision‑making, and drive growth. Obvious offers a suite of APIs that enable seamless integration of its analytics platform into existing workflows, delivering real‑time dashboards, predictive modeling, and customizable reporting tools. The firm is committed to transparency, security, and scalability, ensuring that its services meet the rigorous demands of enterprise environments while remaining accessible to developers through comprehensive documentation and robust support.
image: https://obvious-marketing-assets.s3.amazonaws.com/marketing/og/og-home.jpg
layout: provider
modified: '2026-10-24'
name: Obvious
nav: Providers
network: true
overview: 'Obvious is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, AI, Enterprise, and APIs.


  Obvious'' developer surface includes changelog, authentication, pricing, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Obvious Plans Pricing
  plan_count: 6
  slug: obvious-plans-pricing
random_paper: 7
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 50.0
    operational_transparency: 42.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Obvious Authentication
  slug: obvious-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Obvious Domain Security
  slug: obvious-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Obvious Trust Center
  slug: obvious-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: obvious
tags:
- Company
- Data Analytics
- AI
- Enterprise
- APIs
website: https://obvious.ai/
---
