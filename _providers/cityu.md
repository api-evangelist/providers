---
access_model:
  confidence: high
  label: Free · Institutional affiliation required for everything but OAI-PMH
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
  - conformance
  trial: false
  try_now: true
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
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: Public OAI-PMH 2.0 endpoint for CityUHK Scholars, the university's research information system and institutional repository. The Identify verb returns repositoryName "CityUHK Scholars" with records fr
  name: CityUHK Scholars OAI-PMH
  slug: scholars-oai
- description: CityUHK's deployment of the Elsevier Pure REST web service, reachable at https://scholars.cityu.edu.hk/ws/api and gated by an api-key header. The deployment is CityUHK's; the contract is Elsevier's Pu
  name: CityUHK Scholars Pure Web Service (tenant deployment)
  slug: scholars-pure-ws
- description: CityUHK's own SAML 2.0 Identity Provider, running Shibboleth on the university's own host and publishing live IdP metadata with both an IDPSSODescriptor and an AttributeAuthorityDescriptor. Registered
  name: CityUHK Shibboleth Identity Provider
  slug: shibboleth-idp
- description: CityUHK's OpenID Connect and OAuth 2.0 authorization server on the university's own hostname auth.cityu.edu.hk, which CNAMEs to cityu.customdomains.okta.com. Serves an OpenID Connect Discovery 1.0 doc
  name: CityUHK Single Sign-On (OpenID Connect / OAuth 2.0)
  slug: auth-oidc
- description: CityUHK's Canvas tenant. canvas.cityu.edu.hk CNAMEs to cityuhk-vanity.instructure.com and redirects unauthenticated traffic to the university's Okta SSO with a SAMLRequest. The Canvas REST API and LTI
  name: CityUHK Canvas Learning Management System (tenant deployment)
  slug: canvas
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.cityu.edu.hk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cityu
- group: company
  title: ''
  type: LinkedIn
  url: https://hk.linkedin.com/school/cityu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholars.cityu.edu.hk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp2.cityu.edu.hk/idp/shibboleth
- group: other
  title: ''
  type: AIPolicy
  url: https://www.cityu.edu.hk/GenAI/guidelines.htm
- group: build
  title: ''
  type: AITooling
  url: https://www.cityu.edu.hk/GenAI/gpt-services.htm
- group: docs
  title: ''
  type: Documentation
  url: https://www.cityu.edu.hk/its/services-facilities/api-gateway-and-api-management
- group: auth
  title: ''
  type: Authentication
  url: authentication/cityu-authentication.yml
- group: design
  title: ''
  type: x-conformance
  url: conformance/cityu-education-standards-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cityu-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cityu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cityu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cityu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'City University of Hong Kong (CityUHK) is a publicly funded (UGC) research university in Kowloon, Hong Kong SAR. IT Services runs a real API programme — a gateway and API management practice on MuleSoft Anypoint connecting campus systems — but none of it is published or callable outside the university, and there is no public developer portal. The publicly reachable machine-readable footprint is small and, with one exception, TENANTED rather than built: CityUHK Scholars is an Elsevier Pure deployment (scholars.cityu.edu.hk CNAMEs to cityu.elsevierpure.com) with an open OAI-PMH endpoint and a gated REST service on Elsevier''s contract; Canvas is an Instructure tenant; single sign-on is an Okta tenant at auth.cityu.edu.hk. The exception is the one contract CityUHK operates itself: its Shibboleth Identity Provider at idp2.cityu.edu.hk, registered in eduGAIN via the Hong Kong Access Federation. The official GitHub organisation publishes zero public repositories.'
finops:
- name: Cityu Finops
  service_category: Education
  slug: cityu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cityu.png
layout: provider
modified: '2026-08-30'
name: City University of Hong Kong
nav: Providers
network: true
overview: 'City University of Hong Kong publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Hong Kong, and China.


  City University of Hong Kong''s developer surface includes documentation, authentication, and 13 more developer resources.'
plans:
- name: Cityu Plans Pricing
  plan_count: 2
  slug: cityu-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Cityu Rate Limits
  slug: cityu-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 19.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 34
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cityu/refs/heads/main/screenshots/cityu-2026-06-20T174434.png
security:
- kind: authentication
  name: Cityu Authentication
  slug: cityu-authentication
  summary_line: saml/oidc/oauth2/anonymous · 4 schemes
- kind: domain-security
  name: Cityu Domain Security
  slug: cityu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cityu
tags:
- Education
- Higher Education
- University
- Hong Kong
- China
- Research
- Institutional Repository
- OAI-PMH
- Identity Federation
- Research Data
- Learning Management
website: https://www.cityu.edu.hk/
---
