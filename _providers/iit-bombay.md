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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: 'An OAuth 2.0 (RFC 6749) identity and profile API operated by the IIT Bombay Students'' Gymkhana. It exposes authorization, token, and token-revocation endpoints plus a user resource endpoint returning '
  name: Gymkhana Profiles OAuth API
  slug: gymkhana-profiles
- description: A session-based Single Sign-On service maintained by the Institute Technical Council (ITC) for authenticating IIT Bombay users in student and club projects. A redirect-based ssocall flow returns an ac
  name: ITC Single Sign-On API
  slug: itc-sso
- description: The IIT Bombay Central Library institutional repository is built on DSpace and exposes an OAI-PMH 2.0 metadata harvesting interface over its theses, journal articles, and conference papers. The Identi
  name: DSpace Institutional Repository OAI-PMH
  slug: dspace-oai-pmh
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iit-bombay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iitb.ac.in/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/DevCom-IITB
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/indian-institute-of-technology-bombay/
- group: commercial
  title: ''
  type: Plans
  url: plans/iit-bombay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iit-bombay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iit-bombay-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Indian Institute of Technology Bombay (IIT Bombay), founded in 1958 and located in Powai, Mumbai, is one of India''s premier engineering and research institutions, ranked #97 in the QS World University Rankings 2025. Its public developer footprint is largely student- and community-driven rather than a central institutional API program: the Students'' Gymkhana operates an OAuth 2.0 "Profiles" identity API, the Institute Technical Council runs an ITC Single Sign-On service, and the Central Library exposes an OAI-PMH 2.0 interface over its DSpace institutional repository. No unified central developer portal was found; access to several APIs is gated to IIT Bombay infrastructure.'
finops:
- name: Iit Bombay Finops
  service_category: Education
  slug: iit-bombay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iit-bombay.png
jsonld:
- class_count: 29
  name: Iit Bombay Context
  property_count: 0
  slug: iit-bombay-context
layout: provider
modified: '2026-06-03'
name: Indian Institute of Technology Bombay
nav: Providers
network: true
overview: 'Indian Institute of Technology Bombay publishes 1 API on the [APIs.io](https://apis.io/) network: DSpace Institutional Repository OAI-PMH. Tagged areas include Education, Higher Education, University, Research, and India.


  The Indian Institute of Technology Bombay catalog on APIs.io includes 1 JSON-LD context.


  Indian Institute of Technology Bombay''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: Iit Bombay Plans Pricing
  plan_count: 2
  slug: iit-bombay-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Iit Bombay Rate Limits
  slug: iit-bombay-rate-limits
score:
  band: emerging
  composite: 25.4
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 39.4
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iit-bombay/refs/heads/main/screenshots/iit-bombay-2026-06-20T183229.png
security:
- kind: domain-security
  name: Iit Bombay Domain Security
  slug: iit-bombay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iit-bombay
tags:
- Education
- Higher Education
- University
- Research
- India
- Open Access
- Identity
website: https://www.iitb.ac.in/
---
