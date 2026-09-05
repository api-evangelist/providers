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
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Keio Agentic Access
  operation_count: 0
  slug: keio-agentic-access
  summary_line: 0 operations
api_count: 2
apis:
- baseURL: https://koara.lib.keio.ac.jp/xoonips/modules/xoonips/oai.php
  baseurl_source: declared
  description: KOARA (KeiO Associated Repository of Academic resources) is Keio University's institutional repository, released by the Media Center in 2006 and running on the open-source XooNips platform on Keio's o
  name: KOARA OAI-PMH Metadata API
  slug: koara-oai-pmh
- baseURL: https://dcollections.lib.keio.ac.jp/sites/default/files/iiif/
  baseurl_source: declared
  description: 'The Keio University Media Center serves its digitised special collections as IIIF on two hosts it owns: dcollections.lib.keio.ac.jp for IIIF Presentation API 2.1 manifests, and iiif.lib.keio.ac.jp for'
  name: Keio Media Center Digital Collections IIIF API
  slug: iiif
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
  title: ''
  type: OpenAPI
  url: openapi/keio-koara-oai-pmh-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/keio-iiif-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/keio-iiif-manifest-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/keio-iiif-image-info-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/index.yml
- group: design
  title: ''
  type: Rules
  url: rules/keio-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/keio-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/keio-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: authentication/keio-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/keio-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/keio-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/keio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keio-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keio-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/keio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/keio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/keio-finops.yml
- group: other
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
modified: '2026-09-01'
name: Keio University
nav: Providers
network: true
overview: 'Keio University publishes 2 APIs on the [APIs.io](https://apis.io/) network: KOARA OAI-PMH Metadata API and Keio Media Center Digital Collections IIIF API. Tagged areas include Education, Higher Education, University, Japan, and Research.


  The Keio University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Keio University''s developer surface includes engineering blog, code examples, authentication, YouTube channel, and 27 more developer resources.'
plans:
- name: Keio Plans Pricing
  plan_count: 2
  slug: keio-plans-pricing
random_paper: 4
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
  composite: 35.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 79.0
    catalog_earned_first_party: 0.0
    catalog_gap: 36.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 15.2
    contract_quality: 29.2
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 21.1
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
