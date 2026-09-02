---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ast-spacemobile-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ast-spacemobile-llms.txt
- group: company
  title: ''
  type: Website
  url: https://ast-science.com/
- group: company
  title: ''
  type: About
  url: https://ast-science.com/company/
- group: other
  title: ''
  type: Team
  url: https://ast-science.com/company/our-team/
- group: company
  title: ''
  type: Careers
  url: https://ast-science.com/company/careers/
- group: company
  title: ''
  type: Blog
  url: https://ast-science.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://ast-science.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://ast-science.com/press-releases/
- group: company
  title: ''
  type: Partners
  url: https://ast-science.com/partners/
- group: operate
  title: ''
  type: FAQ
  url: https://ast-science.com/faqs/
- group: operate
  title: ''
  type: Contact
  url: https://ast-science.com/contact/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.ast-science.com/
- group: other
  title: ''
  type: SECFilings
  url: https://investors.ast-science.com/sec-filings
- group: other
  title: ''
  type: Events
  url: https://investors.ast-science.com/events
- group: other
  title: ''
  type: Resources
  url: https://ast-science.com/resources/
- group: other
  title: ''
  type: Images
  url: https://ast-science.com/resources/images/
- group: learn
  title: ''
  type: Videos
  url: https://ast-science.com/resources/videos/
- group: other
  title: ''
  type: BrandResources
  url: https://ast-science.com/resources/brand-resources/
- group: other
  title: ''
  type: Sitemap
  url: https://ast-science.com/sitemap_index.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ast-science.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ast-science.com/terms-of-service/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ast-science/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/AST_SpaceMobile
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/ASTSpaceMobile
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/ast-science.com
created: '2026-07-25'
description: 'AST SpaceMobile (NASDAQ, ASTS) is a United States satellite operator building the SpaceMobile Network, a space-based cellular broadband constellation of BlueBird satellites carrying the largest commercial phased-array antennas in low Earth orbit, designed to deliver 4G and 5G directly to standard, unmodified smartphones. It sits upstream of the retail telecom market as a wholesale coverage layer, not a consumer brand, not a CPaaS: signals from a handset are relayed by satellite to a small number of in-country ground gateways, which compensate for Doppler and delay and then hand the traffic into a mobile network operator''s core, where the operator completes the call and bills the subscriber. Distribution runs entirely through partner carriers, with agreements covering nearly 60 mobile network operators serving over 3 billion subscribers, including AT&T, Verizon, Vodafone, Rakuten, Bell, TELUS and stc, plus strategic investment from Google and American Tower. Its API posture
  is that of a satellite infrastructure company rather than a network-API publisher, honestly assessed as none: as of July 2026 AST SpaceMobile publishes no developer portal, no API documentation, no OpenAPI, no SDKs and no public network-API surface. Probes of developer, developers, docs, api and opengateway subdomains and the corresponding site paths all fail to resolve or return 404, and no CAMARA, GSMA Open Gateway, TM Forum or 3GPP NEF exposure claim appears anywhere on ast-science.com or in its press releases. Any programmable access to SpaceMobile capacity reaches developers only indirectly, through the partner carrier that owns the subscriber relationship and the network APIs.'
image: https://ast-science.com/wp-content/uploads/2025/08/cropped-Rectangle-491-6-192x192.png
layout: provider
modified: '2026-07-25'
name: AST SpaceMobile
nav: Providers
network: true
overview: 'AST SpaceMobile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, United States, Satellite, Direct-to-Device, and Non-Terrestrial Network.


  AST SpaceMobile''s developer surface includes engineering blog, FAQ, YouTube channel, and 23 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ast-spacemobile/refs/heads/main/screenshots/ast-spacemobile-2026-08-07T161812.png
security:
- kind: domain-security
  name: Ast Spacemobile Domain Security
  slug: ast-spacemobile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ast-spacemobile
tags:
- Telecommunications
- United States
- Satellite
- Direct-to-Device
- Non-Terrestrial Network
- Mobile Network Operator
- Broadband
- 5G
- Roaming
- Space
website: https://ast-science.com/
---
