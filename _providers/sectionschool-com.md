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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: ''
  name: Section AI Platform
  slug: section-ai-platform
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/sectionschool-com/plans/sectionschool-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sectionschool-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/sectionschool-com/hosts/sectionschool-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sectionschool-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sectionschool-com/vendors/sectionschool-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sectionschool-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.sectionai.com/trust
- group: operate
  title: ''
  type: Support
  url: http://help.sectionai.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sectionai.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sectionai.com/events/live-events/getting-started-with-ai-for-beginners
- group: docs
  title: ''
  type: Documentation
  url: https://help.sectionschool.com/
- group: auth
  href: https://artifacts.apis.io/sectionschool-com/security/sectionschool-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sectionschool-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sectionschool.com/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's API hosts.
  evidence:
  - status: 0
    url: https://api.sectionai.com/openapi.json
  - status: 0
    url: https://api.sectionschool.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Section provides an Enterprise AI Training & Adoption Platform that helps organizations measure, guide, and scale AI adoption. Their solutions include AI transformation planning, personalized coaching, workflow automation, and agentic enterprise workshops. The platform offers tools for leadership coaching, AI strategy support, and hands‑on consulting to accelerate AI initiatives across the enterprise.
image: https://cdn.prod.website-files.com/69b2e3ac50e9b987b57f1aa1/6abd8242285d08a4cdb6ca59_Section.png
layout: provider
modified: '2026-10-29'
name: Section
nav: Providers
network: true
overview: 'Section is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Enterprise, Training, and Platform.


  Section''s developer surface includes support, pricing, getting-started guide, documentation, and 6 more developer resources.'
plans:
- name: Sectionschool Com Plans Pricing
  plan_count: 5
  slug: sectionschool-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sectionschool Com Domain Security
  slug: sectionschool-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sectionschool-com
tags:
- Company
- AI
- Enterprise
- Training
- Platform
website: https://www.sectionschool.com/
---
