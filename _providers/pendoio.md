---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 32
  human_in_the_loop: 4
  name: Pendoio Agentic Access
  operation_count: 65
  slug: pendoio-agentic-access
  summary_line: 65 operations · 32 acting · 4 human-in-the-loop
api_count: 16
apis:
- description: The Account API from Pendo.io — 2 operation(s) for account.
  name: Pendo.io Account API
  slug: pendoio-account-api
- description: The Admin API from Pendo.io — 1 operation(s) for admin.
  name: Pendo.io Admin API
  slug: pendoio-admin-api
- description: The Aggregation API from Pendo.io — 1 operation(s) for aggregation.
  name: Pendo.io Aggregation API
  slug: pendoio-aggregation-api
- description: The Bulk Deletion (GDPR/CCPA) API from Pendo.io — 4 operation(s) for bulk deletion (gdpr/ccpa).
  name: Pendo.io Bulk Deletion (GDPR/CCPA) API
  slug: pendoio-bulk-deletion-gdpr-ccpa-api
- description: The Conversations API from Pendo.io — 1 operation(s) for conversations.
  name: Pendo.io Conversations API
  slug: pendoio-conversations-api
- description: The Data Sync API from Pendo.io — 3 operation(s) for data sync.
  name: Pendo.io Data Sync API
  slug: pendoio-data-sync-api
- description: The Exclude Lists & Servers API from Pendo.io — 5 operation(s) for exclude lists & servers.
  name: Pendo.io Exclude Lists & Servers API
  slug: pendoio-exclude-lists-servers-api
- description: The Feature API from Pendo.io — 1 operation(s) for feature.
  name: Pendo.io Feature API
  slug: pendoio-feature-api
- description: The Guide API from Pendo.io — 12 operation(s) for guide.
  name: Pendo.io Guide API
  slug: pendoio-guide-api
- description: The Listen API from Pendo.io — 3 operation(s) for listen.
  name: Pendo.io Listen API
  slug: pendoio-listen-api
- description: The Metadata API from Pendo.io — 9 operation(s) for metadata.
  name: Pendo.io Metadata API
  slug: pendoio-metadata-api
- description: The Page API from Pendo.io — 1 operation(s) for page.
  name: Pendo.io Page API
  slug: pendoio-page-api
- description: The Report API from Pendo.io — 3 operation(s) for report.
  name: Pendo.io Report API
  slug: pendoio-report-api
- description: The Segment API from Pendo.io — 10 operation(s) for segment.
  name: Pendo.io Segment API
  slug: pendoio-segment-api
- description: The Track API from Pendo.io — 2 operation(s) for track.
  name: Pendo.io Track API
  slug: pendoio-track-api
- description: The Visitor API from Pendo.io — 3 operation(s) for visitor.
  name: Pendo.io Visitor API
  slug: pendoio-visitor-api
artifact_total: 22
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/pendoio-engage-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.pendo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://engageapi.pendo.io/
- group: docs
  title: ''
  type: APIReference
  url: https://engageapi.pendo.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.pendo.io/learn/courses/27/pendo-api-setup-and-endpoints
- group: operate
  title: ''
  type: Support
  url: https://support.pendo.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.pendo.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pendo-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pendo.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.pendo.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pendo.io/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pendo.io/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pendo.io/
- group: build
  title: ''
  type: Postman
  url: https://engageapi.pendo.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/pendoio-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pendoio-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pendoio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pendoio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pendo.io/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://www.pendo.io/trust/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pendoio-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/pendoio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pendoio-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pendoio-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pendoio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pendoio-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/pendoio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pendoio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pendoio-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pendoio-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pendoio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pendoio-problem-types.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Pendo is a product-experience and product-analytics platform that helps software teams understand and guide how users engage with their applications. Its Engage API provides programmatic access to the pages, features, guides, visitors, accounts, segments, reports, and metadata collected by the Pendo agent, plus a MongoDB-like Aggregation API for running structured queries over product-usage events. The API authenticates with a per-subscription integration key sent in the x-pendo-integration-key header (OAuth 2.0 is additionally published via RFC 8414 authorization-server metadata), and includes GDPR/CCPA bulk-deletion, segment management, in-app guide targeting, and cloud Data Sync export. Pendo was surfaced as a portfolio company of Battery Ventures.
image: https://www.pendo.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: pendoio-mcp.yml
  slug: pendoio-mcpyml
modified: '2026-07-20'
name: Pendo.io
nav: Providers
network: true
overview: 'Pendo.io publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account API, Admin API, Aggregation API, and 13 more. Tagged areas include Company, Product Analytics, Product Experience, Digital Adoption, and User Analytics.


  Pendo.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 30
score:
  band: developing
  composite: 54.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.7
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Pendoio Authentication
  slug: pendoio-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Pendoio Domain Security
  slug: pendoio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pendoio Vulnerability Disclosure
  slug: pendoio-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Pendoio Trust Center
  slug: pendoio-trust-center
  summary_line: SOC 2, HIPAA, TX-RAMP
slug: pendoio
tags:
- Company
- Product Analytics
- Product Experience
- Digital Adoption
- User Analytics
- In-App Guidance
- Customer Feedback
- SaaS
website: https://developers.pendo.io/
---
