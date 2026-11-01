---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
- group: other
  href: https://artifacts.apis.io/assetworks/hosts/assetworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assetworks-hosts.yml
- group: build
  href: https://artifacts.apis.io/assetworks/integrations/assetworks-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/assetworks-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/assetworks/vendors/assetworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assetworks-vendors.yml
- group: auth
  href: https://artifacts.apis.io/assetworks/security/assetworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assetworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.assetworks.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.assetworks.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://www.assetworks.com/careers/
- group: company
  title: ''
  type: Blog
  url: https://www.assetworks.com/eam/blog/2026-trends-to-boost-facility-management-efficiency/
- group: operate
  title: ''
  type: Support
  url: https://community.assetworks.com/hc/en-us
coverage:
  checked: '2026-10-20'
  detail: AssetWorks publishes no developer portal or API docs; its only documentation host, community.assetworks.com (Zendesk), redirects every visitor to a customer sign-in, and sandbox.assetworks.com is a bare IIS default page.
  evidence:
  - status: 403
    url: https://community.assetworks.com/hc/en-us
  - status: 200
    url: https://sandbox.assetworks.com/
  - status: 200
    url: https://www.assetworks.com
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: AssetWorks is an enterprise fleet and asset management software company with more than 40 years of history and over 1,000 customers across commercial and private fleets, government and public works, and higher education. Its products include FleetFocus fleet and enterprise asset management (EAM), Active Assets fixed-asset tracking, Recoup Ops surplus management, and Scan and Validate mobile inventory management. AssetWorks sells on-premise and hosted enterprise software to large fleet and facility operators; as of this profile it publishes no public developer portal, API documentation, or self-serve API program. This repo is a company profile in the API Evangelist network, backed by Battery Ventures.
image: https://www.assetworks.com/wp-content/uploads/2023/06/cropped-AssetWorks-Gear-Icon-Graident-Red-Orange-192x192.png
layout: provider
modified: '2026-07-18'
name: AssetWorks
nav: Providers
network: true
overview: 'AssetWorks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet Management, Asset Management, Enterprise Asset Management, and EAM.


  AssetWorks'' developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 7.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/assetworks/assetworks-2026-07-25T201443.png
security:
- kind: domain-security
  name: Assetworks Domain Security
  slug: assetworks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: assetworks
tags:
- Company
- Fleet Management
- Asset Management
- Enterprise Asset Management
- EAM
- Government
- Higher Education
- Fixed Assets
- Software
website: https://www.assetworks.com
---
