---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/diggle/plans/diggle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/diggle-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://diggle.com/security-policy/
- group: auth
  href: https://artifacts.apis.io/diggle/security/diggle-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/diggle-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/diggle/hosts/diggle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diggle-hosts.yml
- group: other
  href: https://artifacts.apis.io/diggle/vendors/diggle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diggle-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://diggle.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: http://help.diggle.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diggle.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://diggle.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://diggle.com/blog/2023/12/20/projects-pwc/
- group: docs
  title: ''
  type: Documentation
  url: https://help.diggle.com/
- group: auth
  href: https://artifacts.apis.io/diggle/security/diggle-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/diggle-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/diggle/security/diggle-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/diggle-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/diggle/security/diggle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diggle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diggle.com
coverage:
  checked: '2026-10-23'
  detail: The provider's main site returns Cloudflare interstitial pages, preventing access to any machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://diggle.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Diggle provides an all‑in‑one platform for interactive learning, remote surveys, and real‑time participant engagement. Users can create quizzes, polls, workshops, and collaborative sessions with drag‑and‑drop tools, then analyze results via reporting dashboards. The service offers free, basic, and pro plans for varying participant counts, and includes AI‑assisted content creation, data export, and branding options.
layout: provider
modified: '2026-10-23'
name: Diggle
nav: Providers
network: true
overview: 'Diggle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Collaboration, Surveys, and Software-as-a-Service.


  Diggle''s developer surface includes support, pricing, engineering blog, documentation, and 11 more developer resources.'
plans:
- name: Diggle Plans Pricing
  plan_count: 4
  slug: diggle-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 44.6
    operational_transparency: 10.5
  previous_composite: 25.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/diggle/diggle-2026-11-03T130653.png
security:
- kind: domain-security
  name: Diggle Domain Security
  slug: diggle-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Diggle Vulnerability Disclosure
  slug: diggle-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Diggle Trust Center
  slug: diggle-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: diggle
tags:
- Company
- Education
- Collaboration
- Surveys
- Software-as-a-Service
website: https://diggle.com
---
