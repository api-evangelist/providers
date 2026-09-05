---
access_model:
  confidence: high
  label: Enterprise · Contact sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 355
  human_in_the_loop: 3
  name: Tegna Agentic Access
  operation_count: 657
  slug: tegna-agentic-access
  summary_line: 657 operations · 355 acting · 3 human-in-the-loop
api_count: 4
apis:
- description: 'A live but undocumented and token-gated API behind Premion''s OTT/CTV advertising platform. Probed 2026-08-13: the host root returns 200 {"message":"App is running"}, /health returns 200, and every pat'
  name: Premion Advertising Platform API (gated)
  slug: tegna-premion-platform-api
- baseURL: https://www.tegna.com/wp-json
  baseurl_source: declared
  description: WordPress REST namespace `aioseo/v1` (137 operations).
  name: TEGNA Aioseo/v1 API
  slug: tegna-aioseo-v1-api
- baseURL: https://www.tegna.com/wp-json
  baseurl_source: declared
  description: WordPress REST namespace `contact-form-7/v1` (9 operations).
  name: TEGNA Contact Form 7/v1 API
  slug: tegna-contact-form-7-v1-api
- baseURL: https://www.tegna.com/wp-json
  baseurl_source: declared
  description: WordPress REST namespace `oembed/1.0` (3 operations).
  name: TEGNA Oembed/1.0 API
  slug: tegna-oembed-1-0-api
- baseURL: https://www.tegna.com/wp-json
  baseurl_source: declared
  description: WordPress REST namespace `wp-abilities/v1` (8 operations).
  name: TEGNA Wp Abilities/v1 API
  slug: tegna-wp-abilities-v1-api
- baseURL: https://www.tegna.com/wp-json
  baseurl_source: declared
  description: WordPress REST namespace `wp/v2` (209 operations).
  name: TEGNA Wp/v2 API
  slug: tegna-wp-v2-api
- baseURL: https://www.tegna.com/wp-json
  baseurl_source: declared
  description: WordPress REST namespace `yoast/v1` (51 operations).
  name: TEGNA Yoast/v1 API
  slug: tegna-yoast-v1-api
artifact_total: 17
collections:
- collection_type: open
  name: TEGNA Content API (WordPress REST)
  slug: open-tegna-content-api
- collection_type: open
  name: PREMION Content API (WordPress REST)
  slug: open-tegna-premion-content-api
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tegna-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tegna-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tegna-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tegna-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tegna-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tegna-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tegna-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/tegna-packages.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tegna-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/tegna-track-tegna-press-releases.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/tegna-map-tegna-content-surface.md
- group: other
  title: ''
  type: Overlay
  url: overlays/tegna-content-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tegna-domain-security.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tegna-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/tegna-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tegna-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tegna-rate-limits.yml
- group: commercial
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
- name: Tegna Finops
  service_category: Media / Advertising
  slug: tegna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tegna.png
layout: provider
modified: '2026-08-13'
name: TEGNA
nav: Providers
network: true
overview: 'TEGNA publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Aioseo/v1 API, Contact Form 7/v1 API, Oembed/1.0 API, and 3 more. Tagged areas include Broadcasting, Media, Television, Digital Advertising, and OTT.


  The TEGNA catalog on APIs.io includes 2 Spectral governance rulesets.


  TEGNA''s developer surface includes authentication, documentation, support, engineering blog, and 30 more developer resources.'
plans:
- name: Tegna Plans Pricing
  plan_count: 1
  slug: tegna-plans-pricing
press:
- date: '2026-05-25'
  title: Nexstar Media Group's proposed acquisition of Tegna Inc. ...
  url: https://www.facebook.com/12NewsNow/posts/nexstar-media-groups-proposed-acquisition-of-tegna-inc-was-announced-in-august-2/1411894880980522/
- date: '2026-05-25'
  title: 'Ask ChatGPT: Why Should I Advertise with TEGNA?'
  url: https://www.tegna.com/advertise/ask-chatgpt-why-should-i-advertise-with-tegna/
- date: '2026-05-25'
  title: How Local Stations Are Leveraging AI To Increase ...
  url: https://tvnewscheck.com/ai/article/how-local-stations-are-leveraging-ai-to-increase-revenue-and-improve-efficiencies/
- date: '2026-05-25'
  title: Big Tent AI Comments to OMB
  url: https://publicknowledge.org/policy/big-tent-ai-comments-to-omb/
- date: '2026-05-25'
  title: Nexstar Media Group, Inc. Enters into Definitive Agreement ...
  url: https://www.nexstar.tv/nexstar-media-group-inc-enters-into-definitive-agreement-to-acquire-tegna-inc-for-6-2-billion-in-accretive-transaction/
random_paper: 2
rate_limits:
- limit_count: 2
  name: Tegna Rate Limits
  slug: tegna-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TEGNA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tegna-jsonschema-spectral-rules
- effective_rule_count: 51
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
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.5
    catalog_earned_first_party: 8.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 33.3
    contract_quality: 15.1
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 21.1
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tegna/refs/heads/main/screenshots/tegna-2026-06-20T195014.png
security:
- kind: authentication
  name: Tegna Authentication
  slug: tegna-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tegna Domain Security
  slug: tegna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
