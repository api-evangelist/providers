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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/orumhq-com/well-known/orumhq-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/orumhq-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/orumhq-com/well-known/orumhq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/orumhq-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/orumhq-com/llms/orumhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orumhq-com-llms.txt
- group: other
  href: https://artifacts.apis.io/orumhq-com/hosts/orumhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orumhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/orumhq-com/vendors/orumhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orumhq-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.orum.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orum.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.orum.com/orum/directories
- group: operate
  title: ''
  type: StatusPage
  url: https://status.orum.com/
- group: auth
  title: ''
  type: Security
  url: https://www.orum.com/platform/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orum.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.orum.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.orum.com/blog
- group: auth
  href: https://artifacts.apis.io/orumhq-com/security/orumhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orumhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orumhq.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://orumhq.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Orum provides an agentic AI-powered cold calling software and sales dialer platform that automates dialing sessions, improves rep performance, and integrates with various sales tools. The solution offers features like intelligent call routing, real-time coaching, analytics, and compliance tools, targeting sales teams seeking to increase efficiency and scale outreach.
image: https://www.orum.com/logo.png
layout: provider
modified: '2026-10-25'
name: Orum
nav: Providers
network: true
overview: 'Orum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Sales, Automation, and Cold-Calling.


  Orum''s developer surface includes support, pricing, engineering blog, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Orumhq Com Domain Security
  slug: orumhq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: orumhq-com
tags:
- Company
- AI
- Sales
- Automation
- Cold-Calling
- SaaS
website: https://orumhq.com
---
