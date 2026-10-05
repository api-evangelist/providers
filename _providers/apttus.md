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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/conventions/apttus-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apttus-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/security/apttus-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/apttus-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/authentication/apttus-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apttus-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/llms/apttus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apttus-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/well-known/apttus-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apttus-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/well-known/apttus-learningcenter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apttus-learningcenter-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/well-known/apttus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apttus-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/hosts/apttus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apttus-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/vendors/apttus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apttus-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.conga.com/site/terms
- group: operate
  title: ''
  type: Support
  url: https://support.conga.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conga.com/
- group: start
  title: ''
  type: SignUp
  url: https://community.conga.com/member/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conga.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://conga.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://conga.com/press
- group: other
  title: ''
  type: Leadership
  url: https://conga.com/de/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://documentation.conga.com/en/release-notes
- group: company
  title: ''
  type: Blog
  url: https://conga.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.conga.com/revenue/reference/post_split-criteria-1
- group: docs
  title: ''
  type: Documentation
  url: https://developer.conga.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/security/apttus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apttus-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apttus/refs/heads/main/security/apttus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apttus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conga.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://developer.conga.com/mcp
  - status: 403
    url: https://community.conga.com/mcp
  - status: 403
    url: https://forgeglobal.com/apttus_stock/
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Apttus, now part of Conga, provides cloud-based solutions for quote‑to‑cash, contract lifecycle management, and document automation. The company offers a unified platform that helps enterprises streamline pricing, sales, and legal processes, integrating CPQ, CLM, e‑signature, and revenue management into a single SaaS solution.
image: https://conga.com/sites/default/files/styles/large/public/image/2026-03/Social%20Share%20%281%29%20%281%29.png?itok=uH7gF5iu
layout: provider
modified: '2026-09-25'
name: Apttus
nav: Providers
network: true
overview: 'Apttus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Software-as-a-Service, CPQ, Contract Lifecycle Management, Document Automation, and Quote-to-Cash.


  Apttus'' developer surface includes authentication, support, signup flow, pricing, changelog, engineering blog, getting-started guide, and 17 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 58.9
    operational_transparency: 42.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apttus Authentication
  slug: apttus-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apttus Domain Security
  slug: apttus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Apttus Vulnerability Disclosure
  slug: apttus-vulnerability-disclosure
  summary_line: disclosure policy published
slug: apttus
tags:
- Software-as-a-Service
- CPQ
- Contract Lifecycle Management
- Document Automation
- Quote-to-Cash
- Company
website: https://conga.com/
---
