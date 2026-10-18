---
agent_readiness:
  band: agent-ready
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://dev.cobot.me
  baseurl_source: declared
  description: Cobot API 2.0 for coworking management
  name: Cobot API
  slug: cobot-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/plans/cobot2-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cobot2-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/authentication/cobot2-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cobot2-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/conformance/cobot2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cobot2-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/llms/cobot2-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cobot2-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/well-known/cobot2-helpcenter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cobot2-helpcenter-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/well-known/cobot2-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cobot2-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/hosts/cobot2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cobot2-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/packages/cobot2-packages.yml
  title: ''
  type: SDKs
  url: packages/cobot2-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/packages/cobot2-packages.yml
  title: ''
  type: Packages
  url: packages/cobot2-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cobot.me/en/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.cobot.me/en/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cobot.me/en/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cobot.me/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.cobot.me/en/press
- group: start
  title: ''
  type: Login
  url: https://www.cobot.me/login
- group: company
  title: ''
  type: Blog
  url: https://blog.cobot.me/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.cobot.me/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cobot
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cobot2/refs/heads/main/security/cobot2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cobot2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cobot.me
created: '2026-10-09'
description: Cobot2 provides coworking management software that helps operators automate member onboarding, bookings, invoicing, access control, and community engagement. The platform offers a mobile app, white‑label member portal, analytics, and integrations with payment and access systems, serving coworking spaces worldwide.
image: https://www-cdn.cobot.me/assets/meta/cobot-management-software-41203b82.jpg
layout: provider
modified: '2026-10-09'
name: Cobot2
nav: Providers
network: true
overview: 'Cobot2 is listed with 1 API on the [APIs.io](https://apis.io/) network: Cobot API. Tagged areas include Co-Working, Software-as-a-Service, Management, Software, and Collaboration.


  Cobot2''s developer surface includes authentication, support, pricing, engineering blog, documentation, and 15 more developer resources.'
plans:
- name: Cobot2 Plans Pricing
  plan_count: 4
  slug: cobot2-plans-pricing
random_paper: 13
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 26.9
    developer_ergonomics: 35.7
    discoverability: 75.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Cobot2 Authentication
  slug: cobot2-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cobot2 Domain Security
  slug: cobot2-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cobot2
tags:
- Co-Working
- Software-as-a-Service
- Management
- Software
- Collaboration
- Company
website: https://www.cobot.me
---
