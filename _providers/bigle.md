---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bigle/hosts/bigle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigle-hosts.yml
- group: other
  href: https://artifacts.apis.io/bigle/vendors/bigle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bigle-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biglelegal.com/en/policies/legal-notice
- group: operate
  title: ''
  type: Support
  url: https://support.biglelegal.com/en/knowledge-base/bigle-legal-api
- group: start
  title: ''
  type: SignUp
  url: https://www.biglelegal.com/en/sign-up
- group: auth
  title: ''
  type: Security
  url: https://www.biglelegal.com/en/policies/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biglelegal.com/en/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.biglelegal.com/en/company/press
- group: start
  title: ''
  type: GettingStarted
  url: https://www.biglelegal.com/en/get-started
- group: company
  title: ''
  type: Blog
  url: https://blog.biglelegal.com/en
- group: auth
  href: https://artifacts.apis.io/bigle/security/bigle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biglelegal.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://blog.biglelegal.com/mcp
  - status: 403
    url: https://support.biglelegal.com/mcp
  - status: 200
    url: https://www.biglelegal.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Bigle provides an all‑in‑one cloud‑based Contract Lifecycle Management (CLM) software platform that automates legal operations for companies. The suite includes document automation, contract management, electronic signature, intelligent workflows and a generative AI assistant called Libra. It serves legal departments across sectors such as real estate, corporations, law firms and notaries, offering integrations with other business software and a focus on security and compliance.
image: https://cdn.prod.website-files.com/5dc1853887ad3ecba18bb835/5de52ec15f17623aec4528d8_Logo%20Bigle%20Legal%202019%20cut-p-500.png
layout: provider
modified: '2026-10-25'
name: Bigle
nav: Providers
network: true
overview: 'Bigle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Contract Lifecycle Management, Legal Tech, Electronic Signature, Generative AI, and Real Estate.


  Bigle''s developer surface includes support, signup flow, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Bigle Plans Pricing
  plan_count: 0
  slug: bigle-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bigle Domain Security
  slug: bigle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bigle
tags:
- Contract Lifecycle Management
- Legal Tech
- Electronic Signature
- Generative AI
- Real Estate
- Corporations
- Law Firms
- Notaries
website: https://www.biglelegal.com
---
