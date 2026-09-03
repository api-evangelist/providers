---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - '{''url'': ''https://venafi.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.paloaltonetworks.com/network-security/next-gen-trust-security/certificate-manager — a different registrable domain (venafi.com -> paloaltonetworks.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Venafi / CyberArk Certificate Manager - SaaS REST API. 184 operations across 120 paths covering certificate inventory and search, certificate requests and issuing templates, applications, machines
  name: Certificate Manager - SaaS API (Venafi Control Plane)
  slug: certificate-manager-saas
- baseURL: https://{dnsname}/
  baseurl_source: declared
  description: The self-hosted Venafi / CyberArk Trust Protection Foundation Web SDK, version 26.1.1. 388 operations across 364 paths covering certificate management, discovery, identity and permissions, OAuth appli
  name: Trust Protection Foundation WebSDK (Venafi Trust Protection Platform)
  slug: trust-protection-foundation-websdk
artifact_total: 8
asyncapis:
- description: ''
  name: Venafi Certificate Manager Saas Webhooks
  slug: venafi-certificate-manager-saas-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/venafi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/venafi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://venafi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.venafi.com/tlsprotectcloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.venafi.cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.venafi.com/tlsprotectcloud/reference/tls-protect-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.venafi.cloud/api/api-setup/
- group: operate
  title: ''
  type: Support
  url: https://community.cyberark.com/s/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Venafi
- group: start
  title: ''
  type: SignUp
  url: https://login.venafi.cloud/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.venafi.cloud/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.venafi.cloud/whatsnew/
- group: build
  title: ''
  type: Packages
  url: packages/venafi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/venafi-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/venafi-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/venafi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/venafi-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/venafi-certificate-manager-saas-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/venafi-trust-protection-foundation-websdk-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/venafi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/venafi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/venafi-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/venafi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/venafi-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/venafi-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/venafi-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/venafi-certificate-manager-saas-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/venafi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/venafi-rate-limits.yml
created: '2026-09-02'
description: 'Venafi is the machine identity security platform for discovering, issuing, provisioning and retiring TLS/SSL certificates, SSH keys, code-signing keys and workload identities across data centers, clouds and Kubernetes. Its Control Plane ships two public REST contracts: the SaaS "Certificate Manager - SaaS" API on api.venafi.cloud (six data-residency regions) and the self-hosted Trust Protection Foundation WebSDK. Venafi was acquired by CyberArk in 2024 and the products now carry CyberArk Certificate Manager branding; venafi.com itself 301s to Palo Alto Networks following its acquisition of CyberArk, while developer.venafi.com, docs.venafi.com, docs.venafi.cloud, api.venafi.cloud and github.com/Venafi remain live and are where every artifact in this profile came from.'
image: https://avatars.githubusercontent.com/u/7817722?v=4
layout: provider
modified: '2026-09-02'
name: Venafi
nav: Providers
network: true
overview: 'Venafi publishes 2 APIs on the [APIs.io](https://apis.io/) network: Certificate Manager - SaaS API (Venafi Control Plane) and Trust Protection Foundation WebSDK (Venafi Trust Protection Platform). Tagged areas include Company, Security, Certificates, PKI, and Machine Identity.


  The Venafi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Venafi''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, changelog, and 23 more developer resources.'
plans:
- name: Venafi Plans Pricing
  plan_count: 0
  slug: venafi-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Venafi Rate Limits
  slug: venafi-rate-limits
scopes:
- name: Venafi Scopes
  scope_count: 0
  slug: venafi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 60.0
    developer_ergonomics: 70.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 46.6
  provenance:
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Venafi Authentication
  slug: venafi-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Venafi Domain Security
  slug: venafi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: venafi
tags:
- Company
- Security
- Certificates
- PKI
- Machine Identity
- Identity
- Cryptography
- Key Management
- Certificate Lifecycle Management
- DevOps
- Kubernetes
- Code Signing
website: https://venafi.com/
---
