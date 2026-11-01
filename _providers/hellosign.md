---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Hellosign Agentic Access
  operation_count: 73
  slug: hellosign-agentic-access
  summary_line: 73 operations · 46 acting
api_count: 1
apis:
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/account-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Account API
  slug: hellosign-account-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/api-app-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Api App API
  slug: hellosign-api-app-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/bulk-send-job-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Bulk Send Job API
  slug: hellosign-bulk-send-job-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/embedded-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Embedded API
  slug: hellosign-embedded-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: The Fax API from Dropbox Sign (HelloSign) — 4 operation(s) for fax.
  name: Dropbox Sign (HelloSign) Fax API
  slug: hellosign-fax-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/fax-lines-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Fax Line API
  slug: hellosign-fax-line-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/report-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Report API
  slug: hellosign-report-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/signature-request-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Signature Request API
  slug: hellosign-signature-request-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/team-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Team API
  slug: hellosign-team-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/template-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Template API
  slug: hellosign-template-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/unclaimed-draft-tag-description.md''}'
  name: Dropbox Sign (HelloSign) Unclaimed Draft API
  slug: hellosign-unclaimed-draft-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: The Callbacks and Events API from Dropbox Sign (HelloSign) — 0 operation(s) for callbacks and events.
  name: Dropbox Sign (HelloSign) Callbacks and Events API
  slug: hellosign-callbacks-and-events-api
- baseURL: https://api.hellosign.com/v3
  baseurl_source: declared
  description: '{''$ref'': ''./markdown/en/tags/oauth-tag-description.md''}'
  name: Dropbox Sign (HelloSign) O Auth API
  slug: hellosign-oauth-api
artifact_total: 52
asyncapis:
- description: 'AsyncAPI description of the Dropbox Sign (formerly HelloSign) outbound event / callback surface. Dropbox Sign delivers event notifications by issuing HTTP POST requests to a subscriber-configured URL '
  name: Dropbox Sign Events and Callbacks
  slug: hellosign-events-asyncapi
- description: ''
  name: Hellosign Events Webhooks
  slug: hellosign-events-webhooks
collections:
- collection_type: postman
  name: Dropbox Sign Account API
  slug: postman-hellosign-account-api
- collection_type: postman
  name: Dropbox Sign Account Api App API
  slug: postman-hellosign-api-app-api
- collection_type: postman
  name: Dropbox Sign Account Bulk Send Job API
  slug: postman-hellosign-bulk-send-job-api
- collection_type: postman
  name: Dropbox Sign Account Embedded API
  slug: postman-hellosign-embedded-api
- collection_type: postman
  name: Dropbox Sign Account Fax API
  slug: postman-hellosign-fax-api
- collection_type: postman
  name: Dropbox Sign Account Fax Line API
  slug: postman-hellosign-fax-line-api
- collection_type: postman
  name: Dropbox Sign Account OAuth API
  slug: postman-hellosign-oauth-api
- collection_type: postman
  name: Dropbox Sign Account Report API
  slug: postman-hellosign-report-api
- collection_type: postman
  name: Dropbox Sign Account Signature Request API
  slug: postman-hellosign-signature-request-api
- collection_type: postman
  name: Dropbox Sign Account Team API
  slug: postman-hellosign-team-api
- collection_type: postman
  name: Dropbox Sign Account Template API
  slug: postman-hellosign-template-api
- collection_type: postman
  name: Dropbox Sign Account Unclaimed Draft API
  slug: postman-hellosign-unclaimed-draft-api
- collection_type: open
  name: Dropbox Sign Account API
  slug: open-hellosign-account-api
- collection_type: open
  name: Dropbox Sign Account Api App API
  slug: open-hellosign-api-app-api
- collection_type: open
  name: Dropbox Sign Account Bulk Send Job API
  slug: open-hellosign-bulk-send-job-api
- collection_type: open
  name: Dropbox Sign Account Embedded API
  slug: open-hellosign-embedded-api
- collection_type: open
  name: Dropbox Sign Account Fax API
  slug: open-hellosign-fax-api
- collection_type: open
  name: Dropbox Sign Account Fax Line API
  slug: open-hellosign-fax-line-api
- collection_type: open
  name: Dropbox Sign Account OAuth API
  slug: open-hellosign-oauth-api
- collection_type: open
  name: Dropbox Sign Account Report API
  slug: open-hellosign-report-api
- collection_type: open
  name: Dropbox Sign Account Signature Request API
  slug: open-hellosign-signature-request-api
- collection_type: open
  name: Dropbox Sign Account Team API
  slug: open-hellosign-team-api
- collection_type: open
  name: Dropbox Sign Account Template API
  slug: open-hellosign-template-api
- collection_type: open
  name: Dropbox Sign Account Unclaimed Draft API
  slug: open-hellosign-unclaimed-draft-api
common:
- group: commercial
  href: https://artifacts.apis.io/hellosign/plans/hellosign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hellosign-plans-pricing.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dropboxsign
- group: company
  title: ''
  type: Blog
  url: https://sign.dropbox.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.hellosign.com/llms.txt
- group: other
  href: https://artifacts.apis.io/hellosign/capabilities/hellosign-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hellosign-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://hellosign.com
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/dropbox/
- group: other
  href: https://artifacts.apis.io/hellosign/overlays/hellosign-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hellosign-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dropbox-sign-hellosign/overview
- group: agent
  href: https://artifacts.apis.io/hellosign/agentic-access/hellosign-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hellosign-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/hellosign/security/hellosign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hellosign-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hellosign/authentication/hellosign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hellosign-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hellosign/scopes/hellosign-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hellosign-scopes.yml
- group: agent
  href: https://artifacts.apis.io/hellosign/mcp/hellosign-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hellosign-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hellosign/llms/hellosign-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hellosign-llms.txt
- group: build
  href: https://artifacts.apis.io/hellosign/packages/hellosign-packages.yml
  title: ''
  type: Packages
  url: packages/hellosign-packages.yml
- group: build
  href: https://artifacts.apis.io/hellosign/packages/hellosign-packages.yml
  title: ''
  type: SDKs
  url: packages/hellosign-packages.yml
- group: design
  href: https://artifacts.apis.io/hellosign/errors/hellosign-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/hellosign-error-codes.yml
- group: design
  href: https://artifacts.apis.io/hellosign/conventions/hellosign-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hellosign-conventions.yml
- group: design
  href: https://artifacts.apis.io/hellosign/lifecycle/hellosign-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hellosign-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hellosign.com/
- group: operate
  href: https://artifacts.apis.io/hellosign/lifecycle/hellosign-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hellosign-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hellosign/conformance/hellosign-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hellosign-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sign.dropbox.com/trust
- group: auth
  href: https://artifacts.apis.io/hellosign/security/hellosign-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hellosign-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hellosign/security/hellosign-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hellosign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://app.intigriti.com/programs/dropbox/dropbox-vdp
- group: design
  href: https://artifacts.apis.io/hellosign/asyncapi/hellosign-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hellosign-events-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/hellosign/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/hellosign/sandbox/hellosign-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hellosign-sandbox.yml
- group: design
  href: https://artifacts.apis.io/hellosign/components/hellosign-components.yml
  title: ''
  type: Components
  url: components/hellosign-components.yml
- group: design
  href: https://artifacts.apis.io/hellosign/data-model/hellosign-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hellosign-data-model.yml
- group: operate
  href: https://artifacts.apis.io/hellosign/changelog/hellosign-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hellosign-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hellosign.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hellosign.com/docs/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hellosign.com/api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hellosign.com/api/api-quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.dropbox.com/sign
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hellosign
- group: commercial
  title: ''
  type: Pricing
  url: https://sign.dropbox.com/products/api
- group: start
  title: ''
  type: SignUp
  url: https://app.hellosign.com/account/signUp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellosign.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellosign.com/privacy
created: '2026-07-17'
description: Dropbox Sign (formerly HelloSign) is an eSignature platform whose v3 REST API lets developers send documents for legally binding electronic signature, build reusable templates, embed signing directly in their own apps, run bulk send jobs, and manage accounts, teams, and API apps. The API exposes 73 operations across 12 product areas (Signature Request, Template, Bulk Send, Embedded, Account, Team, Report, Fax, Fax Line, Unclaimed Draft, API App, OAuth), with API-key and OAuth 2.0 authentication, 23 webhook event types, official SDKs in six languages, and a published hosted documentation MCP server. HelloSign was a Y Combinator company (S11), acquired by Dropbox in 2019 and rebranded to Dropbox Sign in 2022; the API base host remains api.hellosign.com.
finops:
- has_sources: true
  method: derived
  name: Hellosign Finops
  primary_unit: subscription
  service_category: ''
  slug: hellosign-finops
  template: false
image: https://github.com/hellosign.png
layout: provider
mcp_servers:
- description: Official hosted MCP server published by Dropbox Sign (formerly HelloSign) for AI client integration (Claude Code, Cursor, etc.), advertised in the docs llms.txt. Serves the Dropbox Sign developer docu
  name: Dropbox Sign (HelloSign) MCP Server
  slug: dropbox-sign-docs
modified: '2026-09-16'
name: Dropbox Sign (HelloSign)
nav: Providers
network: true
overview: 'Dropbox Sign (HelloSign) publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Api App API, Bulk Send Job API, and 10 more. Tagged areas include Company, E-Signature, Documents, Digital Agreements, and Signature Workflow.


  The Dropbox Sign (HelloSign) catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Dropbox Sign (HelloSign)''s developer surface includes engineering blog, authentication, sandbox, changelog, documentation, API reference, getting-started guide, and 36 more developer resources.'
plans:
- name: Hellosign Plans Pricing
  plan_count: 3
  slug: hellosign-plans-pricing
- name: Hellosign Price Estimates
  plan_count: 0
  slug: hellosign-price-estimates
random_paper: 5
scopes:
- name: Hellosign Scopes
  scope_count: 7
  slug: hellosign-scopes
  summary_line: 7 scopes
score:
  band: exemplar
  composite: 71.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 59.5
    developer_ergonomics: 74.4
    discoverability: 71.7
    operational_transparency: 63.2
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hellosign/hellosign-2026-07-25T220935.png
security:
- kind: authentication
  name: Hellosign Authentication
  slug: hellosign-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Hellosign Domain Security
  slug: hellosign-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hellosign Vulnerability Disclosure
  slug: hellosign-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Hellosign Trust Center
  slug: hellosign-trust-center
  summary_line: HIPAA, ISO 9001, SOC (CPA/AICPA attestation), Skyhigh Enterprise-Ready
skill_count: 3
skills:
- name: Embedded signing with Dropbox Sign
  slug: hellosign-embedded-signing
- name: Send a signature request with Dropbox Sign
  slug: hellosign-send-signature-request
- name: Reuse a template and bulk-send with Dropbox Sign
  slug: hellosign-templates-and-bulk-send
slug: hellosign
tags:
- Company
- E-Signature
- Documents
- Digital Agreements
- Signature Workflow
- Embedded Signing
- Compliance
website: https://hellosign.com
---
