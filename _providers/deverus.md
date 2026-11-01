---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 6.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/deverus/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/deverus/hosts/deverus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deverus-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.deverus.com/
- group: operate
  title: ''
  type: Support
  url: https://help.deverus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.deverus.com/login_form.cfm
- group: company
  title: ''
  type: Blog
  url: https://blog.deverus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-doc.deverus.com/
- group: auth
  href: https://artifacts.apis.io/deverus/security/deverus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deverus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deverus.com
coverage:
  checked: '2026-10-23'
  detail: Docs at https://docs.deverus.com/ render via JavaScript and provide no machine‑readable spec
  evidence:
  - status: 200
    url: https://docs.deverus.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Deverus helps background screening companies modernize operations with Workflow AS and Verocity 2.0, offering practical automation solutions for CRA processes. The platform provides tools to streamline background checks, improve efficiency, and reduce reliance on AI hype, delivering a modernized workflow for compliance and risk management.
image: https://deverus.com/preview-image.jpg
layout: provider
modified: '2026-10-23'
name: Deverus
nav: Providers
network: true
overview: 'Deverus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Background Screening, Automation, Compliance, and Workflows.


  Deverus'' developer surface includes support, engineering blog, documentation, and 6 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deverus Domain Security
  slug: deverus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deverus
tags:
- Company
- Background Screening
- Automation
- Compliance
- Workflows
website: https://www.deverus.com
---
