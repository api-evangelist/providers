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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/careerist/refs/heads/main/hosts/careerist-hosts.yml
  title: ''
  type: Hosts
  url: hosts/careerist-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/careerist/refs/heads/main/vendors/careerist-vendors.yml
  title: ''
  type: Vendors
  url: vendors/careerist-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/careerist/refs/heads/main/security/careerist-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/careerist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://careerist.cc/
- group: docs
  title: ''
  type: Documentation
  url: https://careerist.cc/about
- group: start
  title: ''
  type: GettingStarted
  url: https://careerist.cc/ai-automation
- group: commercial
  title: ''
  type: Pricing
  url: https://careerist.cc/payments
- group: commercial
  title: ''
  type: TermsOfService
  url: https://careerist.cc/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://careerist.cc/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://careerist.cc/insights
coverage:
  checked: 2026-10-07 'Careerist is an online education platform that helps individuals launch tech careers quickly. It offers programs in AI automation, QA engineering, and software development, providing mentorship, internships, and a money‑back guarantee. The service includes free tools like CV builders and salary calculators, flexible payment options, and a community of partners and ambassadors.'
  detail: The developer docs pages return JavaScript-rendered shells with no machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://careerist.cc/docs
  - status: 301
    url: https://api.careerist.cc/docs/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Careerist is an online education platform that helps individuals launch tech careers quickly. It offers programs in AI automation, QA engineering, and software development, providing mentorship, internships, and a money‑back guarantee.
image: https://careerist.cc/cdn/uploads/landings/og/1645001476613/og-1645001476462.jpeg
layout: provider
modified: '2026-10-07'
name: Careerist
nav: Providers
network: true
overview: 'Careerist is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Tech Education, Career Training, AI Automation, Internship, and Career Coaching.


  Careerist''s developer surface includes documentation, getting-started guide, pricing, engineering blog, and 6 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Careerist Domain Security
  slug: careerist-domain-security
  summary_line: TLSv1.3
slug: careerist
tags:
- Tech Education
- Career Training
- AI Automation
- Internship
- Career Coaching
website: https://careerist.cc/
---
