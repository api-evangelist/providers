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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-11-06'
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
- baseURL: https://www.clarity.ms
  baseurl_source: declared
  description: Project live insights data export
  name: Microsoft Clarity Data Export API
  slug: microsoft-clarity-data-export-api
artifact_total: 18
collections:
- collection_type: open
  name: Microsoft Clarity Data Export DataExport API
  slug: open-microsoft-clarity-dataexport-api
- collection_type: open
  name: Microsoft Clarity Data Export API
  slug: open-microsoft-clarity
common:
- group: design
  href: https://artifacts.apis.io/microsoft-clarity/rules/microsoft-clarity-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-clarity-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-clarity/json-ld/microsoft-clarity-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-clarity-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-clarity/vocabulary/microsoft-clarity-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-clarity-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/microsoft-clarity/hosts/microsoft-clarity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-clarity-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-clarity/integrations/microsoft-clarity-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-clarity-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-clarity/vendors/microsoft-clarity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-clarity-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: auth
  href: https://artifacts.apis.io/microsoft-clarity/security/microsoft-clarity-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-clarity-trust-center.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-clarity/finops/microsoft-clarity-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-clarity-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-clarity/capabilities/microsoft-clarity-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-clarity-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-clarity/overlays/microsoft-clarity-dataexport-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-clarity-dataexport-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://clarity.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-clarity/agentic-access/microsoft-clarity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-clarity-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-clarity/security/microsoft-clarity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-clarity-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-clarity/security/microsoft-clarity-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-clarity-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-clarity/security/microsoft-clarity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-clarity-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-clarity/authentication/microsoft-clarity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-clarity-authentication.yml
- group: build
  href: https://artifacts.apis.io/microsoft-clarity/packages/microsoft-clarity-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-clarity-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-clarity/packages/microsoft-clarity-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-clarity-packages.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-clarity/well-known/microsoft-clarity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-clarity-well-known.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-clarity/well-known/microsoft-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-clarity-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-clarity/mcp/microsoft-clarity-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-clarity-mcp.yml
- group: build
  href: https://artifacts.apis.io/microsoft-clarity/mcp/microsoft-clarity-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-clarity-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-clarity/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-clarity/llms/microsoft-clarity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-clarity-llms.txt
- group: design
  href: https://artifacts.apis.io/microsoft-clarity/conformance/microsoft-clarity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-clarity-conformance.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-clarity/conformance/microsoft-clarity-conformance.yml
  title: ''
  type: Compliance
  url: conformance/microsoft-clarity-conformance.yml
- group: design
  href: https://artifacts.apis.io/microsoft-clarity/conventions/microsoft-clarity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-clarity-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-clarity/lifecycle/microsoft-clarity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-clarity-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-clarity/changelog/microsoft-clarity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-clarity-changelog.yml
- group: design
  href: https://artifacts.apis.io/microsoft-clarity/components/microsoft-clarity-components.yml
  title: ''
  type: Components
  url: components/microsoft-clarity-components.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-clarity/plans/microsoft-clarity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-clarity-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-clarity/rate-limits/microsoft-clarity-rate-limits.yml
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
- has_sources: true
  method: derived
  name: Microsoft Clarity Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-clarity-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-clarity.png
json_schemas:
- name: MetricEntry
  property_count: 2
  slug: microsoft-clarity-metric-entry
jsonld:
- class_count: 1
  name: Microsoft Clarity Context
  property_count: 2
  slug: microsoft-clarity-context
layout: provider
mcp_servers:
- description: First-party Model Context Protocol server for Microsoft Clarity, published by Microsoft as @microsoft/clarity-mcp-server and documented on Microsoft Learn. It wraps the Clarity Data Export API and the
  name: Microsoft Clarity MCP Server
  slug: microsoft-clarity-mcp-server
modified: '2026-08-13'
name: Microsoft Clarity
nav: Providers
network: true
overview: 'Microsoft Clarity publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data Export API, and 1 more. Tagged areas include Analytics, Heatmaps, Session Recording, Web Analytics, and Behavioral Analytics.


  The Microsoft Clarity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Clarity''s developer surface includes authentication, changelog, developer portal, documentation, API reference, getting-started guide, pricing, and 40 more developer resources.'
plans:
- name: Microsoft Clarity Plans Pricing
  plan_count: 1
  slug: microsoft-clarity-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Microsoft Clarity Rate Limits
  slug: microsoft-clarity-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Microsoft Clarity API Rules
  rule_count: 59
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-clarity-rules
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 35
    catalog_earned: 73.2
    catalog_earned_first_party: 20.0
    catalog_gap: 41.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 71.1
    contract_governance: 35.6
    contract_quality: 58.5
    developer_ergonomics: 66.1
    discoverability: 80.0
    operational_transparency: 60.5
  previous_composite: 61.3
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/microsoft-clarity/microsoft-clarity-2026-06-20T185449.png
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
- kind: trust-center
  name: Microsoft Clarity Trust Center
  slug: microsoft-clarity-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: microsoft-clarity-diagnose-friction
  slug: microsoft-clarity-diagnose-friction
- name: microsoft-clarity-export-daily-insights
  slug: microsoft-clarity-export-daily-insights
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
website: https://clarity.microsoft.com/
---
