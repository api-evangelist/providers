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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/cape-analytics/conformance/cape-analytics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cape-analytics-conformance.yml
- group: other
  href: https://artifacts.apis.io/cape-analytics/hosts/cape-analytics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cape-analytics-hosts.yml
- group: build
  href: https://artifacts.apis.io/cape-analytics/integrations/cape-analytics-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/cape-analytics-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/cape-analytics/vendors/cape-analytics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cape-analytics-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://capeanalytics.com/feed/
- group: company
  title: ''
  type: Website
  url: https://capeanalytics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://capeanalytics.com/capabilities/
- group: company
  title: ''
  type: Blog
  url: https://capeanalytics.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://capeanalytics.com/contact/
- group: start
  title: ''
  type: Login
  url: https://client.capeanalytics.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capeanalytics.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capeanalytics.com/terms-of-use/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capeanalytics
- group: agent
  href: https://artifacts.apis.io/cape-analytics/well-known/cape-analytics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cape-analytics-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cape-analytics/security/cape-analytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cape-analytics-domain-security.yml
coverage:
  checked: '2026-10-20'
  detail: The Data Delivery page advertises a sub-two-second API but publishes no reference or spec; access runs through "Request A Consultation" and the client.capeanalytics.com login, and api.capeanalytics.com does not resolve publicly.
  evidence:
  - status: 200
    url: https://capeanalytics.com/capabilities/cape-access/
  - status: 200
    url: https://client.capeanalytics.com/
  - status: 404
    url: https://capeanalytics.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Cape Analytics (now part of Moody's) is a geospatial property intelligence provider that applies computer vision and machine learning to high-resolution aerial and satellite imagery, property records, and other novel data sources to produce inspection-quality condition and characteristic data for over 100 million residential and commercial structures across the United States and Canada. Its insights — roof condition and material, swimming pools, solar panels, accessory structures, tree overhang, wildfire and wind exposure, distance to hazards, and a proprietary Liquidity Score — are delivered to insurance underwriters, lenders, and real estate investors in under two seconds via API, batch/bulk files, an Automated Property Condition Report (aPCR), and a customer web portal, as well as through third-party platforms such as Guidewire and Duck Creek. Cape does not publish a public, self-service developer portal or open API specification; API access is provisioned to customers and
  partners through a gated onboarding flow.
image: https://capeanalytics.com/wp-content/uploads/2025/10/mdy_logo_rgb_white-reduced-centered.png
layout: provider
modified: '2026-10-20'
name: Cape Analytics
nav: Providers
network: true
overview: 'Cape Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Property Intelligence, Geospatial, Computer Vision, and Machine Learning.


  Cape Analytics'' developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 2.6
  previous_composite: 16.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cape-analytics/cape-analytics-2026-07-25T204404.png
security:
- kind: domain-security
  name: Cape Analytics Domain Security
  slug: cape-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cape-analytics
tags:
- Company
- Property Intelligence
- Geospatial
- Computer Vision
- Machine Learning
- Real Estate
- Insurance
- Underwriting
- Aerial Imagery
- Risk Analytics
website: https://capeanalytics.com/
---
