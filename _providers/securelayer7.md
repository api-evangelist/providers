---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API Penetration Testing service offering testing of REST, GraphQL, and gRPC APIs.
  name: API Penetration Testing
  slug: api-penetration-testing
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/securelayer7/plans/securelayer7-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/securelayer7-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/securelayer7/llms/securelayer7-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/securelayer7-llms.txt
- group: other
  href: https://artifacts.apis.io/securelayer7/hosts/securelayer7-hosts.yml
  title: ''
  type: Hosts
  url: hosts/securelayer7-hosts.yml
- group: other
  href: https://artifacts.apis.io/securelayer7/vendors/securelayer7-vendors.yml
  title: ''
  type: Vendors
  url: vendors/securelayer7-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://securelayer7.net/newsroom
- group: auth
  href: https://artifacts.apis.io/securelayer7/security/securelayer7-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/securelayer7-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://securelayer7.net/
- group: company
  title: ''
  type: Blog
  url: https://blog.securelayer7.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://securelayer7.net/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://securelayer7.net/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://securelayer7.net/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SecureLayer7
- group: operate
  title: ''
  type: Contact
  url: https://securelayer7.net/contact-us
created: '2026-10-21'
description: SecureLayer7 provides penetration testing and offensive security services, offering AI‑driven autonomous pentesting, on‑premise API scanning, and comprehensive red‑team assessments. Their platform continuously monitors and attacks APIs, web applications, cloud resources, and infrastructure to uncover real‑world exploits, delivering detailed remediation reports and integrations with JIRA, Slack, and CI/CD pipelines. Trusted by fintech, SaaS, enterprise, and critical infrastructure sectors, SecureLayer7 combines over a decade of research with a modern CTEM framework to protect evolving attack surfaces.
image: https://securelayer7.net/media/og-index-4383b4ae.png
layout: provider
modified: '2026-10-21'
name: SecureLayer7
nav: Providers
network: true
overview: 'SecureLayer7 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Penetration Testing, Offensive Security, API Protection, and Red Team.


  SecureLayer7''s developer surface includes engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Securelayer7 Plans Pricing
  plan_count: 4
  slug: securelayer7-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 65.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/securelayer7/securelayer7-2026-11-03T142948.png
security:
- kind: domain-security
  name: Securelayer7 Domain Security
  slug: securelayer7-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: securelayer7
tags:
- Security
- Penetration Testing
- Offensive Security
- API Protection
- Red Team
website: https://securelayer7.net/
---
