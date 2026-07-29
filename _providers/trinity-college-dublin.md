---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: TARA is Trinity College Dublin's open-access institutional repository, built on DSpace. It exposes an OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting) interface for harvesting Dubli
  name: TARA OAI-PMH (Trinity's Access to Research Archive)
  slug: tara-oai
- description: 'Digital Collections is the Library of Trinity College Dublin''s Hyrax/Samvera-based digital asset repository, providing access to digitised manuscripts and collections including the Book of Kells. The '
  name: TCD Digital Collections (IIIF)
  slug: digital-collections-iiif
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trinity-college-dublin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tcd.ie/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TCDLibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/trinity-college-dublin/
- group: build
  title: ''
  type: Library
  url: https://www.tcd.ie/library/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TCDLibrary/TCD-Hyrax-Web-App
- group: auth
  title: ''
  type: Authentication
  url: https://www.heanet.ie/services/identity-access/edugate
- group: commercial
  title: ''
  type: Plans
  url: plans/trinity-college-dublin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trinity-college-dublin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trinity-college-dublin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trinity-college-dublin-context.jsonld
created: '2026-06-03'
description: 'Trinity College Dublin (the University of Dublin) is Ireland''s oldest university, founded in 1592, and ranked #98 in the QS World University Rankings 2025. Its public developer/API footprint is not organized around a dedicated developer portal or a documented open-API program; instead it is expressed through standards-based scholarly infrastructure. The Library of Trinity College Dublin runs TARA (Trinity''s Access to Research Archive), a DSpace institutional repository that exposes an OAI-PMH metadata interface, and Digital Collections, a Hyrax/Samvera platform that serves IIIF Presentation manifests for digitised manuscripts including the Book of Kells. Both are publicly reachable in a browser but currently sit behind bot-mitigation (Cloudflare / reCAPTCHA), so they are not openly machine-callable without interactive access. Federated identity is provided through HEAnet''s Edugate (eduGAIN) SAML federation rather than a public OAuth/OpenID developer API.'
finops:
- name: Trinity College Dublin Finops
  service_category: Education
  slug: trinity-college-dublin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trinity-college-dublin.png
jsonld:
- class_count: 20
  name: Trinity College Dublin Context
  property_count: 2
  slug: trinity-college-dublin-context
layout: provider
modified: '2026-06-03'
name: Trinity College Dublin
nav: Providers
network: true
overview: 'Trinity College Dublin publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Ireland, and Library.


  The Trinity College Dublin catalog on APIs.io includes 1 JSON-LD context.


  Trinity College Dublin''s developer surface includes GitHub presence, authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Trinity College Dublin Plans Pricing
  plan_count: 2
  slug: trinity-college-dublin-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Trinity College Dublin Rate Limits
  slug: trinity-college-dublin-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 13.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trinity-college-dublin/refs/heads/main/screenshots/trinity-college-dublin-2026-06-20T195720.png
security:
- kind: domain-security
  name: Trinity College Dublin Domain Security
  slug: trinity-college-dublin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trinity-college-dublin
tags:
- Education
- Higher Education
- University
- Ireland
- Library
- Repository
- Open Access
- IIIF
- OAI-PMH
website: https://www.tcd.ie/
---
