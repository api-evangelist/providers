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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-01'
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
- group: auth
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
  title: ''
  type: Packages
  url: packages/alibaba-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alibaba-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alibaba-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alibaba-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/alibaba-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alibaba-lifecycle.yml
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
overview: 'Alibaba publishes 1 API on the [APIs.io](https://apis.io/) network: Cloud API. Tagged areas include Cloud, Cloud Computing, E-Commerce, Commerce, and Artificial Intelligence.


  Alibaba''s developer surface includes documentation, developer portal, GitHub presence, SDKs, signup flow, pricing, engineering blog, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 25.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
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
- Machine-Learning
- Big Data
- Storage
- Networking
- Serverless
- Developer Tools
website: https://www.alibaba.com
---
