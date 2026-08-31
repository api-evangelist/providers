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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Kubeark Webhooks
  slug: kubeark-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://kubeark.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kubeark.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kubeark.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://kubeark.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://kubeark.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://kubeark.com/support-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kubeark.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kubeark.com/wp-content/uploads/2025/01/2023.02.10.kubeark-privacy-statement.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kubeark
- group: other
  title: ''
  type: CaseStudies
  url: https://kubeark.com/success-stories/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kubeark.com/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kubeark-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kubeark-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.kubeark.com/product-lifecycle
- group: auth
  title: ''
  type: Authentication
  url: authentication/kubeark-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kubeark-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kubeark-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kubeark-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kubeark-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubeark-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kubeark-llms.txt
created: '2026-07-17'
description: 'Kubeark is an enterprise orchestration and AI automation platform that standardizes system integration across hybrid estates. It combines three surfaces: workflow automation, where technical teams and end users build language-agnostic workflows and long-running jobs from a node-based editor; integration, which connects existing systems, SaaS applications, databases and internal APIs through prebuilt connectors and actions; and agentic automation, which deploys autonomous AI agents that can run on-premise for compliance-sensitive environments. The platform operates on two perspectives, a Kubernetes perspective covering clusters, templates and deployments, and a Terraform-centric infrastructure perspective for provisioning. Kubeark bundles its own identity provider, Kubeark Identity, supporting SAML2, LDAP, OAuth2, OIDC and SCIM, plus local and global vaults for secrets. It ships as self-hosted, cloud, hybrid or on-premises software licensed by number of templates and clusters,
  and publishes no public API, OpenAPI description or SDKs.'
image: https://kubeark.com/wp-content/uploads/2025/01/cropped-kubeark-flaticon-270x270.png
layout: provider
modified: '2026-07-19'
name: Kubeark
nav: Providers
network: true
overview: 'Kubeark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Orchestration, Automation, Workflow-Automation, and Integration.


  The Kubeark catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kubeark''s developer surface includes documentation, getting-started guide, engineering blog, support, changelog, authentication, and 15 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 33.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 31.8
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubeark/refs/heads/main/screenshots/kubeark-2026-07-25T224325.png
security:
- kind: authentication
  name: Kubeark Authentication
  slug: kubeark-authentication
  summary_line: openIdConnect/oauth2/saml2/ldap/apiKey · 0 schemes
- kind: domain-security
  name: Kubeark Domain Security
  slug: kubeark-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kubeark
tags:
- Company
- Orchestration
- Automation
- Workflow-Automation
- Integration
- Kubernetes
- Infrastructure as Code
- Terraform
- Identity and Access Management
- Agentic AI
- DevOps
- Self-Hosted
website: https://kubeark.com/
---
