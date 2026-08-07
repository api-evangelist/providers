---
access_model:
  confidence: high
  label: No published developer API; corporate-site content and MCP surfaces only
  onboarding: unknown
  pricing: free
  public: false
  source:
  - probe
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 130
  human_in_the_loop: 0
  name: Harbinger Health Agentic Access
  operation_count: 236
  slug: harbinger-health-agentic-access
  summary_line: 236 operations · 130 acting
api_count: 2
apis:
- description: The stock WordPress REST API served by Harbinger Health's corporate site at https://harbinger-health.com/wp-json/. Confirmed live and anonymously readable on 2026-08-04 (HTTP 200, application/json, 25
  name: Harbinger Health WordPress REST API
  slug: harbinger-health-wordpress-rest-api
- description: A live Model Context Protocol server namespace published on Harbinger Health's own host at https://harbinger-health.com/wp-json/mcp/, exposing two servers - mcp-oauth-server and mcp-adapter-default-se
  name: Harbinger Health MCP Server
  slug: harbinger-health-mcp-server
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://harbinger-health.com/
- group: company
  title: ''
  type: About
  url: https://harbinger-health.com/about/
- group: company
  title: ''
  type: Blog
  url: https://harbinger-health.com/news-insights/
- group: operate
  title: ''
  type: Support
  url: https://harbinger-health.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harbinger-health.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harbinger-health.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://harbinger-health.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://harbinger-health.com/job/
- group: company
  title: ''
  type: Partners
  url: https://harbinger-health.com/partnerships/
- group: other
  title: ''
  type: Product
  url: https://harbinger-health.com/resolve/
- group: other
  title: ''
  type: Product
  url: https://harbinger-health.com/platform-technology/
- group: company
  title: ''
  type: PressRoom
  url: https://harbinger-health.com/news-insights/
- group: other
  title: ''
  type: Sitemap
  url: https://harbinger-health.com/sitemap_index.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harbinger-health
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/harbingerhlth
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@HarbingerHealth
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/harbingerhealth/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/p/Harbinger-Health-61555320668795/
- group: auth
  title: ''
  type: Authentication
  url: authentication/harbinger-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/harbinger-health-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/harbinger-health-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/harbinger-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/harbinger-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harbinger-health-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/harbinger-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/harbinger-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harbinger-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/harbinger-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://harbinger-health.com/resolve/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harbinger-health-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/harbinger-health-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/harbinger-health-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harbinger-health-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/harbinger-health-wordpress-wp-v2-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
created: '2026-08-04'
description: 'Harbinger Health is a Cambridge, Massachusetts biotechnology company founded out of Flagship Pioneering''s Flagship Labs in 2018 that is building blood-based early cancer detection on the premise that the earliest phases of oncogenesis are marked by the reactivation of core developmental programs. Its proprietary Harbinger HX platform pairs cell-free DNA methylation assay chemistry tuned for low tumour fraction with machine learning operating under biologically informed constraints, and supports cancer signal detection, tumour content estimation and tissue-of-origin inference. RESOLVE, the company''s clinical application of that platform, is positioned to generate clarity in the uncertain window between suspicion of cancer and diagnosis, across cancer types and clinical contexts, and is run out of a CLIA-certified and CAP-accredited high-complexity laboratory. The company raised a 100 million dollar round to expand its blood-based detection suite and is led by CEO Ajit Singh
  with Chief Innovation Officer Tony Shuber, a co-founder of Exact Sciences. Harbinger Health''s API posture is minimal and clinical rather than commercial: there is no developer portal, no published documentation, no OpenAPI, no SDKs, no pricing and no self-serve API access, and the developer., docs., api., portal., status. and trust. subdomains do not resolve. What it does publish is unusual for a company with no developer programme - the corporate site serves a live, anonymously readable WordPress REST API (268 routes across 15 namespaces), an RFC 8414 OAuth 2.1 authorization-server metadata document, an RFC 9728 protected-resource document, and a real Model Context Protocol server namespace gated behind an mcp scope, alongside the WordPress Abilities API. That makes Harbinger Health machine-discoverable at the agent layer while none of its clinical, laboratory or diagnostic capability is exposed programmatically to third parties.'
examples:
- key_count: 3
  name: Harbinger Health Error 400
  slug: harbinger-health-error-400
- key_count: 3
  name: Harbinger Health Error 401
  slug: harbinger-health-error-401
- key_count: 3
  name: Harbinger Health Error 404
  slug: harbinger-health-error-404
- key_count: 3
  name: Harbinger Health Error No Route
  slug: harbinger-health-error-no-route
- key_count: 12
  name: Harbinger Health Types Response
  slug: harbinger-health-types-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: harbinger-health-mcp.yml
  slug: harbinger-health-mcpyml
modified: '2026-08-04'
name: Harbinger Health
nav: Providers
network: true
overview: 'Harbinger Health publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Health, Healthcare, Biotechnology, Cancer Detection, and Diagnostics.


  Harbinger Health''s developer surface includes engineering blog, support, YouTube channel, authentication, code examples, and 31 more developer resources.'
random_paper: 39
scopes:
- name: Harbinger Health Scopes
  scope_count: 1
  slug: harbinger-health-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 42.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.2
    developer_ergonomics: 27.7
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 42.8
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
    matched_via: tags
    regime: Health
    regime_id: health
    score: 75.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Harbinger Health Authentication
  slug: harbinger-health-authentication
  summary_line: none/http/oauth2 · 3 schemes
- kind: domain-security
  name: Harbinger Health Domain Security
  slug: harbinger-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: harbinger-health
tags:
- Health
- Healthcare
- Biotechnology
- Cancer Detection
- Diagnostics
- Genomics
- Artificial Intelligence
- Machine Learning
- Life Sciences
- Clinical Laboratory
- Precision Medicine
- United States
- Company
website: https://harbinger-health.com/
---
