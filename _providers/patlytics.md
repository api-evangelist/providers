---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Patlytics Patent Search connector — a hosted Model Context Protocol server (Streamable HTTP) that brings concept-level, AI-native patent intelligence into MCP clients such as Claude. Five read-onl
  name: Patlytics Patent Search (MCP)
  slug: patent-search-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.patlytics.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.patlytics.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://mcp.patlytics.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.patlytics.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://mcp.patlytics.ai/docs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/patlytics-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/patlytics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/patlytics-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/patlytics-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/patlytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/patlytics-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/patlytics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/patlytics-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.patlytics.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patlytics-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/patlytics-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.patlytics.ai/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/patlytics-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.patlytics.ai/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@patlytics.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/patlytics
- group: start
  title: ''
  type: SignUp
  url: https://explore.patlytics.ai/demo-request
- group: start
  title: ''
  type: Login
  url: https://dashboard.patlytics.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.patlytics.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.patlytics.ai/privacy-policy
- group: company
  title: ''
  type: News
  url: https://www.patlytics.ai/news
- group: company
  title: ''
  type: About
  url: https://www.patlytics.ai/about
created: '2026-08-02'
description: 'Patlytics is an AI-powered patent intelligence platform purpose-built for intellectual-property work, applying generative AI and large language models across the full patent lifecycle: invention harvesting and disclosure, patent application drafting, office-action analysis, prior-art and novelty search, infringement detection, invalidity contentions, claim-chart generation, portfolio pruning, vault and classification, and transactional IP due diligence. Founded in 2023 and headquartered in New York, the company raised a $40M Series B led by SignalFire in April 2026 (roughly $65M total) and counts more than 40% of the Am Law 100 among its customers. Its machine-readable surface is a hosted, OAuth-protected Model Context Protocol server at mcp.patlytics.ai that exposes read-only semantic patent search, patent/claims lookup, non-patent-literature search over OpenAlex, and access to an organization''s private Patlytics portfolios and vault; there is no public REST OpenAPI, and
  the platform API at api.patlytics.ai is fully authentication-gated.'
image: https://cdn.prod.website-files.com/6799236636ce53b60c8d8ba8/679c097be11626243bdde318_Patlytics-Share.webp
layout: provider
mcp_servers:
- description: Concept-level, AI-native patent intelligence inside an MCP client. Describe an invention in plain language and get semantically similar patents, look up a specific patent's claims, search academic lit
  name: Patlytics MCP Server
  slug: patlytics-mcp-server
modified: '2026-08-02'
name: Patlytics
nav: Providers
network: true
overview: 'Patlytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Intellectual Property, Patents, Legal Tech, and Artificial Intelligence.


  Patlytics'' developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 20 more developer resources.'
random_paper: 2
scopes:
- name: Patlytics Scopes
  scope_count: 2
  slug: patlytics-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 33.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/patlytics/refs/heads/main/screenshots/patlytics-2026-08-07T191555.png
security:
- kind: authentication
  name: Patlytics Authentication
  slug: patlytics-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Patlytics Domain Security
  slug: patlytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Patlytics Trust Center
  slug: patlytics-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, ISO 42001, GDPR
slug: patlytics
tags:
- Company
- Intellectual Property
- Patents
- Legal Tech
- Artificial Intelligence
- Patent Search
- Prior Art
- MCP
- Agents
- Research
website: https://www.patlytics.ai/
---
