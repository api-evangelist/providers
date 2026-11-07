---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Tegna Agentic Access
  operation_count: 51
  slug: tegna-agentic-access
  summary_line: 51 operations · 33 acting
api_count: 4
apis:
- description: 'A live but undocumented and token-gated API behind Premion''s OTT/CTV advertising platform. Probed 2026-08-13: the host root returns 200 {"message":"App is running"}, /health returns 200, and every pat'
  name: Premion Advertising Platform API (gated)
  slug: tegna-premion-platform-api
- description: 'The public WordPress REST API (wp-json) of the TEGNA website at www.tegna.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: TEGNA Website (WordPress REST)
  slug: tegna-com-website-wordpress-rest
- description: 'The public WordPress REST API (wp-json) of the TEGNA website at premion.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: TEGNA Website (WordPress REST)
  slug: premion-com-website-wordpress-rest
artifact_total: 14
collections:
- collection_type: open
  name: PREMION Content API (WordPress REST)
  slug: open-tegna-premion-content-api
common:
- group: agent
  href: https://artifacts.apis.io/tegna/llms/tegna-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tegna-llms.txt
- group: auth
  href: https://artifacts.apis.io/tegna/authentication/tegna-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tegna-authentication.yml
- group: design
  href: https://artifacts.apis.io/tegna/conventions/tegna-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tegna-conventions.yml
- group: design
  href: https://artifacts.apis.io/tegna/errors/tegna-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tegna-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tegna/data-model/tegna-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tegna-data-model.yml
- group: design
  href: https://artifacts.apis.io/tegna/lifecycle/tegna-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tegna-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tegna/conformance/tegna-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tegna-conformance.yml
- group: build
  href: https://artifacts.apis.io/tegna/packages/tegna-packages.yml
  title: ''
  type: Packages
  url: packages/tegna-packages.yml
- group: agent
  href: https://artifacts.apis.io/tegna/agentic-access/tegna-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tegna-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/tegna/skills/_index.yml
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/tegna/skills/tegna-track-tegna-press-releases.md
  title: ''
  type: AgentSkill
  url: skills/tegna-track-tegna-press-releases.md
- group: agent
  href: https://artifacts.apis.io/tegna/skills/tegna-map-tegna-content-surface.md
  title: ''
  type: AgentSkill
  url: skills/tegna-map-tegna-content-surface.md
- group: auth
  href: https://artifacts.apis.io/tegna/security/tegna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tegna-domain-security.yml
- group: design
  href: https://artifacts.apis.io/tegna/vocabulary/tegna-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tegna-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tegna/rules/tegna-rules.yml
  title: ''
  type: SpectralRules
  url: rules/tegna-rules.yml
- group: commercial
  href: https://artifacts.apis.io/tegna/plans/tegna-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tegna-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tegna/rate-limits/tegna-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tegna-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tegna/finops/tegna-finops.yml
  title: ''
  type: FinOps
  url: finops/tegna-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.tegna.com
- group: company
  title: ''
  type: Website
  url: https://www.nexstar.tv/
- group: other
  title: ''
  type: Advertising
  url: https://www.tegna.com/advertise/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tegna.com/advertise/solutions/digital/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tegna.com/advertise/solutions/broadcast/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tegna.com/advertise/solutions/streaming/
- group: company
  title: ''
  type: Website
  url: https://premion.com/
- group: operate
  title: ''
  type: Support
  url: https://www.tegna.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://tegnadigital.atlassian.net/servicedesk/customer/portal/17
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tegna.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tegna.com/privacy-policy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://premion.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tegna
- group: company
  title: ''
  type: Blog
  url: https://www.tegna.com/press/
- group: company
  title: ''
  type: Blog
  url: https://www.tegna.com/feed/
created: '2026-03-24'
description: 'TEGNA Inc. is an American broadcast, digital media, and marketing services company headquartered in Tysons, Virginia, operating as a subsidiary of Nexstar Media Group following FCC approval of the $6.2 billion acquisition in March 2026. TEGNA operates 64 full-power broadcast television stations across 51 U.S. markets, reaching approximately 39 percent of all television households. Its digital marketing portfolio includes AudienceOne first-party data targeting, OTT/CTV advertising through the Premion platform, and the TEGNA Marketing Solutions full-service agency. TEGNA runs no public developer program and publishes no developer portal: those advertising products are transacted through insertion orders, programmatic deal IDs and agency contracts. The only publicly callable, machine-readable API surfaces TEGNA serves are the WordPress REST content APIs behind its corporate site and premion.com; the Premion advertising platform API at api.premion.com is live but token-gated and
  undocumented.'
finops:
- has_sources: true
  method: generated
  name: Tegna Finops
  primary_unit: ''
  service_category: Media / Advertising
  slug: tegna-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tegna.png
layout: provider
modified: '2026-08-13'
name: TEGNA
nav: Providers
network: true
overview: 'TEGNA publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Broadcasting, Media, Television, Digital Advertising, and OTT.


  The TEGNA catalog on APIs.io includes 2 Spectral governance rulesets.


  TEGNA''s developer surface includes authentication, documentation, support, engineering blog, and 29 more developer resources.'
plans:
- name: Tegna Plans Pricing
  plan_count: 1
  slug: tegna-plans-pricing
press:
- date: ''
  title: Nexstar Media Group's proposed acquisition of Tegna Inc. ...
  url: https://www.facebook.com/12NewsNow/posts/nexstar-media-groups-proposed-acquisition-of-tegna-inc-was-announced-in-august-2/1411894880980522/
- date: ''
  title: 'Ask ChatGPT: Why Should I Advertise with TEGNA?'
  url: https://www.tegna.com/advertise/ask-chatgpt-why-should-i-advertise-with-tegna/
- date: ''
  title: How Local Stations Are Leveraging AI To Increase ...
  url: https://tvnewscheck.com/ai/article/how-local-stations-are-leveraging-ai-to-increase-revenue-and-improve-efficiencies/
- date: ''
  title: Big Tent AI Comments to OMB
  url: https://publicknowledge.org/policy/big-tent-ai-comments-to-omb/
- date: ''
  title: Nexstar Media Group, Inc. Enters into Definitive Agreement ...
  url: https://www.nexstar.tv/nexstar-media-group-inc-enters-into-definitive-agreement-to-acquire-tegna-inc-for-6-2-billion-in-accretive-transaction/
random_paper: 23
rate_limits:
- limit_count: 2
  name: Tegna Rate Limits
  slug: tegna-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: TEGNA — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tegna-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: TEGNA API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: tegna-rules
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 54.0
    catalog_earned_first_party: 8.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 31.8
    contract_quality: 1.7
    developer_ergonomics: 30.4
    discoverability: 69.6
    operational_transparency: 21.1
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
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
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
screenshot: https://apis.io/screenshots/tegna/tegna-2026-06-20T195014.png
security:
- kind: authentication
  name: Tegna Authentication
  slug: tegna-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tegna Domain Security
  slug: tegna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: map-tegna-content-surface
  slug: tegna-map-tegna-content-surface
- name: track-tegna-press-releases
  slug: tegna-track-tegna-press-releases
slug: tegna
tags:
- Broadcasting
- Media
- Television
- Digital Advertising
- OTT
- CTV
- Local News
- content-api
- Fortune 500
website: https://www.tegna.com
---
