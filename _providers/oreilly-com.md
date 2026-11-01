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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/oreilly-com/well-known/oreilly-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oreilly-com-well-known.yml
- group: commercial
  href: https://artifacts.apis.io/oreilly-com/plans/oreilly-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oreilly-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.oreilly.com/
- group: agent
  href: https://artifacts.apis.io/oreilly-com/llms/oreilly-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oreilly-com-llms.txt
- group: other
  href: https://artifacts.apis.io/oreilly-com/hosts/oreilly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oreilly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/oreilly-com/vendors/oreilly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oreilly-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.oreilly.com/search/skills/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.oreilly.com/press/
- group: start
  title: ''
  type: Login
  url: https://www.oreilly.com/member/login/?next=
- group: auth
  href: https://artifacts.apis.io/oreilly-com/security/oreilly-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/oreilly-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/oreilly-com/security/oreilly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oreilly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oreilly.com/
- group: operate
  title: ''
  type: Support
  url: https://www.oreilly.com/online-learning/support/
- group: company
  title: ''
  type: Blog
  url: https://www.oreilly.com/radar/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oreilly.com/online-learning/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oreilly.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oreilly.com/privacy.html
coverage:
  checked: '2026-10-30'
  detail: MCP endpoint https://api.oreilly.com/mcp returns 403, indicating access is gated behind authentication.
  evidence:
  - status: 403
    url: https://api.oreilly.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-30'
description: O'Reilly Media provides technology and business training through its learning platform, offering books, online courses, live training, and conferences. It serves individuals and organizations seeking to build skills in software development, data, cloud, AI, and more, with a focus on practical, up‑to‑date content and expert instruction.
image: https://cdn.oreillystatic.com/oreilly/images/oreilly-social-200.png
layout: provider
modified: '2026-10-30'
name: oreilly-com
nav: Providers
network: true
overview: 'oreilly-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Technology, Training, and Publishing.


  oreilly-com''s developer surface includes support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Oreilly Com Plans Pricing
  plan_count: 5
  slug: oreilly-com-plans-pricing
random_paper: 4
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Oreilly Com Domain Security
  slug: oreilly-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Oreilly Com Trust Center
  slug: oreilly-com-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: oreilly-com
tags:
- Company
- Education
- Technology
- Training
- Publishing
website: https://oreilly.com/
---
