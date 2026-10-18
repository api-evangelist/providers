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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Vroozi API documentation and developer resources.
  name: Vroozi API
  slug: vroozi-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vroozi/refs/heads/main/llms/vroozi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vroozi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vroozi/refs/heads/main/well-known/vroozi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vroozi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vroozi/refs/heads/main/hosts/vroozi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vroozi-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vroozi.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vroozi.com/pricing/
- group: other
  title: ''
  type: Leadership
  url: https://www.vroozi.com/team/
- group: company
  title: ''
  type: Blog
  url: https://www.vroozi.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.vroozi.com/blog/the-true-cost-of-supplier-onboarding-and-how-to-streamline-it/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vroozi
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vroozi/refs/heads/main/security/vroozi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vroozi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vroozi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs-api.vroozi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://go.vroozi.com
coverage:
  checked: '2026-10-13'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the documented API hosts.
  evidence:
  - status: 403
    url: https://docs-api.vroozi.com/openapi.json
  - status: 403
    url: https://docs-api.vroozi.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Vroozi provides an intelligent procure-to-pay platform that automates purchasing, invoice processing, and supplier collaboration. Their cloud‑based solution integrates with ERP systems like SAP, Oracle, NetSuite, and Microsoft Dynamics, offering features such as punch‑out catalogs, spend analytics, and a trusted supplier network. Vroozi aims to simplify procurement workflows, reduce manual effort, and deliver actionable insights for smarter spend management across enterprises.
image: https://www.vroozi.com/wp-content/uploads/vroozi-default-thumbnail.png
layout: provider
modified: '2026-10-13'
name: Vroozi
nav: Providers
network: true
overview: 'Vroozi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, Software-as-a-Service, Automation, and Spend Management.


  Vroozi''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Vroozi Domain Security
  slug: vroozi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vroozi
tags:
- Company
- Procurement
- Software-as-a-Service
- Automation
- Spend Management
website: https://www.vroozi.com
---
