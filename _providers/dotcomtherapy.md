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
- group: agent
  href: https://artifacts.apis.io/dotcomtherapy/llms/dotcomtherapy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dotcomtherapy-llms.txt
- group: other
  href: https://artifacts.apis.io/dotcomtherapy/hosts/dotcomtherapy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dotcomtherapy-hosts.yml
- group: other
  href: https://artifacts.apis.io/dotcomtherapy/vendors/dotcomtherapy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dotcomtherapy-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.huddleupcare.com/blog
- group: auth
  href: https://artifacts.apis.io/dotcomtherapy/security/dotcomtherapy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dotcomtherapy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.huddleupcare.com
coverage:
  checked: '2026-10-24'
  detail: The provider's website is a Wix site that serves only HTML with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.huddleupcare.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Dotcomtherapy, now operating as Huddle Up, provides virtual and in‑person special‑education therapy services—including speech, occupational, mental health, and school psychology—to K‑12 districts across the United States. Founded in 2015, the company leverages a proprietary platform to streamline provider workflows, support compliance, and deliver over one million therapy sessions, maintaining a 96% provider retention rate and high clinical quality scores.
image: https://static.wixstatic.com/media/7c7e5c_3ee1d83f8e2c4367a2047489c4b172df%7Emv2.png/v1/fit/w_2500,h_1330,al_c/7c7e5c_3ee1d83f8e2c4367a2047489c4b172df%7Emv2.png
layout: provider
modified: '2026-10-24'
name: Dotcomtherapy
nav: Providers
network: true
overview: 'Dotcomtherapy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Healthcare, Telehealth, and Therapy.


  Dotcomtherapy''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 7
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
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dotcomtherapy Domain Security
  slug: dotcomtherapy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dotcomtherapy
tags:
- Company
- Education
- Healthcare
- Telehealth
- Therapy
website: https://www.huddleupcare.com
---
