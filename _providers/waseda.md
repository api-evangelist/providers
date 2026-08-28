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
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for the Waseda University institutional repository, hosted on the NII WEKO/JAIRO Cloud platform. Exposes journal articles, dissertations, bulletin papers, work
  name: Waseda University Repository (OAI-PMH)
  slug: repository-oai
- description: 'Waseda University Library''s discovery service (WINE) runs on the Ex Libris Primo/Alma platform, institution code 81SOKEI_WUNI. The underlying Primo platform supports programmatic search via the Primo '
  name: WINE Library Discovery (Ex Libris Primo)
  slug: wine-primo
- description: Waseda's institutional single sign-on is provided through a Shibboleth SAML Identity Provider, used to authenticate access to MyWaseda and federated services. The IdP metadata/SSO endpoint is reachabl
  name: Waseda Identity Provider (Shibboleth SAML SSO)
  slug: shibboleth-sso
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waseda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.waseda.jp/top/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wasedatime
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/wasedauniversity/
- group: auth
  title: ''
  type: Authentication
  url: https://iaidp.ia.waseda.jp/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/waseda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/waseda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/waseda-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Waseda University is a leading private research university in Tokyo, Japan, ranked #181 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on scholarly infrastructure rather than a dedicated developer portal: the Waseda University Repository exposes an OAI-PMH 2.0 metadata interface (hosted on the NII WEKO/JAIRO Cloud), and the library''s WINE discovery service runs on the Ex Libris Primo/Alma platform (institution code 81SOKEI_WUNI), which provides standard Primo and SRU interfaces. Identity is handled via Shibboleth SAML SSO. There is no single official Waseda University GitHub organization; an unofficial student project (WasedaTime) operates a community syllabus/timetable backend that is not publicly documented.'
finops:
- name: Waseda Finops
  service_category: Education
  slug: waseda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waseda.png
jsonld:
- class_count: 23
  name: Waseda Context
  property_count: 1
  slug: waseda-context
layout: provider
modified: '2026-06-03'
name: Waseda University
nav: Providers
network: true
overview: 'Waseda University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Waseda University catalog on APIs.io includes 1 JSON-LD context.


  Waseda University''s developer surface includes GitHub presence, authentication, and 7 more developer resources.'
plans:
- name: Waseda Plans Pricing
  plan_count: 2
  slug: waseda-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Waseda Rate Limits
  slug: waseda-rate-limits
score:
  band: emerging
  composite: 23.2
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/waseda/refs/heads/main/screenshots/waseda-2026-06-20T201241.png
security:
- kind: domain-security
  name: Waseda Domain Security
  slug: waseda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: waseda
tags:
- Education
- Higher Education
- University
- Research
- Library
- Open Access
- Japan
website: https://www.waseda.jp/top/en/
---
