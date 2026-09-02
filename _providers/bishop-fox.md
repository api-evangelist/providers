---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 18.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Authenticated REST API for the Bishop Fox Cosmos attack-surface management platform. Exposes the customer's discovered asset inventory through /v5/asset-view/* resources (domains, subdomains, dns-reco
  name: Bishop Fox Cosmos API (v5)
  slug: bishop-fox-cosmos-api-v5
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://bishopfox.com/
- group: start
  title: ''
  type: Portal
  url: https://cosmos.bishopfox.com/
- group: start
  title: ''
  type: Login
  url: https://cosmos.bishopfox.com/
- group: company
  title: ''
  type: Blog
  url: https://bishopfox.com/blog
- group: operate
  title: ''
  type: Support
  url: https://bishopfox.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BishopFox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bishopfox.com/privacy-statement
- group: auth
  title: ''
  type: Security
  url: https://bishopfox.com/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bishop-fox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bishop-fox-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bishop-fox-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bishop-fox-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bishop-fox-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bishop-fox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bishop-fox-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bishop-fox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bishop-fox-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bishop-fox-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bishop-fox-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bishop-fox-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/bishop-fox-packages.yml
- group: build
  title: ''
  type: OpenSourceTools
  url: https://bishopfox.com/tools
created: '2026-08-02'
description: Bishop Fox is an offensive security firm delivering penetration testing, red teaming, application and cloud security assessment, and continuous threat exposure management. Its managed Cosmos platform keeps a living inventory of an organization's external attack surface — domains, subdomains, DNS records, network ranges, IP addresses, open ports, and IP/hostname services — pairing continuous automated discovery with human operator validation so customers receive triaged, exploitable findings instead of scanner noise. Customers consume Cosmos data programmatically through the authenticated Cosmos v5 REST API at api.cosmos.bishopfox.com, secured with OAuth 2.0 client-credentials tokens issued by Bishop Fox's Auth0 tenant against the cosmos_public audience, and through bi-directional Jira and ServiceNow integrations plus AWS, GCP, Azure, Cloudflare, and Oracle cloud connectors. Bishop Fox also publishes a widely used open-source offensive-security toolkit — Sliver, CloudFox, sj
  (Swagger Jacker), jsluice, and aimap — from its GitHub organization.
image: https://assets.bishopfox.com/prod-1437/Images/og/_1200x630_crop_center-center_82_none/services-v1.jpg
layout: provider
modified: '2026-08-02'
name: Bishop Fox
nav: Providers
network: true
overview: 'Bishop Fox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Offensive Security, Penetration Testing, and Attack Surface Management.


  Bishop Fox''s developer surface includes developer portal, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 15
scopes:
- name: Bishop Fox Scopes
  scope_count: 7
  slug: bishop-fox-scopes
  summary_line: 7 scopes · clientCredentials
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 20.3
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bishop-fox/refs/heads/main/screenshots/bishop-fox-2026-08-07T162514.png
security:
- kind: authentication
  name: Bishop Fox Authentication
  slug: bishop-fox-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Bishop Fox Domain Security
  slug: bishop-fox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bishop Fox Vulnerability Disclosure
  slug: bishop-fox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bishop-fox
tags:
- Company
- Cybersecurity
- Offensive Security
- Penetration Testing
- Attack Surface Management
- Exposure Management
- Red Teaming
- Vulnerability Management
- Security Findings
- Asset Discovery
- Continuous Threat Exposure Management
- Authentication
website: https://bishopfox.com/
---
