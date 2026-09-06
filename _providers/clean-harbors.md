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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 168
  human_in_the_loop: 0
  name: Clean Harbors Agentic Access
  operation_count: 237
  slug: clean-harbors-agentic-access
  summary_line: 237 operations · 168 acting
api_count: 4
apis:
- description: Unauthenticated JSON API over Clean Harbors' open positions, served from the company's own careers host and documented by the company in its published llms.txt. One HTTP GET endpoint selects among fou
  name: Clean Harbors Careers Job Query API
  slug: careers-jobs
- description: Live GraphQL endpoint behind the Safety-Kleen online store and five sibling Clean Harbors brand storefronts (Thermo Fluids, Noble Oil, Emerald Renewable Energy, Murphy's Waste Oil and Synergy Recyclin
  name: Clean Harbors / Safety-Kleen Commerce GraphQL API
  slug: store-graphql
- description: Clean Harbors Online Services (CHOS) — the authenticated web portal where customers create waste profiles, raise drum and bulk service requests, manage on-site waste inventory, and retrieve manifests,
  name: Clean Harbors Customer Portal (CLH SaaS)
  slug: customer-portal
- description: Clean Harbors participates in the EPA's RCRA e-Manifest programme for hazardous-waste manifest tracking. Its own e-Manifest page states the company "is in compliance, initially using the paper manifes
  name: EPA e-Manifest Integration
  slug: e-manifest
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clean-harbors-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clean-harbors
- group: company
  title: ''
  type: Website
  url: https://www.cleanharbors.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cleanharbors.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.cleanharbors.com/contact-us
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clean-harbors-context.jsonld
- group: start
  title: ''
  type: X-CustomerPortal
  url: https://clhsaas.cleanharbors.com/
- group: company
  title: ''
  type: X-SubsidiaryWebsite
  url: https://www.safety-kleen.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.cleanharbors.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cleanharbors.com/terms-of-service
- group: docs
  title: ''
  type: GraphQLSchema
  url: graphql/clean-harbors-store-schema.graphql
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clean-harbors-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/clean-harbors-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clean-harbors-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clean-harbors-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clean-harbors-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clean-harbors-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clean-harbors-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clean-harbors-conformance.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/clean-harbors-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clean-harbors-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clean-harbors-rate-limits.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clean-harbors-agentic-access.yml
- group: build
  title: ''
  type: Examples
  url: examples/clean-harbors-examples.yml
- group: start
  title: ''
  type: SignUp
  url: https://store.safety-kleen.com/customer/account/create/
- group: start
  title: ''
  type: Login
  url: https://clhsaas.cleanharbors.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cleanharbors.com/chos-reference-guides
- group: company
  title: ''
  type: Careers
  url: https://careers.cleanharbors.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cleanharbors.com/about-us/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.cleanharbors.com/about-us/news
- group: other
  title: ''
  type: Sustainability
  url: https://www.cleanharbors.com/sustainability
- group: operate
  title: ''
  type: ContactUs
  url: https://www.cleanharbors.com/contact-us
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Clean_Harbors
- group: other
  title: ''
  type: X
  url: https://twitter.com/cleanharbors
created: '2026-03-23'
description: 'Clean Harbors is the largest provider of environmental and industrial services in North America — hazardous and non-hazardous waste management, emergency response, industrial cleaning, remediation, and used-oil and solvent recycling through its Safety-Kleen subsidiary. It runs no developer programme: no developer portal, no API documentation, no SDK in any registry, no GitHub organisation, and no /.well-known/ document on any host. Customers use the authenticated Clean Harbors Online Services portal at clhsaas.cleanharbors.com and the EPA''s RCRA e-Manifest programme, whose machine-readable surface belongs to the EPA. Two callable contracts nonetheless run on Clean Harbors hosts, both found by direct probing: an anonymous, fully introspectable GraphQL endpoint at store.safety-kleen.com fronting six brand storefronts on one Adobe Commerce instance, and an unauthenticated Job Query API at careers.cleanharbors.com that the company documents in a published llms.txt.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clean-harbors.png
jsonld:
- class_count: 12
  name: Clean Harbors Context
  property_count: 0
  slug: clean-harbors-context
layout: provider
modified: '2026-09-05'
name: Clean Harbors
nav: Providers
network: true
overview: 'Clean Harbors publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Adobe Commerce, Emergency Response, Environmental Services, Fortune 1000, and GraphQL.


  The Clean Harbors catalog on APIs.io includes 1 JSON-LD context.


  Clean Harbors'' developer surface includes support, authentication, code examples, signup flow, documentation, engineering blog, and 29 more developer resources.'
plans:
- name: Clean Harbors Plans Pricing
  plan_count: 0
  slug: clean-harbors-plans-pricing
press:
- date: '2026-05-25'
  title: Form 10-K for Clean Harbors INC filed 02/18/2026
  url: https://ir.cleanharbors.com/static-files/6b594bf5-0d42-431a-ad55-00d59200cb4c
- date: '2026-05-25'
  title: Clean Harbors Announces Acquisition of Terra Nova ...
  url: https://investor.wedbush.com/wedbush/article/bizwire-2026-5-14-clean-harbors-announces-acquisition-of-terra-nova-solutions
- date: '2026-05-25'
  title: 'Hazardous Waste Management: Safety and Compliance'
  url: https://www.waste360.com/hazardous-waste/hazardous-waste-management-safety-and-compliance
- date: '2026-05-25'
  title: First Quarter 2026 Investor Review
  url: https://ir.cleanharbors.com/static-files/e2b1bdd3-68eb-412b-ae86-2f389b7fb5c8
- date: '2026-05-25'
  title: Depot Connect International Streamlines Portfolio with ...
  url: https://www.prnewswire.com/news-releases/depot-connect-international-streamlines-portfolio-with-sale-of-industrial-and-rail-services-to-clean-harbors-302692747.html
random_paper: 11
rate_limits:
- limit_count: 0
  name: Clean Harbors Rate Limits
  slug: clean-harbors-rate-limits
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 48.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 22.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 55.3
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 12.8
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/clean-harbors/refs/heads/main/screenshots/clean-harbors-2026-06-20T174450.png
security:
- kind: authentication
  name: Clean Harbors Authentication
  slug: clean-harbors-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Clean Harbors Domain Security
  slug: clean-harbors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clean-harbors
tags:
- Adobe Commerce
- Emergency Response
- Environmental Services
- Fortune 1000
- GraphQL
- Hazardous Waste
- Industrial Services
- Job Postings
- Manifest Tracking
- Recycling
- Remediation
website: https://www.cleanharbors.com/
---
