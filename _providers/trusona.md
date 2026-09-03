---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Trusona Agentic Access
  operation_count: 15
  slug: trusona-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 3
apis:
- baseURL: https://authcloud.trusona.net
  baseurl_source: declared
  description: 'REST API to create and read identity verifications: send a hosted scan link by SMS or email, read overall risk, per-verifier checks, risk scores, scanned documents and the devices seen during the veri'
  name: Trusona ATO Protect Verification API
  slug: trusona-ato-protect-verification-api
- baseURL: https://authcloud.trusona.net
  baseurl_source: declared
  description: REST API that submits supplied identity data for asynchronous driver-license verification against State DMV records over AAMVA and against mobile network operator (MNO) records, returning per-field ma
  name: Trusona Driver License Verification API (IDV API)
  slug: trusona-driver-license-verification-api-idv-api
- description: 'Legacy AAMVA identity-document proofing REST surface documented on the Trusona site rather than as an OpenAPI: barcode verifications, verifications, a verification lookup by transaction locator id, a '
  name: Trusona ID Proofing API (v2)
  slug: trusona-id-proofing-api-v2
artifact_total: 10
asyncapis:
- description: ''
  name: Trusona Webhooks
  slug: trusona-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trusona-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trusona-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trusona-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trusona-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.trusona.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.trusona.com/integrations
- group: docs
  title: ''
  type: Documentation
  url: https://www.trusona.com/docs-and-guides
- group: docs
  title: ''
  type: APIReference
  url: https://authcloud.trusona.net/docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.trusona.com/integrations/trusona-id-proofing-integration-guide
- group: operate
  title: ''
  type: Support
  url: https://help.trusona.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.trusona.com/category/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.trusona.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trusona
- group: start
  title: ''
  type: Login
  url: https://dashboard.trusona.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trusona.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trusona.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trusona-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/trusona-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/trusona-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trusona-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trusona-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trusona-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trusona-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.trusona.com/
- group: design
  title: ''
  type: DataModel
  url: data-model/trusona-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trusona-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/trusona-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/trusona-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trusona-rate-limits.yml
created: '2026-09-01'
description: Trusona is a Scottsdale, Arizona identity impersonation detection company founded in 2015 by fraud-prevention expert Ori Eisen, funded by Kleiner Perkins and advised by Frank Abagnale. Its ATO Protect suite verifies that the person behind a help-desk call, account-recovery request, MFA reset, HR onboarding or wire approval is really who they claim to be — checking a government-issued ID against authoritative sources such as State DMVs over the AAMVA network and layering SIM-swap/port-out detection, patented man-in-the-middle detection (US Patent 10,601,859) and anti-replay technology, deliberately without a liveness selfie. Trusona publishes two OpenAPI 3.1 contracts at authcloud.trusona.net — the Verification API (v2.2.0) and the Driver License Verification API (v1.0.0) — a legacy AAMVA ID Proofing v2 REST surface, an Apache-2.0 Claude Agent Skill, an llms.txt, and server/mobile SDKs for Java, Ruby, JavaScript, .NET, C, iOS and Android.
image: https://www.trusona.com/wp-content/uploads/2020/12/Trusona_logomark.png
layout: provider
modified: '2026-09-01'
name: Trusona
nav: Providers
network: true
overview: 'Trusona publishes 2 APIs on the [APIs.io](https://apis.io/) network: ATO Protect Verification API and Driver License Verification API (IDV API). Tagged areas include Company, Authentication, Identity, Identity Verification, and Fraud Detection.


  The Trusona catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trusona''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 23 more developer resources.'
plans:
- name: Trusona Plans Pricing
  plan_count: 0
  slug: trusona-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Trusona Rate Limits
  slug: trusona-rate-limits
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 65.3
    developer_ergonomics: 78.6
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trusona/refs/heads/main/screenshots/trusona-2026-09-02T164411.png
security:
- kind: authentication
  name: Trusona Authentication
  slug: trusona-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trusona Domain Security
  slug: trusona-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trusona Trust Center
  slug: trusona-trust-center
  summary_line: SOC 2
slug: trusona
tags:
- Company
- Authentication
- Identity
- Identity Verification
- Fraud Detection
- Account Takeover
- Security
- Deepfake Detection
- Cybersecurity
- Agent Skills
website: https://www.trusona.com/
---
