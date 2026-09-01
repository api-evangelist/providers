---
access_model:
  confidence: high
  label: Free · No registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - openapi
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Carnegie Mellon University Agentic Access
  operation_count: 16
  slug: carnegie-mellon-university-agentic-access
  summary_line: 16 operations
api_count: 6
apis:
- description: Carnegie Mellon's campus-wide single sign-on identity provider, running Shibboleth on CMU's own host and address space (login.cmu.edu, 128.2.42.22). Its SAML 2.0 metadata is publicly readable at the c
  name: CMU Web Login (Shibboleth SAML 2.0 Identity Provider)
  slug: web-login-sso
- description: KiltHub is Carnegie Mellon's institutional repository for research data and scholarly output. The data, the collections and the DOIs are CMU's; the platform, the API and the OAI-PMH endpoint are figsh
  name: KiltHub Institutional Repository (figshare) — tenant
  slug: kilthub-figshare-tenant
- description: 'CMU''s learning management system serves an LTI 1.3 / LTI Advantage JWKS at canvas.cmu.edu/api/lti/security/jwks, so the LTI standard is genuinely in play in CMU''s teaching environment. It is recorded '
  name: Canvas LTI 1.3 Advantage (Instructure) — tenant
  slug: canvas-lti-tenant
- description: A public JSON API for Carnegie Mellon dining locations, hours and menus, built and run by ScottyLabs, a CMU student organization, at api.cmueats.com. It exists because CMU's own dining surface does no
  name: CMU Eats API (ScottyLabs) — student-operated
  slug: cmu-eats-scottylabs
- description: Published articles.
  name: Carnegie Mellon University Articles API
  slug: carnegie-mellon-university-articles-api
- description: COVIDcast real-time indicator signals across geographies.
  name: Carnegie Mellon University Covidcast API
  slug: carnegie-mellon-university-covidcast-api
- description: Syndication.
  name: Carnegie Mellon University Feeds API
  slug: carnegie-mellon-university-feeds-api
- description: US ILINet influenza-like-illness surveillance (CDC FluView).
  name: Carnegie Mellon University Fluview API
  slug: carnegie-mellon-university-fluview-api
- description: Delphi's own nowcasts and forecasts.
  name: Carnegie Mellon University Forecasts API
  slug: carnegie-mellon-university-forecasts-api
- description: Issues within a journal.
  name: Carnegie Mellon University Issues API
  slug: carnegie-mellon-university-issues-api
- description: The journals CMU Libraries publishes.
  name: Carnegie Mellon University Journals API
  slug: carnegie-mellon-university-journals-api
- description: Service metadata and version.
  name: Carnegie Mellon University Meta API
  slug: carnegie-mellon-university-meta-api
- description: Vulnerability Notes.
  name: Carnegie Mellon University Notes API
  slug: carnegie-mellon-university-notes-api
- description: OAI-PMH 2.0 metadata harvesting provider.
  name: Carnegie Mellon University Oai Pmh API
  slug: carnegie-mellon-university-oai-pmh-api
- description: Preprint repository objects.
  name: Carnegie Mellon University Preprints API
  slug: carnegie-mellon-university-preprints-api
- description: Per-vendor coordination status.
  name: Carnegie Mellon University Vendors API
  slug: carnegie-mellon-university-vendors-api
artifact_total: 34
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/cmu-delphi/delphi-epidata/blob/dev/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.cmu.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://cmu-delphi.github.io/delphi-epidata/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kb.cert.org/vuls/
- group: docs
  title: ''
  type: APIReference
  url: https://cmu-delphi.github.io/delphi-epidata/api/README.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cmu-delphi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CERTCC
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cmu-sei
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cmu-lib
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.cmu.edu/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/https%3A%2F%2Flogin.cmu.edu%2Fidp%2Fshibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://lps.library.cmu.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://kilthub.cmu.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.library.cmu.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://enr-apps.as.cmu.edu/open/SOC/SOCServlet
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.cmu.edu/computing/services/research/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.cmu.edu/teaching/technology/aitools/
- group: auth
  title: ''
  type: Authentication
  url: https://www.cmu.edu/computing/services/security/identity-access/authentication/sso-provider.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cmu.edu/legal/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cmu.edu/legal/
- group: operate
  title: ''
  type: Support
  url: https://www.cmu.edu/computing/support/
- group: company
  title: ''
  type: Blog
  url: https://www.cmu.edu/news/
- group: company
  title: ''
  type: Blog
  url: https://insights.sei.cmu.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/carnegie-mellon-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/carnegie-mellon-university-education-standards-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carnegie-mellon-university-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/carnegie-mellon-university-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/carnegie-mellon-university-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carnegie-mellon-university-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/carnegie-mellon-university-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: json-ld/carnegie-mellon-university-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/carnegie-mellon-university-delphi-fluview-example.json
- group: build
  title: ''
  type: Examples
  url: examples/carnegie-mellon-university-cert-vulnerability-note-example.json
- group: design
  title: ''
  type: Rules
  url: rules/carnegie-mellon-university-rules.yml
- group: design
  title: ''
  type: Rules
  url: rules/carnegie-mellon-university-jsonschema-spectral-rules.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/carnegie-mellon-university-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carnegie-mellon-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/carnegie-mellon-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carnegie-mellon-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/carnegie-mellon-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Carnegie Mellon University is a private research university in Pittsburgh, Pennsylvania, ranked 49th in the QS World University Rankings. It operates no central developer portal, no API gateway and no institution-wide developer program — api.cmu.edu and data.cmu.edu do not exist as developer surfaces — but unlike most of this cohort it does genuinely engineer public APIs, in three unrelated units that share no identifier, envelope or error model. The Delphi research group runs the Delphi Epidata API for real-time epidemiological surveillance; the CERT Coordination Center at the Software Engineering Institute runs the Vulnerability Notes API, the machine-readable record of coordinated vulnerability disclosure; and University Libraries self-hosts the Library Publishing Service, five open-access journals behind a REST API and a conformant OAI-PMH 2.0 provider on CMU''s own hardware. None of the three publishes an OpenAPI, a changelog on the API host, a status page or a deprecation
  policy, and both research APIs return errors with HTTP 200. Everything else that carries CMU''s name is a tenancy: KiltHub is figshare, Canvas is Instructure, and the eleven figshare-derived contracts this profile held until 2026-08-19 were a vendor''s engineering credited to the university.'
examples:
- key_count: 2
  name: Carnegie Mellon University Cert Note Cves Example
  slug: carnegie-mellon-university-cert-note-cves-example
- key_count: 2
  name: Carnegie Mellon University Cert Vendor Statements Example
  slug: carnegie-mellon-university-cert-vendor-statements-example
- key_count: 2
  name: Carnegie Mellon University Cert Vulnerability Note Example
  slug: carnegie-mellon-university-cert-vulnerability-note-example
- key_count: 2
  name: Carnegie Mellon University Delphi Covidcast Example
  slug: carnegie-mellon-university-delphi-covidcast-example
- key_count: 2
  name: Carnegie Mellon University Delphi Error Example
  slug: carnegie-mellon-university-delphi-error-example
- key_count: 2
  name: Carnegie Mellon University Delphi Fluview Example
  slug: carnegie-mellon-university-delphi-fluview-example
finops:
- name: Carnegie Mellon University Finops
  service_category: Education
  slug: carnegie-mellon-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carnegie-mellon-university.png
json_schemas:
- name: CERT/CC Vulnerability Note
  property_count: 30
  slug: carnegie-mellon-university-cert-vulnerability-note
- name: Delphi Epidata response envelope
  property_count: 3
  slug: carnegie-mellon-university-delphi-epidata-envelope
jsonld:
- class_count: 28
  name: Carnegie Mellon University Context
  property_count: 7
  slug: carnegie-mellon-university-context
layout: provider
modified: '2026-08-19'
name: Carnegie Mellon University
nav: Providers
network: true
overview: 'Carnegie Mellon University publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Covidcast API, Feeds API, and 9 more. Tagged areas include University, Higher Education, Education, United States, and Private Research University.


  The Carnegie Mellon University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Carnegie Mellon University''s developer surface includes documentation, API reference, authentication, support, engineering blog, code examples, and 35 more developer resources.'
plans:
- name: Carnegie Mellon University Plans Pricing
  plan_count: 2
  slug: carnegie-mellon-university-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Carnegie Mellon University Rate Limits
  slug: carnegie-mellon-university-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Carnegie Mellon University API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: carnegie-mellon-university-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Carnegie Mellon University API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 3
  slug: carnegie-mellon-university-rules
scopes:
- name: Carnegie Mellon University Scopes
  scope_count: 0
  slug: carnegie-mellon-university-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 32.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 17.4
    contract_quality: 29.0
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 17.4
    operational_transparency: 23.7
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carnegie-mellon-university/refs/heads/main/screenshots/carnegie-mellon-university-2026-06-20T174011.png
security:
- kind: authentication
  name: Carnegie Mellon University Authentication
  slug: carnegie-mellon-university-authentication
  summary_line: none/saml · 3 schemes
- kind: domain-security
  name: Carnegie Mellon University Domain Security
  slug: carnegie-mellon-university-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: carnegie-mellon-university
tags:
- University
- Higher Education
- Education
- United States
- Private Research University
- Research
- Epidemiology
- Public Health
- Cybersecurity
- Vulnerability Disclosure
- Scholarly Publishing
- Institutional Repository
- Identity Federation
- Open Access
- Open Data
website: https://www.cmu.edu/
---
