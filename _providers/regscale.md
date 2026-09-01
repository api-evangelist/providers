---
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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: The RegScale REST API is the primary programmable surface of the RegScale platform. It is served from each customer's own RegScale tenant under the /api path, authenticated with a JSON Web Token obtai
  name: RegScale REST API
  slug: regscale-rest-api
- description: RegScale exposes a GraphQL endpoint at /graphql on each customer tenant, used by the first-party RegScale CLI for high-volume paginated reads. Queries follow the HotChocolate connection shape - items,
  name: RegScale GraphQL API
  slug: regscale-graphql-api
- description: 'RegScale publishes a gRPC contract library, rs-data, covering three high-volume ingestion services: AssetIngestionService, IssueIngestionService and VulnIngestionService. Each service exposes a unary '
  name: RegScale gRPC Ingestion Services
  slug: regscale-grpc-ingestion
artifact_total: 10
asyncapis:
- description: ''
  name: Regscale Webhooks
  slug: regscale-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regscale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://regscale.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://regscale.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://regscale.readme.io/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://regscale.readme.io/docs/overview
- group: operate
  title: ''
  type: Support
  url: https://regscale.readme.io/docs/opening-tickets
- group: docs
  title: ''
  type: APIReference
  url: https://regscale.readme.io/reference/regscale-api-documentation
- group: company
  title: ''
  type: Blog
  url: https://regscale.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RegScale
- group: commercial
  title: ''
  type: TermsOfService
  url: https://regscale.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://regscale.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://regscale.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.regscale.com/
- group: auth
  title: ''
  type: Compliance
  url: https://regscale.com/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://regscale.readme.io/changelog
- group: build
  title: ''
  type: Packages
  url: packages/regscale-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/regscale-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/regscale-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/regscale-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/regscale-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/regscale-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/regscale-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/regscale-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/regscale-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/regscale-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/regscale-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/regscale-plans-pricing.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/regscale-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/regscale-trust-center.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/regscale-conventions.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/regscale-asset-service.proto
- group: design
  title: ''
  type: Webhooks
  url: https://regscale.readme.io/docs/webhooks
created: '2026-08-26'
description: 'RegScale is a Continuous Controls Monitoring (CCM) and compliance-automation company whose cloud-native, OSCAL-native GRC platform keeps organizations continuously audit-ready by turning compliance documentation into living, machine-readable data. The platform ships as a customer-tenanted deployment (SaaS, hybrid, or on-premises) and exposes its data through three programmable surfaces: a JWT-authenticated REST API under /api, a HotChocolate-style GraphQL endpoint at /graphql, and a published gRPC contract library (rs-data) covering asset, issue and vulnerability ingestion. RegScale also publishes a first-party Python CLI/SDK (regscale-cli) that doubles as an integration framework for 70+ scanners, cloud providers and ITSM tools, and holds FedRAMP High, SOC 2 Type 2, ISO 27001:2022, TX-RAMP Level 2 and CSA STAR credentials.'
image: https://regscale.com/wp-content/uploads/2024/04/cropped-Regscale-Favicon-192x192.png
layout: provider
modified: '2026-08-26'
name: RegScale
nav: Providers
network: true
overview: 'RegScale publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, Governance Risk and Compliance, Continuous Controls Monitoring, and Security.


  The RegScale catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RegScale''s developer surface includes documentation, getting-started guide, support, API reference, engineering blog, changelog, CLI, and 25 more developer resources.'
plans:
- name: Regscale Plans Pricing
  plan_count: 0
  slug: regscale-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Regscale Rate Limits
  slug: regscale-rate-limits
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 51.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 66.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Regscale Authentication
  slug: regscale-authentication
  summary_line: http/oauth2/openIdConnect/saml · 4 schemes
- kind: domain-security
  name: Regscale Domain Security
  slug: regscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Regscale Vulnerability Disclosure
  slug: regscale-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Regscale Trust Center
  slug: regscale-trust-center
  summary_line: FedRAMP High, SOC 2 Type 2, ISO 27001:2022, TX-RAMP Level 2, CSA STAR Level 1, CSA STAR Valid-AI-ted, DoD IL5 (in process), HIPAA, GDPR
slug: regscale
tags:
- Company
- Compliance
- Governance Risk and Compliance
- Continuous Controls Monitoring
- Security
- FedRAMP
- OSCAL
- Risk Management
- Audit
- Compliance as Code
- Vulnerability Management
- Government
website: https://regscale.com/
---
