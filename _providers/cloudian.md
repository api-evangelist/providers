---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudian/refs/heads/main/cli/cloudian-cli.yml
  title: ''
  type: CLI
  url: cli/cloudian-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudian/refs/heads/main/authentication/cloudian-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudian-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudian/refs/heads/main/conformance/cloudian-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudian-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudian/refs/heads/main/llms/cloudian-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudian-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudian/refs/heads/main/hosts/cloudian-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudian-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudian/refs/heads/main/vendors/cloudian-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudian-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudian/refs/heads/main/packages/cloudian-packages.yml
  title: ''
  type: SDKs
  url: packages/cloudian-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudian/refs/heads/main/packages/cloudian-packages.yml
  title: ''
  type: Packages
  url: packages/cloudian-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudian.com/disclosures/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://cloudian.com/support/
- group: auth
  title: ''
  type: Security
  url: https://cloudian.com/solutions/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudian.com/privacy-policy-2/
- group: company
  title: ''
  type: Newsroom
  url: https://cloudian.com/press/cloud-data-repatriation-survey/
- group: docs
  title: ''
  type: Documentation
  url: https://cloudian.com/guides/veeam/
- group: company
  title: ''
  type: Blog
  url: https://cloudian.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudian
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudian/refs/heads/main/security/cloudian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudian.com
coverage:
  checked: 2026-10-09 'Cloudian provides an AI‑ready, exabyte‑scale object storage platform designed for enterprise workloads. Its software‑defined storage solution offers on‑premises security, S3 compatibility, and high performance for AI and data‑intensive applications. Founded to simplify data protection and enable modern cloud‑native architectures, Cloudian serves global customers across industries with robust, scalable storage infrastructure.'
  detail: Developer pages return a 404 page not found and the site is heavily JavaScript‑rendered, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://cloudian.com/developers/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cloudian offers object storage products such as HyperStore, HyperScale AIDP, and HyperIQ for enterprises, government agencies, and service providers. Its solutions provide S3‑compatible, on‑premises and hybrid cloud storage for AI workloads, data lakes, backup, and ransomware protection. The company targets sectors including financial services, healthcare, education, and telecommunications.
image: https://cloudian.com/wp-content/uploads/2020/02/Cloudian-featured-image.jpg
layout: provider
modified: '2026-10-09'
name: Cloudian
nav: Providers
network: true
overview: 'Cloudian is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, Object-Storage, Artificial Intelligence, and Enterprise.


  Cloudian''s developer surface includes CLI, authentication, support, documentation, engineering blog, and 13 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cloudian Authentication
  slug: cloudian-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cloudian Domain Security
  slug: cloudian-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudian
tags:
- Company
- Storage
- Object-Storage
- Artificial Intelligence
- Enterprise
website: https://cloudian.com
---
