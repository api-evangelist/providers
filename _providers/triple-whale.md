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
  band: agent-native
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
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Triple Whale Agentic Access
  operation_count: 16
  slug: triple-whale-agentic-access
  summary_line: 16 operations · 15 acting
api_count: 3
apis:
- description: The API Keys API from Triple Whale — 1 operation(s) for api keys.
  name: Triple Whale API Keys API
  slug: triple-whale-api-keys-api
- description: The Compliance API from Triple Whale — 1 operation(s) for compliance.
  name: Triple Whale Compliance API
  slug: triple-whale-compliance-api
- description: The Data In API from Triple Whale — 10 operation(s) for data in.
  name: Triple Whale Data In API
  slug: triple-whale-data-in-api
- description: The Data Out API from Triple Whale — 4 operation(s) for data out.
  name: Triple Whale Data Out API
  slug: triple-whale-data-out-api
- description: The bi API from Triple Whale — 1 operation(s) for bi.
  name: Triple Whale Bi API
  slug: triple-whale-bi-api
artifact_total: 27
collections:
- collection_type: postman
  name: Triple Whale API Keys API
  slug: postman-triple-whale-api-keys-api
- collection_type: postman
  name: Triple Whale API Keys Compliance API
  slug: postman-triple-whale-compliance-api
- collection_type: postman
  name: Triple Whale API Keys Data In API
  slug: postman-triple-whale-data-in-api
- collection_type: postman
  name: Triple Whale API Keys Data Out API
  slug: postman-triple-whale-data-out-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Triple Whale API Keys API
  slug: open-triple-whale-api-keys-api
- collection_type: open
  name: Triple Whale API Keys Compliance API
  slug: open-triple-whale-compliance-api
- collection_type: open
  name: Triple Whale API Keys Data In API
  slug: open-triple-whale-data-in-api
- collection_type: open
  name: Triple Whale API Keys Data Out API
  slug: open-triple-whale-data-out-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Triple-Whale/triple-whale-public-apis/issues
- group: other
  title: ''
  type: Overlay
  url: overlays/triple-whale-bi-benchmarks-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/triple-whale/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/triple-whale-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/triple-whale-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triple-whale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/triple-whale-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.triplewhale.com
- group: docs
  title: ''
  type: Documentation
  url: https://triplewhale.readme.io/reference/introduction-to-the-triple-whale-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Triple-Whale
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triple-whale
- group: company
  title: ''
  type: Blog
  url: https://www.triplewhale.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.triplewhale.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.triplewhale.com
- group: other
  title: ''
  type: X
  url: https://x.com/triplewhale
- group: commercial
  title: ''
  type: Plans
  url: plans/triple-whale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/triple-whale-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/triple-whale-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/triple-whale-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.triplewhale.com/
- group: docs
  title: ''
  type: APIReference
  url: https://triplewhale.readme.io/reference/introduction-to-the-triple-whale-api
- group: start
  title: ''
  type: GettingStarted
  url: https://triplewhale.readme.io/reference/api-setup-guide-for-custom-sales-platform
- group: operate
  title: ''
  type: HelpCenter
  url: https://kb.triplewhale.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.triplewhale.com/signup-free
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.triplewhale.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.triplewhale.com/pages/privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Triple-Whale
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Triple-Whale/triple-whale-public-apis
- group: build
  title: ''
  type: Packages
  url: packages/triple-whale-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/triple-whale-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/triple-whale-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/triple-whale-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/triple-whale-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/triple-whale-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/triple-whale-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/triple-whale-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/triple-whale-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/triple-whale-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/triple-whale-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/triple-whale-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/triple-whale-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/triple-whale-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.triplewhale.com/
- group: design
  title: ''
  type: DataModel
  url: data-model/triple-whale-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/triple-whale-api-keys-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/triple-whale-compliance-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/triple-whale-data-in-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/triple-whale-data-out-api-overlay.yaml
created: '2026-06-13'
description: E-commerce analytics and attribution platform for Shopify brands with a REST API for accessing pixel data, cohort analytics, creative metrics, and blended ROAS. Offers a two-way data highway with Data-In and Data-Out APIs supporting OAuth2 and API key authentication.
finops:
- name: Triple Whale Finops
  service_category: ''
  slug: triple-whale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/triple-whale.png
json_schemas:
- name: Triple Whale Ad Record
  property_count: 10
  slug: triple-whale-ad
- name: Triple Whale Order
  property_count: 19
  slug: triple-whale-order
jsonld:
- class_count: 0
  name: Triple Whale Context
  property_count: 37
  slug: triple-whale-context
layout: provider
mcp_servers:
- description: Triple Whale ships an MCP surface in two distinct forms. A hosted remote server at https://mcp.triplewhale.com/sse answers JSON-RPC over HTTP and is protected by OAuth 2.1 (PKCE S256, dynamic client r
  name: Triple Whale MCP (Moby)
  slug: triple-whale-mcp-moby
modified: '2026-08-13'
name: Triple Whale
nav: Providers
network: true
overview: 'Triple Whale publishes 5 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Compliance API, Data In API, and 2 more. Tagged areas include E-Commerce, Analytics, Attribution, Shopify, and Pixel Tracking.


  The Triple Whale catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Triple Whale''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, signup flow, and 42 more developer resources.'
plans:
- name: Triple Whale Plans Pricing
  plan_count: 4
  slug: triple-whale-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Triple Whale Rate Limits
  slug: triple-whale-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Triple Whale API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: triple-whale-jsonschema-spectral-rules
scopes:
- name: Triple Whale Scopes
  scope_count: 0
  slug: triple-whale-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 30
    catalog_gap: 26.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 14.4
    contract_quality: 67.1
    developer_ergonomics: 63.7
    discoverability: 81.5
    governance: 14.4
    operational_transparency: 65.8
  open_source:
    applies: true
    score: 0.0
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triple-whale/refs/heads/main/screenshots/triple-whale-2026-06-20T195726.png
security:
- kind: authentication
  name: Triple Whale Authentication
  slug: triple-whale-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Triple Whale Domain Security
  slug: triple-whale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Triple Whale Trust Center
  slug: triple-whale-trust-center
  summary_line: SOC 2, GDPR
slug: triple-whale
tags:
- E-Commerce
- Analytics
- Attribution
- Shopify
- Pixel Tracking
- ROAS
- DTC
- Marketing
website: https://www.triplewhale.com
---
