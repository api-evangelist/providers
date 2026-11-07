---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: StarIO.Online makes cloud printing simple—no servers, no firewalls, no headaches. With just one REST API call, developers can print to any CloudPRNT‑compatible device, while IT teams gain full visibil
  name: CloudPRNT API
  slug: cloudprnt-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/star-micronics/llms/star-micronics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/star-micronics-llms.txt
- group: other
  href: https://artifacts.apis.io/star-micronics/hosts/star-micronics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/star-micronics-hosts.yml
- group: other
  href: https://artifacts.apis.io/star-micronics/vendors/star-micronics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/star-micronics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://starmicronics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://starmicronics.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/star-micronics/security/star-micronics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/star-micronics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://starmicronics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://starmicronics.com/technology/pos-hardware-integration-for-developers
- group: docs
  title: ''
  type: Documentation
  url: https://starmicronics.com/technology/cloudprnt
- group: operate
  title: ''
  type: Support
  url: https://starmicronics.com/star-micronics-technical-support
- group: company
  title: ''
  type: Blog
  url: https://starmicronics.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/star-micronics
coverage:
  checked: '2026-10-28'
  detail: Developer documentation mentions a REST API call but provides no machine‑readable specification or base URL.
  evidence:
  - status: 200
    url: https://starmicronics.com/technology/pos-hardware-integration-for-developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Star Micronics, founded in 1947, is a global manufacturer of point‑of‑sale (POS) hardware and technology. It offers a range of printers, label printers, kiosks, cash‑drawers and cloud‑based solutions such as CloudPRNT, enabling retailers and hospitality venues to print receipts and labels directly from cloud services. The company serves millions of businesses worldwide across retail, food service and other verticals, emphasizing reliable hardware, broad compatibility and developer resources.
image: https://starmicronics.com/wp-content/uploads/2024/04/sp700-1536x1536-1.png
layout: provider
modified: '2026-10-28'
name: Star Micronics CloudPRNT
nav: Providers
network: true
overview: 'Star Micronics CloudPRNT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point-of-Sale, Hardware, Printing, and Cloud.


  Star Micronics CloudPRNT''s developer surface includes documentation, support, engineering blog, and 9 more developer resources.'
random_paper: 14
scopes:
- name: Star Micronics Scopes
  scope_count: 0
  slug: star-micronics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 64.3
    operational_transparency: 2.6
  previous_composite: 17.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/star-micronics/star-micronics-2026-11-03T143729.png
security:
- kind: authentication
  name: Star Micronics Authentication
  slug: star-micronics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Star Micronics Domain Security
  slug: star-micronics-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: star-micronics
tags:
- Company
- Point-of-Sale
- Hardware
- Printing
- Cloud
- Technology
website: https://starmicronics.com/
---
