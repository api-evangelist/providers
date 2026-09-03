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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/three-uk-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/three-uk-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/three-uk-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/three-uk-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.three.co.uk/support/network-and-coverage/affected-areas
- group: build
  title: ''
  type: Packages
  url: packages/three-uk-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/three-uk-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.three.co.uk/
- group: company
  title: ''
  type: BusinessWebsite
  url: https://www.three.co.uk/business
- group: company
  title: ''
  type: Blog
  url: https://www.three.co.uk/blog
- group: operate
  title: ''
  type: Support
  url: https://www.three.co.uk/support
- group: company
  title: ''
  type: GroupWebsite
  url: https://groupsolutions.three.com/
- group: company
  title: ''
  type: ParentWebsite
  url: https://ckhiod.com/
- group: start
  title: ''
  type: Login
  url: https://www.three.co.uk/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.three.co.uk/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.three.co.uk/privacy-safety/about-privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.three.co.uk/terms-conditions/price-guides/latest-price-guides
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/three-uk
- group: other
  title: ''
  type: Standards
  url: https://github.com/camaraproject/Governance/blob/main/PARTICIPANTS.MD
- group: other
  title: ''
  type: Standards
  url: https://camaraproject.org/
- group: other
  title: ''
  type: Standards
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/
- group: operate
  title: ''
  type: PressRelease
  url: https://www.gsma.com/newsroom/press-release/uk-mobile-operators-launch-age-verification-and-anti-fraud-apis-through-gsma-open-gateway-initiative/
created: '2026-07-25'
description: 'Three UK (Hutchison 3G UK Limited, Reading, England) is a United Kingdom mobile network operator that launched in 2003 as the country''s first 3G-only carrier and grew into a consumer and business mobile, 5G, and home broadband provider, also operating the SMARTY sub-brand. Since 31 May 2025 Three UK has been a wholly owned subsidiary of VodafoneThree, the merged Vodafone UK / Three UK joint venture that is 51% Vodafone Group and 49% CK Hutchison Holdings, serving roughly 27 million UK customers. In the telecom value chain Three UK is a network owner and access provider, not a developer platform: it sells connectivity, spectrum-backed coverage, wholesale and MVNO capacity, and business connectivity, while its group-level enterprise, IoT, private-network and wholesale propositions are marketed through CK Hutchison''s CKH IOD and Three Group Solutions. Its API posture is partner-gated and sales-led. Three UK publishes no public developer portal, no self-serve signup, no downloadable
  OpenAPI, no SDKs, and no public Postman workspace; every candidate developer hostname (developer, developers, docs, apis, sandbox, opengateway) resolves only to a wildcard Akamai record whose certificate does not cover it, and the Wayback Machine holds no snapshot of a Three UK developer portal ever existing. Three UK is nonetheless a real participant in the sector''s standards layer: it is named in the CAMARA Project''s governance participants list, its parent CK Hutchison Holdings is listed as an Operator in the CAMARA landscape, and on 23 September 2025 CK Hutchison Group Telecom (Three) commercially launched CAMARA KYC Age Verification and KYC Tenure network APIs alongside BT/EE, Virgin Media O2, and Vodafone under GSMA Open Gateway, on top of an already-available SIM Swap API, with KYC Match committed. Those APIs are reachable only through channel partners and aggregators — JT Group and TMT.ID are named as processing UK operator network API traffic, and Three UK''s majority owner
  Vodafone Group is a founding venture partner in Aduna — never through a Three UK developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Three UK
nav: Providers
network: true
overview: 'Three UK is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, United Kingdom, Mobile Network Operator, Network APIs, and CAMARA.


  Three UK''s developer surface includes engineering blog, support, pricing, and 19 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 20.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/three-uk/refs/heads/main/screenshots/three-uk-2026-09-02T163620.png
security:
- kind: domain-security
  name: Three Uk Domain Security
  slug: three-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: three-uk
tags:
- Telecommunications
- United Kingdom
- Mobile Network Operator
- Network APIs
- CAMARA
- GSMA Open Gateway
- 5G
- Broadband
- Roaming
- SIM Swap
- Identity Verification
- Age Verification
- Wholesale
- MVNO
- Partner Gated
website: https://www.three.co.uk/
---
