---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.2
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Action-based RPC API covering every UCloud product (compute, networking, storage, databases, Kubernetes, monitoring, AI) through a single signed gateway. Requests carry an Action name plus PublicKey/S
  name: UCloud Open API
  slug: ucloud-open-api
artifact_total: 5
asyncapis:
- description: ''
  name: Ucloud Webhooks
  slug: ucloud-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucloud-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ucloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://src.ucloud.cn/
- group: company
  title: ''
  type: Website
  url: https://www.ucloud.cn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.ucloud.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ucloud.cn/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ucloud.cn/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ucloud.cn/api/summary/public
- group: operate
  title: ''
  type: Support
  url: https://spt.ucloud.cn/
- group: company
  title: ''
  type: Blog
  url: https://www.ucloud-global.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ucloud
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ucloud-global.com/en/price
- group: start
  title: ''
  type: SignUp
  url: https://passport.ucloud.cn/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ucloud-global.com/en/docs/agreement/ServicesAgreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ucloud-global.com/en/docs/agreement/PrivacyPolicy
- group: build
  title: ''
  type: CLI
  url: cli/ucloud-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/ucloud-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ucloud-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ucloud-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ucloud-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ucloud-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ucloud-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucloud-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ucloud-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ucloud-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ucloud-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ucloud-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ucloud-cli-SKILL.md
created: '2026-07-17'
description: UCloud (优刻得, UCloud Technology Co., Ltd.) is a neutral Chinese cloud computing provider listed on the SSE STAR Market (688158), offering compute (UHost, bare-metal, GPU), object storage (UFile/US3), networking (VPC, ULB, EIP), Kubernetes (UK8S), databases, CDN, monitoring and AI infrastructure across China and 20+ global regions. Everything is managed through one Action-based Open API at api.ucloud.cn with signed requests, first-party SDKs in five languages, a CLI with an official published agent skill, and a Terraform provider. UCloud also runs an international arm at ucloud-global.com.
image: https://avatars.githubusercontent.com/u/14289247?v=4
layout: provider
modified: '2026-07-21'
name: UCloud
nav: Providers
network: true
overview: 'UCloud publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Cloud Computing, Infrastructure-as-a-Service, and GPU.


  The UCloud catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  UCloud''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 31.0
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 37.8
  provenance:
    conformance: derived
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucloud/refs/heads/main/screenshots/ucloud-2026-08-17T082534.png
security:
- kind: authentication
  name: Ucloud Authentication
  slug: ucloud-authentication
  summary_line: signature · 2 schemes
- kind: domain-security
  name: Ucloud Domain Security
  slug: ucloud-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ucloud Vulnerability Disclosure
  slug: ucloud-vulnerability-disclosure
  summary_line: Hackerone
slug: ucloud
tags:
- Company
- Enterprise
- Cloud Computing
- Infrastructure-as-a-Service
- GPU
- Kubernetes
- Object Storage
- CDN
- China
website: https://www.ucloud.cn/
---
