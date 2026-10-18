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
api_count: 1
apis:
- description: Clockspring offers a low-code integration platform with REST APIs for connecting systems, data migration, and workflow automation.
  name: Clockspring API
  slug: clockspring-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clockspring/refs/heads/main/plans/clockspring-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clockspring-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clockspring/refs/heads/main/llms/clockspring-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clockspring-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clockspring/refs/heads/main/hosts/clockspring-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clockspring-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clockspring/refs/heads/main/vendors/clockspring-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clockspring-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clockspring/refs/heads/main/security/clockspring-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clockspring-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clockspring.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.clockspring.net/resources
- group: docs
  title: ''
  type: APIReference
  url: https://www.clockspring.net/solutions/api-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://www.clockspring.net/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clockspring.net/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.clockspring.net
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clockspring.net/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.clockspring.net/contact
coverage:
  checked: '2026-10-16'
  detail: No OpenAPI or other machine‑readable spec is published; attempts to fetch common spec URLs returned 404 or no response.
  evidence:
  - status: 0
    url: https://api.clockspring.net/openapi.json
  - status: 404
    url: https://www.clockspring.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Clockspring is a technology company specializing in precision timing components and synchronization solutions for industrial automation, robotics, and consumer electronics. Founded to address the growing demand for reliable, high-performance clock mechanisms, Clockspring offers a suite of APIs that enable developers to integrate real-time timing data, device health monitoring, and predictive maintenance capabilities into their applications. The company emphasizes robust security, extensive documentation, and developer-friendly tools to accelerate integration and foster innovation across sectors.
image: https://www.clockspring.net/images/clockspring-social.png
layout: provider
modified: '2026-10-16'
name: Clockspring
nav: Providers
network: true
overview: 'Clockspring is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Integration, Data-Integration, and Enterprise.


  Clockspring''s developer surface includes documentation, API reference, getting-started guide, pricing, support, and 8 more developer resources.'
plans:
- name: Clockspring Plans Pricing
  plan_count: 3
  slug: clockspring-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 55.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clockspring Domain Security
  slug: clockspring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clockspring
tags:
- Automation
- Integration
- Data-Integration
- Enterprise
website: https://www.clockspring.net/
---
