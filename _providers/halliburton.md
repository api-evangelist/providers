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
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/halliburton/well-known/halliburton-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/halliburton-well-known.yml
- group: other
  href: https://artifacts.apis.io/halliburton/hosts/halliburton-hosts.yml
  title: ''
  type: Hosts
  url: hosts/halliburton-hosts.yml
- group: other
  href: https://artifacts.apis.io/halliburton/vendors/halliburton-vendors.yml
  title: ''
  type: Vendors
  url: vendors/halliburton-vendors.yml
- group: auth
  href: https://artifacts.apis.io/halliburton/security/halliburton-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/halliburton-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Halliburton-Landmark
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/halliburton
- group: company
  title: ''
  type: Website
  url: https://www.halliburton.com
- group: other
  title: ''
  type: Landmark
  url: https://www.landmark.solutions
- group: other
  title: ''
  type: OSDU
  url: https://osduforum.org
- group: operate
  title: ''
  type: Support
  url: https://www.halliburton.com/en/software/customer-support
- group: start
  title: ''
  type: Login
  url: https://login.ienergycloud.solutions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.halliburton.com/en/about-us/corporate-governance/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.halliburton.com/en/about-us/corporate-governance/terms-and-conditions
coverage:
  checked: '2026-10-20'
  detail: Halliburton publishes no public API or developer docs; Landmark/DecisionSpace software documentation and support sit behind the css.lgc.com customer portal and the iEnergy cloud login, and developer/api hosts do not resolve.
  evidence:
  - status: 200
    url: https://www.halliburton.com/en/software/customer-support
  - status: 404
    url: https://www.halliburton.com/llms.txt
  - status: 200
    url: https://www.halliburton.com/en/software/osdu.html
  reason: customer-only-docs
  state: gated
created: '2026-03-21'
description: Halliburton delivers advanced products and services to meet the evolving needs of the global energy industry, driving innovation, reliability, and performance. Halliburton operates enterprise software platforms such as DecisionSpace 365, Landmark, and iEnergy, but does not currently publish a public, openly accessible REST API for general developer use. Its Landmark software (now served from halliburton.com/en/software) supports the OSDU Data Platform, and customer support runs through a Landmark customer portal and iEnergy cloud login.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/halliburton.png
layout: provider
modified: '2026-10-20'
name: Halliburton
nav: Providers
network: true
overview: 'Halliburton is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Fortune 500, Oil and Gas, Oilfield Services, and Software.


  Halliburton''s developer surface includes support and 12 more developer resources.'
press:
- date: ''
  title: Press Releases - Halliburton
  url: https://halliburton.gcs-web.com/news-and-events/press-releases?_correlationId=1896&page=9
- date: ''
  title: News and Press Releases
  url: https://www.halliburton.com/en/about-us/press-release
- date: ''
  title: Press Releases
  url: https://ir.halliburton.com/news-and-events/press-releases
- date: ''
  title: World's first AI-enabled technology successfully ...
  url: https://www.halliburton.com/en/about-us/press-release/world-first-ai-enabled-technology-successfully-implemented-by-aiq-and-halliburton-in-adnoc-upstream-operations
- date: ''
  title: Accelerating Digital Supply Chain Transformation
  url: https://www.halliburton.com/en/about-us/press-release/halliburton-accenture-digital-supply-chain-transformation
random_paper: 12
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/halliburton/halliburton-2026-06-20T182503.png
security:
- kind: domain-security
  name: Halliburton Domain Security
  slug: halliburton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: halliburton
tags:
- Energy
- Fortune 500
- Oil and Gas
- Oilfield Services
- Software
- Data-Platforms
- OSDU
website: https://www.halliburton.com
---
