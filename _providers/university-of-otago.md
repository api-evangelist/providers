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
- description: OUR Archive (Otago University Research Archive) is the University of Otago institutional research repository, now hosted on Ex Libris / Clarivate Esploro. It exposes an OAI-PMH (Open Archives Initiati
  name: OUR Archive OAI-PMH Metadata
  slug: our-archive-oai
- description: The University of Otago operates a SAML 2.0 / Shibboleth Identity Provider (IdP) as a member of the Tuakiri NZ Access Federation, administered by REANNZ. This provides browser-based single sign-on for
  name: Tuakiri Federated Identity (SAML 2.0 / Shibboleth)
  slug: tuakiri-sso
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-otago-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.otago.ac.nz/
- group: other
  title: ''
  type: Repository
  url: https://ourarchive.otago.ac.nz/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-otago/
- group: auth
  title: ''
  type: Authentication
  url: https://ask.otago.ac.nz/knowledgebase/article/KA-10002700/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-otago-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-otago-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-otago-finops.yml
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
  url: json-ld/university-of-otago-context.jsonld
created: '2026-06-03'
description: 'The University of Otago is New Zealand''s oldest university, founded in 1869 and based in Dunedin, ranked #214 in the QS World University Rankings 2025. Its public developer and API footprint is limited and infrastructure-oriented rather than product-oriented: there is no dedicated public developer portal or documented public API program. The most concrete machine interface is OUR Archive (Otago University Research Archive), the institutional research repository now running on Ex Libris / Clarivate Esploro, which exposes a standards-based OAI-PMH endpoint (currently not publicly authorized for harvesting). Identity is provided through the Tuakiri NZ Access Federation using SAML 2.0 / Shibboleth single sign-on. Most administrative, student, course, and timetable systems are gated behind institutional credentials or the campus network and are not openly documented.'
finops:
- name: University Of Otago Finops
  service_category: Education
  slug: university-of-otago-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-otago.png
jsonld:
- class_count: 8
  name: University Of Otago Context
  property_count: 3
  slug: university-of-otago-context
layout: provider
modified: '2026-06-03'
name: University of Otago
nav: Providers
network: true
overview: 'University of Otago publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The University of Otago catalog on APIs.io includes 1 JSON-LD context.


  University of Otago''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: University Of Otago Plans Pricing
  plan_count: 2
  slug: university-of-otago-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 1
  name: University Of Otago Rate Limits
  slug: university-of-otago-rate-limits
score:
  band: emerging
  composite: 20.3
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 13.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-otago/refs/heads/main/screenshots/university-of-otago-2026-06-20T200216.png
security:
- kind: domain-security
  name: University Of Otago Domain Security
  slug: university-of-otago-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-otago
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Repository
- Identity
- New Zealand
website: https://www.otago.ac.nz/
---
