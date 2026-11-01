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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/collabora-online/plans/collabora-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/collabora-online-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/collabora-online/llms/collabora-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/collabora-online-llms.txt
- group: other
  href: https://artifacts.apis.io/collabora-online/hosts/collabora-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/collabora-online-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.collaboraonline.com/terms/
- group: auth
  title: ''
  type: Security
  url: https://www.collaboraonline.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.collaboraonline.com/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://www.collaboraonline.com/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CollaboraOnline
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.collaboraonline.com/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://www.collaboraonline.com/blog/
- group: auth
  href: https://artifacts.apis.io/collabora-online/security/collabora-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/collabora-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://collaboraonline.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sdk.collaboraonline.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.collaboraonline.com/developer-blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.collaboraonline.com/subscriptions/
- group: operate
  title: ''
  type: Support
  url: https://www.collaboraonline.com/partner-client-portal/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's API host.
  evidence:
  - status: 0
    url: https://api.collaboraonline.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Collabora Online provides collaborative online office suite solutions, offering Collabora Online for web-based document editing and Collabora Office for desktop environments. Their products enable real-time co-authoring of text documents, spreadsheets, presentations, and graphics, targeting enterprises, service providers, and educational institutions. The platform supports integration with cloud services, offers on-premises deployment options, and includes a developer SDK for extending functionality.
image: https://www.collaboraonline.com/wp-content/uploads/2025/02/Collab-rabbits.png
layout: provider
modified: '2026-10-27'
name: Collabora Online
nav: Providers
network: true
overview: 'Collabora Online is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Collaboration, Office Suite, Real-time Editing, and Enterprise.


  Collabora Online''s developer surface includes changelog, engineering blog, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Collabora Online Plans Pricing
  plan_count: 7
  slug: collabora-online-plans-pricing
random_paper: 1
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Collabora Online Domain Security
  slug: collabora-online-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: collabora-online
tags:
- Company
- Collaboration
- Office Suite
- Real-time Editing
- Enterprise
website: https://collaboraonline.com/
---
