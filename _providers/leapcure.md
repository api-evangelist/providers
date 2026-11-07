---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Leapcure website at blog.leapcure.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate AP'
  name: Leapcure Website (WordPress REST)
  slug: blog-leapcure-com-website-wordpress-rest
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/leapcure/overlays/leapcure-blog-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leapcure-blog-content-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/leapcure/authentication/leapcure-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leapcure-authentication.yml
- group: design
  href: https://artifacts.apis.io/leapcure/conventions/leapcure-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leapcure-conventions.yml
- group: design
  href: https://artifacts.apis.io/leapcure/errors/leapcure-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leapcure-problem-types.yml
- group: design
  href: https://artifacts.apis.io/leapcure/data-model/leapcure-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leapcure-data-model.yml
- group: design
  href: https://artifacts.apis.io/leapcure/lifecycle/leapcure-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leapcure-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/leapcure/conformance/leapcure-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leapcure-conformance.yml
- group: agent
  href: https://artifacts.apis.io/leapcure/mcp/leapcure-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/leapcure-mcp.yml
- group: agent
  href: https://artifacts.apis.io/leapcure/skills/leapcure-browse-blog-content.md
  title: ''
  type: AgentSkill
  url: skills/leapcure-browse-blog-content.md
- group: agent
  href: https://artifacts.apis.io/leapcure/skills/leapcure-search-content.md
  title: ''
  type: AgentSkill
  url: skills/leapcure-search-content.md
- group: agent
  href: https://artifacts.apis.io/leapcure/llms/leapcure-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leapcure-llms.txt
- group: auth
  href: https://artifacts.apis.io/leapcure/security/leapcure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leapcure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leapcure.com
- group: company
  title: ''
  type: Blog
  url: https://blog.leapcure.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leapcure.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leapcure.com/terms-of-service
created: '2026-07-17'
description: Leapcure is a clinical-trial patient recruitment company whose mission is "where patient advocacy meets research" — connecting patients with clinical studies and helping research sites and sponsors reach and enroll participants. Leapcure was surfaced as a portfolio company of 500 Global and added to the API Evangelist network. The company publishes no product API of its own; the single machine-readable surface it operates is the WordPress REST API (wp/v2) behind its blog at blog.leapcure.com, which exposes read access to posts, pages, categories, tags, users, media, comments and search, plus authenticated write operations via WordPress application passwords. This profile was enriched by the API Evangelist pipeline from that live surface.
image: https://blog.leapcure.com/wp-content/uploads/2022/10/cropped-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at blog.leapcure.com over HTTP.
  name: Leapcure MCP Server
  slug: leapcure-blog
modified: '2026-07-20'
name: Leapcure
nav: Providers
network: true
overview: 'Leapcure publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Clinical Trials, Patient Recruitment, Healthcare, and Blog.


  Leapcure''s developer surface includes authentication, engineering blog, and 14 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 17.0
  provenance:
    conformance: derived
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/leapcure/leapcure-2026-07-25T224748.png
security:
- kind: authentication
  name: Leapcure Authentication
  slug: leapcure-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Leapcure Domain Security
  slug: leapcure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Browse Leapcure blog content
  slug: leapcure-browse-blog-content
- name: Search across the Leapcure blog
  slug: leapcure-search-content
slug: leapcure
tags:
- Company
- Clinical Trials
- Patient Recruitment
- Healthcare
- Blog
- content-api
- WordPress
website: https://leapcure.com
---
