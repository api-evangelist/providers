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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: NetDocuments provides a cloud‑based document and email management platform. The public support site lists product guides and workflows but no machine‑readable API specifications were found.
  name: NetDocuments API
  slug: netdocuments-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/netdocuments/well-known/netdocuments-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netdocuments-well-known.yml
- group: other
  href: https://artifacts.apis.io/netdocuments/hosts/netdocuments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netdocuments-hosts.yml
- group: other
  href: https://artifacts.apis.io/netdocuments/vendors/netdocuments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netdocuments-vendors.yml
- group: build
  href: https://artifacts.apis.io/netdocuments/packages/netdocuments-packages.yml
  title: ''
  type: SDKs
  url: packages/netdocuments-packages.yml
- group: build
  href: https://artifacts.apis.io/netdocuments/packages/netdocuments-packages.yml
  title: ''
  type: Packages
  url: packages/netdocuments-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.netdocuments.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.netdocuments.com/s/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netdocuments.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.netdocuments.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NetDocuments
- group: auth
  href: https://artifacts.apis.io/netdocuments/security/netdocuments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netdocuments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://netdocuments.com/
created: '2026-10-28'
description: NetDocuments provides cloud‑based document and email management solutions for legal firms and departments, offering secure storage, collaboration, AI‑driven context, and integration with Microsoft 365, Salesforce, and other enterprise tools. The platform emphasizes compliance, data governance, and advanced search capabilities to streamline legal workflows and improve productivity across organizations.
image: https://www.netdocuments.com/wp-content/uploads/2026/06/generic-OG.jpg
layout: provider
modified: '2026-10-28'
name: NetDocuments
nav: Providers
network: true
overview: 'NetDocuments is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Document Management, Email Management, Legal AI, Workflow Automation, and Integrations.


  NetDocuments'' developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Netdocuments Domain Security
  slug: netdocuments-domain-security
  summary_line: TLSv1.3 · DMARC
slug: netdocuments
tags:
- Document Management
- Email Management
- Legal AI
- Workflow Automation
- Integrations
- Security
website: https://netdocuments.com/
---
