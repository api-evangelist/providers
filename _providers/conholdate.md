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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/conholdate/llms/conholdate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/conholdate-llms.txt
- group: other
  href: https://artifacts.apis.io/conholdate/hosts/conholdate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conholdate-hosts.yml
- group: other
  href: https://artifacts.apis.io/conholdate/vendors/conholdate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conholdate-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.conholdate.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.conholdate.com/legal/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conholdate.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.conholdate.com/legal/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.conholdate.com/Developers
- group: company
  title: ''
  type: Blog
  url: https://blog.conholdate.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.conholdate.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conholdate
- group: auth
  href: https://artifacts.apis.io/conholdate/security/conholdate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conholdate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conholdate.com/
coverage:
  checked: '2026-10-19'
  detail: Documentation pages are JavaScript-rendered shells preventing machine-readable spec discovery.
  evidence:
  - status: unreachable
    url: https://docs.conholdate.com/net
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Conholdate offers native file format and document processing SDKs for .NET and Java platforms. The SDKs enable developers to build applications that convert, edit, compare, merge, annotate, redact, and sign documents and images across more than 100 supported formats. Their products are used by software and consulting companies, banks, government organizations, and educational institutions worldwide.
layout: provider
modified: '2026-10-19'
name: Conholdate
nav: Providers
network: true
overview: 'Conholdate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SDK, Document Processing, File Conversion, .NET, and Java.


  Conholdate''s developer surface includes engineering blog, documentation, and 11 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Conholdate Domain Security
  slug: conholdate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: conholdate
tags:
- SDK
- Document Processing
- File Conversion
- .NET
- Java
website: https://conholdate.com/
---
