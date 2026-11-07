---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Broadcom developer portal provides API documentation for various Broadcom products, including VMware Cloud Director and other solutions.
  name: Broadcom APIs
  slug: broadcom-apis
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/connectall/well-known/connectall-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connectall-well-known.yml
- group: other
  href: https://artifacts.apis.io/connectall/hosts/connectall-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connectall-hosts.yml
- group: other
  href: https://artifacts.apis.io/connectall/vendors/connectall-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connectall-vendors.yml
- group: build
  href: https://artifacts.apis.io/connectall/packages/connectall-packages.yml
  title: ''
  type: SDKs
  url: packages/connectall-packages.yml
- group: build
  href: https://artifacts.apis.io/connectall/packages/connectall-packages.yml
  title: ''
  type: Packages
  url: packages/connectall-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.broadcom.com/company/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.broadcom.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.broadcom.com/
- group: start
  title: ''
  type: SignUp
  url: https://community.broadcom.com/register
- group: auth
  title: ''
  type: Security
  url: https://www.broadcom.com/products/mainframe/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadcom.com/company/legal/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.broadcom.com/products/cybersecurity/endpoint/management/it-management-suite
- group: docs
  title: ''
  type: Documentation
  url: https://developer.broadcom.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Broadcom
- group: auth
  href: https://artifacts.apis.io/connectall/security/connectall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connectall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.broadcom.com/
coverage:
  checked: '2026-10-20'
  detail: Developer portal pages render via JavaScript and do not expose raw OpenAPI JSON/YAML files.
  evidence:
  - status: 200
    url: https://developer.broadcom.com/xapis/vmware-cloud-director-openapi/latest/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Broadcom Inc. is a global technology company that designs, develops, and supplies a broad range of semiconductor and infrastructure software solutions. It serves customers in data center, networking, software, broadband, wireless, and storage markets, offering products such as ASICs, processors, and enterprise software. Broadcom’s portfolio includes networking chips, storage adapters, and a suite of software for security, management, and cloud services, positioning it as a key player in the digital transformation of enterprises worldwide.
image: https://www.broadcom.com/media/blt4ac44e0e6c6d8341/bltc5b68e1455ec0786/6954499867fae30d2f04a43e/brcm_preview_image@72ppi.jpg
layout: provider
modified: '2026-10-20'
name: Broadcom
nav: Providers
network: true
overview: 'Broadcom is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Software, Infrastructure, and Enterprise.


  Broadcom''s developer surface includes support, signup flow, documentation, and 13 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 58.0
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/connectall/connectall-2026-11-03T125113.png
security:
- kind: domain-security
  name: Connectall Domain Security
  slug: connectall-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: connectall
tags:
- Company
- Semiconductors
- Software
- Infrastructure
- Enterprise
website: https://www.broadcom.com/
---
