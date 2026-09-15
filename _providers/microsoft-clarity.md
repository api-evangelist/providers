---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-09-14'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Microsoft Clarity Agentic Access
  operation_count: 1
  slug: microsoft-clarity-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Microsoft Clarity provides heatmaps, session recordings, and behavioral analytics with API access for custom integrations.
  name: Microsoft Clarity API
  slug: api
- baseURL: https://www.clarity.ms/
  baseurl_source: declared
  description: 'Project live insights data export. One JWT-authenticated GET returns Clarity dashboard metrics as JSON for the last one to three days, sliced by up to three of nine dimensions. Capped at ten requests '
  name: Microsoft Clarity DataExport API
  slug: microsoft-clarity-dataexport-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Clarity Data Export DataExport API
  slug: open-microsoft-clarity-dataexport-api
- collection_type: open
  name: Microsoft Clarity Data Export API
  slug: open-microsoft-clarity
common:
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/agentic-access/microsoft-clarity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-clarity-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/security/microsoft-clarity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-clarity-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/security/microsoft-clarity-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-clarity-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/security/microsoft-clarity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-clarity-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/authentication/microsoft-clarity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-clarity-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/packages/microsoft-clarity-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-clarity-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/packages/microsoft-clarity-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-clarity-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/well-known/microsoft-clarity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-clarity-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/well-known/microsoft-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/mcp/microsoft-clarity-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-clarity-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/mcp/microsoft-clarity-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-clarity-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/llms/microsoft-clarity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-clarity-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/conformance/microsoft-clarity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-clarity-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/conformance/microsoft-clarity-conformance.yml
  title: ''
  type: Compliance
  url: conformance/microsoft-clarity-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/conventions/microsoft-clarity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-clarity-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/lifecycle/microsoft-clarity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-clarity-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/changelog/microsoft-clarity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-clarity-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/components/microsoft-clarity-components.yml
  title: ''
  type: Components
  url: components/microsoft-clarity-components.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/plans/microsoft-clarity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-clarity-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/rate-limits/microsoft-clarity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-clarity-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microsoft-clarity
- group: start
  title: ''
  type: Portal
  url: https://clarity.microsoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/clarity/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/clarity/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-data-export-api
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-setup
- group: commercial
  title: ''
  type: Pricing
  url: https://clarity.microsoft.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://clarity.microsoft.com/
- group: operate
  title: ''
  type: FAQ
  url: https://learn.microsoft.com/en-us/clarity/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://clarity.microsoft.com/blog/feed
created: '2026-03-13'
description: Microsoft Clarity is a free behavioral analytics service from Microsoft that captures heatmaps, session recordings and frustration signals — rage clicks, dead clicks, excessive scroll, quickback clicks and script errors — for websites and mobile apps. Instrumentation is a client-side tracking tag or a first-party SDK for Android, iOS, Flutter, React Native and Cordova. Data comes back out through the Data Export API, a single JWT-authenticated GET that returns dashboard metrics for the last one to three days broken down by up to three dimensions, and through a first-party Model Context Protocol server that wraps the same endpoint for AI agents. Clarity is free forever with no paid tier; the binding constraint on any integration is a quota of ten API requests per project per day.
finops:
- name: Microsoft Clarity Finops
  service_category: API
  slug: microsoft-clarity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-clarity.png
layout: provider
mcp_servers:
- description: First-party Model Context Protocol server for Microsoft Clarity, published by Microsoft as @microsoft/clarity-mcp-server and documented on Microsoft Learn. It wraps the Clarity Data Export API and the
  name: Microsoft Clarity MCP Server
  slug: microsoft-clarity-mcp-server
modified: '2026-08-13'
name: Microsoft Clarity
nav: Providers
network: true
overview: 'Microsoft Clarity publishes 1 API on the [APIs.io](https://apis.io/) network: DataExport API. Tagged areas include Analytics, Heatmaps, Session Recording, Web Analytics, and Behavioral Analytics.


  Microsoft Clarity''s developer surface includes authentication, changelog, developer portal, documentation, API reference, getting-started guide, pricing, and 29 more developer resources.'
plans:
- name: Microsoft Clarity Plans Pricing
  plan_count: 1
  slug: microsoft-clarity-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Microsoft Clarity Rate Limits
  slug: microsoft-clarity-rate-limits
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 66.1
    discoverability: 83.3
    operational_transparency: 60.5
  previous_composite: 60.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/screenshots/microsoft-clarity-2026-06-20T185449.png
security:
- kind: authentication
  name: Microsoft Clarity Authentication
  slug: microsoft-clarity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Clarity Domain Security
  slug: microsoft-clarity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Clarity Vulnerability Disclosure
  slug: microsoft-clarity-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-clarity
tags:
- Analytics
- Heatmaps
- Session Recording
- Web Analytics
- Behavioral Analytics
- Product Analytics
- User Experience
- Data Export
- MCP
website: https://www.microsoft.com/
---
