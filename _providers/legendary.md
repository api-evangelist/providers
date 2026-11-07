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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Legendary Entertainment website at www.legendary.com: the route index of the site''s content management system, catalogued as one site surface rather than'
  name: Legendary Entertainment Website (WordPress REST)
  slug: legendary-com-website-wordpress-rest
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/legendary/overlays/legendary-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/legendary-wp-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.legendary.com
- group: company
  title: ''
  type: About
  url: https://www.legendary.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.legendary.com/latest-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.legendary.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.legendary.com/about/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.legendary.com/about/privacy/
- group: auth
  href: https://artifacts.apis.io/legendary/authentication/legendary-authentication.yml
  title: ''
  type: Authentication
  url: authentication/legendary-authentication.yml
- group: design
  href: https://artifacts.apis.io/legendary/conventions/legendary-conventions.yml
  title: ''
  type: Conventions
  url: conventions/legendary-conventions.yml
- group: design
  href: https://artifacts.apis.io/legendary/errors/legendary-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/legendary-problem-types.yml
- group: design
  href: https://artifacts.apis.io/legendary/data-model/legendary-data-model.yml
  title: ''
  type: DataModel
  url: data-model/legendary-data-model.yml
- group: design
  href: https://artifacts.apis.io/legendary/lifecycle/legendary-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/legendary-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/legendary/conformance/legendary-conformance.yml
  title: ''
  type: Conformance
  url: conformance/legendary-conformance.yml
- group: agent
  href: https://artifacts.apis.io/legendary/mcp/legendary-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/legendary-mcp.yml
- group: agent
  href: https://artifacts.apis.io/legendary/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/legendary/llms/legendary-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/legendary-llms.txt
- group: auth
  href: https://artifacts.apis.io/legendary/security/legendary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/legendary-domain-security.yml
created: '2026-07-17'
description: 'Legendary Entertainment is a Burbank, California media company that owns, produces and distributes content to worldwide audiences across three divisions: Legendary Pictures (film), Legendary Television and Digital Media, and Legendary Comics. Its productions have grossed more than $20 billion worldwide at the box office, spanning franchises such as Dune, Godzilla and Kong, A Minecraft Movie, Street Fighter, Enola Holmes and Monarch: Legacy of Monsters, with an explicit focus on the fandom demographic. Legendary runs no public developer program and publishes no documented API. It does, however, expose a live, publicly readable WordPress REST API on legendary.com that serves its news posts and its film, television, comics, trailer and digital catalogs as JSON — captured here as a platform-exposed content API rather than a supported product.'
image: https://www.legendary.com/wp-content/uploads/2015/06/home-social1.jpg
layout: provider
modified: '2026-07-19'
name: Legendary Entertainment
nav: Providers
network: true
overview: 'Legendary Entertainment publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Media, Entertainment, and Film.


  Legendary Entertainment''s developer surface includes engineering blog, authentication, and 15 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 17.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/legendary/legendary-2026-07-25T224830.png
security:
- kind: authentication
  name: Legendary Authentication
  slug: legendary-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Legendary Domain Security
  slug: legendary-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: Look up Legendary Entertainment titles and news
  slug: legendary-catalog-lookup
slug: legendary
tags:
- Company
- Consumer
- Media
- Entertainment
- Film
- Television
- Comics
- Content
- Publishing
- WordPress
website: https://www.legendary.com
---
