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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atomic-machines/refs/heads/main/hosts/atomic-machines-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atomic-machines-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atomic-machines/refs/heads/main/vendors/atomic-machines-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atomic-machines-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atomicmachines
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atomic-machines/refs/heads/main/security/atomic-machines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atomic-machines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atomicmachines.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atomicmachines.com/privacypolicy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.atomicmachines.com/join
- group: start
  title: ''
  type: SignUp
  url: https://www.atomicmachines.com/join
coverage:
  checked: 2026-09-26
  detail: The site serves only a JavaScript shell with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.atomicmachines.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Atomic Machines is a manufacturing technology company developing automation systems that enable flexible, precision assembly for small‑batch and custom products. Its platform combines robotics, vision systems, and software to streamline production workflows, improve scalability, and reduce time‑to‑market. Founded in 2019 by Jeff Holden and Prashant Patil, Atomic Machines is headquartered in Berkeley, California, and focuses on industrial robotics and advanced manufacturing solutions.
image: https://images.squarespace-cdn.com/content/v1/5e3eafb762402c0ce35af896/1593725289569-5OTARBMYQVFVNRKI02S3/FFCD_Brass_0012AutoContrast.jpg
layout: provider
modified: '2026-09-26'
name: Atomic Machines
nav: Providers
network: true
overview: 'Atomic Machines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Robotics, Automation, and Silicon.


  Atomic Machines'' developer surface includes getting-started guide, signup flow, and 6 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atomic Machines Domain Security
  slug: atomic-machines-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: atomic-machines
tags:
- Company
- Manufacturing
- Robotics
- Automation
- Silicon
- MEMS
website: https://www.atomicmachines.com/
---
