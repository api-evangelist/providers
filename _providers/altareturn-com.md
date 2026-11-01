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
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/altareturn-com/well-known/altareturn-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/altareturn-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/altareturn-com/well-known/altareturn-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altareturn-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/altareturn-com/hosts/altareturn-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altareturn-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/altareturn-com/vendors/altareturn-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altareturn-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/altareturn-com/packages/altareturn-com-packages.yml
  title: ''
  type: SDKs
  url: packages/altareturn-com-packages.yml
- group: build
  href: https://artifacts.apis.io/altareturn-com/packages/altareturn-com-packages.yml
  title: ''
  type: Packages
  url: packages/altareturn-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.perforce.com/
- group: operate
  title: ''
  type: Support
  url: https://www.perforce.com/support/eol-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.perforce.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perforce.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.perforce.com/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.perforce.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.perforce.com/products/delphix/whats-new
- group: company
  title: ''
  type: Blog
  url: https://www.perforce.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/perforce
- group: auth
  href: https://artifacts.apis.io/altareturn-com/security/altareturn-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altareturn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.perforce.com/products/delphix
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://portal.perforce.com/mcp/v1
  - status: 403
    url: https://status.perforce.com/mcp
  - status: 200
    url: https://www.perforce.com/products/delphix
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Delphix provides data virtualization and data masking solutions, enabling organizations to accelerate software development and testing by delivering realistic, secure synthetic data. Acquired by Perforce, Delphix integrates with the Perforce platform to offer intelligent data automation across cloud, on‑premises, and hybrid environments, supporting compliance, data security, and rapid release cycles.
image: https://www.perforce.com/sites/default/files/image-social-share-default.jpg
layout: provider
modified: '2026-10-22'
name: Delphix
nav: Providers
network: true
overview: 'Delphix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Virtualization, Data Masking, Synthetic Data, and DevOps.


  Delphix''s developer surface includes support, changelog, engineering blog, and 14 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 47.4
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
  name: Altareturn Com Domain Security
  slug: altareturn-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: altareturn-com
tags:
- Company
- Data Virtualization
- Data Masking
- Synthetic Data
- DevOps
website: https://www.perforce.com/products/delphix
---
