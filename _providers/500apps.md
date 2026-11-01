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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/500apps/hosts/500apps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/500apps-hosts.yml
- group: other
  href: https://artifacts.apis.io/500apps/vendors/500apps-vendors.yml
  title: ''
  type: Vendors
  url: vendors/500apps-vendors.yml
- group: auth
  href: https://artifacts.apis.io/500apps/security/500apps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/500apps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://500apps.com/
- group: docs
  title: ''
  type: Documentation
  url: https://500apps.com/docs
- group: company
  title: ''
  type: Blog
  url: https://500apps.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://500apps.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://500apps.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://500apps.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://500apps.com/contact
coverage:
  checked: '2026-10-19'
  detail: 500apps website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://500apps.com/
  reason: no-developer-program
  state: none
created: '2026-10-19'
description: 500apps is transitioning from a suite of 50 separate business tools to a unified AI-driven platform called 500agents. The company announced winding down its legacy products over a 90‑day period, offering customers data export support and early access to the new platform. Founded by Manohar and team, 500apps operates out of Hyderabad and Dubai, focusing on conversational AI that adapts UI to user workflows, integrates with existing tools, and continuously learns from interactions.
layout: provider
modified: '2026-10-19'
name: 500apps
nav: Providers
network: true
overview: '500apps is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Artificial Intelligence, Conversational AI, and Platform.


  500apps'' developer surface includes documentation, engineering blog, pricing, support, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 0.0
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
  name: 500Apps Domain Security
  slug: 500apps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 500apps
tags:
- Company
- Software-as-a-Service
- Artificial Intelligence
- Conversational AI
- Platform
website: https://500apps.com/
---
