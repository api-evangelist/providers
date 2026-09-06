---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Xbow Agentic Access
  operation_count: 40
  slug: xbow-agentic-access
  summary_line: 40 operations · 21 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://console.xbow.com/api/v1
  baseurl_source: declared
  description: Endpoints related to assessments for assets. All endpoints require an _organization_ API key.
  name: Xbow Assessments API
  slug: xbow-assessments-api
- baseURL: https://console.xbow.com/api/v1
  baseurl_source: declared
  description: Endpoints related to assets within an organization. All endpoints require an _organization_ API key.
  name: Xbow Assets API
  slug: xbow-assets-api
- baseURL: https://console.xbow.com/api/v1
  baseurl_source: declared
  description: Endpoints for viewing and managing findings. All endpoints require an _organization_ API key.
  name: Xbow Findings API
  slug: xbow-findings-api
- baseURL: https://console.xbow.com/api/v1
  baseurl_source: declared
  description: Endpoints related to Lightspeed assessment requests.
  name: Xbow Lightspeed API
  slug: xbow-lightspeed-api
- baseURL: https://console.xbow.com/api/v1
  baseurl_source: declared
  description: Instance metadata endpoints.
  name: Xbow Meta API
  slug: xbow-meta-api
- baseURL: https://console.xbow.com/api/v1
  baseurl_source: declared
  description: Endpoints related to organizations and their management.
  name: Xbow Organizations API
  slug: xbow-organizations-api
- baseURL: https://console.xbow.com/api/v1
  baseurl_source: declared
  description: Endpoints for downloading and viewing reports. All endpoints require an _organization_ API key.
  name: Xbow Reports API
  slug: xbow-reports-api
- baseURL: https://console.xbow.com/api/v1
  baseurl_source: declared
  description: 'Upload and manage files used in assessments, such as source code archives. All endpoints require an _organization_ API key. ## Upload flow Resources use a multipart S3 upload. The full flow is: 1. **C'
  name: Xbow Resources API
  slug: xbow-resources-api
- baseURL: https://console.xbow.com/api/v1
  baseurl_source: declared
  description: Manage webhook subscriptions and receive event notifications. When creating an organization, you may provide an HTTPS webhook URL to receive events related to the organization's resources. We implemen
  name: Xbow Webhooks API
  slug: xbow-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Xbow Webhooks
  slug: xbow-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: XBOW Assessments API
  slug: open-xbow-assessments-api
- collection_type: open
  name: XBOW Assessments Assets API
  slug: open-xbow-assets-api
- collection_type: open
  name: XBOW Assessments Findings API
  slug: open-xbow-findings-api
- collection_type: open
  name: XBOW Assessments Lightspeed API
  slug: open-xbow-lightspeed-api
- collection_type: open
  name: XBOW Assessments Meta API
  slug: open-xbow-meta-api
- collection_type: open
  name: XBOW Assessments Organizations API
  slug: open-xbow-organizations-api
- collection_type: open
  name: XBOW Assessments Reports API
  slug: open-xbow-reports-api
- collection_type: open
  name: XBOW Assessments Resources API
  slug: open-xbow-resources-api
- collection_type: open
  name: XBOW Assessments Webhooks API
  slug: open-xbow-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/xbow-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xbow-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/xbow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xbow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xbow-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://xbow.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.xbow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xbow.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.xbow.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.xbow.com/console/get-started/introduction/
- group: operate
  title: ''
  type: Support
  url: mailto:support@xbow.com
- group: company
  title: ''
  type: Blog
  url: https://xbow.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xbow-engineering
- group: commercial
  title: ''
  type: Pricing
  url: https://xbow.com/pricing
- group: start
  title: ''
  type: Login
  url: https://console.xbow.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xbow.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xbow.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xbow.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.xbow.com/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.xbow.com/console/get-started/trust-and-safety/
- group: auth
  title: ''
  type: Security
  url: https://xbow.com/security-policy
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.xbow.com/api/#description/version-lifecycle
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xbow-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/xbow-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/xbow-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/xbow-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xbow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xbow-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xbow-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xbow-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xbow-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'XBOW is an autonomous offensive security platform that uses AI to perform penetration testing with real exploit validation — it identifies vulnerabilities, chains them into attack paths, and proves exploitability before findings reach security teams. The XBOW API (public preview) exposes the full platform workflow: register assets, launch and manage assessments, fetch validated findings and reports, upload source-code resources for gray-box testing, and subscribe webhooks with Ed25519-signed deliveries. XBOW has ranked #1 on the HackerOne and Microsoft MSRC leaderboards and is used by 150+ security teams.'
image: https://docs.xbow.com/xbow-logomark.svg
layout: provider
modified: '2026-07-21'
name: Xbow
nav: Providers
network: true
overview: 'Xbow publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Assessments API, Assets API, Findings API, and 6 more. Tagged areas include Security, Penetration Testing, Offensive Security, Artificial Intelligence, and Vulnerability Management.


  The Xbow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Xbow''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 61.2
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 60.5
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xbow/refs/heads/main/screenshots/xbow-2026-08-17T083001.png
security:
- kind: authentication
  name: Xbow Authentication
  slug: xbow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Xbow Domain Security
  slug: xbow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Xbow Vulnerability Disclosure
  slug: xbow-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Xbow Trust Center
  slug: xbow-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, GDPR, HIPAA
slug: xbow
tags:
- Security
- Penetration Testing
- Offensive Security
- Artificial Intelligence
- Vulnerability Management
- Cybersecurity
- Application Security
website: https://xbow.com
---
