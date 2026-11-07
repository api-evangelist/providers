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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/acunetix/plans/acunetix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acunetix-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/acunetix/security/acunetix-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/acunetix-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/acunetix/conformance/acunetix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acunetix-conformance.yml
- group: auth
  href: https://artifacts.apis.io/acunetix/well-known/acunetix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/acunetix-security.txt
- group: agent
  href: https://artifacts.apis.io/acunetix/well-known/acunetix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acunetix-well-known.yml
- group: other
  href: https://artifacts.apis.io/acunetix/hosts/acunetix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acunetix-hosts.yml
- group: other
  href: https://artifacts.apis.io/acunetix/vendors/acunetix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acunetix-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acunetix.com/about/terms_conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.acunetix.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://www.acunetix.com/vulnerability-scanner/register-conf-onsite/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acunetix.com/about/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.acunetix.com/news/web-vulnerabilities/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.acunetix.com/support/docs/a360/getting-started/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.acunetix.com/blog/releases/acunetix-wvs-v7-rc1/
- group: auth
  href: https://artifacts.apis.io/acunetix/security/acunetix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/acunetix-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/acunetix/security/acunetix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acunetix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acunetix.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.acunetix.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acunetix.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.acunetix.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://www.acunetix.com/contact
- group: company
  title: ''
  type: About
  url: https://www.acunetix.com/about
coverage:
  checked: '2026-11-01'
  detail: The provider’s documentation site loads via JavaScript and does not expose a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.acunetix.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Invicti (formerly Acunetix) provides a leading web application security scanner and API testing platform. The company offers automated vulnerability detection, AI‑driven risk scoring, and comprehensive coverage for web apps, APIs, and cloud services. It serves enterprises and mid‑size organizations worldwide, delivering detailed reports, remediation guidance, and integration with DevSecOps pipelines. The platform includes products like Invicti Web + API, Acunetix360, and various sensor technologies, supporting compliance and continuous security testing.
image: https://cdn.acunetix.com/wp-content/uploads/2023/11/22101126/acunetix-by-invicti-2023.png
layout: provider
modified: '2026-11-01'
name: Invicti (formerly Acunetix)
nav: Providers
network: true
overview: 'Invicti (formerly Acunetix) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Web Application Security, Vulnerability Scanning, API Testing, and DevSecOps.


  Invicti (formerly Acunetix)''s developer surface includes support, signup flow, getting-started guide, changelog, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Acunetix Plans Pricing
  plan_count: 1
  slug: acunetix-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 49.1
    operational_transparency: 18.4
  previous_composite: 30.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acunetix Domain Security
  slug: acunetix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Acunetix Vulnerability Disclosure
  slug: acunetix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: acunetix
tags:
- Security
- Web Application Security
- Vulnerability Scanning
- API Testing
- DevSecOps
website: https://www.acunetix.com
---
