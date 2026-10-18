---
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
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Hospitality management platform API
  name: Canary API
  slug: canary-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://security.canarytechnologies.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canary4227/refs/heads/main/llms/canary4227-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canary4227-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canary4227/refs/heads/main/well-known/canary4227-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/canary4227-www-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canary4227/refs/heads/main/well-known/canary4227-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canary4227-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canary4227/refs/heads/main/hosts/canary4227-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canary4227-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canary4227/refs/heads/main/vendors/canary4227-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canary4227-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canarytechnologies.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canarytechnologies.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.canarytechnologies.com/press
- group: start
  title: ''
  type: Login
  url: https://www.canarytechnologies.com/login/
- group: company
  title: ''
  type: Blog
  url: https://www.canarytechnologies.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canary4227/refs/heads/main/security/canary4227-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/canary4227-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canary4227/refs/heads/main/security/canary4227-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canary4227-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.canarytechnologies.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.canarytechnologies.com/company
- group: commercial
  title: ''
  type: Pricing
  url: https://www.canarytechnologies.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://www.canarytechnologies.com/company
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://api.canarytechnologies.com/mcp
  - status: 200
    url: https://www.canarytechnologies.com
  - status: 403
    url: https://equityzen.com/company/canary4227
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Canary4227 is an AI‑powered investment analyst platform that provides software and data to help sophisticated investors make better decisions. Founded in 2022 and based in Wilmington, DE, the company offers tools for valuation, cap table analysis, revenue insights, and risk assessment, targeting accredited investors and institutional partners. Through its partnership with EquityZen, Canary enables private market access to pre‑IPO shares, delivering comprehensive analytics and research to support portfolio diversification and growth.
image: https://dioguwdgf472v.cloudfront.net/media/logos/equityinvest/Company/canary4227_logo-9df4b364785464a9.jpg
layout: provider
modified: '2026-10-06'
name: Canary4227
nav: Providers
network: true
overview: 'Canary4227 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Investment, Artificial Intelligence, and Analytics.


  Canary4227''s developer surface includes engineering blog, documentation, pricing, getting-started guide, and 13 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canary4227 Domain Security
  slug: canary4227-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Canary4227 Trust Center
  slug: canary4227-trust-center
  summary_line: SOC 2, PCI DSS
slug: canary4227
tags:
- Company
- Finance
- Investment
- Artificial Intelligence
- Analytics
- Private-Market
website: https://www.canarytechnologies.com
---
