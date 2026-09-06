---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://kondukto.io'', ''status'': 301, ''note'': ''declared website redirects to https://www.invicti.com/ — a different registrable domain (kondukto.io -> invicti.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Kondukto Agentic Access
  operation_count: 51
  slug: kondukto-agentic-access
  summary_line: 51 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Authorization Managers API from Kondukto — 1 operation(s) for authorization managers.
  name: Kondukto Authorization Managers API
  slug: kondukto-authorization-managers-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Events API from Kondukto — 1 operation(s) for events.
  name: Kondukto Events API
  slug: kondukto-events-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Health API from Kondukto — 1 operation(s) for health.
  name: Kondukto Health API
  slug: kondukto-health-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Labels API from Kondukto — 3 operation(s) for labels.
  name: Kondukto Labels API
  slug: kondukto-labels-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Products API from Kondukto — 2 operation(s) for products.
  name: Kondukto Products API
  slug: kondukto-products-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Projects API from Kondukto — 7 operation(s) for projects.
  name: Kondukto Projects API
  slug: kondukto-projects-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Scanners API from Kondukto — 1 operation(s) for scanners.
  name: Kondukto Scanners API
  slug: kondukto-scanners-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Scans API from Kondukto — 10 operation(s) for scans.
  name: Kondukto Scans API
  slug: kondukto-scans-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Teams API from Kondukto — 5 operation(s) for teams.
  name: Kondukto Teams API
  slug: kondukto-teams-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Users API from Kondukto — 2 operation(s) for users.
  name: Kondukto Users API
  slug: kondukto-users-api
- baseURL: https://api.kondukto.io/api/v2
  baseurl_source: declared
  description: The Vulnerabilities API from Kondukto — 9 operation(s) for vulnerabilities.
  name: Kondukto Vulnerabilities API
  slug: kondukto-vulnerabilities-api
artifact_total: 41
asyncapis:
- description: ''
  name: Kondukto Webhooks
  slug: kondukto-webhooks
collections:
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers API
  slug: postman-kondukto-authorization-managers-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Events API
  slug: postman-kondukto-events-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Health API
  slug: postman-kondukto-health-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Labels API
  slug: postman-kondukto-labels-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Products API
  slug: postman-kondukto-products-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Projects API
  slug: postman-kondukto-projects-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Scanners API
  slug: postman-kondukto-scanners-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Scans API
  slug: postman-kondukto-scans-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Teams API
  slug: postman-kondukto-teams-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Users API
  slug: postman-kondukto-users-api
- collection_type: postman
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Vulnerabilities API
  slug: postman-kondukto-vulnerabilities-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers API
  slug: open-kondukto-authorization-managers-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Events API
  slug: open-kondukto-events-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Health API
  slug: open-kondukto-health-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Labels API
  slug: open-kondukto-labels-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Products API
  slug: open-kondukto-products-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Projects API
  slug: open-kondukto-projects-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Scanners API
  slug: open-kondukto-scanners-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Scans API
  slug: open-kondukto-scans-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Teams API
  slug: open-kondukto-teams-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Users API
  slug: open-kondukto-users-api
- collection_type: open
  name: Invicti ASPM (Kondukto) REST API v2 Authorization Managers Vulnerabilities API
  slug: open-kondukto-vulnerabilities-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kondukto-aspm-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kondukto/overview
- group: company
  title: ''
  type: Website
  url: https://kondukto.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kondukto.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kondukto.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kondukto.io/reference/starting-with-kondukto-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kondukto.io/reference/starting-with-kondukto-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kondukto-io
- group: company
  title: ''
  type: Blog
  url: https://www.invicti.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.invicti.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.invicti.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.invicti.com/get-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.invicti.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.invicti.com/compliance/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.invicti.com
- group: auth
  title: ''
  type: Security
  url: https://www.invicti.com/.well-known/security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.invicti.com/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/kondukto-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kondukto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kondukto-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kondukto-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kondukto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kondukto-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kondukto-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kondukto-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kondukto-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kondukto-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kondukto-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kondukto-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kondukto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kondukto-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kondukto-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kondukto-plans.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kondukto-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kondukto-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kondukto-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kondukto-agentic-access.yml
created: '2026-07-17'
description: Kondukto — now shipped as Invicti ASPM following Invicti Security's acquisition of the company — is an Application Security Posture Management platform that centralizes and automates the AppSec vulnerability management lifecycle. It ingests, deduplicates and correlates findings from more than eighty security scanners across SAST, DAST, SCA, container, infrastructure and pentest testing, enriches them with CWE, CVSS, EPSS, CISA KEV, EUVD threat intelligence and VEX exploitability data, and routes them to owning teams through Jira, GitLab, ServiceNow and webhook issue managers. Kondukto publishes a documented REST API v2 covering projects, products, teams, labels, scans and vulnerabilities, an open-source Go command-line client (KDT) that drives the same API from CI/CD pipelines, and a webhook surface for both outbound platform events and customer-hosted issue managers. The platform is deployed per customer, so the API host is deployment-specific.
image: https://cdn.kondukto.io/img/logo/a990cbe5-f31f-49a0-a135-2ea0b7abb0ec.png
layout: provider
modified: '2026-07-19'
name: Kondukto
nav: Providers
network: true
overview: 'Kondukto publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authorization Managers API, Events API, Health API, and 8 more. Tagged areas include Company, Application Security, ASPM, Vulnerability Management, and DevSecOps.


  The Kondukto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kondukto''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Kondukto Plans
  plan_count: 2
  slug: kondukto-plans
random_paper: 18
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 4.5
    contract_quality: 64.4
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 58.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kondukto/refs/heads/main/screenshots/kondukto-2026-07-25T224148.png
security:
- kind: authentication
  name: Kondukto Authentication
  slug: kondukto-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kondukto Domain Security
  slug: kondukto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kondukto Vulnerability Disclosure
  slug: kondukto-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kondukto Trust Center
  slug: kondukto-trust-center
  summary_line: SOC 2 Type 2, ISO 27001:2025
slug: kondukto
tags:
- Company
- Application Security
- ASPM
- Vulnerability Management
- DevSecOps
- Security Orchestration
- SAST
- DAST
- SCA
- Software Composition Analysis
- Container Security
- SBOM
- Security Testing
- CI/CD
- Security
website: https://kondukto.io
---
