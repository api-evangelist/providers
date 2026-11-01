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
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/jobzmall/plans/jobzmall-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jobzmall-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.jobzmall.com/
- group: agent
  href: https://artifacts.apis.io/jobzmall/llms/jobzmall-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jobzmall-llms.txt
- group: auth
  href: https://artifacts.apis.io/jobzmall/well-known/jobzmall-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jobzmall-security.txt
- group: agent
  href: https://artifacts.apis.io/jobzmall/well-known/jobzmall-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jobzmall-well-known.yml
- group: other
  href: https://artifacts.apis.io/jobzmall/hosts/jobzmall-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jobzmall-hosts.yml
- group: other
  href: https://artifacts.apis.io/jobzmall/vendors/jobzmall-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jobzmall-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.jobzmall.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://help.jobzmall.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jobzmall.com
- group: auth
  title: ''
  type: Security
  url: https://www.jobzmall.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.jobzmall.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jobzmall.com/employers/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.jobzmall.com/press
- group: company
  title: ''
  type: Blog
  url: https://blog.jobzmall.com
- group: start
  title: ''
  type: GettingStarted
  url: https://help.jobzmall.com/en/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.jobzmall.com/
- group: auth
  href: https://artifacts.apis.io/jobzmall/security/jobzmall-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jobzmall-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/jobzmall/security/jobzmall-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jobzmall-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jobzmall/security/jobzmall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jobzmall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jobzmall.com/
created: '2026-10-26'
description: JobzMall is a video‑first talent marketplace that connects job seekers and employers through interactive video resumes and interviews. It aims to make the job‑finding process enjoyable, engaging and accessible for everyone, offering tools for creating video resumes, browsing opportunities, and hiring via video interviews.
layout: provider
modified: '2026-10-26'
name: JobzMall
nav: Providers
network: true
overview: 'JobzMall is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, video, talent, marketplace, and hiring.


  JobzMall''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Jobzmall Plans Pricing
  plan_count: 4
  slug: jobzmall-plans-pricing
random_paper: 19
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 46.4
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jobzmall Domain Security
  slug: jobzmall-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jobzmall Vulnerability Disclosure
  slug: jobzmall-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jobzmall Trust Center
  slug: jobzmall-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: jobzmall
tags:
- Company
- video
- talent
- marketplace
- hiring
- resumes
website: https://www.jobzmall.com/
---
