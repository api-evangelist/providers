---
access_model:
  confidence: low
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
api_count: 0
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/domainposture-com/well-known/domainposture-com-domainposture-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainposture-com-domainposture-security.txt
- group: commercial
  href: https://artifacts.apis.io/domainposture-com/plans/domainposture-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domainposture-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.domainposture.com/trust
- group: auth
  href: https://artifacts.apis.io/domainposture-com/security/domainposture-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/domainposture-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/domainposture-com/llms/domainposture-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domainposture-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/domainposture-com/well-known/domainposture-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainposture-com-www-security.txt
- group: auth
  href: https://artifacts.apis.io/domainposture-com/well-known/domainposture-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/domainposture-com-security.txt
- group: agent
  href: https://artifacts.apis.io/domainposture-com/well-known/domainposture-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domainposture-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/domainposture-com/hosts/domainposture-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domainposture-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/domainposture-com/vendors/domainposture-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domainposture-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.domainposture.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.domainposture.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.domainposture.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.domainposture.com/auth/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.domainposture.com/blog
- group: auth
  href: https://artifacts.apis.io/domainposture-com/security/domainposture-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/domainposture-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/domainposture-com/security/domainposture-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/domainposture-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/domainposture-com/security/domainposture-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domainposture-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domainposture.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://domainposture.com/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: Domain Posture provides a free external security scan for any domain, checking DNS, SPF/DKIM/DMARC email authentication, TLS configuration, security headers, and AI-crawler policies. The service requires no signup and is aimed at security teams and consultants who need quick, audit‑grade domain hygiene assessments. It also offers an observatory for deeper insights and a consulting‑focused offering for enterprises.
image: https://www.domainposture.com/opengraph-image?7722cef5ffa56a3a
layout: provider
modified: '2026-11-05'
name: Domain Posture
nav: Providers
network: true
overview: 'Domain Posture is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Domain, and Monitoring.


  Domain Posture''s developer surface includes pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Domainposture Com Plans Pricing
  plan_count: 2
  slug: domainposture-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domainposture Com Domain Security
  slug: domainposture-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Domainposture Com Vulnerability Disclosure
  slug: domainposture-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Domainposture Com Trust Center
  slug: domainposture-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: domainposture-com
tags:
- Security
- Domain
- Monitoring
website: https://domainposture.com/
---
