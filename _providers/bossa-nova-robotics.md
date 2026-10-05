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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Public documentation and example templates for Bossa Nova Robotics, hosted at https://www.bossanova.com/docs. No machine‑readable API contract was found.
  name: Bossa Nova Robotics API
  slug: bossa-nova-robotics-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bossa-nova-robotics/refs/heads/main/hosts/bossa-nova-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bossa-nova-robotics-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.bossanova.com/docs
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bossa-nova-robotics/refs/heads/main/security/bossa-nova-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bossa-nova-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bossanova.com/
coverage:
  checked: '2026-10-03'
  detail: Documentation is served as HTML with embedded Google Docs links and no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.bossanova.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Bossa Nova Robotics develops autonomous retail robots and AI solutions for inventory management. Their flagship robot, Bossa Nova, scans store aisles in Walmart and other retailers, providing real‑time out‑of‑stock detection and analytics. The company shares its technology and learnings through open documentation and APIs to help other businesses build similar automation solutions.
image: https://lh7-us.googleusercontent.com/sitesv-images-rt/AMxu72tgPd7dWQ6ZgsFTzLY2CE5UfcOsopnL4QFZoj59qEMoz_4y9XQhkZKMhP0DJtytY_tCKHYzgbChN0n8rKew4zvxhmFYcTwVrCq1URpwZlemIC1e50UcOhT_ffyeujKefbU2c5r7l88cF5uGebZxGbzioIAXW8C6K0iA9SdOu7isfgLqrTwL8hw0Yi5t=w16383
layout: provider
modified: '2026-10-03'
name: Bossa Nova Robotics
nav: Providers
network: true
overview: 'Bossa Nova Robotics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Retail, Artificial Intelligence, and Automation.


  Bossa Nova Robotics'' developer surface includes documentation and 3 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bossa Nova Robotics Domain Security
  slug: bossa-nova-robotics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bossa-nova-robotics
tags:
- Company
- Robotics
- Retail
- Artificial Intelligence
- Automation
website: https://www.bossanova.com/
---
