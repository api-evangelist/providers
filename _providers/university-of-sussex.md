---
access_model:
  confidence: high
  label: Affiliation-gated · no public developer registration
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
  - probe
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
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: The university's own Shibboleth IdP, publishing signed SAML 2.0 metadata as a machine-readable EntityDescriptor. entityID https://idp.sussex.ac.uk/shibboleth, shibmd:Scope sussex.ac.uk, IDPSSODescript
  name: University of Sussex Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: identity-federation
- description: Sussex's Okta organization, reached on the Sussex-branded hostname okta.sussex.ac.uk, which CNAMEs to sussexac.customdomains.okta.com. It serves a complete OpenID Connect discovery document (issuer ht
  name: University of Sussex Single Sign-On (Okta tenant)
  slug: okta-sso
- description: Sussex's virtual learning environment, an Instructure Canvas deployment on the university's own hostname canvas.sussex.ac.uk, which CNAMEs to universityofsussex-vanity.instructure.com. The Canvas REST
  name: University of Sussex Canvas VLE (Instructure tenant)
  slug: canvas-vle
- description: 'Sussex''s institutional research repository, a Figshare tenant at sussex.figshare.com (CNAME to figshare.com). The relationship is independently confirmed by DataCite, where the university is a member '
  name: University of Sussex Research Data Repository (Figshare tenant)
  slug: figshare-repository
- description: Library discovery for Sussex runs on Ex Libris Primo VE as institution view 44SUS_INST / 44SUS_VU1, hosted on the vendor's shared platform at sussex.primo.exlibrisgroup.com. Sussex owns the view and t
  name: University of Sussex Library Discovery (Ex Libris Primo tenant)
  slug: primo-discovery
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.sussex.ac.uk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.sussex.ac.uk/idp/shibboleth
- group: design
  title: ''
  type: SAMLMetadata
  url: authentication/university-of-sussex-idp-saml-metadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://sussex.figshare.com/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://sussex.primo.exlibrisgroup.com/discovery/search?vid=44SUS_INST:44SUS_VU1
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.sussex.ac.uk/study/undergraduate/courses
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.sussex.ac.uk/its/services/research/highperformance
- group: docs
  title: ''
  type: Documentation
  url: https://www.sussex.ac.uk/its/about/servicedescriptions
- group: operate
  title: ''
  type: Support
  url: https://www.sussex.ac.uk/its/help/
- group: company
  title: ''
  type: Blog
  url: https://www.sussex.ac.uk/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sussex.ac.uk/about/website/privacy-and-cookies/privacy
- group: other
  title: ''
  type: Accessibility
  url: https://www.sussex.ac.uk/about/website/accessibility
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/universityofsussex
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-sussex/
- group: other
  title: ''
  type: Publications
  url: https://www.sussex.ac.uk/research/publications
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-sussex-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-sussex-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-sussex-domain-standards.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-sussex-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-sussex-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-sussex-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-sussex-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Sussex operates exactly one machine-readable contract of its own — the Shibboleth SAML 2.0 identity-provider metadata at idp.sussex.ac.uk, whose host CNAMEs to a Sussex-run Azure instance (uos-idp-shib-prod.uksouth.cloudapp.azure.com), not to a vendor. Every other programmable surface reachable under a Sussex name is a vendor platform on a Sussex-branded hostname: okta.sussex.ac.uk CNAMEs to sussexac.customdomains.okta.com, canvas.sussex.ac.uk to universityofsussex-vanity.instructure.com, sussex.figshare.com to figshare.com, and library discovery is an Ex Libris Primo view (44SUS_INST). There is no developer portal, no institution-authored OpenAPI, no open-data portal (data.sussex.ac.uk and api.sussex.ac.uk do not resolve), and the GitHub organization has zero public repositories. One probe was blocked rather than answered: sussex.figshare.com returns an AWS WAF challenge (HTTP 202, x-amzn-waf-action: challenge, empty body) to every request including ?verb=Identify, so the Figshare
    tenant''s OAI-PMH endpoint could not be confirmed either way. This profile previously carried ten OpenAPIs and thirty-eight artifacts derived from them; all ten were Figshare''s generic v2 contract with an empty servers block, shipped identically by eleven other institutions, and have been removed.'
  evidence:
  - status: 200
    url: https://idp.sussex.ac.uk/idp/shibboleth
  - status: 200
    url: https://okta.sussex.ac.uk/.well-known/openid-configuration
  - status: 401
    url: https://canvas.sussex.ac.uk/api/v1/accounts
  - status: 200
    url: https://canvas.sussex.ac.uk/api/lti/security/jwks
  - status: 202
    url: https://sussex.figshare.com/oai?verb=Identify
  - status: 200
    url: https://sro.sussex.ac.uk/cgi/oai2?verb=Identify
  - status: 200
    url: https://sussex.primo.exlibrisgroup.com/discovery/search?vid=44SUS_INST:44SUS_VU1
  - status: 200
    url: https://api.github.com/orgs/universityofsussex/repos
  - status: 0
    url: https://data.sussex.ac.uk/
  - status: 0
    url: https://api.sussex.ac.uk/
  - status: 404
    url: https://www.sussex.ac.uk/llms.txt
  reason: tenant_only
  state: gated
created: '2026-06-03'
description: 'The University of Sussex is a research-intensive public university at Falmer near Brighton in the United Kingdom, a member of the Russell Group''s peer set of UK research institutions and ranked #247 in the QS World University Rankings 2025. Its programmable footprint is small and almost entirely indirect, and this profile says so rather than padding it. The one surface the university genuinely operates and publishes machine-readably is its own Shibboleth identity provider: idp.sussex.ac.uk serves signed SAML 2.0 metadata with an entityID of https://idp.sussex.ac.uk/shibboleth and a shibmd:Scope of sussex.ac.uk, running on a Sussex-controlled Azure deployment rather than a vendor''s multi-tenant service. Everything else that looks like a Sussex API is a vendor product running under a Sussex name: Okta for single sign-on at okta.sussex.ac.uk, Instructure Canvas for the VLE at canvas.sussex.ac.uk, Figshare for the research repository at sussex.figshare.com, and Ex Libris Primo
  for library discovery. Those relationships are recorded here as tenant surfaces because they are real institutional facts, but the contracts behind them belong to the vendors and are scored against the vendors'' own profiles. Sussex operates no public developer portal, publishes no OpenAPI of its own, and its GitHub organization has no public repositories. The former Sussex Research Online EPrints repository and its OAI-PMH endpoint have been decommissioned and now redirect to an HTML publications page.'
finops:
- name: University Of Sussex Finops
  service_category: Education
  slug: university-of-sussex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-sussex.png
layout: provider
modified: '2026-08-30'
name: University of Sussex
nav: Providers
network: true
overview: 'University of Sussex publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, United Kingdom, and Russell Group.


  University of Sussex''s developer surface includes documentation, support, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: University Of Sussex Plans Pricing
  plan_count: 2
  slug: university-of-sussex-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: University Of Sussex Rate Limits
  slug: university-of-sussex-rate-limits
scopes:
- name: University Of Sussex Scopes
  scope_count: 7
  slug: university-of-sussex-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 4.4
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 32.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-sussex/refs/heads/main/screenshots/university-of-sussex-2026-06-20T200307.png
security:
- kind: authentication
  name: University Of Sussex Authentication
  slug: university-of-sussex-authentication
  summary_line: saml2/oidc/oauth2 · 3 schemes
- kind: domain-security
  name: University Of Sussex Domain Security
  slug: university-of-sussex-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-sussex
tags:
- University
- Higher Education
- Education
- United Kingdom
- Russell Group
- Public Research University
- Identity Federation
- Research Repository
- Library
- Learning Management
- Research
- Open Access
website: https://www.sussex.ac.uk/
---
