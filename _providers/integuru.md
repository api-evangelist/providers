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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.integuru.com/trust
- group: agent
  href: https://artifacts.apis.io/integuru/llms/integuru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/integuru-llms.txt
- group: other
  href: https://artifacts.apis.io/integuru/hosts/integuru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/integuru-hosts.yml
- group: other
  href: https://artifacts.apis.io/integuru/vendors/integuru-vendors.yml
  title: ''
  type: Vendors
  url: vendors/integuru-vendors.yml
- group: auth
  href: https://artifacts.apis.io/integuru/security/integuru-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/integuru-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/integuru/security/integuru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/integuru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.integuru.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.integuru.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.integuru.com/platform-api-guides
- group: start
  title: ''
  type: GettingStarted
  url: https://www.integuru.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://www.integuru.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.integuru.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.integuru.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.integuru.com/privacy
coverage:
  checked: '2026-10-18'
  detail: No API documentation or OpenAPI spec found at known hosts.
  evidence:
  - status: 404
    url: https://api.integuru.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-17'
description: Integuru provides a platform that generates production‑ready APIs for websites and web systems without using browser automation or traditional RPA. Backed by Y Combinator, it powers over 10 million API calls monthly, offering fast, reliable, high‑throughput integrations across industries such as AI, healthcare, finance, logistics, and more. Users can start for free via a CLI or the web UI, and the service includes authentication support, auto‑healing, and 24/7 on‑call maintenance.
image: https://www.integuru.com/opengraph-image-20260525-v2
layout: provider
modified: '2026-10-17'
name: Integuru
nav: Providers
network: true
overview: 'Integuru is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Generation, Automation, Integration, and Y Combinator.


  Integuru''s developer surface includes documentation, API reference, getting-started guide, support, pricing, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 21.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Integuru Domain Security
  slug: integuru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Integuru Trust Center
  slug: integuru-trust-center
  summary_line: HIPAA, GDPR
slug: integuru
tags:
- Company
- API Generation
- Automation
- Integration
- Y Combinator
website: https://www.integuru.com/
---
