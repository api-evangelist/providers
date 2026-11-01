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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/orchard-robotics-com/hosts/orchard-robotics-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orchard-robotics-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/orchard-robotics-com/vendors/orchard-robotics-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orchard-robotics-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.orchard.ai
- group: auth
  href: https://artifacts.apis.io/orchard-robotics-com/security/orchard-robotics-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orchard-robotics-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orchard.ai/
coverage:
  checked: '2026-10-24'
  detail: The provider's documentation site returns HTML shells and requires JavaScript to render, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://www.orchard.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Orchard Robotics develops advanced robotic solutions for orchard management, leveraging AI-driven navigation, precision pruning, and automated harvesting technologies. The company aims to increase yield, reduce labor costs, and promote sustainable agriculture through innovative hardware and software platforms. Founded with backing from General Catalyst, Orchard Robotics collaborates with growers worldwide to integrate robotics into modern fruit production, offering scalable systems that adapt to diverse orchard environments.
image: https://orchard.ai/images/og-image.jpg
layout: provider
modified: '2026-10-24'
name: Orchard Robotics
nav: Providers
network: true
overview: Orchard Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Agriculture, AI, and Automation.
random_paper: 1
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Orchard Robotics Com Domain Security
  slug: orchard-robotics-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: orchard-robotics-com
tags:
- Company
- Robotics
- Agriculture
- AI
- Automation
website: https://orchard.ai/
---
