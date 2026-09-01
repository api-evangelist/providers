---
access_model:
  confidence: high
  label: Free · No signup, no developer portal
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 24.3
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: KFUPM's own identity provider at sts.kfupm.edu.sa (Microsoft AD FS). Publishes signed SAML 2.0 federation metadata (80 KB, entityID http://sts.kfupm.edu.sa/adfs/services/trust, IDPSSODescriptor with H
  name: KFUPM Identity Federation (SAML 2.0 + OpenID Connect)
  slug: identity-federation
- description: 'Live OAI-PMH 2.0 harvesting interface for the KFUPM ePrints institutional repository (EPrints 3.4.1), self-hosted on the university''s own domain. repositoryIdentifier eprints.kfupm.edu.sa, adminEmail '
  name: KFUPM ePrints OAI-PMH Repository Interface
  slug: eprints-oai-pmh
- description: Record-level and search-level JSON from the same self-hosted KFUPM ePrints repository, served without authentication. /cgi/export/eprint/{eprintid}/JSON/{filename} returns the full record as applicati
  name: KFUPM ePrints Export & Search (JSON)
  slug: eprints-export
- description: KFUPM runs an Elsevier Pure research information system at pure.kfupm.edu.sa and its Pure Web Services REST API is reachable at /ws/api, authenticated with a Pure api-key header. The deployment, the t
  name: KFUPM Elsevier Pure Web Services (tenant deployment)
  slug: pure-tenant
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.kfupm.edu.sa/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kfupm.edu.sa/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kfupm.edu.sa/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://news.kfupm.edu.sa/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/kfupm/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sts.kfupm.edu.sa/FederationMetadata/2007-06/FederationMetadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.kfupm.edu.sa/
- group: start
  title: ''
  type: ResearchPortal
  url: https://pure.kfupm.edu.sa/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://registrar.kfupm.edu.sa/courses-classes/course-offering1/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library-web.kfupm.edu.sa/
- group: build
  title: ''
  type: AITooling
  url: https://www.kfupm.edu.sa/about-us/discover/ai-x
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KFUPM-OSC
- group: auth
  title: ''
  type: Authentication
  url: authentication/kfupm-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/kfupm-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kfupm-conformance.yml
- group: design
  title: ''
  type: Errors
  url: errors/kfupm-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kfupm-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/kfupm-vocabulary.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kfupm-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kfupm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kfupm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kfupm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'King Fahd University of Petroleum & Minerals (KFUPM) is a public research university in Dhahran, Saudi Arabia. Its programmable footprint is small, and most of what previously appeared in this profile was not its own: 37 OpenAPI definitions attributed to KFUPM here were the Elsevier Pure Web Services contract (info.title "Pure API", contact pure-support@elsevier.com, version 5.35.3-4) served from the university''s Pure tenant at pure.kfupm.edu.sa. That contract is Elsevier''s and has been removed; the tenant relationship is recorded instead. What KFUPM genuinely operates is three surfaces on its own infrastructure. Its identity provider at sts.kfupm.edu.sa publishes signed SAML 2.0 federation metadata and an OpenID Connect discovery document, and is registered in eduGAIN through MAEEN, the Saudi identity federation, with scope kfupm.edu.sa — an institution-operated machine-readable surface by definition. The KFUPM ePrints repository (EPrints 3.4.1) serves a live, unauthenticated
  OAI-PMH 2.0 harvesting interface with six working verbs and six metadata formats, plus record-level and search-level JSON export whose record model carries a KFUPM-local `arabic_abstract` field. The registrar publishes a live course offering system, but it answers only an HTML form POST and returns no machine-readable format. There is no central developer portal, no API documentation, no changelog, no status page, no robots.txt, no sitemap and no llms.txt on the university''s own domain. The library discovery surface sits behind a Cloudflare bot challenge. KFUPM does not publish an OpenAPI for anything it operates; the three descriptions in this repo were derived by probing the live endpoints.'
examples:
- key_count: 2
  name: Kfupm Sts Openid Configuration
  slug: kfupm-sts-openid-configuration
finops:
- name: Kfupm Finops
  service_category: Education
  slug: kfupm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kfupm.png
json_schemas:
- name: KFUPM ePrints Record
  property_count: 0
  slug: kfupm-eprints-record
layout: provider
modified: '2026-08-30'
name: King Fahd University of Petroleum & Minerals
nav: Providers
network: true
overview: 'King Fahd University of Petroleum & Minerals publishes 3 APIs on the [APIs.io](https://apis.io/) network: KFUPM Identity Federation (SAML 2.0 + OpenID Connect), KFUPM ePrints OAI-PMH Repository Interface, and KFUPM ePrints Export & Search (JSON). Tagged areas include University, Higher Education, Education, Research, and Saudi Arabia.


  King Fahd University of Petroleum & Minerals'' developer surface includes engineering blog, authentication, and 21 more developer resources.'
plans:
- name: Kfupm Plans Pricing
  plan_count: 2
  slug: kfupm-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Kfupm Rate Limits
  slug: kfupm-rate-limits
scopes:
- name: Kfupm Scopes
  scope_count: 0
  slug: kfupm-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 45.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 56.9
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 15.2
    operational_transparency: 23.7
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kfupm/refs/heads/main/screenshots/kfupm-2026-06-20T184024.png
security:
- kind: authentication
  name: Kfupm Authentication
  slug: kfupm-authentication
  summary_line: openIdConnect/oauth2/saml2/apiKey/none · 4 schemes
- kind: domain-security
  name: Kfupm Domain Security
  slug: kfupm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kfupm
tags:
- University
- Higher Education
- Education
- Research
- Saudi Arabia
- Middle East
- Identity Federation
- Research Repository
- Open Access
- OAI-PMH
- Theses
- Course Catalog
website: https://www.kfupm.edu.sa/
---
