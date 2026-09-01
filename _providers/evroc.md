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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/evroc-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://evroc.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.evroc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evroc.com/introduction.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.evroc.com/apis/compute.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.evroc.com/gettingstarted.html
- group: operate
  title: ''
  type: Support
  url: https://docs.evroc.com/support.html
- group: company
  title: ''
  type: Blog
  url: https://evroc.com/developer/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evroc-oss
- group: operate
  title: ''
  type: StatusPage
  url: https://status.evroc.com/
- group: start
  title: ''
  type: SignUp
  url: https://signup.evroc.com/
- group: start
  title: ''
  type: Login
  url: https://cloud.evroc.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evroc.com/legal/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evroc.com/legal/privacy-notice
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.evroc.com/changelog.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/evroc-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evroc-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/evroc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/evroc-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/evroc-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evroc-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.evroc.com/changelog.html
- group: design
  title: ''
  type: Conventions
  url: conventions/evroc-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evroc-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://evroc.com/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evroc-domain-security.yml
created: '2026-07-17'
description: evroc is a European sovereign cloud provider headquartered in Stockholm, Sweden, building cloud infrastructure for the AI era for organizations that require the highest level of data security and European data residency. Its platform spans Compute (virtual machines, disks, snapshots, placement groups), Networking (VPCs, subnets, public IPs, security groups, IPv6, load balancers), Storage (S3-compatible object storage and file store), IAM (organizations, projects, service accounts, and a fine-grained RoleBindings permission system), Quotas, and Think (shared and dedicated AI-model inference). Developers reach the platform through a web console, a REST API with Bearer/OIDC access tokens, an official Go SDK, a Terraform provider, a Kubernetes CSI driver, and the evroc CLI. The company emphasizes European sovereignty, sustainability, and security, operating from the Stockholm (se-sto) region.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/evroc.png
layout: provider
modified: '2026-07-19'
name: evroc
nav: Providers
network: true
overview: 'evroc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Computing, Sovereign Cloud, Infrastructure, and Object Storage.


  evroc''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 19 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 36.9
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evroc/refs/heads/main/screenshots/evroc-2026-07-25T213819.png
security:
- kind: authentication
  name: Evroc Authentication
  slug: evroc-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Evroc Domain Security
  slug: evroc-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Evroc Trust Center
  slug: evroc-trust-center
  summary_line: ISO 27001, GDPR
slug: evroc
tags:
- Company
- Cloud Computing
- Sovereign Cloud
- Infrastructure
- Object Storage
- Compute
- AI Infrastructure
- GPU
- Europe
- Infrastructure-as-a-Service
website: https://evroc.com/
---
