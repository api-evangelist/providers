---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 85
  human_in_the_loop: 0
  name: Boston Properties Agentic Access
  operation_count: 193
  slug: boston-properties-agentic-access
  summary_line: 193 operations · 85 acting
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Boston Properties (BXP) website at www.bxp.com: the route index of the site''s content management system, catalogued as one site surface rather than as se'
  name: Boston Properties (BXP) Website (WordPress REST)
  slug: bxp-com-website-wordpress-rest
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/boston-properties/conventions/boston-properties-conventions.yml
  title: ''
  type: Conventions
  url: conventions/boston-properties-conventions.yml
- group: design
  href: https://artifacts.apis.io/boston-properties/errors/boston-properties-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boston-properties-problem-types.yml
- group: design
  href: https://artifacts.apis.io/boston-properties/lifecycle/boston-properties-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/boston-properties-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/boston-properties/conformance/boston-properties-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boston-properties-conformance.yml
- group: design
  href: https://artifacts.apis.io/boston-properties/data-model/boston-properties-data-model.yml
  title: ''
  type: DataModel
  url: data-model/boston-properties-data-model.yml
- group: operate
  href: https://artifacts.apis.io/boston-properties/rate-limits/boston-properties-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/boston-properties-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/boston-properties/plans/boston-properties-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boston-properties-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/boston-properties/llms/boston-properties-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boston-properties-llms.txt
- group: agent
  href: https://artifacts.apis.io/boston-properties/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/boston-properties/mcp/boston-properties-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/boston-properties-mcp.yml
- group: agent
  href: https://artifacts.apis.io/boston-properties/well-known/boston-properties-well-known.yml
  title: ''
  type: x-well-known-probe
  url: well-known/boston-properties-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bxp.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bxp.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.bxp.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bxp.com/news/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.bxp.com/contact
- group: agent
  href: https://artifacts.apis.io/boston-properties/agentic-access/boston-properties-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/boston-properties-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/boston-properties/authentication/boston-properties-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boston-properties-authentication.yml
- group: auth
  href: https://artifacts.apis.io/boston-properties/security/boston-properties-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boston-properties-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boston-properties
- group: company
  title: ''
  type: Website
  url: https://www.bxp.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.bxp.com
- group: other
  title: ''
  type: Properties
  url: https://www.bxp.com/properties
- group: company
  title: ''
  type: Careers
  url: https://edxn.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/
- group: operate
  title: ''
  type: Contact
  url: https://www.bxp.com/contact
created: '2026-03-23'
description: 'BXP (formerly Boston Properties) is the largest publicly traded developer, owner, and manager of premier workplaces in the United States. The company develops, owns, and manages Class A office properties across six major U.S. markets: Boston, Los Angeles, New York, San Francisco, Seattle, and Washington DC. BXP is a self-administered and self-managed REIT focused on premier urban workspace.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boston-properties.png
layout: provider
modified: '2026-09-04'
name: Boston Properties (BXP)
nav: Providers
network: true
overview: 'Boston Properties (BXP) publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Website (WordPress REST). Tagged areas include Real Estate, Commercial Real Estate, REIT, Office Properties, and Workplace.


  The Boston Properties (BXP) catalog on APIs.io includes 1 Spectral governance ruleset.


  Boston Properties (BXP)''s developer surface includes engineering blog, support, authentication, and 22 more developer resources.'
plans:
- name: Boston Properties Plans Pricing
  plan_count: 0
  slug: boston-properties-plans-pricing
press:
- date: ''
  title: AI drives leasing demand at Boston Properties top-tier ...
  url: https://www.linkedin.com/posts/wilcatlin_ai-officesearch-tenantadvisory-activity-7457389515394113537-XF04
- date: ''
  title: Form 10-Q for Boston Properties INC filed 11/07/2023
  url: https://investors.bxp.com/static-files/e2f64ceb-3595-48f4-a4c9-a528fb752ab3
- date: ''
  title: Piper Sandler reiterates Boston Properties stock rating on ...
  url: https://www.investing.com/news/analyst-ratings/piper-sandler-reiterates-boston-properties-stock-rating-on-ai-demand-93CH-4692668
- date: ''
  title: Nantum OS by Prescriptive Data Named Sustainability ...
  url: https://www.nantum.ai/press-releases/nantum-os-by-prescriptive-data-named-sustainability-product-of-the-year
- date: ''
  title: BXP CEO Owen Thomas discusses how AI companies are ...
  url: https://www.facebook.com/cnbc/posts/bxp-ceo-owen-thomas-discusses-how-ai-companies-are-increasing-the-demand-for-off/1234538748547516/
random_paper: 7
rate_limits:
- limit_count: 0
  name: Boston Properties Rate Limits
  slug: boston-properties-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Boston Properties (BXP) API Rules
  rule_count: 62
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 4
  slug: boston-properties-rules
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 25.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 24.9
  provenance:
    agentic_access: derived
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
screenshot: https://apis.io/screenshots/boston-properties/boston-properties-2026-06-20T173614.png
security:
- kind: authentication
  name: Boston Properties Authentication
  slug: boston-properties-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Boston Properties Domain Security
  slug: boston-properties-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: boston-properties-monitor-site-changes
  slug: boston-properties-monitor-site-changes
- name: boston-properties-search-site-content
  slug: boston-properties-search-site-content
slug: boston-properties
tags:
- Real Estate
- Commercial Real Estate
- REIT
- Office Properties
- Workplace
- Fortune 1000
website: https://www.bxp.com
---
