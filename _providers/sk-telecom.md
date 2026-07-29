---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Sk Telecom Agentic Access
  operation_count: 55
  slug: sk-telecom-agentic-access
  summary_line: 55 operations · 20 acting
api_count: 15
apis:
- description: 'Korean text-to-speech built on SK Telecom''s own DNN speech-synthesis models and voice database, operated by SKT''s speech synthesis technology team. Three documented operations — list TTS models, list '
  name: SK Telecom A.X TTS API
  slug: sk-telecom-ax-tts-api
- description: Face recognition and analysis API (published as "NUGU facecan"). Build a per-group, per-subject face database and then detect, recognize and extract landmarks from submitted JPEG images. Nine document
  name: SK Telecom A. facecan API
  slug: sk-telecom-facecan-api
- description: Place congestion and visitor analytics derived from SK Telecom mobile network data, keyed to TMAP points of interest and to commercial AREA identifiers. Sixteen documented operations covering POI/area
  name: SK Telecom Puzzle Place Congestion API
  slug: sk-telecom-puzzle-place-congestion-api
- description: Apartment-complex resident profile analytics derived from SK Telecom network data. Five documented operations returning the apartment complex list plus monthly statistics on resident age distribution,
  name: SK Telecom Puzzle Residence API
  slug: sk-telecom-puzzle-residence-api
- description: Video and image analysis AI served from SK Telecom's sigmeta service. Seven documented operations covering an asynchronous analyzer lifecycle (create analyzer, upload file, start analyzer, get result)
  name: SK Telecom META API
  slug: sk-telecom-meta-api
- description: OVS is SK Telecom's road-event alerting service. Twelve documented operations covering customer company lookup, registration/lookup/deletion of target devices, broadcast of alert messages to devices w
  name: SK Telecom OVS API
  slug: sk-telecom-ovs-api
- description: Geovision is SK Telecom's flagship big-data API service, estimating floating population (footfall) from mobile network signalling. Documented on the SK open API portal; no downloadable OpenAPI was pub
  name: SK Telecom Geovision Floating Population API
  slug: sk-telecom-geovision-api
- description: Congestion data for every station and train on Seoul metropolitan subway lines 1 through 9 and the Shinbundang Line, including a station metadata/search operation. Documented on the SK open API portal
  name: SK Telecom Puzzle Subway Congestion API
  slug: sk-telecom-puzzle-subway-congestion-api
- description: Domestic travel analytics — traveller volume by destination, in-region dwell time, and traveller characteristics (gender, age band, companion type). Documented on the SK open API portal; no downloadab
  name: SK Telecom Puzzle Domestic Travel API
  slug: sk-telecom-puzzle-travel-api
- description: Restaurant rankings and analysis derived from call-volume statistics on SK Telecom's network. Documented on the SK open API portal; no downloadable OpenAPI was published for this product at the time o
  name: SK Telecom Puzzle Restaurant API
  slug: sk-telecom-puzzle-restaurant-api
- description: Private academy (hagwon) rankings and analysis derived from call-volume statistics on SK Telecom's network. Documented on the SK open API portal; no downloadable OpenAPI was published for this product
  name: SK Telecom Puzzle Academy API
  slug: sk-telecom-puzzle-academy-api
- description: SK Telecom's passwordless passkey authentication system for third-party services. The product page links an integration guide at api.passkey-sktelecom.com/docs/api.html; from outside Korea that host a
  name: Passkey by SK Telecom API
  slug: sk-telecom-passkey-api
- description: T ID is SK Telecom's federated identity service, the single sign-on used across SK Telecom and SK affiliate services with roughly 15 million registered users. Third parties integrate T ID login throug
  name: SK Telecom T ID Login API
  slug: sk-telecom-t-id-api
- description: Developer centre for NUGU, SK Telecom's Korean-language voice assistant platform, where third parties build and publish NUGU "plays". The portal is a single-page application; no OpenAPI or machine-rea
  name: NUGU Developers
  slug: sk-telecom-nugu-developers
- description: Quantum random number generation security chip and solution from SK Telecom, listed in the Authentication/Security category of the SK open API portal. Listed as a product rather than a documented REST
  name: SK Telecom QRNG
  slug: sk-telecom-qrng-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sk-telecom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sk-telecom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sk-telecom-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.sktelecom.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openapi.sk.com/
- group: start
  title: ''
  type: SignUp
  url: https://openapi.sk.com/user/signUp
- group: other
  title: ''
  type: SignIn
  url: https://openapi.sk.com/user/login
- group: operate
  title: ''
  type: Support
  url: https://openapi.sk.com/support/qna/qnaListView
- group: operate
  title: ''
  type: FAQ
  url: https://openapi.sk.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openapi.sk.com/stplat/usage/indexView
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.sktelecom.com/view.do?ctg=policy&name=policy
- group: company
  title: ''
  type: Blog
  url: https://news.sktelecom.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sktelecom
- group: other
  title: ''
  type: OpenSource
  url: https://sktelecom.github.io/en/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sk-telecom
- group: other
  title: ''
  type: Email
  url: mailto:skopenapi@sktelecom.com
- group: company
  title: ''
  type: PartnerProgram
  url: https://open2u.sktelecom.com/web/WWO01N051X01.do
- group: other
  title: ''
  type: Enterprise
  url: https://www.sktenterprise.com/
- group: other
  title: ''
  type: Standards
  url: https://github.com/camaraproject/Governance/blob/main/PARTICIPANTS.MD
- group: other
  title: ''
  type: Standards
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma_orgs/sk-telecom/
- group: other
  title: ''
  type: Aggregator
  url: https://www.bridgealliance.com/baex/
- group: other
  title: ''
  type: Aggregator
  url: https://adunaglobal.com/resources/news-aduna-and-sk-telink-announce-collaboration-to-bring-korea-into-the-global-network-api-ecosystem/
- group: docs
  title: ''
  type: Documentation
  url: https://openapi.sk.com/products/detail?linkMenuSeq=61
- group: operate
  title: ''
  type: ChangeLog
  url: https://openapi.sk.com/support/notice/listView
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sk-telecom-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sk-telecom-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sk-telecom-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sk-telecom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sk-telecom-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sk-telecom-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sk-telecom-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sk-telecom-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sk-telecom-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/sk-telecom-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sk-telecom-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sk-telecom-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sk-telecom-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sk-telecom-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sk-telecom-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-25'
description: 'SK Telecom Co., Ltd. is South Korea''s largest mobile network operator, headquartered at SK T-Tower in Jung-gu, Seoul, and the telecom arm of SK Group. It runs the country''s largest 5G and LTE network, sells fixed broadband and IPTV through subsidiary SK Broadband, operates the T world retail and care channel, and has repositioned itself as an "AI company" around its A.X sovereign Korean LLM family, the NUGU voice assistant, and the A. (A dot) assistant. Its position in the telecom value chain is that of a facilities-based incumbent carrier: it owns the radio access network, spectrum, SIM base, and identity rails that the rest of the Korean digital economy authenticates against. Its API posture is split in an unusual way. SK Telecom does run a genuine, self-serve public developer portal — SK open API at openapi.sk.com, operated by SK Telecom Co., Ltd. — but what it publishes there is AI, big-data and mobility product APIs (speech synthesis, face recognition, congestion and
  floating-population analytics, video analysis), not network APIs. The legacy T developers subdomains developer.sktelecom.com and developers.sktelecom.com both resolve in DNS to 211.188.149.18 and refuse connections on port 443 — a dead developer programme with dangling hostnames. On the network-API side SK Telecom is a named CAMARA participant and appears in the CAMARA landscape as an operator, has an organisation page in GSMA''s Open Gateway directory, signed a domestic MoU with KT and LG Uplus in October 2024 to standardise six network APIs through Korea''s TTA, endorsed the Bridge Alliance API Exchange, and signed an MoU with Aduna through subsidiary SK telink in September 2025 — but no CAMARA endpoint (Number Verification, SIM Swap, KYC Match, Quality on Demand) is callable from any SK Telecom-operated developer portal. Developers who want SK Telecom network capability reach it through aggregators — Bridge Alliance BAEx on Singtel''s Paragon platform, surfaced through Nokia''s Network
  as Code developer portal, or Aduna — not from SK Telecom directly.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Five live MCP endpoints on the SK Telecom documentation hubs (ReadMe-provided, tools/list auth-gated); no MCP server for the SK open API gateway itself
  slug: five-live-mcp-endpoints-on-the-sk-telecom-documentation-hubs-readme-provided-toolslist-auth-gated-no-mcp-server-for-the-sk-open-api-gateway-itself
modified: '2026-07-25'
name: SK Telecom
nav: Providers
network: true
overview: 'SK Telecom publishes 6 APIs on the [APIs.io](https://apis.io/) network, including A.X TTS API, A. facecan API, Puzzle Place Congestion API, and 3 more. Tagged areas include Telecommunications, South Korea, Mobile Network Operator, Network APIs, and CAMARA.


  SK Telecom''s developer surface includes authentication, signup flow, support, FAQ, engineering blog, documentation, changelog, and 33 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 0
  name: Sk Telecom Rate Limits
  slug: sk-telecom-rate-limits
score:
  band: thin
  composite: 39.4
  delta: -0.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 32.3
    developer_ergonomics: 51.6
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sk Telecom Authentication
  slug: sk-telecom-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sk Telecom Domain Security
  slug: sk-telecom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sk-telecom
tags:
- Telecommunications
- South Korea
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- 5G
- Identity Verification
- SIM Swap
- Artificial Intelligence
- Location
- Big Data
website: https://www.sktelecom.com/
---
