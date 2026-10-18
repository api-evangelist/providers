---
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 6
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/rate-limits/meistertask-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/meistertask-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/plans/meistertask-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meistertask-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/conventions/meistertask-conventions.yml
  title: ''
  type: Conventions
  url: conventions/meistertask-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.meistertask.com/pages/pt/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/authentication/meistertask-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meistertask-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/conformance/meistertask-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meistertask-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/llms/meistertask-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meistertask-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/well-known/meistertask-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/meistertask-www-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/well-known/meistertask-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/meistertask-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/well-known/meistertask-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meistertask-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/hosts/meistertask-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meistertask-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/vendors/meistertask-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meistertask-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meistertask.com/pages/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.meistertask.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.meistertask.com/
- group: auth
  title: ''
  type: Security
  url: https://www.meistertask.com/pages/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meistertask.com/pages/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.meistertask.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developers.meistertask.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/security/meistertask-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/meistertask-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/security/meistertask-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/meistertask-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meistertask/refs/heads/main/security/meistertask-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meistertask-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.meistertask.com
coverage:
  checked: '2026-10-14'
  detail: Documentation pages exist but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://developers.meistertask.com/reference/authentication.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: MeisterTask is a secure work management SaaS platform that helps teams organize tasks, projects, and collaboration in a visual board format. It offers features such as task tracking, knowledge base, reporting, time tracking, and integrations, targeting productivity and agile workflows for businesses of all sizes. The service is GDPR compliant, EU‑based, and trusted by thousands of companies worldwide.
image: https://a.storyblok.com/f/289344/1200x631/472173adb4/mt_default-sharing-image_1200x630_en.png
layout: provider
modified: '2026-10-14'
name: MeisterTask
nav: Providers
network: true
overview: 'MeisterTask is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Project Management, Collaboration, and Productivity.


  MeisterTask''s developer surface includes authentication, support, engineering blog, documentation, and 19 more developer resources.'
plans:
- name: Meistertask Plans Pricing
  plan_count: 4
  slug: meistertask-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Meistertask Rate Limits
  slug: meistertask-rate-limits
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 47.0
    catalog_earned_first_party: 20.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 55.4
    operational_transparency: 47.4
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Meistertask Authentication
  slug: meistertask-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Meistertask Domain Security
  slug: meistertask-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Meistertask Vulnerability Disclosure
  slug: meistertask-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Meistertask Trust Center
  slug: meistertask-trust-center
  summary_line: ISO 27001, GDPR
slug: meistertask
tags:
- Company
- Software-as-a-Service
- Project Management
- Collaboration
- Productivity
website: https://www.meistertask.com
---
