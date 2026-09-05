---
access_model:
  confidence: medium
  label: Self-service
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - https://newoldstamp.com/pricing/
  trial: true
  try_now: true
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
    error_semantics: false
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
  score: 18.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The undocumented application GraphQL API that powers the Newoldstamp dashboard — signatures, departments, campaigns, segments, Google Workspace and Microsoft 365 deployment, and billing. Introspection
  name: Newoldstamp GraphQL API
  slug: newoldstamp-graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newoldstamp-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newoldstamp-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/newoldstamp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/newoldstamp-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://newoldstamp.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.newoldstamp.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://newoldstamp.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://newoldstamp.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.newoldstamp.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.newoldstamp.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.newoldstamp.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newoldstamp.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newoldstamp.com/privacy/
created: '2026-07-17'
description: Newoldstamp is an email signature management platform that lets companies create, brand, and centrally manage professional email signatures across their teams. It provides a signature generator with customizable templates, department- and role-based signature deployment, email signature marketing banners and campaigns, click analytics, and integrations with Google Workspace, Microsoft 365, and popular email clients. Newoldstamp also operates Pearl Diver, a website-visitor identification product. Founded in 2016 and a wholly-owned subsidiary of Blackpearl Group since 2025 (previously backed by 500 Global), it serves marketing, sales, and IT teams that want consistent branded email signatures at scale. Newoldstamp publishes no documented public developer program, but its dashboard is powered by a GraphQL API at newoldstamp.com/api/graphql (41 queries, 71 mutations, 4 subscriptions) whose introspection is anonymously open.
image: https://newoldstamp.com/images/logo-v4.svg
layout: provider
modified: '2026-08-13'
name: Newoldstamp
nav: Providers
network: true
overview: 'Newoldstamp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Signatures, Email Signature Management, Email Marketing, and Branding.


  Newoldstamp''s developer surface includes documentation, pricing, engineering blog, support, signup flow, and 9 more developer resources.'
plans:
- name: Newoldstamp Plans Pricing
  plan_count: 2
  slug: newoldstamp-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Newoldstamp Rate Limits
  slug: newoldstamp-rate-limits
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 36.1
  provenance:
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newoldstamp/refs/heads/main/screenshots/newoldstamp-2026-08-07T185122.png
security:
- kind: authentication
  name: Newoldstamp Authentication
  slug: newoldstamp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Newoldstamp Domain Security
  slug: newoldstamp-domain-security
  summary_line: TLSv1.3
slug: newoldstamp
tags:
- Company
- Email Signatures
- Email Signature Management
- Email Marketing
- Branding
- Software-as-a-Service
- Productivity
- Website Visitor Identification
- GraphQL
website: https://newoldstamp.com
---
