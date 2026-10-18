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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Filehub provides a no‑code automation platform with API endpoints for document workflows, invoicing, data extraction and integrations.
  name: Filehub API
  slug: filehub-api
artifact_total: 3
common:
- group: start
  title: ''
  type: Login
  url: https://filehub.one/de/login
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/filehub/refs/heads/main/plans/filehub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/filehub-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/filehub/refs/heads/main/hosts/filehub-hosts.yml
  title: ''
  type: Hosts
  url: hosts/filehub-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/filehub/refs/heads/main/vendors/filehub-vendors.yml
  title: ''
  type: Vendors
  url: vendors/filehub-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://filehub.one/solutions/management
- group: operate
  title: ''
  type: ChangeLog
  url: https://filehub.one/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/filehub/refs/heads/main/security/filehub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/filehub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://filehub.one/
- group: operate
  title: ''
  type: Support
  url: https://filehub.one/contact-us
- group: company
  title: ''
  type: Blog
  url: https://filehub.one/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://filehub.one/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://filehub.one/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://filehub.one/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://filehub.one/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/filehub/workspace
coverage:
  checked: '2026-10-16'
  detail: The API reference page https://filehub.one/api returns a 404 and provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 404
    url: https://filehub.one/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: filehub GmbH provides a no‑code automation platform that connects apps, portals and software to automate document flows such as invoice download, data extraction, archiving and workflow management. It serves finance, procurement, sales and operations teams with templates, integrations and compliance‑ready processes, offering a free plan and paid tiers for enterprises.
image: https://cdn.filehub.one/images/facebook-card.png
layout: provider
modified: '2026-10-16'
name: filehub GmbH
nav: Providers
network: true
overview: 'filehub GmbH is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Document Management, Finance, Procurement, and Software-as-a-Service.


  filehub GmbH''s developer surface includes changelog, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Filehub Plans Pricing
  plan_count: 7
  slug: filehub-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Filehub Domain Security
  slug: filehub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: filehub
tags:
- Automation
- Document Management
- Finance
- Procurement
- Software-as-a-Service
website: https://filehub.one/
---
