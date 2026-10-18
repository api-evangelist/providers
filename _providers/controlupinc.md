---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/vendors/controlupinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/controlupinc-vendors.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/changelog/controlupinc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/controlupinc-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/conventions/controlupinc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/controlupinc-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/llms/controlupinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/controlupinc-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/well-known/controlupinc-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/controlupinc-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/well-known/controlupinc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/controlupinc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/hosts/controlupinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/controlupinc-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/packages/controlupinc-packages.yml
  title: ''
  type: SDKs
  url: packages/controlupinc-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/packages/controlupinc-packages.yml
  title: ''
  type: Packages
  url: packages/controlupinc-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.controlup.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.controlup.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.controlup.com/
- group: auth
  title: ''
  type: Security
  url: https://www.controlup.com/security/cve-2022-27905/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.controlup.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.controlup.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.controlup.com/press/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.controlup.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.controlup.com/docs/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.controlup.com/resources/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.controlup.com/docs/getting-started-with-the-dex-platform
- group: docs
  title: ''
  type: Documentation
  url: https://help.controlup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/controlup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlupinc/refs/heads/main/security/controlupinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/controlupinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.controlup.com
coverage:
  checked: '2026-10-11'
  detail: Developer portal returns HTML without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://developer.controlup.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: ControlUp provides an AI-powered digital employee experience platform that automates, monitors, and optimizes IT environments across desktops, applications, and cloud workloads. Their solutions include real‑time performance monitoring, automated remediation, and analytics to improve operational efficiency and end‑user experience. Founded to empower IT teams, ControlUp serves enterprises worldwide with a focus on proactive management and AI-driven insights.
image: https://www.controlup.com/wp-content/uploads/controlup_prev.webp
layout: provider
modified: '2026-10-10'
name: Controlupinc
nav: Providers
network: true
overview: 'Controlupinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IT Management, AI Platform, Digital Employee Experience, and Monitoring.


  Controlupinc''s developer surface includes changelog, support, pricing, engineering blog, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 47.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Controlupinc Domain Security
  slug: controlupinc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: controlupinc
tags:
- Company
- IT Management
- AI Platform
- Digital Employee Experience
- Monitoring
- Automation
website: https://www.controlup.com
---
