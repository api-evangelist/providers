---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: AssetPlanner is Ameresco's enterprise asset management and capital planning platform, served to customer tenants at https://assetplanner.com/logon and certified to ISO/IEC 27001:2022. Ameresco's own p
  name: Ameresco AssetPlanner Platform
  slug: ameresco-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.ameresco.com
- group: company
  title: ''
  type: Blog
  url: https://www.ameresco.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ameresco
- group: agent
  title: ''
  type: LLMsTxt
  url: https://ameresco.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ameresco
- group: operate
  title: ''
  type: Support
  url: https://help.ameresco.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ameresco.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ameresco.com/terms-and-conditions/
- group: auth
  title: ''
  type: Compliance
  url: https://www.ameresco.com/certifications/
- group: auth
  title: ''
  type: TrustCenter
  url: security/ameresco-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://assetplanner.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ameresco-assetplanner-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ameresco-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ameresco-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ameresco-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ameresco-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/ameresco-packages.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ameresco-finops.yml
coverage:
  checked: '2026-09-02'
  detail: 'Ameresco markets AssetPlanner as an enterprise asset-management platform and says on its own product page that it "can build custom APIs" per engagement, but every reference for it sits behind a tenant login: assetplanner.com serves only a logon form, help.ameresco.com 301s to an Ameresco Help Center on Jira Service Management with anonymousEnabled=false, and the developer.ameresco.com and api.ameresco.com hosts a prior round of this profile asserted do not exist in DNS at all — the only machine-readable surface left on the corporate domain is WordPress''s own default /wp-json/ CMS index (284 routes, 18 plugin namespaces), not a product API.'
  evidence:
  - status: NXDOMAIN
    url: https://developer.ameresco.com
  - status: NXDOMAIN
    url: https://api.ameresco.com
  - status: 301
    url: https://help.ameresco.com/
  - status: 200
    url: https://ameresco.atlassian.net/servicedesk/customer/portals
  - status: 200
    url: https://assetplanner.com/docs/
  - status: 404
    url: https://assetplanner.com/swagger/v1/swagger.json
  - status: 404
    url: https://www.ameresco.com/openapi.json
  - status: 404
    url: https://www.ameresco.com/.well-known/api-catalog
  - status: 404
    url: https://www.ameresco.com/.well-known/agent-card.json
  - status: 200
    url: https://www.ameresco.com/wp-json/
  - status: 200
    url: https://assetplanner.com/.well-known/security.txt
  - status: 200
    url: https://ameresco.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-04-19'
description: 'Ameresco, Inc. (NYSE: AMRC) is an energy infrastructure company that develops, builds, owns and operates energy efficiency, renewable energy, distributed generation and asset management projects for federal, state, municipal, education, healthcare and commercial customers across North America and Europe. Its software product is AssetPlanner, an enterprise asset management and capital planning platform delivered as a customer-tenant web application. Ameresco publishes no developer portal, API reference or machine-readable API contract on any host it controls; where integration is offered it is built bespoke per engagement, and the customer help center is login-gated.'
finops:
- name: Ameresco Finops
  service_category: Energy Services
  slug: ameresco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ameresco.png
layout: provider
modified: '2026-09-02'
name: Ameresco
nav: Providers
network: true
overview: 'Ameresco publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy Efficiency, Clean Energy, Energy Management, Asset Management, and Facilities.


  Ameresco''s developer surface includes engineering blog, support, and 16 more developer resources.'
plans:
- name: Ameresco Plans Pricing
  plan_count: 0
  slug: ameresco-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Ameresco Rate Limits
  slug: ameresco-rate-limits
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 27.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ameresco/refs/heads/main/screenshots/ameresco-2026-06-20T171904.png
security:
- kind: domain-security
  name: Ameresco Domain Security
  slug: ameresco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ameresco Vulnerability Disclosure
  slug: ameresco-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ameresco Trust Center
  slug: ameresco-trust-center
  summary_line: ISO/IEC 27001:2022, ISO 9001:2015, ISO 14001:2015, ISO 45001:2018, ISO 50001:2018, UNI CEI 11352:2014, SOA
slug: ameresco
tags:
- Energy Efficiency
- Clean Energy
- Energy Management
- Asset Management
- Facilities
- Sustainability
- Infrastructure
- Services
website: https://www.ameresco.com
---
