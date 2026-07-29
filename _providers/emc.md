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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The ECS Management REST API provides programmatic access to manage Dell EMC Elastic Cloud Storage (ECS) object storage platform. It supports namespace management, user management, storage pool configu
  name: EMC ECS Management REST API
  slug: ecs-management-api
- description: The Unisphere Management REST API provides programmatic access to manage Dell EMC Unity and PowerStore storage arrays. It supports storage resource provisioning, performance monitoring, alert manageme
  name: EMC Unisphere REST API
  slug: unisphere-api
artifact_total: 26
common:
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
  url: https://www.dell.com/support/kbdoc/en-us/000020064/ecs-api-documentation
- group: operate
  title: ''
  type: Support
  url: https://www.dell.com/support/home/en-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dell.com/
created: '2026-03-24'
description: EMC Corporation (now Dell EMC, a division of Dell Technologies) provides enterprise storage, data management, and cloud infrastructure solutions. EMC products include VMAX, VNX, Isilon, and ECS storage platforms, as well as data protection and information management solutions. EMC was acquired by Dell Technologies in 2016.
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
modified: '2026-04-18'
name: EMC
nav: Providers
network: true
overview: 'EMC publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Infrastructure, Data Management, Data Protection, Enterprise Storage, and Storage.


  EMC''s developer surface includes documentation, support, and 5 more developer resources.'
plans:
- name: Emc Plans Pricing
  plan_count: 3
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
random_paper: 66
rate_limits:
- limit_count: 5
  name: Emc Rate Limits
  slug: emc-rate-limits
score:
  band: emerging
  composite: 23.9
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 26.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emc/refs/heads/main/screenshots/emc-2026-06-20T180631.png
security:
- kind: domain-security
  name: Emc Domain Security
  slug: emc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Emc Vulnerability Disclosure
  slug: emc-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: emc
tags:
- Cloud Infrastructure
- Data Management
- Data Protection
- Enterprise Storage
- Storage
- Fortune 500
use_cases:
- Managing enterprise storage infrastructure programmatically
- Automating storage provisioning for cloud workloads
- Monitoring storage array health and performance
- Configuring data protection and replication policies
- Managing multi-tenant storage environments
website: https://developer.dell.com/
---
