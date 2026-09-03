---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The REST-compliant, microservices-based API of ModelOp Center. It exposes the governance inventory (StoredModel entities — Use Cases and Model Implementations), snapshots (immutable model versions), a
  name: ModelOp Center REST API
  slug: modelop-center-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Modelop Runtime Streams
  slug: modelop-runtime-streams
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modelop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.modelop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://modelopdocs.atlassian.net/wiki/spaces/MDHV
- group: start
  title: ''
  type: GettingStarted
  url: https://modelopdocs.atlassian.net/wiki/spaces/MDHV/pages/3159982123/Getting+Started+with+ModelOp+Center
- group: operate
  title: ''
  type: Support
  url: https://www.modelop.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.modelop.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modelop
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modelop.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modelop-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/modelop-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/modelop-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modelop-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modelop-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modelop-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/modelop-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modelop-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/modelop-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/modelop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modelop-rate-limits.yml
created: '2026-08-25'
description: ModelOp is enterprise software for governing and operationalizing artificial intelligence at scale. Founded as Open Data Group and headquartered in Chicago, Illinois, it sells an "AI system of record" — the Enterprise AI Command Center, powered by the ModelOp AI Delivery Engine (MADE) and delivered as ModelOp Center — that lets large regulated organizations inventory every AI asset, automate the model lifecycle from intake through retirement, enforce governance and regulatory policy, and report on cost, risk and ROI across traditional machine learning, generative AI and agentic AI. The platform is customer-deployed (Helm chart on Kubernetes) with a REST-compliant microservices architecture, a `moc` CLI, OAuth 2.0/OIDC authentication against the enterprise's own identity provider, and 50+ integrations spanning cloud, AI/ML platforms, data, BI, GRC, ITSM and security systems. Because ModelOp Center runs inside the customer's own infrastructure, its Swagger UI and OpenAPI document
  are served only from a customer instance and are not published at any public URL.
image: https://cdn.prod.website-files.com/66205eb2534d2143f98716a4/6a1e0cff57f08839578807be_Homepage%20Image%20for%20Website%20Metadata%20-%201200x630%20v2.png
layout: provider
modified: '2026-08-25'
name: ModelOp
nav: Providers
network: true
overview: 'ModelOp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Governance, Model Risk Management, Machine-Learning, MLOps, and ModelOps.


  The ModelOp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ModelOp''s developer surface includes documentation, getting-started guide, support, engineering blog, CLI, authentication, changelog, and 12 more developer resources.'
plans:
- name: Modelop Plans Pricing
  plan_count: 0
  slug: modelop-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Modelop Rate Limits
  slug: modelop-rate-limits
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 34.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modelop/refs/heads/main/screenshots/modelop-2026-09-02T150603.png
security:
- kind: authentication
  name: Modelop Authentication
  slug: modelop-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Modelop Domain Security
  slug: modelop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modelop
tags:
- AI Governance
- Model Risk Management
- Machine-Learning
- MLOps
- ModelOps
- AI Lifecycle Automation
- Enterprise Software
- Compliance
- Model Monitoring
- Governance Risk and Compliance
- Artificial Intelligence
website: https://www.modelop.com/
---
