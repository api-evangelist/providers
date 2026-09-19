---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-09-18'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Semrush Agentic Access
  operation_count: 6
  slug: semrush-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.semrush.com
  baseurl_source: declared
  description: The Hermes Partner API API from Semrush — 4 operation(s) for hermes partner api.
  name: Semrush Hermes Partner API
  slug: semrush-hermes-partner-api-api
- baseURL: https://api.semrush.com
  baseurl_source: declared
  description: The JWT Issuer API from Semrush — 1 operation(s) for jwt issuer.
  name: Semrush JWT Issuer API
  slug: semrush-jwt-issuer-api
- baseURL: https://api.semrush.com
  baseurl_source: declared
  description: The Partner Service API from Semrush — 1 operation(s) for partner service.
  name: Semrush Partner Service API
  slug: semrush-partner-service-api
- description: Semrush's first-party hosted Model Context Protocol server. Streamable HTTP transport only, OAuth-gated with the single scope mcp.access, and metered against the same API unit balance as the REST APIs
  name: Semrush MCP
  slug: semrush-mcp
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Semrush Hermes Partner API API
  slug: open-semrush-hermes-partner-api-api
- collection_type: open
  name: Semrush Hermes Partner API JWT Issuer API
  slug: open-semrush-jwt-issuer-api
- collection_type: open
  name: Semrush Hermes Partner API Partner Service API
  slug: open-semrush-partner-service-api
- collection_type: open
  name: Semrush
  slug: open-semrush
common:
- group: company
  title: ''
  type: Website
  url: https://www.semrush.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/agentic-access/semrush-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/semrush-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/security/semrush-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/semrush-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/security/semrush-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/semrush-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/security/semrush-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/semrush-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/security/semrush-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/semrush-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/security/semrush-trust-center.yml
  title: ''
  type: Compliance
  url: security/semrush-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/authentication/semrush-authentication.yml
  title: ''
  type: Authentication
  url: authentication/semrush-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/scopes/semrush-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/semrush-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/conventions/semrush-conventions.yml
  title: ''
  type: Conventions
  url: conventions/semrush-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/errors/semrush-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/semrush-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/lifecycle/semrush-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/semrush-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/lifecycle/semrush-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/semrush-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/conformance/semrush-conformance.yml
  title: ''
  type: Conformance
  url: conformance/semrush-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/changelog/semrush-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/semrush-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/components/semrush-components.yml
  title: ''
  type: Components
  url: components/semrush-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/data-model/semrush-data-model.yml
  title: ''
  type: DataModel
  url: data-model/semrush-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/packages/semrush-packages.yml
  title: ''
  type: Packages
  url: packages/semrush-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/well-known/semrush-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/semrush-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/mcp/semrush-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/semrush-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/mcp/semrush-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/semrush-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/llms/semrush-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/semrush-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/plans/semrush-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/semrush-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/rate-limits/semrush-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/semrush-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/finops/semrush-finops.yml
  title: ''
  type: FinOps
  url: finops/semrush-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.semrush.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.semrush.com/api/v4/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.semrush.com/api/v4/seo/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.semrush.com/api/v4/get-started/quick-start/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.semrush.com/prices/
- group: start
  title: ''
  type: Signup
  url: https://www.semrush.com/signup/
- group: operate
  title: ''
  type: Support
  url: https://www.semrush.com/kb/
- group: company
  title: ''
  type: Blog
  url: https://www.semrush.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.semrush.com/company/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.semrush.com/company/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/semrush
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/semrush
created: '2024-11-14'
description: SEMrush is an all-in-one digital marketing tool that helps businesses improve their online visibility and attract more customers. This powerful software provides a range of tools and features for keyword research, website analysis, competitive analysis, and more. With SEMrush, businesses can track their online rankings, discover new keywords to target, analyze their competitors' strategies, and optimize their website for better search engine performance.
finops:
- name: Semrush Finops
  service_category: API
  slug: semrush-finops
graphqls:
- description: 'Semrush is an online marketing analytics platform. The API covers keyword research, domain analytics, backlink data, site audit, position tracking, content analysis, advertising research, and traffic '
  name: Semrush GraphQL API
  slug: semrush-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semrush.png
layout: provider
mcp_servers:
- description: Semrush ships a first-party, hosted MCP server that exposes its public API data to AI agents over streamable HTTP. Per the provider's own documentation the server fronts the Trends API (subject to the
  name: Semrush MCP
  slug: semrush-mcp
modified: '2026-09-16'
name: Semrush
nav: Providers
network: true
overview: 'Semrush publishes 3 APIs on the [APIs.io](https://apis.io/) network: Hermes Partner API, JWT Issuer API, and Partner Service API. Tagged areas include Data, Search Engines, SEO, Marketing, and Marketing Intelligence.


  Semrush''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Semrush Plans Pricing
  plan_count: 6
  slug: semrush-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 13
  name: Semrush Rate Limits
  slug: semrush-rate-limits
scopes:
- name: Semrush Scopes
  scope_count: 0
  slug: semrush-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 56.6
    developer_ergonomics: 60.1
    discoverability: 75.9
    operational_transparency: 68.4
  previous_composite: 64.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/semrush/refs/heads/main/screenshots/semrush-2026-06-20T193655.png
security:
- kind: authentication
  name: Semrush Authentication
  slug: semrush-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Semrush Domain Security
  slug: semrush-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Semrush Vulnerability Disclosure
  slug: semrush-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Semrush Trust Center
  slug: semrush-trust-center
  summary_line: PCI DSS, GDPR, CCPA, LGPD
slug: semrush
tags:
- Data
- Search Engines
- SEO
- Marketing
- Marketing Intelligence
- Content Marketing
- Advertising
- Competitive Intelligence
- Keyword Research
- Backlinks
- Rank Tracking
- AI Search Visibility
- Local SEO
- MCP
website: https://www.semrush.com/
---
