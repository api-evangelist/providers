---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-09-04'
api_count: 8
apis:
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The APIKeyService API from Akuity — 4 operation(s) for apikeyservice.
  name: Akuity API Key Service API
  slug: akuity-apikeyservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The ArgoCDService API from Akuity — 111 operation(s) for argocdservice.
  name: Akuity Argo CD Service API
  slug: akuity-argocdservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The AuthService API from Akuity — 4 operation(s) for authservice.
  name: Akuity Auth Service API
  slug: akuity-authservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The CustomRoleService API from Akuity — 2 operation(s) for customroleservice.
  name: Akuity Custom Role Service API
  slug: akuity-customroleservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The ExtensionService API from Akuity — 6 operation(s) for extensionservice.
  name: Akuity Extension Service API
  slug: akuity-extensionservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The KargoService API from Akuity — 39 operation(s) for kargoservice.
  name: Akuity Kargo Service API
  slug: akuity-kargoservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The OrganizationService API from Akuity — 153 operation(s) for organizationservice.
  name: Akuity Organization Service API
  slug: akuity-organizationservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The SystemService API from Akuity — 14 operation(s) for systemservice.
  name: Akuity System Service API
  slug: akuity-systemservice-api
artifact_total: 23
asyncapis:
- description: ''
  name: Akuity Notifications Webhooks
  slug: akuity-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Akuity Platform API — API Keys API Key Service API
  slug: open-akuity-apikeyservice-api
- collection_type: open
  name: Akuity Platform API — Argo CD Argo CD Service API
  slug: open-akuity-argocdservice-api
- collection_type: open
  name: Akuity Platform API — Auth Auth Service API
  slug: open-akuity-authservice-api
- collection_type: open
  name: Akuity Platform API — Custom Roles Custom Role Service API
  slug: open-akuity-customroleservice-api
- collection_type: open
  name: Akuity Platform API — Extension Extension Service API
  slug: open-akuity-extensionservice-api
- collection_type: open
  name: Akuity Platform API — Kargo Kargo Service API
  slug: open-akuity-kargoservice-api
- collection_type: open
  name: Akuity Platform API — Organization Organization Service API
  slug: open-akuity-organizationservice-api
- collection_type: open
  name: Akuity Platform API — System System Service API
  slug: open-akuity-systemservice-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/akuity-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akuity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://akuity.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.akuity.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.akuity.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.akuity.io/akuity-portal/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.akuity.io/argocd/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://akuity.io/connect-with-akuity
- group: operate
  title: ''
  type: Community
  url: https://akuity.community/
- group: company
  title: ''
  type: Blog
  url: https://akuity.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akuity
- group: commercial
  title: ''
  type: Pricing
  url: https://akuity.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://akuity.cloud
- group: start
  title: ''
  type: Login
  url: https://akuity.cloud
- group: commercial
  title: ''
  type: TermsOfService
  url: https://akuity.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://akuity.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.akuity.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/akuity-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://akuity.io/security-compliance
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/akuity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/akuity-vulnerability-disclosure.yml
- group: learn
  title: ''
  type: Training
  url: https://academy.akuity.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/akuity-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/akuity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/akuity-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/akuity-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/akuity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/akuity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/akuity-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/akuity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/akuity-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/akuity-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/akuity-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/akuity-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/akuity-notifications-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/akuity-platform-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/akuity-plans.yml
created: '2026-08-06'
description: 'Akuity is the enterprise software delivery company founded by the creators of Argo CD and Kargo. The Akuity Platform is its commercial, fully-managed offering: hosted, enterprise-grade Argo CD control planes for GitOps continuous delivery, managed Kargo for multi-stage progressive promotion, the Akuity Agent for connecting target Kubernetes clusters, and Akuity Intelligence — an AI layer adding multi-cluster insight dashboards, on-call and promotion advisor agents, and AI-assisted remediation. The platform is controlled by a REST API at https://akuity.cloud/api/v1/, an `akuity` CLI, a Terraform provider and a Crossplane provider, all of which speak the same grpc-gateway service surface. Akuity runs on AWS with US and EU data residency and maintains SOC 2 Type II, ISO 27001:2022, PCI DSS 4.0.1, HIPAA-aligned and CSA STAR Level 1 posture.'
image: https://framerusercontent.com/images/GquIfu25ll0uHAbX9oobc0UUUE.png
layout: provider
modified: '2026-08-06'
name: Akuity
nav: Providers
network: true
overview: 'Akuity publishes 8 APIs on the [APIs.io](https://apis.io/) network, including API Key Service API, Argo CD Service API, Auth Service API, and 5 more. Tagged areas include GitOps, Continuous Delivery, Kubernetes, ArgoCD, and Kargo.


  The Akuity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Akuity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Akuity Plans
  plan_count: 3
  slug: akuity-plans
random_paper: 12
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 63.6
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 66.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/screenshots/akuity-2026-08-07T161137.png
security:
- kind: authentication
  name: Akuity Authentication
  slug: akuity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Akuity Domain Security
  slug: akuity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Akuity Vulnerability Disclosure
  slug: akuity-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Akuity Trust Center
  slug: akuity-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, PCI DSS v4.0.1, HIPAA, CSA STAR Level 1, GDPR
slug: akuity
tags:
- GitOps
- Continuous Delivery
- Kubernetes
- ArgoCD
- Kargo
- Platform Engineering
- DevOps
- Progressive Delivery
- Cloud-Native
- AIOps
- Developer Tools
website: https://akuity.io
---
