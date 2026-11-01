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
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/checkmk/plans/checkmk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/checkmk-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.checkmk.com/
- group: auth
  title: ''
  type: Security
  url: https://checkmk.com/responsible-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/checkmk/well-known/checkmk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/checkmk-security.txt
- group: agent
  href: https://artifacts.apis.io/checkmk/well-known/checkmk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/checkmk-well-known.yml
- group: other
  href: https://artifacts.apis.io/checkmk/hosts/checkmk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/checkmk-hosts.yml
- group: build
  href: https://artifacts.apis.io/checkmk/packages/checkmk-packages.yml
  title: ''
  type: SDKs
  url: packages/checkmk-packages.yml
- group: build
  href: https://artifacts.apis.io/checkmk/packages/checkmk-packages.yml
  title: ''
  type: Packages
  url: packages/checkmk-packages.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://checkmk.com/product/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://checkmk.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://checkmk.com/company/newsroom
- group: start
  title: ''
  type: GettingStarted
  url: https://checkmk.com/community/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://checkmk.com/product/release-notes/2-5-0
- group: auth
  href: https://artifacts.apis.io/checkmk/security/checkmk-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/checkmk-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/checkmk/security/checkmk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/checkmk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/checkmk/security/checkmk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/checkmk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://checkmk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.checkmk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://checkmk.com/download
- group: commercial
  title: ''
  type: Pricing
  url: https://checkmk.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://checkmk.com/support
- group: company
  title: ''
  type: Blog
  url: https://checkmk.com/blog
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided as HTML pages without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.checkmk.com/latest/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Checkmk provides a full‑stack monitoring and observability platform for hybrid IT environments, supporting both cloud‑native and on‑premises infrastructures. It offers self‑hosted and SaaS editions, integrates with tools like ServiceNow, Jira, and Slack, and exposes flexible APIs for data extraction and automation. The platform includes AI‑assisted root‑cause analysis, extensive dashboards, and a marketplace of plug‑ins for diverse monitoring needs.
image: https://checkmk.com/packages/tribe29_core/themes/checkmk/images/share_image.png
layout: provider
modified: '2026-10-28'
name: Checkmk
nav: Providers
network: true
overview: 'Checkmk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Monitoring, Observability, IT Infrastructure, Open Source, and SaaS.


  Checkmk''s developer surface includes getting-started guide, changelog, documentation, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Checkmk Plans Pricing
  plan_count: 5
  slug: checkmk-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 50.0
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Checkmk Domain Security
  slug: checkmk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Checkmk Vulnerability Disclosure
  slug: checkmk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Checkmk Trust Center
  slug: checkmk-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: checkmk
tags:
- Monitoring
- Observability
- IT Infrastructure
- Open Source
- SaaS
website: https://checkmk.com/
---
