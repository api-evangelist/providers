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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Keio Agentic Access
  operation_count: 0
  slug: keio-agentic-access
  summary_line: 0 operations
api_count: 4
apis:
- description: Keio operates its own SAML 2.0 identity provider under entityID https://gakunin1.keio.ac.jp/idp/shibboleth, registered in GakuNin — the Japanese academic access-management federation operated by the N
  name: Keio University Identity Provider (GakuNin / eduGAIN)
  slug: gakunin-idp
- description: Keio runs an Okta tenant at keio.okta.com behind its campus applications; gslbs.keio.jp redirects an anonymous request into a SAML authentication request against it. The tenant's OpenID Connect discov
  name: Keio Okta Tenant — OpenID Connect
  slug: okta
- description: K-RIS (慶應義塾 研究者情報データベース) is Keio's researcher information system, holding faculty profiles, publications and research outputs. It runs on Elsevier Pure at k-ris.keio.ac.jp. The researchers, the output
  name: K-RIS — Keio Research Information System (Elsevier Pure)
  slug: k-ris
- description: 'Keio holds a Figshare research-data repository, evidenced not by the platform host but by DataCite''s own registry: DataCite client `keio.figshare` (symbol KEIO.FIGSHARE, clientType repository, domains'
  name: Keio Figshare Research Data Repository
  slug: figshare
- description: Keio University is a registered DataCite provider — id `keio`, symbol KEIO, memberType consortium_organization, non-profit, active — holding DOI prefix 10.71825 through the FSCO (Figshare) consortium,
  name: DataCite Membership — provider `keio`
  slug: datacite
- description: 'Two Keio units are Crossref members in their own right: member 1082, "Keio Journal of Medicine", DOI prefix 10.2302, with 1,743 DOIs (54 current, 1,689 backfile) reaching back to 1952; and member 1443'
  name: Crossref Memberships — Keio units
  slug: crossref
- description: Keio University is registered in the Research Organization Registry as https://ror.org/02kn6nx58, with domain keio.ac.jp, established 1858, located in Tokyo, and cross-referenced to Funder Registry 50
  name: ROR Registration — Keio University
  slug: ror
- baseURL: https://koara.lib.keio.ac.jp/xoonips/modules/xoonips/oai.php
  baseurl_source: declared
  description: IIIF Presentation and Image API surfaces for Keio's digitised collections.
  name: Keio University IIIF API
  slug: keio-iiif-api
- baseURL: https://koara.lib.keio.ac.jp/xoonips/modules/xoonips/oai.php
  baseurl_source: declared
  description: OAI-PMH 2.0 verbs for discovering and harvesting KOARA's scholarly metadata.
  name: Keio University Metadata Harvesting API
  slug: keio-metadata-harvesting-api
artifact_total: 23
common:
- group: company
  title: ''
  type: Website
  url: https://www.keio.ac.jp/en/
- group: build
  title: ''
  type: LibraryWebsite
  url: https://www.lib.keio.ac.jp/en/
- group: other
  title: ''
  type: ResearchRepository
  url: https://koara.lib.keio.ac.jp/
- group: build
  title: ''
  type: DigitalCollections
  url: https://dcollections.lib.keio.ac.jp/en
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/identity-federation/keio-identity-federation.yml
  title: ''
  type: IdentityFederation
  url: identity-federation/keio-identity-federation.yml
- group: other
  title: ''
  type: AIPolicy
  url: https://www.st.itc.keio.ac.jp/en/software_ai_guideline.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keio.ac.jp/en/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.keio.ac.jp/en/news/
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/openapi/_original/keio-koara-oai-pmh-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/keio-koara-oai-pmh-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/openapi/_original/keio-iiif-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/keio-iiif-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/json-schema/keio-iiif-manifest-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/keio-iiif-manifest-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/json-schema/keio-iiif-image-info-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/keio-iiif-image-info-schema.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/examples/index.yml
  title: ''
  type: Examples
  url: examples/index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/rules/keio-rules.yml
  title: ''
  type: Rules
  url: rules/keio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/vocabulary/keio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/keio-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/json-ld/keio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/keio-context.jsonld
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/authentication/keio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/keio-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/scopes/keio-scopes.yml
  title: ''
  type: Scopes
  url: scopes/keio-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/errors/keio-errors.yml
  title: ''
  type: Errors
  url: errors/keio-errors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/conformance/keio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keio-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/lifecycle/keio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/keio-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/agentic-access/keio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/keio-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/security/keio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keio-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/plans/keio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/keio-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/rate-limits/keio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/keio-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/finops/keio-finops.yml
  title: ''
  type: FinOps
  url: finops/keio-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Keio_univ_PR
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/keio-university
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/keio_university
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/keiouniversity
created: '2026-06-03'
description: 'Keio University (慶應義塾大学) is a private research university in Tokyo, Japan, founded by Fukuzawa Yukichi in 1858 and the oldest institution of modern higher education in the country. Its programmable footprint is small, entirely non-commercial, and — unusually for this cohort — genuinely its own rather than a vendor''s running under its name. Two surfaces are operated by Keio on Keio''s hosts and are anonymously consumable today: KOARA, the institutional repository, which serves a live OAI-PMH 2.0 harvesting interface advertising Dublin Core and the NII junii2 schema across 100 faculty and research-centre sets; and the Media Center''s Digital Collections, which serve IIIF Presentation 2.1 manifests and IIIF Image 2.0 Level 1 tiles for the university''s digitised rare books, including all 656 folios of its Gutenberg 42-line Bible. Keio also operates its own Shibboleth/SAML identity provider, registered in the GakuNin federation since 2014 and republished into eduGAIN — the strongest
  institution-owned machine-readable artifact it has. Beyond those, the estate is a set of tenancies and registry memberships rather than engineering: K-RIS runs on Elsevier Pure, campus sign-on runs through an Okta tenant and an Extic-hosted SSO service, research data DOIs are minted through a Figshare consortium seat at DataCite, and two Keio units hold Crossref memberships in their own right. There is no developer portal, no API key, no changelog and no published OpenAPI anywhere in the estate; every contract in this repository was written by API Evangelist from live probes and is marked as such.'
examples:
- key_count: 8
  name: Keio Iiif Image Info
  slug: keio-iiif-image-info
- key_count: 10
  name: Keio Iiif Manifest Excerpt
  slug: keio-iiif-manifest-excerpt
- key_count: 29
  name: Keio Okta Openid Configuration
  slug: keio-okta-openid-configuration
finops:
- name: Keio Finops
  service_category: Education
  slug: keio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keio.png
json_schemas:
- name: Keio IIIF Image API 2.0 Image Information
  property_count: 8
  slug: keio-iiif-image-info
- name: Keio IIIF Presentation API 2.1 Manifest
  property_count: 7
  slug: keio-iiif-manifest
jsonld:
- class_count: 18
  name: Keio Context
  property_count: 8
  slug: keio-context
layout: provider
modified: '2026-09-16'
name: Keio University
nav: Providers
network: true
overview: 'Keio University publishes 2 APIs on the [APIs.io](https://apis.io/) network: IIIF API and Metadata Harvesting API. Tagged areas include Education, Higher Education, University, Japan, and Research.


  The Keio University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Keio University''s developer surface includes engineering blog, code examples, authentication, YouTube channel, and 27 more developer resources.'
plans:
- name: Keio Plans Pricing
  plan_count: 2
  slug: keio-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Keio Rate Limits
  slug: keio-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Keio University API Rules
  rule_count: 12
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 6
  slug: keio-rules
scopes:
- name: Keio Scopes
  scope_count: 0
  slug: keio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 82.0
    catalog_earned_first_party: 0.0
    catalog_gap: 33.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 39.5
    contract_governance: 15.2
    contract_quality: 29.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 57.4
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/keio/refs/heads/main/screenshots/keio-2026-06-20T183942.png
security:
- kind: authentication
  name: Keio Authentication
  slug: keio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Keio Domain Security
  slug: keio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: keio
tags:
- Education
- Higher Education
- University
- Japan
- Research
- Institutional Repository
- Research Repository
- Identity Federation
- Digital Collections
- IIIF
- OAI-PMH
- Open Access
- Cultural Heritage
website: https://www.keio.ac.jp/en/
---
