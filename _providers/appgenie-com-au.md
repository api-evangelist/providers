---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 5.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AppGenie's Compliance MCP platform, documented at the developer portal.
  name: Compliance MCP API
  slug: compliance-mcp-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/appgenie-com-au/authentication/appgenie-com-au-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appgenie-com-au-authentication.yml
- group: other
  href: https://artifacts.apis.io/appgenie-com-au/hosts/appgenie-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appgenie-com-au-hosts.yml
- group: other
  href: https://artifacts.apis.io/appgenie-com-au/vendors/appgenie-com-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appgenie-com-au-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://appgenie.com.au/compliance-mcp/releases
- group: auth
  href: https://artifacts.apis.io/appgenie-com-au/security/appgenie-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appgenie-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appgenie.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appgenie.com.au/developer_services
- group: docs
  title: ''
  type: Documentation
  url: https://appgenie.com.au/compliance-mcp/docs
- group: company
  title: ''
  type: Blog
  url: https://appgenie.com.au/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appgenie.com.au/Legal/Terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appgenie.com.au/Legal/Privacy
coverage:
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://appgenie.com.au/compliance-mcp/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AppGenie is a distinguished B2B-oriented IT service provider specializing in Salesforce, AWS, Azure and DevSecOps solutions. They help businesses transition to cloud platforms, optimise applications, and deliver custom software, consulting and staffing across Australia, New Zealand and India. Over 20 years of experience underpin their Salesforce ISV and consulting partnership, offering integration, migration and managed services.
image: https://appgenie.com.au/img/social/og-default.jpg
layout: provider
modified: '2026-11-01'
name: AppGenie
nav: Providers
network: true
overview: 'AppGenie is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Cloud, Salesforce, DevSecOps, and Consulting.


  AppGenie''s developer surface includes authentication, changelog, documentation, engineering blog, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 19.3
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
security:
- kind: authentication
  name: Appgenie Com Au Authentication
  slug: appgenie-com-au-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Appgenie Com Au Domain Security
  slug: appgenie-com-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appgenie-com-au
tags:
- B2B
- Cloud
- Salesforce
- DevSecOps
- Consulting
website: https://appgenie.com.au/
---
