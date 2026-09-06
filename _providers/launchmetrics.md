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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-05'
api_count: 5
apis:
- description: Search API for Launchmetrics publications. GET/POST /documents runs a Lucene-syntax query across the indexed publication corpus with filters for period, channel type, topic path, language, country and
  name: Launchmetrics Search API
  slug: launchmetrics-search
- description: Document retrieval API. GET/POST /documents/{ids} returns full publication documents by id with optional response_type and highlight controls; /socialMediaSearch resolves a social media URL to its doc
  name: Launchmetrics Documents API
  slug: launchmetrics-documents
- description: Version 2 of the Launchmetrics document retrieval API, served on its own URI-path version. GET /documents/{ids} and POST /documents retrieve publication documents by identifier. Shares the NAP envelop
  name: Launchmetrics Documents v2 API
  slug: launchmetrics-documents-v2
- description: Media-outlet API. GET/POST /medias/{ids} retrieves online media outlets by id; /medias/search searches online media by query with response_type and limit; /medias/print/search searches the print media
  name: Launchmetrics Medias API
  slug: launchmetrics-medias
- description: Audit log API. GET /auditlogs/{team}{group}{id} returns audit log entries scoped by team, group and object id with type, limit and sort parameters, alongside the standard /ping and /stats health opera
  name: Launchmetrics Auditlogs API
  slug: launchmetrics-auditlogs
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/launchmetrics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://launchmetrics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nap.launchmetrics.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://nap.launchmetrics.com/docs
- group: operate
  title: ''
  type: Support
  url: https://help.launchmetrics.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.launchmetrics.com/
- group: company
  title: ''
  type: Blog
  url: https://www.launchmetrics.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/launchmetrics
- group: commercial
  title: ''
  type: Pricing
  url: https://www.launchmetrics.com/launchmetrics-pricing-solutions
- group: start
  title: ''
  type: Login
  url: https://connect.launchmetrics.com/Account/Login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://connect.launchmetrics.com/Home/en/GeneralTerms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.launchmetrics.com/en/product-portal-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.launchmetrics.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/launchmetrics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/launchmetrics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/launchmetrics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/launchmetrics-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/launchmetrics-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/launchmetrics-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/launchmetrics-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/launchmetrics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/launchmetrics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/launchmetrics-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/launchmetrics-api-catalog.json
- group: commercial
  title: ''
  type: Plans
  url: plans/launchmetrics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/launchmetrics-rate-limits.yml
created: '2026-08-17'
description: Launchmetrics is the Brand Performance Cloud for the fashion, luxury and beauty (FLB) industries, formed from Fashion GPS and Augure and headquartered in Paris and New York. Its SaaS platform bundles Discover (PR and social media monitoring), Insights (brand performance benchmarking and Media Impact Value), Samples (product sample tracking and logistics), Events (event, RSVP and seating management), Contacts (contact and mailing management) and Spotlight (visual asset galleries). Launchmetrics publishes a small, public REST API reference at nap.launchmetrics.com/docs covering five services — Search, Documents, Documents v2, Medias and Auditlogs — that expose the publication, media-outlet and audit-log data behind Discover and Insights. Requests are authenticated with an app_id issued by Launchmetrics R&D, optionally strengthened with an HMAC-SHA1 request signature. A separate Events API is marketed as a CRM connector but is sales-gated with no public reference.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-17'
name: Launchmetrics
nav: Providers
network: true
overview: 'Launchmetrics publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Marketing, Public Relations, and Media Monitoring.


  Launchmetrics'' developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Launchmetrics Plans Pricing
  plan_count: 0
  slug: launchmetrics-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Launchmetrics Rate Limits
  slug: launchmetrics-rate-limits
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 20.5
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/launchmetrics/refs/heads/main/screenshots/launchmetrics-2026-09-02T150220.png
security:
- kind: authentication
  name: Launchmetrics Authentication
  slug: launchmetrics-authentication
  summary_line: apiKey/custom-signature · 2 schemes
- kind: domain-security
  name: Launchmetrics Domain Security
  slug: launchmetrics-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Launchmetrics Vulnerability Disclosure
  slug: launchmetrics-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: launchmetrics
tags:
- Company
- Software-as-a-Service
- Marketing
- Public Relations
- Media Monitoring
- Social-Media
- Analytics
- Fashion
- Luxury
- Beauty
- Brand Performance
- Event Management
- Search
website: https://launchmetrics.com/
---
