---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-06'
api_count: 8
apis:
- description: 'The organization root of the Akuity Platform: organizations, workspaces, members, teams, invitations, API keys, audit logs and archives, SSO and OIDC mapping, quotas, billing and plans, notification c'
  name: Akuity Platform API — Organizations, Workspaces and Kubernetes Inventory
  slug: akuity-platform-api-organizations-workspaces-and-kubernetes-inventory
- description: 'Managed Argo CD control planes: instance create/update/delete/apply/export, target cluster registration and agent manifests, cluster addons and addon repositories, repositories, notification settings '
  name: Akuity Platform API — Argo CD
  slug: akuity-platform-api-argo-cd
- description: 'Managed Kargo control planes for multi-stage progressive promotion: instance lifecycle, Kargo agent creation and manifests, credential rotation, maintenance mode, agent version upgrades, promotion eve'
  name: Akuity Platform API — Kargo
  slug: akuity-platform-api-kargo
- description: 'The anonymous, unauthenticated corner of the platform: platform build version, system status and settings, available Argo CD / Kargo / Akuity Agent / image-updater versions, agent size specs, the anno'
  name: Akuity Platform API — System
  slug: akuity-platform-api-system
- description: Lifecycle of the AKUITY_API_KEY_ID / AKUITY_API_KEY_SECRET credential pair — get, delete and secret regeneration, at both organization and workspace scope. 6 operations.
  name: Akuity Platform API — API Keys
  slug: akuity-platform-api-api-keys
- description: Named authorization policies attached to an organization or workspace, used to narrow an API key beyond the coarse Owner/Member roles. 5 operations.
  name: Akuity Platform API — Custom Roles
  slug: akuity-platform-api-custom-roles
- description: The OAuth 2.0 Device Authorization Grant (RFC 8628) endpoints behind `akuity login`, plus OIDC provider details. Published in Akuity's own client module but not documented for third-party clients — ma
  name: Akuity Platform API — Authentication
  slug: akuity-platform-api-authentication
- description: The `/ext-api/v1/` surface that backs Akuity's UI extensions inside the managed Argo CD web UI — per-application audit records, sync-operation events and stats, Kargo analysis-run logs and extension s
  name: Akuity Platform API — Argo CD UI Extensions
  slug: akuity-platform-api-argo-cd-ui-extensions
artifact_total: 14
asyncapis:
- description: ''
  name: Akuity Notifications Webhooks
  slug: akuity-notifications-webhooks
common:
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
overview: 'Akuity publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Platform API — Organizations, Workspaces and Kubernetes Inventory, Platform API — Argo CD, Platform API — Kargo, and 5 more. Tagged areas include GitOps, Continuous Delivery, Kubernetes, Argo CD, and Kargo.


  The Akuity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Akuity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Akuity Plans
  plan_count: 3
  slug: akuity-plans
random_paper: 98
score:
  band: exemplar
  composite: 67.8
  facets:
    commercial_clarity: 92.1
    contract_quality: 64.3
    developer_ergonomics: 71.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
- Argo CD
- Kargo
- Platform Engineering
- DevOps
- Progressive Delivery
- Cloud Native
- AIOps
- Developer Tools
website: https://akuity.io
---
