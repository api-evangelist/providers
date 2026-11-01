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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/mentor-graphics/well-known/mentor-graphics-productcert-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mentor-graphics-productcert-security.txt
- group: auth
  title: ''
  type: Security
  url: https://productcert.siemens.com/vulnerability-handling-and-disclosure-process/
- group: agent
  href: https://artifacts.apis.io/mentor-graphics/llms/mentor-graphics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mentor-graphics-llms.txt
- group: other
  href: https://artifacts.apis.io/mentor-graphics/a2a/mentor-graphics-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mentor-graphics-a2a.yml
- group: auth
  href: https://artifacts.apis.io/mentor-graphics/well-known/mentor-graphics-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mentor-graphics-security.txt
- group: auth
  href: https://artifacts.apis.io/mentor-graphics/well-known/mentor-graphics-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mentor-graphics-apis-security.txt
- group: agent
  href: https://artifacts.apis.io/mentor-graphics/well-known/mentor-graphics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mentor-graphics-well-known.yml
- group: other
  href: https://artifacts.apis.io/mentor-graphics/hosts/mentor-graphics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mentor-graphics-hosts.yml
- group: other
  href: https://artifacts.apis.io/mentor-graphics/vendors/mentor-graphics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mentor-graphics-vendors.yml
- group: build
  href: https://artifacts.apis.io/mentor-graphics/packages/mentor-graphics-packages.yml
  title: ''
  type: SDKs
  url: packages/mentor-graphics-packages.yml
- group: build
  href: https://artifacts.apis.io/mentor-graphics/packages/mentor-graphics-packages.yml
  title: ''
  type: Packages
  url: packages/mentor-graphics-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.siemens.com/en-us/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.siemens.com/en-us/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.siemens.com/en-us/privacy-notice/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.siemens.com/en-us/products/capital/offerings/capital-x-panel-designer/pricing/
- group: other
  title: ''
  type: Leadership
  url: https://www.siemens.com/en-us/company/leadership/management/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.siemens.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.siemens.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.siemens.com/building-x-openness/api/accounts-api/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developer.internal.siemens.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/siemens
- group: auth
  href: https://artifacts.apis.io/mentor-graphics/security/mentor-graphics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mentor-graphics-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mentor-graphics/security/mentor-graphics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mentor-graphics-domain-security.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/siemens/
- group: company
  title: ''
  type: Website
  url: https://www.siemens.com/en-us/company/electronic-design-automation/
coverage:
  checked: '2026-10-20'
  detail: mentor.com and eda.sw.siemens.com both redirect to a Siemens EDA marketing page; Siemens EDA publishes no public developer API, spec or portal for the former Mentor tools.
  evidence:
  - status: 200
    url: https://www.mentor.com/
  - status: 404
    url: https://eda.sw.siemens.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Mentor Graphics was a leading electronic design automation (EDA) software vendor whose tools span integrated-circuit design and verification, PCB and electronic-systems design, and manufacturing analysis. Battery Ventures held a position in the company. In 2017 Mentor Graphics was acquired by Siemens and its portfolio now ships as Siemens EDA (part of Siemens Digital Industries Software), including Calibre for physical verification and DFM, the Questa functional verification platform, and the Xpedition / PADS PCB design suites. The mentor.com domain now redirects to the Siemens EDA site. Siemens EDA delivers desktop and cloud-hosted engineering software and managed services; it does not publish a public developer REST API, OpenAPI definition, or self-serve developer portal, so there is no public API surface to enrich for this provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mentor-graphics.png
layout: provider
modified: '2026-07-20'
name: Mentor Graphics
nav: Providers
network: true
overview: 'Mentor Graphics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electronic Design Automation, EDA, Semiconductors, and PCB Design.


  Mentor Graphics'' developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 20 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 50.0
    operational_transparency: 15.8
  previous_composite: 24.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mentor-graphics/mentor-graphics-2026-10-11T191624.png
security:
- kind: domain-security
  name: Mentor Graphics Domain Security
  slug: mentor-graphics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mentor Graphics Vulnerability Disclosure
  slug: mentor-graphics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mentor-graphics
tags:
- Company
- Electronic Design Automation
- EDA
- Semiconductors
- PCB Design
- Chip Verification
- Engineering Software
- Siemens
website: https://www.siemens.com/en-us/company/electronic-design-automation/
---
