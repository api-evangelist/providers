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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.breachlock.com/compliance/vendor-assessment/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breachlock/refs/heads/main/llms/breachlock-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breachlock-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breachlock/refs/heads/main/well-known/breachlock-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breachlock-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breachlock/refs/heads/main/hosts/breachlock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breachlock-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breachlock/refs/heads/main/vendors/breachlock-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breachlock-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breachlock.com/about/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breachlock.com/about/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.breachlock.com/resources/news/your-api-security-is-calling-you/
- group: other
  title: ''
  type: Leadership
  url: https://www.breachlock.com/about/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breachlock/refs/heads/main/security/breachlock-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/breachlock-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breachlock/refs/heads/main/security/breachlock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breachlock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.breachlock.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.breachlock.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.breachlock.com/schedule-a-discovery-call
- group: operate
  title: ''
  type: Support
  url: https://www.breachlock.com/about/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.breachlock.com/pricing/penetration-testing-pricing/
created: '2026-10-03'
description: BreachLock provides comprehensive attack surface discovery, penetration testing, and red‑team services. Their platform offers Penetration Testing as a Service (PTaaS), continuous testing, breach‑response automation, and attack surface management solutions for enterprises seeking proactive security validation and risk reduction.
layout: provider
modified: '2026-10-03'
name: BreachLock
nav: Providers
network: true
overview: 'BreachLock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Penetration Testing, Attack Surface Management, Red Team, and Software-as-a-Service.


  BreachLock''s developer surface includes documentation, getting-started guide, support, pricing, and 12 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 55.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Breachlock Domain Security
  slug: breachlock-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Breachlock Trust Center
  slug: breachlock-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: breachlock
tags:
- Security
- Penetration Testing
- Attack Surface Management
- Red Team
- Software-as-a-Service
website: https://www.breachlock.com/
---
