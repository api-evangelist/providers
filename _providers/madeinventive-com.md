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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/madeinventive-com/llms/madeinventive-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/madeinventive-com-llms.txt
- group: other
  href: https://artifacts.apis.io/madeinventive-com/hosts/madeinventive-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/madeinventive-com-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://www.madeinventive.com/blog
- group: auth
  href: https://artifacts.apis.io/madeinventive-com/security/madeinventive-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/madeinventive-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.madeinventive.com/
coverage:
  checked: '2026-10-24'
  detail: The provider’s website is a JavaScript‑rendered site with no machine‑readable API specification discovered.
  evidence:
  - status: 200
    url: https://www.madeinventive.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Inventive builds the quality standard for customer‑facing AI, offering built‑in quality and learning systems that enable businesses to deploy reliable, performant AI experiences. Founded by the team behind embedded analytics at Looker/Google, the company is backed by Wing VC and focuses on AI‑driven analytics, compliance, and continuous improvement for enterprise applications.
image: https://framerusercontent.com/assets/ZHit9rOKlMLvgQ7cJ7tzGGS9Yrs.png
layout: provider
modified: '2026-10-24'
name: Inventive
nav: Providers
network: true
overview: 'Inventive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Analytics, Enterprise, Quality, and Customer-Facing.


  Inventive''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Madeinventive Com Domain Security
  slug: madeinventive-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: madeinventive-com
tags:
- AI
- Analytics
- Enterprise
- Quality
- Customer-Facing
- Company
website: https://www.madeinventive.com/
---
