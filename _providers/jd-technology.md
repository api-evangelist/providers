---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: JD Cloud OpenAPI is the programmatic control plane for JD Technology's public cloud — compute (VM), storage, databases (RDS), networking, containers, CDN, AI and security services. Each product expose
  name: JD Cloud OpenAPI
  slug: jd-cloud-openapi
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.jdcloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jdcloud.com/cn/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jdcloud.com/cn/common-declaration/api/introduction
- group: company
  title: ''
  type: Website
  url: https://www.jdt.com.cn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jdcloud-api
- group: start
  title: ''
  type: SignUp
  url: https://login.jdcloud.com/
- group: build
  title: ''
  type: Packages
  url: packages/jd-technology-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/jd-technology-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/jd-technology-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jd-technology-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jd-technology-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jd-technology-llms.txt
created: '2026-07-17'
description: JD Technology Group (京东科技集团) is the technology and cloud subsidiary of JD.com, delivering digital-transformation services to government, financial institutions, and enterprises. Its primary developer surface is JD Cloud (京东云), a full-stack public cloud offering compute, storage, databases, networking, AI, security, and industry solutions exposed through the JD Cloud OpenAPI. Developers integrate via signed (access-key / secret-key) OpenAPI calls to per-service endpoints, and JD Technology publishes first-party SDKs for Java, Go, Python, PHP, .NET, Node.js and iOS plus a cross-platform command line (jdc) on GitHub. This profile was surfaced as a portfolio company of hongshan and enriched from JD Technology's public developer surfaces.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jd-technology.png
layout: provider
modified: '2026-07-19'
name: JD Technology
nav: Providers
network: true
overview: 'JD Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Cloud, Cloud Computing, and Infrastructure.


  JD Technology''s developer surface includes documentation, API reference, signup flow, CLI, authentication, and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jd-technology/refs/heads/main/screenshots/jd-technology-2026-07-25T223219.png
security:
- kind: authentication
  name: Jd Technology Authentication
  slug: jd-technology-authentication
  summary_line: requestSignature · 2 schemes
- kind: domain-security
  name: Jd Technology Domain Security
  slug: jd-technology-domain-security
  summary_line: TLSv1.3 · HSTS
slug: jd-technology
tags:
- Company
- Technology
- Cloud
- Cloud Computing
- Infrastructure
- Fintech
- Artificial Intelligence
- Developer Platform
- OpenAPI
- China
website: https://www.jdt.com.cn/
---
