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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fadv.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/first-advantage/refs/heads/main/security/first-advantage-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/first-advantage-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/first-advantage/refs/heads/main/llms/first-advantage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/first-advantage-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/first-advantage/refs/heads/main/well-known/first-advantage-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/first-advantage-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/first-advantage/refs/heads/main/well-known/first-advantage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/first-advantage-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/first-advantage/refs/heads/main/hosts/first-advantage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/first-advantage-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/first-advantage/refs/heads/main/vendors/first-advantage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/first-advantage-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://fadv.com/news/register-for-back-to-basics-screening-compliance-summer-wrap-up-webinar-aug-30/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fadv.com/privacy-center/
- group: company
  title: ''
  type: Newsroom
  url: https://fadv.com/news/napbs-accredited/
- group: docs
  title: ''
  type: Documentation
  url: https://help.fadv.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/first-advantage/refs/heads/main/security/first-advantage-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/first-advantage-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/first-advantage/refs/heads/main/security/first-advantage-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/first-advantage-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/first-advantage/refs/heads/main/security/first-advantage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/first-advantage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fadv.com
coverage:
  checked: '2026-10-14'
  detail: The developer portal at https://help.fadv.com redirects to a JavaScript‑rendered support site with no machine‑readable OpenAPI, GraphQL or AsyncAPI specifications.
  evidence:
  - status: 301
    url: https://help.fadv.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: First Advantage provides global background check and screening solutions for employers, candidates, and customers. Their platform offers identity verification, criminal record searches, employment tax credit screening, and industry-specific background checks, helping organizations mitigate risk and build workforce trust across the employee lifecycle.
image: https://fadv.com/wp-content/uploads/Hero-4x.png
layout: provider
modified: '2026-10-14'
name: First Advantage
nav: Providers
network: true
overview: 'First Advantage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Background-Checks, Screening, Identity-Verification, and Employment.


  First Advantage''s developer surface includes signup flow, documentation, and 13 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: First Advantage Domain Security
  slug: first-advantage-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: First Advantage Vulnerability Disclosure
  slug: first-advantage-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: First Advantage Trust Center
  slug: first-advantage-trust-center
  summary_line: SOC 2, ISO 27001
slug: first-advantage
tags:
- Company
- Background-Checks
- Screening
- Identity-Verification
- Employment
website: https://fadv.com
---
