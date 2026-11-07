---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/abode/conformance/abode-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abode-conformance.yml
- group: agent
  href: https://artifacts.apis.io/abode/llms/abode-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abode-llms.txt
- group: auth
  href: https://artifacts.apis.io/abode/well-known/abode-intercom-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/abode-intercom-security.txt
- group: agent
  href: https://artifacts.apis.io/abode/well-known/abode-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abode-well-known.yml
- group: other
  href: https://artifacts.apis.io/abode/hosts/abode-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abode-hosts.yml
- group: other
  href: https://artifacts.apis.io/abode/vendors/abode-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abode-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abodehr.com/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.abodehr.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abodehr.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.abodehr.com/blog/dell-internships
- group: start
  title: ''
  type: GettingStarted
  url: https://www.abodehr.com/blog/10-early-career-onboarding-mistakes-and-how-to-avoid-them
- group: docs
  title: ''
  type: Documentation
  url: https://dev.abodehr.com/
- group: auth
  href: https://artifacts.apis.io/abode/security/abode-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/abode-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/abode/security/abode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abode-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abodehr.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://abodehr.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Abode offers an AI‑powered platform that supports the full early‑career talent journey, from attracting students and capturing interest at events to engaging candidates and converting interns into full‑time hires. The platform provides tools for recruiting, program management, mentorship, leadership development, high‑volume new‑hire experiences, and military hiring for enterprises and small businesses.
image: https://cdn.prod.website-files.com/631eca7a60e214c6f64f5faf/631edb5c59ae5a5a380fe9c6_AdobeSocial.jpg
layout: provider
modified: '2026-10-21'
name: Abode
nav: Providers
network: true
overview: 'Abode is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Early‑Career Recruiting, Program Management, Mentorship, Leadership Development, and High-Volume Hiring.


  Abode''s developer surface includes engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
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
screenshot: https://apis.io/screenshots/abode/abode-2026-11-03T120143.png
security:
- kind: domain-security
  name: Abode Domain Security
  slug: abode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Abode Vulnerability Disclosure
  slug: abode-vulnerability-disclosure
  summary_line: no policy recorded
slug: abode
tags:
- Early‑Career Recruiting
- Program Management
- Mentorship
- Leadership Development
- High-Volume Hiring
- Military Hiring
- Analytics
website: https://abodehr.com
---
