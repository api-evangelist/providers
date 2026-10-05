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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Alibaba Cloud provides a comprehensive API ecosystem covering all major cloud services including Elastic Compute Service (ECS), Object Storage Service (OSS), Container Service for Kubernetes (ACK), Re
  name: Alibaba Cloud API
  slug: alibaba-cloud-api
artifact_total: 4
collections:
- collection_type: open
  name: API Collection
  slug: open-alibaba
common:
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alibabacloud.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/overlays/alibaba-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/alibaba-openapi-overlay.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/mcp/alibaba-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/alibaba-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/hosts/alibaba-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alibaba-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/vendors/alibaba-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alibaba-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/packages/alibaba-packages.yml
  title: ''
  type: SDKs
  url: packages/alibaba-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/security/alibaba-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alibaba-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alibaba.com
- group: company
  title: ''
  type: Website
  url: https://www.alibabacloud.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.alibabacloud.com/
- group: start
  title: ''
  type: Portal
  url: https://www.alibabacloud.com/en/product/openapiexplorer
- group: build
  title: ''
  type: GitHub
  url: https://github.com/aliyun
- group: build
  title: ''
  type: GitHub
  url: https://github.com/alibabacloud-go
- group: build
  title: ''
  type: SDK
  url: https://www.alibabacloud.com/help/en/sdk/product-overview/alibaba-cloud-sdk
- group: start
  title: ''
  type: Login
  url: https://account.alibabacloud.com/login/login.htm
- group: start
  title: ''
  type: SignUp
  url: https://account.alibabacloud.com/register/intl_register.htm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alibabacloud.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.alizila.com/feed/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/packages/alibaba-packages.yml
  title: ''
  type: Packages
  url: packages/alibaba-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/well-known/alibaba-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alibaba-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/mcp/alibaba-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alibaba-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/conformance/alibaba-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alibaba-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/lifecycle/alibaba-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alibaba-lifecycle.yml
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.alibaba.com
  reason: no-machine-readable-spec
  state: unreadable
description: Alibaba is a multinational technology conglomerate founded in 1999 by Jack Ma, focused on e-commerce, retail, internet, and technology. The company operates major online marketplaces including Taobao, Tmall, and AliExpress, connecting millions of sellers with consumers globally. Alibaba Cloud (Aliyun), founded in 2009, is a global leader in cloud computing and artificial intelligence, serving enterprises, developers, and government organizations in more than 200 countries. Alibaba Cloud provides cloud computing, storage, networking, big data, AI/ML, security, and developer services through a comprehensive API ecosystem. The OpenAPI Explorer provides a web interface for discovering, testing, and generating SDK code for hundreds of Alibaba Cloud service APIs. The company also operates Alipay (digital payments), DingTalk (enterprise collaboration), and 1688 (B2B wholesale).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alibaba.png
layout: provider
mcp_servers:
- description: 'Official Alibaba Cloud MCP server (aliyun GitHub org) that fronts tens of thousands of Alibaba Cloud OpenAPIs through a small set of core tools plus a catalog of system MCP services. Supports SSE and '
  name: Alibaba Cloud OpenAPI MCP Server
  slug: alibaba-cloud-openapi-mcp-server
modified: '2026-06-20'
name: Alibaba
nav: Providers
network: true
overview: 'Alibaba publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Cloud Computing, E-Commerce, Commerce, and Artificial Intelligence.


  Alibaba''s developer surface includes documentation, developer portal, GitHub presence, SDKs, signup flow, pricing, engineering blog, and 16 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 71.7
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 25.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/alibaba/refs/heads/main/screenshots/alibaba-2026-07-25T195614.png
security:
- kind: domain-security
  name: Alibaba Domain Security
  slug: alibaba-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alibaba
tags:
- Cloud
- Cloud Computing
- E-Commerce
- Commerce
- Artificial Intelligence
- Machine Learning
- Big Data
- Storage
- Networking
- Serverless
- Developer Tools
website: https://www.alibaba.com
---
