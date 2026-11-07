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
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iqvia.com/solutions/commercialization/commercial-analytics/pricing-and-market-access
- group: other
  href: https://artifacts.apis.io/iqvia/hosts/iqvia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iqvia-hosts.yml
- group: build
  href: https://artifacts.apis.io/iqvia/integrations/iqvia-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/iqvia-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/iqvia/vendors/iqvia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iqvia-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.iqvia.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.iqvia.com/about-us/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.iqvia.com/newsroom
- group: auth
  href: https://artifacts.apis.io/iqvia/security/iqvia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iqvia-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IQVIA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iqvia
- group: company
  title: ''
  type: Website
  url: https://www.iqvia.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quintilesims
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iqvia.com/about-us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iqvia.com/about-us/privacy
- group: start
  title: ''
  type: Login
  url: https://login.customerportal.iqvia.com/
coverage:
  checked: '2026-10-20'
  detail: developer.iqvia.com 302-redirects to deviq.iqvia.com/docs/developer-migration/, a host that does not resolve publicly, and the only other developer-facing surface is the login.customerportal.iqvia.com customer login.
  evidence:
  - status: 302
    url: https://developer.iqvia.com
  - status: 200
    url: https://login.customerportal.iqvia.com/
  - status: 404
    url: https://www.iqvia.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-03-21'
description: 'IQVIA empowers life sciences organizations to accelerate innovation, improve patient outcomes, and bring treatments to market faster through advanced analytics and technology. IQVIA is a Fortune 500 company offering data, analytics, clinical research, and connected intelligence services. IQVIA publishes no public API reference: developer.iqvia.com redirects to deviq.iqvia.com, which does not resolve on the public internet.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iqvia.png
layout: provider
modified: '2026-10-20'
name: IQVIA
nav: Providers
network: true
overview: 'IQVIA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Clinical Research, Fortune 500, Healthcare, and Life Sciences.


  IQVIA''s developer surface includes pricing, engineering blog, and 13 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 2.6
  previous_composite: 14.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/iqvia/iqvia-2026-06-20T183608.png
security:
- kind: domain-security
  name: Iqvia Domain Security
  slug: iqvia-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: iqvia
tags:
- Analytics
- Clinical Research
- Fortune 500
- Healthcare
- Life Sciences
- Clinical Trials
- Pharmaceuticals
- Biotechnology
website: https://www.iqvia.com
---
