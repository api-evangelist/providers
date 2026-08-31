---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The ECS Management REST API provides programmatic access to manage Dell EMC Elastic Cloud Storage (ECS) object storage platform. It supports namespace management, user management, storage pool configu
  name: EMC ECS Management REST API
  slug: ecs-management-api
- description: The Unisphere Management REST API provides programmatic access to manage Dell EMC Unity and PowerStore storage arrays. It supports storage resource provisioning, performance monitoring, alert manageme
  name: EMC Unisphere REST API
  slug: unisphere-api
artifact_total: 29
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/dell-technologies/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/emc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emc-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emccorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emc-corporation
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dell.com/apis
- group: operate
  title: ''
  type: Support
  url: https://www.dell.com/support/home/en-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dell.com/
- group: build
  title: ''
  type: Packages
  url: packages/emc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/emc-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/emc-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/emc-security.txt
- group: auth
  title: ''
  type: Security
  url: security/emc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/emc-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/emc-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/emc-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/emc-error-codes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/emc-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/emc-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emc-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/emc-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/emc-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/emc-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emc-llms.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/emc-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emc-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/emc-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/emc-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dell.com/apis
- group: company
  title: ''
  type: Blog
  url: https://www.dell.com/en-us/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dell.com/en-us/lp/terms-of-sale
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dell.com/en-us/lp/legal/privacy-statement
- group: start
  title: ''
  type: SignUp
  url: https://www.dell.com/en-us/lp/sign-in
- group: company
  title: ''
  type: Website
  url: https://www.delltechnologies.com/en-us/index.htm
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/EMCECS
created: '2026-03-24'
description: 'EMC Corporation, acquired by Dell Technologies in 2016 and now operating as Dell EMC, builds enterprise storage, data management and data protection platforms — ECS/ObjectScale object storage, Unity, VNX, PowerMax (VMAX lineage), PowerScale (Isilon) and PowerFlex (ScaleIO). Two management APIs are profiled: the ECS Management REST API and the Unisphere REST API. Both are appliance APIs served on port 4443 and 8443 by hardware the customer owns, so there is no EMC-operated endpoint, no API key, no plan and no rate limit — a fact that shapes every artifact in this repo. ECS is multi-protocol, implementing the Amazon S3, OpenStack Swift, EMC Atmos, EMC CAS, HDFS and NFSv3 interfaces, which means an S3-speaking application integrates by changing an endpoint rather than writing a connector. No OpenAPI is publicly downloadable: Dell publishes references on developer.dell.com, but the portal is a client-rendered SPA whose specification API returns HTTP 401 to anonymous callers, so
  this profile is built from EMC''s own published client libraries on github.com/EMCECS and github.com/dell.'
features:
- Enterprise-grade object and block storage
- Multi-protocol support (S3, Swift, Atmos, HDFS)
- Geo-distributed replication
- Namespace and tenant management
- Role-based access control
- Performance monitoring and alerting
- Storage pool and provisioning management
finops:
- name: Emc Finops
  service_category: API
  slug: emc-finops
image: /assets/icons/emc.png
integrations:
- VMware vSphere
- Microsoft Hyper-V
- Amazon S3
- OpenStack Swift
- Hadoop HDFS
- Kubernetes CSI
- Ansible
layout: provider
mcp_servers:
- description: ''
  name: EMC MCP Server
  slug: emc-mcp-server
modified: '2026-08-29'
name: EMC
nav: Providers
network: true
overview: 'EMC publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Infrastructure, Data Management, Data Protection, Enterprise Storage, and Object Storage.


  EMC''s developer surface includes documentation, support, authentication, changelog, sandbox, API reference, engineering blog, and 29 more developer resources.'
plans:
- name: Emc Plans Pricing
  plan_count: 0
  slug: emc-plans-pricing
press:
- date: '2026-05-25'
  title: Dell EMC Accelerates Artificial Intelligence Adoption for ...
  url: https://www.prnewswire.com/news-releases/dell-emc-accelerates-artificial-intelligence-adoption-for-digital-transformation-300693271.html
- date: '2026-05-25'
  title: EMC Insurance Adopts Full Suite of CLARA Analytics AI- ...
  url: https://claraanalytics.com/news/emc-insurance-adopts-full-suite-of-clara-analytics-ai-based-products/
- date: '2026-05-25'
  title: Dell Technologies Makes Artificial Intelligence and Machine ...
  url: https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2018~05~dell-technologies-makes-artificial-intelligence-and-machine-learning-real.htm
- date: '2026-05-25'
  title: 'Modeling for EMC: From Physics to AI'
  url: https://www.emcs.org/event/modeling-for-emc-from-physics-to-ai/
- date: '2026-05-25'
  title: Comparative Study of AI Methods for EMC Prediction in ...
  url: https://www.mdpi.com/2079-9292/15/1/165
random_paper: 15
rate_limits:
- limit_count: 0
  name: Emc Rate Limits
  slug: emc-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 33.3
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 28.9
  previous_composite: 30.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emc/refs/heads/main/screenshots/emc-2026-06-20T180631.png
security:
- kind: authentication
  name: Emc Authentication
  slug: emc-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Emc Domain Security
  slug: emc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Emc Vulnerability Disclosure
  slug: emc-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Emc Trust Center
  slug: emc-trust-center
  summary_line: ISO 27001, SOC 1 Type 2, SOC 2 Type 2, PCI DSS (Level 2 Merchant), Common Criteria (EAL2+, ALC_FLR.2), O-TTPS / ISO-IEC 20243:2023, TISAX, IRAP, Cyber Essentials, Esquema Nacional de Seguridad (ENS), NHS DSPT, Swift CSP, JOSCAR, CyberGRX, CyberVadis, KY3P, EU Data Act
slug: emc
tags:
- Cloud Infrastructure
- Data Management
- Data Protection
- Enterprise Storage
- Object Storage
- Storage
- S3 Compatible
- Fortune 500
use_cases:
- Managing enterprise storage infrastructure programmatically
- Automating storage provisioning for cloud workloads
- Monitoring storage array health and performance
- Configuring data protection and replication policies
- Managing multi-tenant storage environments
website: https://www.delltechnologies.com/en-us/index.htm
---
