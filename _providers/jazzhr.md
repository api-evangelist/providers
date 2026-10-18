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
api_count: 1
apis:
- description: Recruiting API documented on the pricing page.
  name: JazzHR API
  slug: jazzhr-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/jazzhr/refs/heads/main/plans/jazzhr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jazzhr-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.jazzhr.com/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jazzhr/refs/heads/main/llms/jazzhr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jazzhr-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jazzhr/refs/heads/main/well-known/jazzhr-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jazzhr-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/jazzhr/refs/heads/main/well-known/jazzhr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jazzhr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jazzhr/refs/heads/main/hosts/jazzhr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jazzhr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jazzhr/refs/heads/main/vendors/jazzhr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jazzhr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jazzhr.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jazzhr.com/
- group: auth
  title: ''
  type: Security
  url: https://www.jazzhr.com/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jazzhr.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.jazzhr.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.jazzhr.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jazzhr/refs/heads/main/security/jazzhr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jazzhr-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jazzhr/refs/heads/main/security/jazzhr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jazzhr-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jazzhr/refs/heads/main/security/jazzhr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jazzhr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jazzhr.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://status.jazzhr.com/mcp
  - status: 200
    url: https://www.jazzhr.com
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: JazzHR provides an easy-to-use recruiting software platform designed for small businesses to streamline hiring processes. The solution offers applicant tracking, job posting, candidate sourcing, interview scheduling, and offer management, all through an intuitive web interface. JazzHR aims to reduce the complexity of enterprise ATS systems while delivering robust features such as customizable workflows, reporting, and integrations with popular HR tools. It serves companies looking to hire faster and more efficiently without extensive technical overhead.
image: https://www.jazzhr.com/images/og-default.png
layout: provider
modified: '2026-10-14'
name: JazzHR
nav: Providers
network: true
overview: 'JazzHR is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Recruiting, Applicant Tracking, Small Business, Hiring, and Software-as-a-Service.


  JazzHR''s developer surface includes pricing, engineering blog, documentation, and 14 more developer resources.'
plans:
- name: Jazzhr Plans Pricing
  plan_count: 3
  slug: jazzhr-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jazzhr Domain Security
  slug: jazzhr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jazzhr Vulnerability Disclosure
  slug: jazzhr-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Jazzhr Trust Center
  slug: jazzhr-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: jazzhr
tags:
- Recruiting
- Applicant Tracking
- Small Business
- Hiring
- Software-as-a-Service
- Company
website: https://www.jazzhr.com
---
