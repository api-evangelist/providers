---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/gridspace-com/vendors/gridspace-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gridspace-com-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/gridspace-com/plans/gridspace-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gridspace-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gridspace-com/changelog/gridspace-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gridspace-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/gridspace-com/authentication/gridspace-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gridspace-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/gridspace-com/conformance/gridspace-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gridspace-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/gridspace-com/a2a/gridspace-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gridspace-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gridspace-com/well-known/gridspace-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gridspace-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/gridspace-com/hosts/gridspace-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gridspace-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/gridspace-com/packages/gridspace-com-packages.yml
  title: ''
  type: SDKs
  url: packages/gridspace-com-packages.yml
- group: build
  href: https://artifacts.apis.io/gridspace-com/packages/gridspace-com-packages.yml
  title: ''
  type: Packages
  url: packages/gridspace-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goguava.ai:443/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gridspace.com/status/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goguava.ai:443/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://goguava.ai:443/pricing
- group: other
  title: ''
  type: Leadership
  url: https://goguava.ai:443/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goguava-ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://goguava.ai:443/developers
- group: company
  title: ''
  type: Blog
  url: https://goguava.ai:443/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.goguava.ai/getting-started/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gridspace.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.goguava.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/gridspace-com/security/gridspace-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gridspace-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gridspace.com
coverage:
  checked: '2026-10-22'
  detail: Provider's documentation does not publish a machine‑readable OpenAPI spec for Gridspace; only a Guava API spec unrelated to Gridspace was found.
  evidence:
  - status: 200
    url: https://docs.goguava.ai/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Guava provides a voice agent API that lets developers and businesses build conversational voice applications for regulated call environments. The platform offers a proprietary stack with built‑in compliance (SOC 2, HITRUST, PCI DSS) and real‑time telephony, targeting sectors such as healthcare, insurance, fintech, government, and BPO.
image: https://goguava.ai/og/default.png
layout: provider
modified: '2026-10-21'
name: Gridspace
nav: Providers
network: true
overview: 'Gridspace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Voice AI, API, Regulated Compliance, Healthcare, and Insurance.


  Gridspace''s developer surface includes changelog, authentication, pricing, engineering blog, getting-started guide, documentation, API reference, and 16 more developer resources.'
plans:
- name: Gridspace Com Plans Pricing
  plan_count: 4
  slug: gridspace-com-plans-pricing
random_paper: 14
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 50.0
    operational_transparency: 36.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gridspace Com Authentication
  slug: gridspace-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gridspace Com Domain Security
  slug: gridspace-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gridspace-com
tags:
- Voice AI
- API
- Regulated Compliance
- Healthcare
- Insurance
- Fintech
- Government
- BPO
website: https://www.gridspace.com
---
