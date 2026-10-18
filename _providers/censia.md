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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://developer.censia.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.censia.com/security/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/censia/refs/heads/main/llms/censia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/censia-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/censia/refs/heads/main/hosts/censia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/censia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/censia/refs/heads/main/vendors/censia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/censia-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.censia.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.censia.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Censia
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/censia/refs/heads/main/security/censia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/censia-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/censia/refs/heads/main/security/censia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/censia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.censia.com
- group: company
  title: ''
  type: Blog
  url: https://www.censia.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.censia.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.censia.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.censia.com/contact
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://api.censia.com/mcp
  - status: 401
    url: https://support.censia.com/mcp
  - status: 200
    url: https://www.censia.com
  - status: 403
    url: https://equityzen.com/company/censia
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Censia AI provides workforce intelligence solutions for the AI enterprise, delivering dynamic talent intelligence that enables organizations to understand, develop, and mobilize their workforce. Their platform offers capabilities such as upskilling, benchmarking, skills‑gap analysis, succession planning, and talent mobility, helping companies transform talent data into actionable insights.
image: https://www.censia.com/wp-content/uploads/2024/12/censia-og.png
layout: provider
modified: '2026-10-07'
name: Censia
nav: Providers
network: true
overview: 'Censia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Workforce Intelligence, Talent Analytics, Talent Mobility, and Upskilling.


  Censia''s developer surface includes documentation, engineering blog, support, and 12 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Censia Domain Security
  slug: censia-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Censia Trust Center
  slug: censia-trust-center
  summary_line: ISO 27001, GDPR
slug: censia
tags:
- Artificial Intelligence
- Workforce Intelligence
- Talent Analytics
- Talent Mobility
- Upskilling
- Enterprise
website: https://www.censia.com
---
