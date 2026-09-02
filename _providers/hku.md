---
access_model:
  confidence: high
  label: Affiliation-gated · No public self-serve access
  onboarding: unknown
  pricing: free
  public: false
  source:
  - https://developer.hku.hk/
  - https://api.hku.hk/
  - authentication/hku-authentication.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
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
  score: 26.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: Hku Agentic Access
  operation_count: 157
  slug: hku-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The University of Hong Kong's own Shibboleth SAML 2.0 identity provider, entityID https://hkafidp.hku.hk/idp/shibboleth, scope hku.hk. It self-publishes signed metadata (HTTP 200, application/xml, 14,
  name: HKU Shibboleth Identity Provider
  slug: identity-federation
- description: HKU Information Technology Services runs an Azure API Management gateway at api.hku.hk and a developer portal at developer.hku.hk. Since 17 March 2026 the portal has issued subscription keys to studen
  name: HKU ITS API Developer Portal and Gateway
  slug: its-api-portal
- description: HKU Scholars Hub is the University's DSpace-based open-access institutional repository and current research information system, on HKU's own host. It is documented as exposing an OAI-PMH metadata inte
  name: HKU Scholars Hub OAI-PMH
  slug: scholars-hub-oai
- description: HKU DataHub is the University's research-data repository, running as a Figshare tenancy — datahub.hku.hk is a CNAME to figshare.com and the same content is served at hku.figshare.com. The data, the co
  name: HKU DataHub (Figshare tenancy)
  slug: datahub-figshare
- description: 'HKU Libraries'' discovery layer runs on Ex Libris Primo VE at julac-hku.primo.exlibrisgroup.com under the JULAC consortium view 852JULAC_HKU. The catalog records are HKU''s; the discovery and Alma APIs '
  name: HKU Libraries Discovery (Ex Libris Primo tenancy)
  slug: library-primo
- description: HKU's Microsoft Entra ID tenant (42f9b54e-2477-41ba-bf09-7a0d2a83ff09) publishes a live OpenID Connect discovery document for the hku.hk domain. It is institution-specific and machine-readable, but it
  name: HKU Microsoft Entra ID Tenant
  slug: entra-tenant
- description: Metadata documents that describe the identity service.
  name: University of Hong Kong Discovery API
  slug: hku-discovery-api
- description: OAuth 2.0 / OpenID Connect protocol endpoints.
  name: University of Hong Kong O Auth API
  slug: hku-oauth-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Figshare altmetric API
  slug: open-hku-altmetric-api
- collection_type: open
  name: Figshare altmetric articles API
  slug: open-hku-articles-api
- collection_type: open
  name: Figshare altmetric authors API
  slug: open-hku-authors-api
- collection_type: open
  name: Figshare altmetric collections API
  slug: open-hku-collections-api
- collection_type: open
  name: Figshare altmetric institutions API
  slug: open-hku-institutions-api
- collection_type: open
  name: Figshare altmetric oauth API
  slug: open-hku-oauth-api
- collection_type: open
  name: Figshare altmetric other API
  slug: open-hku-other-api
- collection_type: open
  name: Figshare altmetric profiles API
  slug: open-hku-profiles-api
- collection_type: open
  name: Figshare altmetric projects API
  slug: open-hku-projects-api
- collection_type: open
  name: Figshare altmetric symplectic API
  slug: open-hku-symplectic-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.hku.hk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hku.hk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://hkafidp.hku.hk/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://hub.hku.hk/
- group: other
  title: ''
  type: OpenData
  url: https://datahub.hku.hk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://julac-hku.primo.exlibrisgroup.com/discovery/search?vid=852JULAC_HKU:HKU
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.hku.hk/
- group: other
  title: ''
  type: AIPolicy
  url: https://aied.talic.hku.hk/aipolicy/
- group: build
  title: ''
  type: AITooling
  url: https://genai.hku.hk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hku.hk/about/policies_reports/privacy_policy.html
- group: operate
  title: ''
  type: Support
  url: https://www.hku.hk/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.hku.hk/press/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.hku.hk/press/rss.xml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hku-official
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-hong-kong/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/hku-identity-openapi.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hku-adfs-openid-configuration.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hku-openid-configuration.schema.json
- group: build
  title: ''
  type: Examples
  url: examples/hku-identity-examples.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hku-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hku-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hku-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hku-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hku-identity-attributes.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hku-organization.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/hku-identity-rules.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hku-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hku-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hku-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'HKU operates real APIs and a real gateway, but the only route to their contracts is an institutional sign-in. developer.hku.hk returns 200 on every route and redirects all of them to /signin; api.hku.hk answers with the Azure API Management 404 envelope on every unauthenticated path. What is publicly readable is identity infrastructure — a Shibboleth SAML IdP and an AD FS OIDC issuer, both on HKU hosts, both machine-readable, both catalogued here. Two further surfaces are blocked rather than absent: hub.hku.hk (DSpace/OAI-PMH) sits behind a Cloudflare challenge, and datahub.hku.hk (Figshare tenancy) returns an empty 202 to machine clients. No fabrication was needed to fill the gap and none was performed.'
  evidence:
  - status: 200
    url: https://hkafidp.hku.hk/idp/shibboleth
  - status: 200
    url: https://adfs.hku.hk/adfs/.well-known/openid-configuration
  - status: 200
    url: https://adfs.hku.hk/adfs/discovery/keys
  - status: 200
    url: https://adfs.hku.hk/FederationMetadata/2007-06/FederationMetadata.xml
  - status: 401
    url: https://adfs.hku.hk/adfs/userinfo
  - note: redirects to /signin
    status: 200
    url: https://developer.hku.hk/apis
  - status: 404
    url: https://api.hku.hk/
  - note: Cloudflare challenge
    status: 403
    url: https://hub.hku.hk/oai/request?verb=Identify
  - note: empty body
    status: 202
    url: https://datahub.hku.hk/
  - status: 404
    url: https://www.hku.hk/robots.txt
  - status: 404
    url: https://www.hku.hk/llms.txt
  - note: empty array — the official GitHub org has no public repositories
    status: 200
    url: https://api.github.com/orgs/hku-official/repos
  reason: affiliation_gated_developer_portal
  state: gated
created: '2026-06-03'
description: 'The University of Hong Kong (HKU) is a public research university in Hong Kong SAR, founded in 1911 and ranked in the top 30 of the QS World University Rankings. It operates no public, self-serve API programme. The machine-readable surfaces HKU genuinely runs on its own hosts are identity infrastructure: a Shibboleth SAML 2.0 identity provider at hkafidp.hku.hk, registered with the Hong Kong Access Federation in 2016 and exported to eduGAIN with REFEDS Research and Scholarship and SIRTFI declarations, and an AD FS OAuth 2.0 / OpenID Connect issuer at adfs.hku.hk publishing a live discovery document and JWKS. HKU ITS also runs an Azure API Management gateway (api.hku.hk) and developer portal (developer.hku.hk) that opened GenAI chat-completion, embedding and image-generation APIs to students in March 2026 — but every portal route redirects to institutional sign-in, so no specification, scope or endpoint list is publicly readable. Its research repository is a Figshare tenancy
  and its library discovery is an Ex Libris Primo tenancy: real institutional facts, vendor-operated contracts, recorded here as tenant relationships rather than credited to HKU. HKU publishes no OpenAPI, no robots.txt on its main host, no llms.txt, no status page and no API changelog.'
finops:
- name: Hku Finops
  service_category: Education
  slug: hku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hku.png
json_schemas:
- name: HKU AD FS OpenID Provider Metadata
  property_count: 26
  slug: hku-openid-configuration.schema
jsonld:
- class_count: 0
  name: Hku Organization Context
  property_count: 0
  slug: hku-organization
layout: provider
modified: '2026-08-19'
name: University of Hong Kong
nav: Providers
network: true
overview: 'University of Hong Kong publishes 2 APIs on the [APIs.io](https://apis.io/) network: Discovery API and O Auth API. Tagged areas include Education, Higher Education, University, Hong Kong, and Identity Federation.


  The University of Hong Kong catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Hong Kong''s developer surface includes support, engineering blog, GitHub presence, code examples, authentication, and 27 more developer resources.'
plans:
- name: Hku Plans Pricing
  plan_count: 2
  slug: hku-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Hku Rate Limits
  slug: hku-rate-limits
rules:
- effective_rule_count: 11
  extends: []
  name: University of Hong Kong API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 5
  slug: hku-identity-rules
scopes:
- name: Hku Scopes
  scope_count: 9
  slug: hku-scopes
  summary_line: 9 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 29.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.3
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 63.6
    contract_quality: 27.2
    developer_ergonomics: 28.6
    discoverability: 79.6
    governance: 63.6
    operational_transparency: 36.8
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 72.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hku/refs/heads/main/screenshots/hku-2026-06-20T182806.png
security:
- kind: authentication
  name: Hku Authentication
  slug: hku-authentication
  summary_line: oauth2/openIdConnect/saml2/apiKey · 4 schemes
- kind: domain-security
  name: Hku Domain Security
  slug: hku-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: hku
tags:
- Education
- Higher Education
- University
- Hong Kong
- Identity Federation
- Single Sign-On
- Research Data
- Open Access
- Artificial Intelligence
- Research Computing
website: https://www.hku.hk/
---
