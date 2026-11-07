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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/ul-solutions/llms/ul-solutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ul-solutions-llms.txt
- group: other
  href: https://artifacts.apis.io/ul-solutions/hosts/ul-solutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ul-solutions-hosts.yml
- group: other
  href: https://artifacts.apis.io/ul-solutions/vendors/ul-solutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ul-solutions-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ul-solutions/security/ul-solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ul-solutions-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ulsolutions
- group: company
  title: ''
  type: Website
  url: https://www.ul.com
- group: start
  title: ''
  type: Portal
  url: https://my.ul.com
- group: other
  title: ''
  type: ProductIQ
  url: https://productiq.ulprospector.com
- group: other
  title: ''
  type: MarksAndLabelsHub
  url: https://marks.ul.com
- group: other
  title: ''
  type: Software
  url: https://www.ul.com/software
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.ul.com/contact-us
- group: company
  title: ''
  type: News
  url: https://www.ul.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.ul.com/about/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.ul.com
- group: operate
  title: ''
  type: Contact
  url: https://www.ul.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.ul.com/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ul.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ul.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ul.com/resources/online-policies/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ul.com/resources/contracts/terms
- group: operate
  title: ''
  type: Support
  url: https://www.ul.com/resources/help
- group: start
  title: ''
  type: Login
  url: https://my.ul.com/
coverage:
  checked: '2026-10-20'
  detail: UL Solutions runs an Azure APIM developer portal at developer.ul.com whose anonymous catalog shows only the default Echo API, and every docs.ul.com page redirects to the login.ul.com Azure B2C sign-in.
  evidence:
  - status: 200
    url: https://docs.ul.com/docs/abstract
  - status: 200
    url: https://developer.ul.com/apis
  - status: 404
    url: https://docs.ul.com/docs/developer-portal-registration
  reason: partner-login
  state: gated
created: '2026-05-04'
description: UL Solutions is a global leader in applied safety science, providing testing, inspection, certification, advisory, and software solutions to help customers innovate safely, demonstrate compliance, and bring trusted products to market. The company offers software products such as ULTRUS and ComplianceWire, customer portals (myUL, Product iQ), and the Marks and Labels Hub. UL Solutions does not currently expose a public developer-facing API portal with open documentation.
image: https://www.ul.com/favicon.ico
layout: provider
modified: '2026-10-20'
name: UL Solutions
nav: Providers
network: true
overview: 'UL Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Safety Science, Certification, Testing, Compliance, and Standards.


  UL Solutions'' developer surface includes developer portal, product news, engineering blog, documentation, support, and 17 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 24.0
    catalog_earned_first_party: 0.0
    catalog_gap: 91.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.9
    operational_transparency: 0.0
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ul-solutions/ul-solutions-2026-06-20T200006.png
security:
- kind: domain-security
  name: Ul Solutions Domain Security
  slug: ul-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ul-solutions
tags:
- Safety Science
- Certification
- Testing
- Compliance
- Standards
- Inspection
- Developer Portal
website: https://www.ul.com
---
