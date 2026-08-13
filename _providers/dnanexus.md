---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: The DNAnexus Platform API is a JSON-over-HTTPS API of roughly 206 documented methods. Each method is invoked with an HTTP POST to a route of the form /class-xxxx/method (for example /file-xxxx/describ
  name: DNAnexus Platform API
  slug: dnanexus-platform-api
- description: DNAnexus operates an OpenID Connect provider that lets third-party web applications sign users in with their DNAnexus Platform credentials. The provider publishes an OIDC discovery document at https:/
  name: DNAnexus OpenID Connect Provider
  slug: dnanexus-openid-connect-provider
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.dnanexus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.dnanexus.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.dnanexus.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.dnanexus.com/developer/api/api-directory
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.dnanexus.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://community.dnanexus.com/s/
- group: company
  title: ''
  type: Blog
  url: https://blog.dnanexus.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.dnanexus.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dnanexus
- group: start
  title: ''
  type: Console
  url: https://platform.dnanexus.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://academy.dnanexus.com/billing-access-and-orgs/billing_and_pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.dnanexus.com/register
- group: start
  title: ''
  type: Login
  url: https://platform.dnanexus.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dnanexus.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dnanexus.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dnanexus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dnanexus-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://documentation.dnanexus.com/release-notes
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dnanexus-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dnanexus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dnanexus-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dnanexus-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/dnanexus-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dnanexus-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dnanexus-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/dnanexus-job-failure-reasons.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dnanexus-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/dnanexus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dnanexus-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dnanexus-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dnanexus-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dnanexus-security.txt
- group: auth
  title: ''
  type: Security
  url: https://trust.dnanexus.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dnanexus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dnanexus-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dnanexus.com/platform-security-compliance
- group: design
  title: ''
  type: Conformance
  url: conformance/dnanexus-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dnanexus-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dnanexus-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: DNAnexus operates a cloud-based precision health data platform for genomic and multi-omic research, clinical testing and biopharma R&D. The DNAnexus Platform exposes a documented HTTP API of roughly 206 JSON-over-HTTPS methods at api.dnanexus.com covering projects and data containers, files and other data objects, apps, applets, workflows and analyses, jobs and execution containers, organizations and users, the Omics Data Catalog, and Trusted Research Environments (TREs) with data access requests. Every call is an HTTP POST with a JSON body, authenticated with a bearer token, versioned through an optional DNAnexus-API header, and made idempotent through a documented nonce field on object- and job-creation methods. First-party client libraries ship for Python (dxpy), Java, Scala and C++, alongside the dx command-line client, dxfuse and dxda, and the platform is an OpenID Connect provider for third-party sign-in and for job identity tokens.
image: https://www.dnanexus.com/hubfs/DNAnexus/Resources/DNAnexus_logo_headers-1.png
layout: provider
modified: '2026-08-04'
name: DNAnexus
nav: Providers
network: true
overview: 'DNAnexus publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Bioinformatics, Life Sciences, and Healthcare.


  DNAnexus'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, developer console, pricing, and 33 more developer resources.'
random_paper: 30
rate_limits:
- limit_count: 8
  name: Dnanexus Rate Limits
  slug: dnanexus-rate-limits
scopes:
- name: Dnanexus Scopes
  scope_count: 4
  slug: dnanexus-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 50.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 73.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 78.9
  previous_composite: 50.1
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dnanexus/refs/heads/main/screenshots/dnanexus-2026-08-07T164443.png
security:
- kind: authentication
  name: Dnanexus Authentication
  slug: dnanexus-authentication
  summary_line: http/openIdConnect · 3 schemes
- kind: domain-security
  name: Dnanexus Domain Security
  slug: dnanexus-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dnanexus Vulnerability Disclosure
  slug: dnanexus-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dnanexus Trust Center
  slug: dnanexus-trust-center
  summary_line: ISO 27001, FedRAMP, GovRAMP, Cyber Essentials, Cyber Essentials Plus, HIPAA, PCI, EU-U.S. Data Privacy Framework, EcoVadis
slug: dnanexus
tags:
- Company
- Genomics
- Bioinformatics
- Life Sciences
- Healthcare
- Cloud Computing
- Data Platform
- Scientific Computing
- Precision Medicine
- Clinical Research
website: https://www.dnanexus.com/
---
