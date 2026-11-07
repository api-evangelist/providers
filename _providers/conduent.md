---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Knowledge Connection (marketed to learners as Learner Community) is Conduent's learning platform, deployed one portal per customer on a subdomain of knowledgeconnection.conduent.com; the base URL is t
  name: Conduent Knowledge Connection
  slug: conduent-knowledge-connection
artifact_total: 6
asyncapis:
- description: ''
  name: Conduent Knowledge Connection Webhooks
  slug: conduent-knowledge-connection-webhooks
common:
- group: other
  href: https://artifacts.apis.io/conduent/hosts/conduent-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conduent-hosts.yml
- group: build
  href: https://artifacts.apis.io/conduent/integrations/conduent-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/conduent-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/conduent/vendors/conduent-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conduent-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/conduent/finops/conduent-finops.yml
  title: ''
  type: FinOps
  url: finops/conduent-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.news.conduent.com/rss.xml
- group: auth
  href: https://artifacts.apis.io/conduent/security/conduent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conduent-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Conduent
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/conduent
- group: company
  title: ''
  type: Website
  url: https://www.conduent.com
- group: company
  title: ''
  type: Blog
  url: https://insights.conduent.com/conduent-blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.news.conduent.com/
- group: other
  title: ''
  type: Leadership
  url: https://www.conduent.com/conduent-leadership/
- group: operate
  title: ''
  type: Support
  url: https://www.conduent.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.conduent.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.conduent.com/website-terms-and-conditions/
- group: design
  href: https://artifacts.apis.io/conduent/asyncapi/conduent-knowledge-connection-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/conduent-knowledge-connection-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/conduent/changelog/conduent-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/conduent-changelog.yml
- group: design
  href: https://artifacts.apis.io/conduent/lifecycle/conduent-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/conduent-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/conduent/conformance/conduent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/conduent-conformance.yml
- group: design
  href: https://artifacts.apis.io/conduent/conventions/conduent-conventions.yml
  title: ''
  type: Conventions
  url: conventions/conduent-conventions.yml
- group: other
  href: https://artifacts.apis.io/conduent/regulatory/conduent-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/conduent-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/conduent/regulatory/conduent-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/conduent-regulatory-posture.yml
- group: commercial
  href: https://artifacts.apis.io/conduent/plans/conduent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/conduent-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/conduent/rate-limits/conduent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/conduent-rate-limits.yml
coverage:
  checked: '2026-10-19'
  detail: 'Conduent sells BPO and managed services, not software with a developer program: both hosts the record named -- api.conduent.com and developer.conduent.com -- return NXDOMAIN, and full contract discovery across www.conduent.com, insights.conduent.com and the Knowledge Connection help host found no OpenAPI, GraphQL, MCP, agent card or well-known document; the only public integration surface is the Knowledge Connection webhook event list.'
  evidence:
  - status: NXDOMAIN
    url: https://developer.conduent.com
  - status: NXDOMAIN
    url: https://api.conduent.com
  - status: 404
    url: https://www.conduent.com/openapi.json
  - status: 404
    url: https://www.conduent.com/llms.txt
  - status: 404
    url: https://www.conduent.com/.well-known/security.txt
  - status: 200
    url: https://help.knowledgeconnection.conduent.info/help/admin/integrations/webhooks
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'Conduent Incorporated (Nasdaq: CNDT) is a US business process services and solutions company headquartered in Florham Park, New Jersey, delivering customer experience management, finance and procurement, human capital, integrated digital solutions, legal and compliance analytics, government and Medicaid services, transportation and tolling, banking and lending, and healthcare business solutions. Its work is sold as managed services and BPO engagements rather than as a self-serve software product: Conduent publishes no developer portal, no API reference and no machine-readable contract, and programmatic access is provisioned inside enterprise services contracts. The one publicly documented interface is the webhook event catalog of its Knowledge Connection learning platform.'
finops:
- has_sources: true
  method: generated
  name: Conduent Finops
  primary_unit: ''
  service_category: Business Process Services
  slug: conduent-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/conduent.png
layout: provider
modified: '2026-10-06'
name: Conduent
nav: Providers
network: true
overview: 'Conduent is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business Process Services, Technology, Government, Healthcare, and Transportation.


  The Conduent catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Conduent''s developer surface includes engineering blog, support, changelog, and 21 more developer resources.'
plans:
- name: Conduent Plans Pricing
  plan_count: 1
  slug: conduent-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Conduent Rate Limits
  slug: conduent-rate-limits
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 16.7
    discoverability: 67.9
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 32.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/conduent/conduent-2026-07-25T210242.png
security:
- kind: domain-security
  name: Conduent Domain Security
  slug: conduent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conduent
tags:
- Business Process Services
- Technology
- Government
- Healthcare
- Transportation
- Financial Services
- Customer Experience
- Learning
- Webhook
website: https://www.conduent.com
---
