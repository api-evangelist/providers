---
access_model:
  confidence: medium
  label: Quote-only, no public plans or self-serve signup
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.xylem.com/en-us/products--services/software/
  - plans/xylem-plans-pricing.yml
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
    error_semantics: documented
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
  score: 20.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.xylem.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xylem-inc
- group: company
  title: ''
  type: Blog
  url: https://www.xylem.com/en-us/resources/blogs/making-waves/
- group: operate
  title: ''
  type: Support
  url: https://www.xylem.com/en-us/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xylem.com/en-us/support/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xylem.com/en-us/resources/policies/privacy/
- group: start
  title: ''
  type: Login
  url: https://cloud.xylem.com/xcloud/sso/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xylem.com/
- group: auth
  title: ''
  type: Security
  url: security/xylem-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/xylem-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/xylem-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/xylem-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xylem-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/xylem-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xylem-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xylem-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xylem-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xylem-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xylem-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xylem-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/xylem-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/xylem-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xylem-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xylem-llms.txt
created: '2026-03-21'
description: 'Xylem Inc. (NYSE: XYL) is a global water technology company that moves, treats, analyzes, monitors and returns water to the environment across the full water cycle. Its brands include Sensus smart metering and AMI networks, Xylem Vue utility operations software built with Idrica''s GoAigua platform, YSI water quality instrumentation, HYPACK hydrographic survey software, and the Flygt, Godwin, WEDECO and Aanderaa product lines. Xylem operates live, first-party API hosts for Xylem Cloud, the Xylem Vue services and its product selector, but publishes no API contract, developer portal or reference for any of them; the one machine-readable document it serves anonymously is the OpenID Connect discovery metadata for the Xylem Cloud identity realm.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xylem.png
layout: provider
modified: '2026-09-04'
name: Xylem
nav: Providers
network: true
overview: 'Xylem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Water, Water Technology, Utilities, and Smart Metering.


  Xylem''s developer surface includes engineering blog, support, authentication, and 21 more developer resources.'
plans:
- name: Xylem Plans Pricing
  plan_count: 0
  slug: xylem-plans-pricing
press:
- date: '2026-05-25'
  title: 'Reimagining Water Management: Generative AI as a ...'
  url: https://www.bluefieldresearch.com/research/reimagining-water-management-generative-ai-as-a-strategic-utility-asset/
- date: '2026-05-25'
  title: By 2050, AI could add 30 trillion liters of water demand ...
  url: https://www.facebook.com/XylemIncorporated/posts/by-2050-ai-could-add-30-trillion-liters-of-water-demand-each-year-that-scale-car/1289921993170804/
- date: '2026-05-25'
  title: Press Releases | Investor Relations - SEC Filings | Xylem
  url: https://xyleminc.gcs-web.com/news-events/news-releases
- date: '2026-05-25'
  title: AI's Water Demand to Surge Nearly 130% by 2050
  url: https://www.xylem.com/en-il/about-xylem/newsroom/press-releases/ais-water-demand-to-surge-nearly-130-by-2050--new-research-shows-how-to-build-a-water-secure-ai-economy/
- date: '2026-05-25'
  title: '99.1'
  url: https://www.sec.gov/Archives/edgar/data/1524472/000152447226000065/xyl04282026ex991.htm
random_paper: 13
rate_limits:
- limit_count: 0
  name: Xylem Rate Limits
  slug: xylem-rate-limits
scopes:
- name: Xylem Scopes
  scope_count: 0
  slug: xylem-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 27.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 4.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 71.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/xylem/refs/heads/main/screenshots/xylem-2026-06-20T201717.png
security:
- kind: authentication
  name: Xylem Authentication
  slug: xylem-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Xylem Domain Security
  slug: xylem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Xylem Vulnerability Disclosure
  slug: xylem-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Xylem Trust Center
  slug: xylem-trust-center
  summary_line: ISO 27001, SOC 2 Type II, NIST Cybersecurity Framework
slug: xylem
tags:
- Fortune 1000
- Water
- Water Technology
- Utilities
- Smart Metering
- Industrial IoT
- Water Quality
- Wastewater
- Manufacturing
website: https://www.xylem.com
---
