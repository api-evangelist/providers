---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brinker-international-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brinker.com
- group: company
  title: Chili's Grill & Bar
  type: Website
  url: https://www.chilis.com
- group: company
  title: Maggiano's Little Italy
  type: Website
  url: https://www.maggianos.com
- group: start
  title: Partner API Developer Portal (SSO-gated)
  type: DeveloperPortal
  url: https://developer.brinker.com
- group: start
  title: Franchise Partner Portal (login)
  type: Portal
  url: https://franchise.brinker.com
- group: company
  title: Domestic Franchising
  type: Partners
  url: https://brinker.com/franchise/domestic
- group: other
  title: Investor Relations
  type: Resources
  url: https://investors.brinker.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brinker-international
- group: auth
  title: Authentication + onboarding profile (Apigee key/secret, approval-gated)
  type: Authentication
  url: authentication/brinker-international-authentication.yml
- group: commercial
  title: Plans + pricing (none published — partner entitlement only)
  type: Plans
  url: plans/brinker-international-plans-pricing.yml
- group: operate
  title: Rate limits (none published)
  type: RateLimits
  url: rate-limits/brinker-international-rate-limits.yml
- group: agent
  title: llms.txt (generated)
  type: LLMsTxt
  url: llms/brinker-international-llms.txt
- group: start
  title: Developer Portal account registration
  type: SignUp
  url: https://developer.brinker.com/accounts/create
- group: operate
  title: Developer Portal FAQs
  type: Support
  url: https://developer.brinker.com/faqs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brinker.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brinker.com/terms-and-conditions
coverage:
  checked: '2026-09-04'
  detail: Brinker's Apigee developer portal answers HTTP 401 "No authorization header provided" on /portals/api/sites/brinker-portal/apidocs, and its anonymous catalog endpoint returns an empty apiDocs/apiProducts list, so the six API product families its QA site names (LoyaltyEA, Promos, ITSM ServiceNow, GMS, OrderManagement, POS) have no readable contract without a Brinker-API-Team-approved account.
  evidence:
  - status: 401
    url: https://developer.brinker.com/portals/api/sites/brinker-portal/apidocs
  - status: 200
    url: https://developer.brinker.com/portals/api/sites/brinker-portal/liveportal/apis
  - status: 200
    url: https://developerqa.brinker.com/portals/api/sites/brinkerqa-portal/liveportal/apis
  - status: 404
    url: https://api.brinker.com/
  reason: partner-login
  state: gated
created: '2026-03-23'
description: 'Brinker International is a leading casual dining restaurant company that owns, operates, and franchises Chili''s Grill & Bar and Maggiano''s Little Italy. Headquartered in Dallas, Texas, Brinker operates over 1,600 Chili''s locations across 29 countries and over 50 Maggiano''s locations in the United States. The company leverages digital ordering platforms, loyalty programs, mobile apps, in-restaurant kiosks, and point-of-sale integrations for restaurant operations, running a unified open-source e-commerce environment built on Red Hat (RHEL, Satellite, Lightspeed) and using Prismic CMS for digital content management. Brinker runs a real but entirely partner-facing API program on Google Apigee: an Apigee Edge gateway at api.brinker.com and an Apigee Integrated Developer Portal at developer.brinker.com whose API catalog is approval-gated (accounts are approved by the Brinker API Team and API Products assigned by entitlement). The portal''s anonymous catalog endpoint returns an
  empty apiDocs/apiProducts list; its QA sibling names six API product families — LoyaltyEA, Promos, ITSM ServiceNow, GMS, OrderManagement and POS — but exposes no paths, schemas or base URLs. There is no public, self-service developer API, OpenAPI specification, SDK, MCP server, agent card, or open GitHub organization. Consumer-facing surfaces are the Chili''s and Maggiano''s mobile apps and websites and their loyalty programs, with online ordering powered by Olo and site content by Prismic.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brinker-international.png
layout: provider
modified: '2026-09-04'
name: Brinker International
nav: Providers
network: true
overview: 'Brinker International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Casual Dining, Food Service, Franchise, and Chilis.


  Brinker International''s developer surface includes developer portal, authentication, signup flow, support, and 13 more developer resources.'
plans:
- name: Brinker International Plans Pricing
  plan_count: 0
  slug: brinker-international-plans-pricing
press:
- date: '2026-05-25'
  title: BRINKER INTERNATIONAL REPORTS FIRST QUARTER ...
  url: https://www.prnewswire.com/news-releases/brinker-international-reports-first-quarter-of-fiscal-2026-results-and-reiterates-fiscal-2026-guidance-302597831.html
- date: '2026-05-25'
  title: 'Case Study: Brinker International'
  url: https://blackboxintelligence.com/resources/case-studies/case-study-brinker-international/
- date: '2026-05-25'
  title: Financials - Quarterly Results
  url: https://investors.brinker.com/financials/quarterly-results/default.aspx
- date: '2026-05-25'
  title: Brinker makes dining digital with Red Hat
  url: https://www.redhat.com/en/success-stories/brinker
- date: '2026-05-25'
  title: BRINKER INTERNATIONAL REPORTS THIRD QUARTER ...
  url: https://www.prnewswire.com/news-releases/brinker-international-reports-third-quarter-of-fiscal-2026-results-and-updates-fiscal-2026-guidance-302756567.html
random_paper: 10
rate_limits:
- limit_count: 0
  name: Brinker International Rate Limits
  slug: brinker-international-rate-limits
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/brinker-international/refs/heads/main/screenshots/brinker-international-2026-06-20T173707.png
security:
- kind: authentication
  name: Brinker International Authentication
  slug: brinker-international-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Brinker International Domain Security
  slug: brinker-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brinker-international
tags:
- Restaurant
- Casual Dining
- Food Service
- Franchise
- Chilis
- Maggianos
- Fortune 1000
website: https://www.brinker.com
---
