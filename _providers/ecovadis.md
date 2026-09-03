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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: 'The EcoVadis API serves as a pivotal link, connecting your systems, applications, or platforms with EcoVadis'' vast repository of sustainability insights. Its primary function is facilitating seamless '
  name: EcoVadis API
  slug: ecovadis-api
- description: EcoVadis partner connector API enables integration with partner procurement and supply chain platforms to share sustainability rating data.
  name: EcoVadis Partner Connector API
  slug: ecovadis-partner-connector-api
- description: The EcoVadis Marketplace API is a specialized instrument crafted to exchange mission-critical sustainability information seamlessly, transmitting ratings summary data and medal information in real-tim
  name: EcoVadis Marketplace API
  slug: ecovadis-marketplace-api
- description: The EcoVadis Enterprise API enables enterprises to seamlessly incorporate EcoVadis sustainability ratings, carbon evaluations and IQ risk data directly into their procurement and supply chain systems.
  name: EcoVadis Sustainability Ratings, Carbon and IQ API
  slug: ecovadis-sustainability-ratings-carbon-and-iq-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ecovadis-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecovadis-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EcovadisCode
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ecovadis
- group: company
  title: ''
  type: Website
  url: https://ecovadis.com/
- group: operate
  title: ''
  type: Support
  url: https://support.ecovadis.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecovadis.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecovadis.com/terms-conditions/
- group: company
  title: ''
  type: Blog
  url: https://ecovadis.com/blog/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ecovadis-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ecovadis-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/ecovadis-packages.yml
created: '2024-12-25'
description: Ecovadis is a global leader in providing sustainability ratings and performance improvement tools for companies looking to assess and improve their environmental and social practices. Their platform helps organizations evaluate the sustainability performance of their suppliers, partners, and vendors, enabling them to make more informed decisions when it comes to selecting business partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecovadis.png
layout: provider
modified: '2026-07-25'
name: Ecovadis
nav: Providers
network: true
overview: 'Ecovadis publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Businesses, Environment, Ratings, and Sustainability.


  Ecovadis'' developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 85.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecovadis/refs/heads/main/screenshots/ecovadis-2026-07-25T212809.png
security:
- kind: domain-security
  name: Ecovadis Domain Security
  slug: ecovadis-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Ecovadis Trust Center
  slug: ecovadis-trust-center
  summary_line: ISO 27001
slug: ecovadis
tags:
- Businesses
- Environment
- Ratings
- Sustainability
website: https://ecovadis.com/
---
