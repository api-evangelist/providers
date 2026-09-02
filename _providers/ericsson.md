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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ericsson-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ericsson.com/en
- group: other
  title: ''
  type: NetworkAPIs
  url: https://www.ericsson.com/en/enterprise/network-apis
- group: other
  title: ''
  type: Aduna
  url: https://adunaglobal.com/
- group: company
  title: ''
  type: AdunaNewsroom
  url: https://adunaglobal.com/newsroom/
- group: other
  title: ''
  type: Vonage
  url: https://developer.vonage.com/en/home
- group: other
  title: ''
  type: EnterpriseWireless
  url: https://www.cradlepoint.com/
- group: other
  title: ''
  type: IntelligentAutomationPlatform
  url: https://www.ericsson.com/en/cloud-software-and-services/intelligent-automation-platform
- group: other
  title: ''
  type: CAMARA
  url: https://camaraproject.org/
- group: company
  title: ''
  type: About
  url: https://www.ericsson.com/en/about-us
- group: company
  title: ''
  type: Newsroom
  url: https://www.ericsson.com/en/news
- group: company
  title: ''
  type: Blog
  url: https://www.ericsson.com/en/blog
- group: company
  title: ''
  type: ResearchBlog
  url: https://www.ericsson.com/en/blog/research
- group: company
  title: ''
  type: Investors
  url: https://www.ericsson.com/en/investors
- group: company
  title: ''
  type: Careers
  url: https://www.ericsson.com/en/careers
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Ericsson
- group: build
  title: ''
  type: GitHubResearch
  url: https://github.com/EricssonResearch
- group: build
  title: ''
  type: GitHubIAP
  url: https://github.com/ericsson-iap
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ericsson
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ericsson
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ericsson
created: '2026-05-25'
description: 'Ericsson (Telefonaktiebolaget LM Ericsson) is a Swedish multinational networking and telecommunications equipment vendor headquartered in Kista, Stockholm. Founded in 1876, the company supplies mobile and fixed network infrastructure to communication service providers worldwide and operates across three product areas: Networks (5G RAN, 5G Core, Cloud RAN, transport), Cloud Software & Services (OSS/BSS, orchestration, billing, charging, analytics), and Enterprise Wireless Solutions (private 5G via Cradlepoint). Ericsson holds more than 60,000 granted patents and operates 21 R&D centers, with networks that carry roughly 40 percent of the world''s mobile data traffic. In 2024 Ericsson and twelve major operators — AT&T, Bharti Airtel, Deutsche Telekom, KDDI, Orange, Reliance Jio, Singtel, Telefonica, Telstra, T-Mobile, Verizon, and Vodafone — closed Aduna, a 50:50 joint venture that aggregates CAMARA-aligned network APIs (SIM Swap, Number Verification, Quality on Demand, Device
  Location, Device Reachability, Scam Signal, Call Forwarding Signal, Connectivity Insights, OTP SMS) and exposes them through hyperscaler and CPaaS channel partners (Microsoft Azure Marketplace, Google Cloud, Vonage, Sinch, Infobip). Ericsson also owns Vonage (acquired 2022), which operates the public-facing developer portal for many of these network capabilities, and runs the Ericsson Intelligent Automation Platform (EIAP) for ORAN-aligned rApp development. Ericsson does not publish a single consolidated developer portal or canonical OpenAPI catalog at ericsson.com — its programmable surface is delivered indirectly through Aduna, Vonage, and channel partners, and most of its public GitHub presence is research tooling and infrastructure software (CodeChecker, CodeCompass, ecchronos) rather than developer-facing APIs.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ericsson.png
layout: provider
modified: '2026-05-25'
name: Ericsson
nav: Providers
network: true
overview: 'Ericsson is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Networks, 5G, 5G RAN, and 5G Core.


  Ericsson''s developer surface includes engineering blog, GitHub presence, YouTube channel, and 18 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 3.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ericsson/refs/heads/main/screenshots/ericsson-2026-06-20T180812.png
security:
- kind: domain-security
  name: Ericsson Domain Security
  slug: ericsson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ericsson
tags:
- Telecommunications
- Networks
- 5G
- 5G RAN
- 5G Core
- Cloud RAN
- ORAN
- Network APIs
- CAMARA
- Aduna
- Programmable Networks
- Network Exposure
- Telecom Equipment
- Enterprise Wireless
- Private 5G
- OSS BSS
- Vonage
- Cradlepoint
- Sweden
website: https://www.ericsson.com/en
---
