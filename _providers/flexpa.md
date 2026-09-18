---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Flexpa Agentic Access
  operation_count: 15
  slug: flexpa-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.flexpa.com
  baseurl_source: declared
  description: The Access Tokens API from Flexpa — 1 operation(s) for access tokens.
  name: Flexpa Access Tokens API
  slug: flexpa-access-tokens-api
- baseURL: https://api.flexpa.com
  baseurl_source: declared
  description: The Claims Data API from Flexpa — 5 operation(s) for claims data.
  name: Flexpa Claims Data API
  slug: flexpa-claims-data-api
- baseURL: https://api.flexpa.com
  baseurl_source: declared
  description: The FHIR API from Flexpa — 8 operation(s) for fhir.
  name: Flexpa FHIR API
  slug: flexpa-fhir-api
- baseURL: https://api.flexpa.com
  baseurl_source: declared
  description: The Link API from Flexpa — 1 operation(s) for link.
  name: Flexpa Link API
  slug: flexpa-link-api
artifact_total: 20
asyncapis:
- description: ''
  name: Flexpa Webhooks
  slug: flexpa-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flexpa Access Tokens API
  slug: open-flexpa-access-tokens-api
- collection_type: open
  name: Flexpa Access Tokens Claims Data API
  slug: open-flexpa-claims-data-api
- collection_type: open
  name: Flexpa Access Tokens FHIR API
  slug: open-flexpa-fhir-api
- collection_type: open
  name: Flexpa Access Tokens Link API
  slug: open-flexpa-link-api
- collection_type: open
  name: Flexpa API
  slug: open-flexpa
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/capabilities/flexpa-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/flexpa-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/agentic-access/flexpa-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flexpa-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/security/flexpa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flexpa-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/authentication/flexpa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flexpa-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flexpa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flexpa
- group: company
  title: ''
  type: Website
  url: https://www.flexpa.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.flexpa.com/docs
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/plans/flexpa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flexpa-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/rate-limits/flexpa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flexpa-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/finops/flexpa-finops.yml
  title: ''
  type: FinOps
  url: finops/flexpa-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.flexpa.com/blog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/well-known/flexpa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flexpa-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/mcp/flexpa-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/flexpa-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/mcp/flexpa-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/flexpa-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/llms/flexpa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flexpa-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/packages/flexpa-packages.yml
  title: ''
  type: Packages
  url: packages/flexpa-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/packages/flexpa-packages.yml
  title: ''
  type: SDKs
  url: packages/flexpa-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/conventions/flexpa-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flexpa-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/errors/flexpa-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flexpa-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/lifecycle/flexpa-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flexpa-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://flexpastatus.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/changelog/flexpa-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flexpa-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/conformance/flexpa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flexpa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.flexpa.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/security/flexpa-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flexpa-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/scopes/flexpa-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/flexpa-scopes.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/sandbox/flexpa-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/flexpa-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/components/flexpa-components.yml
  title: ''
  type: Components
  url: components/flexpa-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/data-model/flexpa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flexpa-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/asyncapi/flexpa-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/flexpa-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.flexpa.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.flexpa.com/docs/records
- group: start
  title: ''
  type: GettingStarted
  url: https://www.flexpa.com/docs/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.flexpa.com/docs/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flexpa.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.flexpa.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flexpa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flexpa.com/privacy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/flexpa
created: '2026-06-21'
description: Flexpa is a patient-access platform that lets applications connect a patient to their health insurance plan and retrieve claims and clinical data as normalized FHIR R4 resources. Patients authorize access through Flexpa Link / OAuth 2.0 PKCE, and applications read ExplanationOfBenefit, Coverage, Patient, and other resources from a single FHIR API at https://api.flexpa.com.
finops:
- name: Flexpa Finops
  service_category: Healthcare
  slug: flexpa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flexpa.png
layout: provider
mcp_servers:
- description: ''
  name: Flexpa MCP Server
  slug: flexpa-mcp-server
modified: '2026-08-14'
name: Flexpa
nav: Providers
network: true
overview: 'Flexpa publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Access Tokens API, Claims Data API, FHIR API, and 1 more. Tagged areas include Healthcare, FHIR, Patient Access, Claims Data, and Health Insurance.


  The Flexpa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flexpa''s developer surface includes authentication, documentation, engineering blog, changelog, sandbox, API reference, getting-started guide, and 34 more developer resources.'
plans:
- name: Flexpa Plans Pricing
  plan_count: 5
  slug: flexpa-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Flexpa Rate Limits
  slug: flexpa-rate-limits
scopes:
- name: Flexpa Scopes
  scope_count: 0
  slug: flexpa-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 56.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 72.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/flexpa/refs/heads/main/screenshots/flexpa-2026-07-25T214752.png
security:
- kind: authentication
  name: Flexpa Authentication
  slug: flexpa-authentication
  summary_line: oauth2/http/apiKey · 3 schemes
- kind: domain-security
  name: Flexpa Domain Security
  slug: flexpa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flexpa Trust Center
  slug: flexpa-trust-center
  summary_line: SOC 2 (published as "SOC II"), HIPAA, CARIN Alliance Code of Conduct
slug: flexpa
tags:
- Healthcare
- FHIR
- Patient Access
- Claims Data
- Health Insurance
website: https://www.flexpa.com
---
