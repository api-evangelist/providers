---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://conjur.org'', ''status'': 301, ''note'': ''declared website redirects to https://www.paloaltonetworks.com/idira/machine/secrets-management — a different registrable domain (conjur.org -> paloaltonetworks.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    error_semantics: documented
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
  score: 22.7
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://cyberark.github.io/conjur
  baseurl_source: declared
  description: REST API for authenticating machine and human identities, retrieving and rotating secrets, loading policy-as-code, and inspecting RBAC roles and resources. Compatible with Conjur OSS and CyberArk Secr
  name: Conjur / CyberArk Secrets Manager API
  slug: conjur-cyberark-secrets-manager-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Collection
  slug: open-authentication
- collection_type: open
  name: API Collection
  slug: open-cert-auth
- collection_type: open
  name: API Collection
  slug: open-host-factory
- collection_type: open
  name: API Collection
  slug: open-policies
- collection_type: open
  name: API Collection
  slug: open-public-keys
- collection_type: open
  name: API Collection
  slug: open-resources
- collection_type: open
  name: API Collection
  slug: open-roles
- collection_type: open
  name: API Collection
  slug: open-secrets
- collection_type: open
  name: API Collection
  slug: open-status
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cyberark/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cyberark/conjur/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cyberark/conjur/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cyberark/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cyberark/conjur/blob/master/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://conjur.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cyberark.github.io/conjur/
- group: docs
  title: ''
  type: Documentation
  url: https://cyberark.github.io/conjur/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/cyberark/conjur-openapi-spec
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cyberark
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cyberark/conjur
- group: auth
  title: ''
  type: Authentication
  url: authentication/conjur-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/conjur-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/conjur-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/conjur-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/conjur-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/conjur-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/conjur-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/conjur-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/conjur-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conjur-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/conjur-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conjur-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conjur-domain-security.yml
created: '2026-07-17'
description: Conjur is CyberArk's open-source secrets management platform. It automatically secures secrets used by privileged users and machine identities across CI/CD, cloud, and Kubernetes environments. Conjur uses a role-based access control (RBAC) model, policy-as-code, and pluggable cloud-native authenticators (AWS IAM, Azure, GCP, Kubernetes, JWT, OIDC, LDAP) to issue short-lived access tokens and broker secret retrieval, rotation, and auditing. Originally Conjur Inc. (backed by Amplify Partners), it was acquired by CyberArk and is now part of Palo Alto Networks. The Conjur / CyberArk Secrets Manager REST API is published as an OpenAPI 3.1 definition with official Ruby, Python, Go, Java, and .NET client libraries, a CLI, and an official MCP server.
image: https://avatars.githubusercontent.com/u/30869256?v=4
layout: provider
mcp_servers:
- description: ''
  name: CyberArk Secrets Manager MCP server
  slug: cyberark-secrets-manager-mcp-server
modified: '2026-07-18'
name: Conjur
nav: Providers
network: true
overview: 'Conjur publishes 1 API on the [APIs.io](https://apis.io/) network: / CyberArk Secrets Manager API. Tagged areas include Company, Cybersecurity, Secrets Management, Identity and Access Management, and DevSecOps.


  Conjur''s developer surface includes documentation, API reference, authentication, CLI, changelog, and 20 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -3.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 36.1
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 33.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conjur/refs/heads/main/screenshots/conjur-2026-07-25T210258.png
security:
- kind: authentication
  name: Conjur Authentication
  slug: conjur-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Conjur Domain Security
  slug: conjur-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conjur
tags:
- Company
- Cybersecurity
- Secrets Management
- Identity and Access Management
- DevSecOps
- Kubernetes
- Machine Identity
- Open-Source
website: https://conjur.org
---
