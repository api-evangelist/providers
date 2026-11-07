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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 130
  human_in_the_loop: 0
  name: Harbinger Health Agentic Access
  operation_count: 236
  slug: harbinger-health-agentic-access
  summary_line: 236 operations · 130 acting
api_count: 1
apis:
- description: A live Model Context Protocol server namespace published on Harbinger Health's own host at https://harbinger-health.com/wp-json/mcp/, exposing two servers - mcp-oauth-server and mcp-adapter-default-se
  name: Harbinger Health MCP Server
  slug: harbinger-health-mcp-server
- description: 'The public WordPress REST API (wp-json) of the Harbinger Health website at harbinger-health.com: the route index of the site''s content management system, catalogued as one site surface rather than as '
  name: Harbinger Health Website (WordPress REST)
  slug: harbinger-health-com-website-wordpress-rest
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-harbinger-health-wp-json-discovery
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
  href: https://artifacts.apis.io/harbinger-health/authentication/harbinger-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/harbinger-health-authentication.yml
- group: auth
  href: https://artifacts.apis.io/harbinger-health/scopes/harbinger-health-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/harbinger-health-scopes.yml
- group: agent
  href: https://artifacts.apis.io/harbinger-health/well-known/harbinger-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/harbinger-health-well-known.yml
- group: agent
  href: https://artifacts.apis.io/harbinger-health/mcp/harbinger-health-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/harbinger-health-mcp.yml
- group: build
  href: https://artifacts.apis.io/harbinger-health/mcp/harbinger-health-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/harbinger-health-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/harbinger-health/llms/harbinger-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/harbinger-health-llms.txt
- group: design
  href: https://artifacts.apis.io/harbinger-health/conventions/harbinger-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/harbinger-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/harbinger-health/errors/harbinger-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/harbinger-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/harbinger-health/lifecycle/harbinger-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/harbinger-health-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/harbinger-health/conformance/harbinger-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/harbinger-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://harbinger-health.com/resolve/
- group: auth
  href: https://artifacts.apis.io/harbinger-health/security/harbinger-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/harbinger-health-domain-security.yml
- group: design
  href: https://artifacts.apis.io/harbinger-health/data-model/harbinger-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/harbinger-health-data-model.yml
- group: build
  href: https://artifacts.apis.io/harbinger-health/packages/harbinger-health-packages.yml
  title: ''
  type: Packages
  url: packages/harbinger-health-packages.yml
- group: agent
  href: https://artifacts.apis.io/harbinger-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/harbinger-health/agentic-access/harbinger-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/harbinger-health-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/harbinger-health/overlays/harbinger-health-wordpress-wp-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/harbinger-health-wordpress-wp-v2-overlay.yaml
- group: build
  href: https://artifacts.apis.io/harbinger-health/examples/_index.yml
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
- description: Harbinger Health publishes a real, live Model Context Protocol server on its own host. This is not a candidate surface derived from an OpenAPI — the MCP namespace is registered in the site's WordPress
  name: Harbinger Health MCP Server
  slug: harbinger-health-mcp-yml
modified: '2026-08-04'
name: Harbinger Health
nav: Providers
network: true
overview: 'Harbinger Health publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Healthcare, Biotechnology, Cancer Detection, and Diagnostics.


  The Harbinger Health catalog on APIs.io includes 1 Spectral governance ruleset.


  Harbinger Health''s developer surface includes engineering blog, support, YouTube channel, authentication, code examples, and 31 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Harbinger Health API Rules
  rule_count: 64
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 6
  slug: harbinger-health-rules
scopes:
- name: Harbinger Health Scopes
  scope_count: 1
  slug: harbinger-health-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 28.9
    contract_governance: 31.8
    contract_quality: 6.5
    developer_ergonomics: 25.6
    discoverability: 60.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 26.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 34.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/harbinger-health/harbinger-health-2026-08-07T165948.png
security:
- kind: authentication
  name: Harbinger Health Authentication
  slug: harbinger-health-authentication
  summary_line: none/http/oauth2 · 3 schemes
- kind: domain-security
  name: Harbinger Health Domain Security
  slug: harbinger-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: Connect to the Harbinger Health MCP server
  slug: harbinger-health-connect-to-the-mcp-server
- name: Ground an agent on Harbinger Health from primary sources
  slug: harbinger-health-ground-an-agent-on-the-company
- name: Track Harbinger Health company news and scientific updates
  slug: harbinger-health-track-company-news
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
