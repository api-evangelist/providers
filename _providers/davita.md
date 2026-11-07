---
access_model:
  confidence: high
  label: Public · no key, no account, no published plan
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
  score: 8.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the DaVita website at www.davita.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: DaVita Website (WordPress REST)
  slug: davita-com-website-wordpress-rest
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/davita/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Press Release Archive
  url: https://newsroom.davita.com/
- group: auth
  href: https://artifacts.apis.io/davita/authentication/davita-authentication.yml
  title: ''
  type: Authentication
  url: authentication/davita-authentication.yml
- group: auth
  href: https://artifacts.apis.io/davita/security/davita-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/davita-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/davita
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/davita
- group: company
  title: ''
  type: Website
  url: https://www.davita.com
- group: start
  title: ''
  type: Patient Portal
  url: https://www.davita.com/mydavita/
- group: other
  title: ''
  type: Education
  url: https://www.davita.com/education
- group: other
  title: ''
  type: Find a Center
  url: https://davita.com/tools/find-a-dialysis-center/
- group: company
  title: ''
  type: Investor Relations
  url: https://investors.davita.com/
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.davita.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.davita.com/
- group: company
  title: ''
  type: Hospital Partnerships
  url: https://davita.com/partners/hospitals/
- group: company
  title: ''
  type: Physician Partnerships
  url: https://www.davita.com/physicians
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.davita.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.davita.com/terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://newsroom.davita.com/feed/
- group: agent
  href: https://artifacts.apis.io/davita/llms/davita-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/davita-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://davita.com/help-center/
- group: auth
  title: ''
  type: Compliance
  url: https://davita.com/privacy-practices/
- group: design
  href: https://artifacts.apis.io/davita/conventions/davita-conventions.yml
  title: ''
  type: Conventions
  url: conventions/davita-conventions.yml
- group: design
  href: https://artifacts.apis.io/davita/errors/davita-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/davita-problem-types.yml
- group: design
  href: https://artifacts.apis.io/davita/data-model/davita-data-model.yml
  title: ''
  type: DataModel
  url: data-model/davita-data-model.yml
- group: design
  href: https://artifacts.apis.io/davita/lifecycle/davita-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/davita-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/davita/rate-limits/davita-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/davita-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/davita/plans/davita-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/davita-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/davita/conformance/davita-conformance.yml
  title: ''
  type: Conformance
  url: conformance/davita-conformance.yml
- group: agent
  href: https://artifacts.apis.io/davita/mcp/davita-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/davita-mcp.yml
- group: build
  href: https://artifacts.apis.io/davita/packages/davita-packages.yml
  title: ''
  type: Packages
  url: packages/davita-packages.yml
created: '2026-03-21'
description: 'DaVita Inc. is a Fortune 500 kidney care company operating in-center hemodialysis, home hemodialysis, and peritoneal dialysis programs in the United States and abroad, alongside transplant support, integrated kidney care, hospital partnerships, and clinical research. DaVita runs no developer program and publishes no API documentation, but its own web platform serves a live, public, unauthenticated REST API at https://www.davita.com/wp-json/ with a first-party davita/v1 namespace: a dialysis center locator, a Kidney Smart class finder, a USDA-sourced food and nutrient lookup shaped for the kidney diet, and 1,258 kidney-friendly recipes, 570 education articles and a kidney vocabulary alongside them. Clinical integration remains sales-led through payer, hospital and physician partnerships and EHR data exchange; there is no public FHIR endpoint.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/davita.png
layout: provider
modified: '2026-09-05'
name: DaVita
nav: Providers
network: true
overview: 'DaVita publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Chronic Kidney Disease, Dialysis, Fortune 500, Healthcare, and Home Dialysis.


  DaVita''s developer surface includes authentication, engineering blog, support, and 27 more developer resources.'
plans:
- name: Davita Plans Pricing
  plan_count: 0
  slug: davita-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Davita Rate Limits
  slug: davita-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 21.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/davita/davita-2026-06-20T175733.png
security:
- kind: authentication
  name: Davita Authentication
  slug: davita-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Davita Domain Security
  slug: davita-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: davita-find-dialysis-center
  slug: davita-find-dialysis-center
- name: davita-kidney-diet-nutrition
  slug: davita-kidney-diet-nutrition
- name: davita-kidney-education-content
  slug: davita-kidney-education-content
slug: davita
tags:
- Chronic Kidney Disease
- Dialysis
- Fortune 500
- Healthcare
- Home Dialysis
- Hospital Partnerships
- Integrated Kidney Care
- Kidney Care
- Nutrition
- Patient Education
- Recipes
website: https://www.davita.com
---
